import math
import conn
import datetime
import pdfkit
import os 
import re
from urllib.parse import urlparse
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from os import listdir
from os.path import isfile, join, basename
import webbrowser

webbrowser.open_new('http://localhost:8080')
    
pastaApp = os.getcwd()

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    conn.cursor.execute("SELECT * FROM TB_PROJETOS ")
    row = conn.cursor.fetchall()

    return render_template('listaProjetos.html', data = row)


@app.route('/novo_projeto', methods=['GET', 'POST'])
def formNovoProjeto():
    if request.method == 'POST':
        
        data = []
       
        data.append(None)
        data.append(request.form.get('nome_projeto'))
        data.append(request.form.get('responsavel_tecnico'))
        data.append(request.form.get('observacao'))
        data.append(datetime.datetime.now())
        data.append(datetime.datetime.now())
        
        id = conn.cursor.execute(f"INSERT INTO TB_PROJETOS VALUES (?,?,?,?,?,?)", data ).lastrowid
        conn.cnxn.commit()
            
        conn.cursor.execute(f"SELECT * FROM TB_PROJETOS WHERE ID = {id}")
        vDados = conn.cursor.fetchone()

        vParam = None
        
        return render_template('formCreateParamProj.html', vDados = vDados, vParam = vParam)
    
    else:    
        return render_template('formNovoProjeto.html')



@app.route('/projeto', methods=['GET', 'POST'])
def formProjeto():
    
    if request.method == 'GET' and request.args.get('id_projeto'):
        
        id_projeto = request.args.get('id_projeto')
    
        conn.cursor.execute(f"SELECT * FROM TB_PROJETOS WHERE ID = {id_projeto}")

        data = conn.cursor.fetchone()
    
        return render_template('formProjeto.html', data = data)
    
    if request.method == 'POST' and request.form.get('id_projeto'):
        
        data = []
       
        data.append(request.form.get('nome_projeto'))
        data.append(request.form.get('responsavel_tecnico'))
        data.append(request.form.get('observacao'))
        data.append(datetime.datetime.now())
        data.append(request.form.get('id_projeto'))
        
        conn.cursor.execute(""" UPDATE TB_PROJETOS 
                                    SET nome_projeto = ?,                                       
                                        responsavel_tecnico = ?,
                                        observacao = ?,
                                        data_atualizacao = ?
                                WHERE ID = ? """, data )
        
        conn.cnxn.commit()
        
        return redirect(f"/projeto?id_projeto={data[4]}")



@app.route('/del_proj', methods=['POST'])
def delProjeto():
    
    if request.method == 'POST' and request.form.get('idToDelete'):
        
        idToDelete = request.form.get('idToDelete')
    
        conn.cursor.execute(f"DELETE FROM TB_PROJETOS WHERE ID = {idToDelete}")
        conn.cnxn.commit()
        
        conn.cursor.execute(f"DELETE FROM TB_PARAM_PROJETO WHERE id_parametros_proj = {idToDelete}")
        conn.cnxn.commit()

        conn.cursor.execute("SELECT * FROM TB_PROJETOS ")

        row = conn.cursor.fetchall()

        return render_template('listaProjetos.html', data = row)
    


@app.route('/parametros', methods=['GET', 'POST'])
def formParamProjeto():
    
    id = request.args.get('id')

    vErro = request.args.get('erro')

    if vErro:
        vErro = "A quantidade mínima de parâmetros não foi preenchida! Por favor, recalcule."
    
    conn.cursor.execute(f"SELECT * FROM TB_PROJETOS WHERE ID = {id}")

    vDados = conn.cursor.fetchone()
    
    conn.cursor.execute(f"SELECT * FROM TB_PARAM_PROJETO WHERE id_parametros_proj = {id}")

    vParam = conn.cursor.fetchone() 

    return render_template('formParamProj.html' , vDados = vDados , vParam = vParam, vErro = vErro)



@app.route('/metodos', methods=['POST'])
def metodos():
    if request.method == 'POST':
               
        vArranjo = request.form.get('arranjo')

        lista = {}

        if vArranjo == 'Tripolar':
            conn.cursor.execute("SELECT id, grupo||' - '||ESPACAMENTO_A_B AS text FROM TABELA_35_FATORES_CORRECAO_CABOS_TRIPOLARES_REF_A1")
            vMetodos = conn.cursor.fetchall()

        elif vArranjo == 'Unipolar - Trifólio':
            conn.cursor.execute("SELECT id, grupo||' - '||ESPACAMENTO_A_B AS text FROM TABELA_34_FATORES_CORRECAO_CABOS_UNIPOLARES_REF_A1")
            vMetodos = conn.cursor.fetchall()

        else:
            conn.cursor.execute("SELECT * FROM TB_NA ")
            vMetodos = conn.cursor.fetchall()
        
        lista.update(vMetodos)

        return (lista)
        


@app.route('/relatorio')
def out():

    id = request.args.get('id')

    vGerarPdf = request.args.get('gerarPdf')

    conn.cursor.execute(f"SELECT * FROM TB_PROJETOS where id = {id}")

    vDados = conn.cursor.fetchone()

    dados = conn.cursor.execute(f"SELECT * FROM TB_PARAM_PROJETO where id_parametros_proj = {id}")

    # for column in dados.description:
    #     print(column[0])

    vParam = conn.cursor.fetchone()
  
    if (vParam[2])  and vParam[3] and (vParam[30]) and (vParam[18]) and (vParam[7]) and vParam[28]:
        
        calculo = round(((vParam[2]*1000000) / ((3**(1/2))*(vParam[3]*1000))),2)
        
        considerada = round(calculo*(1+(vParam[4]/100))+0.5)

        cccp_barramento = considerada / 0.1 / 1000

        conn.cursor.execute(f"SELECT * FROM TABELA_25_TIPOS_LINHAS where id_metodo = '{vParam[30]}' ")

        vTipoLinha = conn.cursor.fetchone()
                
        # print (f"{vParam[18]} {vTipoLinha[5]} {vTipoLinha[9]} ")

        if "Unipolar" in str({vParam[28]}):
            vInstalacao = f"{(vParam[18]*3) } {vTipoLinha[5]} {vTipoLinha[9]} "
        else:    
            if vParam[18] == 1:    
                vInstalacao = f"{vParam[18]} {vTipoLinha[6]} {vTipoLinha[8]}"
            else:
                vInstalacao = f"{vParam[18]} {vTipoLinha[7]} {vTipoLinha[9]} "
        
        vAngulo = "%.2f" % round(math.degrees(math.acos(vParam[7])),2)

        vFatorpot = math.sin(math.acos(vParam[7]))
        
        fPotencia = "%.4f" % round(vFatorpot,4)
        
        cNominalVeia = vParam[5] / vParam[18]


        if vParam[14] == "EPR – 105ºC":                        #   EPR – 105ºC  Isolação do cabo:</td>
            vTemp = 105
        else:      
            vTemp = 90

                                                                # vParam[31] #Diâmetro nominal do cabo escolhido (mm²)
            
        query_tbcabos = f""" SELECT * FROM Tabela_cabos 
                              where CLASSE_ISOLACAO = '{ vParam[16] }' 
                                and TEMP = { vTemp } 
                                and SECAO = { vParam[31] }"""
        
        conn.cursor.execute(query_tbcabos)

        vCabos = conn.cursor.fetchone()
       
        if vCabos:
            if vParam[28] == 'Unipolar - Espaçados':
                vXl = vCabos[10]
                if vParam[15]=="Alumínio":
                    vRca = vCabos[9]
                else:
                    vRca = vCabos[8]

            if vParam[28] == 'Unipolar - Contíguos':
                vXl = vCabos[7]
                if vParam[15]=="Alumínio":
                    vRca = vCabos[6]
                else:
                    vRca = vCabos[5]
                    
            if vParam[28] == 'Unipolar - Trifólio':
                vXl = vCabos[13]
                if vParam[15]=="Alumínio":
                    vRca = vCabos[12]
                else:
                    vRca = vCabos[11]

            if vParam[28] == 'Tripolar':
                vXl = vCabos[19]
                if vParam[15]=="Alumínio":
                    vRca = vCabos[18]
                else:
                    vRca = vCabos[17]      
        else:
            vXl = 0
            vRca = 0
        
        # TB_METODO_INSTALL

        if vParam[15]=="Alumínio":
            vTipo = f'ALUMINIO_{vTemp}'
        else:
            vTipo = f'COBRE_{vTemp}'

        query_tbinstall = f""" SELECT {vTipoLinha[3]} FROM TB_METODO_INSTALL 
                              where TIPO = '{ vTipo }'
                                and [Seção do condutor mm2] = { vParam[31] }"""

        conn.cursor.execute(query_tbinstall)

        vMetodoInstall = conn.cursor.fetchone()

        conn.cursor.execute(f"SELECT [Temperatura final °C a] FROM TABELA_43_TEMP_CURTO WHERE [Temperatura inicial °C] = '{vTemp}' ")
        vTempCc = conn.cursor.fetchone()

        conn.cursor.execute(f"SELECT [Temperatura final máxima °C a, b] FROM TABELA_44_TEMP_BLINDAGEM_CURTO WHERE [Material da cobertura] = 'ST1 e ST2 c' ")
        vTempBlindagem = conn.cursor.fetchone()

        conn.cursor.execute(f"SELECT * FROM TABELA_42_MATERIAL WHERE [Material] = '{vParam[15]}' ")
        vConstMaterial = conn.cursor.fetchone()

        if "A1" in str(vParam[30]) or "B1" in str(vParam[30]):
            vExposicao = 'Abrigada do sol'
        elif "A2" in str(vParam[30]) or "B2" in str(vParam[30]):     
            vExposicao = 'Exposta ao sol'
        else: 
            vExposicao = 'subterrâneas'   

        conn.cursor.execute(f"""SELECT * FROM TB_FATOR_CORRECAO_TEMP 
                                 where TEMPERATURA_AMBIENTE = {vParam[21]} 
                                   AND TEMP_ISOLACAO = {vTemp}
                                   AND TIPO_EXPOSICAO = '{vExposicao}' """)
        vFatorCorrecaoTemp = conn.cursor.fetchone()

        # vTipoLinha[3] A1...F1 H I 
        # vTipoLinha[3]
        tituloFCorrecaoResis = 'Fator de correção Resistividade Térmica do solo não aplicável'
        tituloFCorrecaoProfu = 'Fator de correção de correção por profundidade não aplicavel:'
        vFatorCorrecaoResist=[1]
        vFatorCorrecaoProfu=[1]
   
        vMets = ['F1','F2','G1','G2','H','I']

        for met in vMets:
            if met in str(vTipoLinha[3]) and vParam[23] > 1.0:

                tituloFCorrecaoResis = 'Fator de correção Resistividade Térmica do solo (Tabela 32 - NBR:14039):'
                tituloFCorrecaoProfu = 'Fator de correção de correção por profundidade (Tabela 33 - NBR:14039):'
                
                query_resist = f"""SELECT [{vParam[23]}] FROM TABELA_32_TB_RESIST_TERM
                                 WHERE METODO = '{vTipoLinha[3]}' """
        
                conn.cursor.execute(query_resist)
        
                vFatorCorrecaoResist = conn.cursor.fetchone()
        
                query_profu = f"""SELECT [{vParam[22]}] FROM TB_FATOR_CORRECAO_PROFUNDIDADE
                                 WHERE METODO = '{vTipoLinha[3]}' """
        
                conn.cursor.execute(query_profu)
        
                vFatorCorrecaoProfu = conn.cursor.fetchone()
            
            # else:
            #     vFatorCorrecaoProfu[0]=1
        
        # {{vParam[21]}} temp meio ambiente
        # vParam[19] diametro blindagem

        vMaxCCCAdmCond = vConstMaterial[2] * vParam[31] * math.sqrt( ( 1 / vParam[20] * (math.log ( ( vTempCc[0] + vConstMaterial[1] ) / ( vTemp + vConstMaterial[1] ) ) ) ) ) /1000
        vMaxCCCAdmCondutor = "%.2f" % round(vMaxCCCAdmCond,2)

        vMaxCCCAdmBlind = vConstMaterial[2] * vParam[19] * math.sqrt( ( 1 / vParam[20] * (math.log ( ( vTempBlindagem[0] + vConstMaterial[1] ) / ( vTemp + vConstMaterial[1] ) ) ) ) ) /1000
        vMaxCCCAdmBlindagem = "%.2f" % round(vMaxCCCAdmBlind,2)

        vQuedaT = cNominalVeia * vParam[17] * (3**(1/2)) * (((vRca * vParam[7]) + (vXl * vFatorpot))) / 1000
        vQuedaTensao = "%.2f" % round(vQuedaT,2)

        vQuedaTPercent = ( vQuedaT / ( vParam[3] * math.sqrt(3) * 1000)) 
        vQuedaTensaoPercent = "%.2f" % round(vQuedaTPercent * 100,2) 

        tituloFatorGrupo = 'Sem fator de correção por agrupamento aplicado (cabo isolado).'
        vFatorGrupo = 1
        vGrupo = [1,1,1,1,1]

        vFats = ['A1','A2','B1','B2']
        for fat in vFats:
            if fat in str(vTipoLinha[3]):          
                if "Unipolar" in str({vParam[28]}):
                    conn.cursor.execute(f"""SELECT * 
                                            FROM TABELA_34_FATORES_CORRECAO_CABOS_UNIPOLARES_REF_A1
                                            WHERE ID = { vParam[32] } """) 
                    tituloFatorGrupo ="Fator de correção para grupos de cabos unipolares dispostos em trifólio ao ar livre Tabela 34 NBR:14039 Métodos A1, A2, B1, B2"
                else:        
                    conn.cursor.execute(f"""SELECT * 
                                            FROM TABELA_35_FATORES_CORRECAO_CABOS_TRIPOLARES_REF_A1
                                            WHERE ID = { vParam[32] } """) 
                    tituloFatorGrupo ='Fator de correção para grupos de cabos tripolares dispostos em trifólio ao ar livre Tabela 35 NBR:14039 Métodos A1, A2, B1, B2'
                vGrupo = conn.cursor.fetchone()                      
                vFatorGrupo = vGrupo[4]

        if vTipoLinha[3] == 'F1': 
                    
            if vParam[31] < 185:
                vSecao = '10 a 150'
            else:
                vSecao = '185 a 1000'

            if vParam[24] > 1 and vParam[25] != 'N/A' and vParam[25] != 'Único':
                conn.cursor.execute(f""" SELECT [{vParam[25]}] FROM TABELA_36_FATOR_CORRECAO_F1 
                                          WHERE [Número de dutos] = {vParam[24]} 
                                            AND [Seção condutor mm2] = '{vSecao}' """)
            
                vGrupo = conn.cursor.fetchone()                      
                vFatorGrupo = vGrupo[0]
                tituloFatorGrupo = 'Fator de correção espaçamento de eletrodutos (Tabela 36 - NBR:14039 - Método F1)'
            else: 
                vFatorGrupo = 1.0          

        if vTipoLinha[3] == 'F2': 
            
            if vParam[31] < 185:
                vSecao = '10 a 150'
            else:
                vSecao = '185 a 1000'

            if vParam[24] > 1:
                conn.cursor.execute(f""" SELECT [{vParam[24]}] FROM TABELA_37_FATOR_CORRECAO_F2  
                                          where [Seção condutor mm2] = '{vSecao}' """)
            
                vGrupo = conn.cursor.fetchone()                      
                vFatorGrupo = vGrupo[0]
                tituloFatorGrupo = 'Fator de correção espaçamento de eletrodutos (Tabela 37 - NBR:14039 - Método F2)'
            else: 
                vFatorGrupo = 1.0           


        if vTipoLinha[3] == 'G1': 
            if vParam[31] < 70:
                vSecao = '10_50'
            elif vParam[31] >= 70 and vParam[31] < 185:
                vSecao = '70_150'
            elif vParam[31] >= 185 and vParam[31] < 500:
                vSecao = '185_400'
            elif vParam[31] >= 500:
                vSecao = '500_1000'           

            if vParam[26] > 0 and (vParam[25] == '200' or vParam[25] == '400' or vParam[25] == '600' or vParam[25] == '800'):    
                
                conn.cursor.execute(f""" SELECT [{vParam[25]}] FROM TABELA_38_FATOR_CORRECAO_G1  
                                          where [Seção condutor mm2] = '{vSecao}' 
                                          and [Número de dutos] = {vParam[26]} """)
            
                vGrupo = conn.cursor.fetchone()                      
                vFatorGrupo = vGrupo[0]
                tituloFatorGrupo = 'Fator de correção espaçamento de eletrodutos (Tabela 38 - NBR:14039 - Método G1)'
            else: 
                vFatorGrupo = 1.0


        if vTipoLinha[3] == 'G2': 

            if vParam[31] < 120:
                vSecao = '10 a 120'
            elif vParam[31] >= 150 and vParam[31] < 300:
                vSecao = '150 a 300'
            elif vParam[31] >= 400:
                vSecao = '400 a 1000'

            if vParam[26] == 6 or vParam[26] == 3 or vParam[26] == 9:    
                
                conn.cursor.execute(f""" SELECT [{vParam[26]}] FROM TABELA_39_FATOR_CORRECAO_G2 
                                          where [Seção condutor mm2] = '{vSecao}' """)
            
                vGrupo = conn.cursor.fetchone()                      
                vFatorGrupo = vGrupo[0]
                
                tituloFatorGrupo = 'Fator de correção espaçamento de eletrodutos (Tabela 39 - NBR:14039 - Método G2)'
            else: 
                vFatorGrupo = 1.0
            
            # TABELA_39_FATOR_CORRECAO_G2

        if vTipoLinha[3] == 'H':
            conn.cursor.execute(f""" SELECT * FROM TABELA_40_FATOR_CORRECAO_H """)
            vGrupo = conn.cursor.fetchone()
            
            
            if (vParam[18] * 3) == 6:
                vFatorGrupo = vGrupo[0]
                tituloFatorGrupo = 'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 40 - NBR:14039 - Método H)'
            elif (vParam[18] * 3) == 9:
                vFatorGrupo = vGrupo[1]
                tituloFatorGrupo = 'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 40 - NBR:14039 - Método H)'
            elif (vParam[18] * 3) == 12:
                vFatorGrupo = vGrupo[2]
                tituloFatorGrupo = 'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 40 - NBR:14039 - Método H)'
            else: 
                vFatorGrupo = 1.0
            

        if vTipoLinha[3] == 'I': 
            
            if vParam[27]=="2·De":
                conn.cursor.execute(f""" SELECT * FROM TABELA_41_FATOR_CORRECAO_I 
                                         WHERE [Espaçamento entre centros de cabos] = '2·De' """)
                vGrupo = conn.cursor.fetchone()
            
            if vParam[27]=="200 mm":
                if vParam[31] < 120:
                    vSecao = '10 a 120'
                elif vParam[31] >= 150 and vParam[31] < 300:
                    vSecao = '150 a 300'
                elif vParam[31] >= 400:
                    vSecao = '400 a 1000'

                conn.cursor.execute(f""" SELECT * FROM TABELA_41_FATOR_CORRECAO_I 
                                         WHERE [Espaçamento entre centros de cabos] = '200 mm' 
                                         AND [Seção condutor mm2] = '{vSecao}' """)
                vGrupo = conn.cursor.fetchone()

            if (vParam[18] * 3) == 3:
                vFatorGrupo = vGrupo[2]
                tituloFatorGrupo = 'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 41 - NBR:14039 - Método I)'
            elif (vParam[18] * 3) == 6:
                vFatorGrupo = vGrupo[3]
                tituloFatorGrupo = 'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 41 - NBR:14039 - Método I)'
            elif (vParam[18] * 3) == 9:
                vFatorGrupo = vGrupo[4]
                tituloFatorGrupo = 'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 41 - NBR:14039 - Método I)'
            elif (vParam[18] * 3) == 12:
                vFatorGrupo = vGrupo[5]
                tituloFatorGrupo = 'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 41 - NBR:14039 - Método I)'
            else:
                vFatorGrupo = 1.0      

            

        maxCCveia = vMetodoInstall[0] * (vFatorCorrecaoTemp[3] * vFatorCorrecaoProfu[0] * vFatorGrupo * vFatorCorrecaoResist[0])
        
        ccTotalVeias = maxCCveia * vParam[18]
        
        potenciaTotalConducao = ccTotalVeias * vParam[3] * math.sqrt(3)

        if ( cNominalVeia / maxCCveia ) <= 1:
            resultado4 = 'APROVADO'
        else:
            resultado4 = 'REPROVADO'    

        maxCCveia = "%.2f" % round(maxCCveia,2) 
        
        ccTotalVeias = "%.2f" % round(ccTotalVeias,2) 

        potenciaTotalConducao = "%.1f" % round(potenciaTotalConducao,1) 


        if ((vQuedaTPercent*100) / vParam[6] ) <= 1:
            resQuedaTensao = 'APROVADO'
        else:
            resQuedaTensao = 'REPROVADO'

        if (vParam[12]) == '':
            cccZtrafo = 1
        else:
            cccZtrafo = vParam[12] 

 

        if (vParam[10]) == '':
            cccSistema = 1
        else:
            cccSistema = vParam[10]

        ccc = [cccSistema, cccp_barramento, cccZtrafo]
        cccBarramentoZtrafo = max(ccc,key=int)

        if (vMaxCCCAdmCond / cccBarramentoZtrafo ) > 1:
            resMaxCCCAdmCondutor = 'APROVADO'
        else:
            resMaxCCCAdmCondutor = 'REPROVADO'
        
        if (vMaxCCCAdmBlind / vParam[13] ) > 1:
            resMaxCCCAdmBlindagem = 'APROVADO'
        else:
            resMaxCCCAdmBlindagem = 'REPROVADO'

        if (resultado4 =='APROVADO' and resQuedaTensao=='APROVADO' and resMaxCCCAdmCondutor == 'APROVADO' and resMaxCCCAdmBlindagem == 'APROVADO'):
            resFinal = f'Cabos de {vParam[31]} mm² APROVADO'
        else: 
            resFinal = f'REPROVADO. RECALCULAR'


        round_cNominalVeia = "%.2f" % round(cNominalVeia,2)

        vArranjo = [
                    vTipoLinha[1],            #  Método de Instalação (Tabela 25 – NBR14039):
                    vTipoLinha[4],            #  Texto Metodo Instalação
                    vInstalacao,              #  Instalação:
                    calculo,                  #  Corrente no condutor calculada(A):
                    considerada,              #  Corrente total considerada (A):
                    cccp_barramento,          #  Corrente de Curto Circuito presente no Barramento ( 10x In ) (kA):
                    vTipoLinha[2],            #  Tipo de Instalação: 
                    vAngulo,                  #  vArranjo[7]
                    fPotencia,                #  vArranjo[8]
                    round_cNominalVeia,       #  vArranjo[9]
                    vRca,                     #  vArranjo[10]
                    vXl,                      #  vArranjo[11]
                    vMetodoInstall[0],        #  vArranjo[12] -> Capacidade de condução de corrente máxima no condutor (A) - (Tabela 29 - NBR14039):
                    vTemp,                    #  vArranjo[13] -> Temperatura do condutor - Tc(ºC):
                    vTempCc[0],               #  vArranjo[14] -> Temperatura do condutor durante um Curto Circuito - T2 (ºC):
                    vTempBlindagem[0],        #  vArranjo[15] -> Temperatura da blindagem durante um Curto Circuito - T2 (ºC):
                    vConstMaterial[1],        #  vArranjo[16] -> Valor da constante β
                    vConstMaterial[2],        #  vArranjo[17] -> Valor da constante K
                    vFatorCorrecaoTemp[3],    #  vArranjo[18] -> FatorCorrecaoTemp
                    vMaxCCCAdmCondutor,       #  vArranjo[19] -> 6- Condutor - Máxima corrente de curto circuito admissível (kA) (Regime Normal):
                    vMaxCCCAdmBlindagem,      #  vArranjo[20] -> 7- Blindagem - Máxima corrente de curto circuito admissível (kA) (Regime Normal):
                    vQuedaTensao,             #  vArranjo[21] -> 5 - Queda de tensão - ∆V (V):
                    vQuedaTensaoPercent,      #  vArranjo[22] -> 5 - Queda de tensão - ∆V% (%):
                    vFatorCorrecaoResist[0],  #  vArranjo[23] -> 3 - Fator de correção Resistividade Térmica do solo
                    tituloFCorrecaoResis,     #  vArranjo[24] -> tituloFCorrecaoResis
                    tituloFCorrecaoProfu,     #  vArranjo[25] -> tituloFCorrecaoProfu
                    vFatorCorrecaoProfu[0],   #  vArranjo[26] -> 3 - Fator de correção de correção por profundidade (Tabela 33 - NBR:14039)
                    tituloFatorGrupo,         #  vArranjo[27] -> 3 - fator de correção por agrupamento aplicado (cabo isolado).
                    vFatorGrupo,              #  vArranjo[28] -> 3  
                    maxCCveia,                #  vArranjo[29] -> 4 - Máxima corrente de condução por veia (A):
                    ccTotalVeias,             #  vArranjo[30] -> 4 - Corrente de condução total - Todas as veias (A):
                    potenciaTotalConducao,    #  vArranjo[31] -> 4 - Potência Total de Condução dos Cabos (MVA):
                    resultado4,               #  vArranjo[32] -> 4 - RESULTADO
                    resQuedaTensao,           #  vArranjo[33] -> 5 - RESULTADO resQuedaTensao
                    resMaxCCCAdmCondutor,     #  vArranjo[34] -> 6 - RESULTADO resMaxCCCAdmCondutor
                    cccBarramentoZtrafo,      #  vArranjo[35] -> 1 - Corrente de Curto Circuito presente no Barramento (Calculada – Z% Trafo) (A):
                    resMaxCCCAdmBlindagem,    #  vArranjo[36] -> 7.1 CÁLCULO DE CURTO CIRCUITO NA BLINDAGEM
                    resFinal                  #  vArranjo[37] -> 8 resultados finais
                    ]

        if vGerarPdf:
            
            arquivoPdf = gerarPdf( vDados, vParam, vArranjo )       

            return send_file(arquivoPdf, mimetype='application/pdf')    

        return render_template('relatorio.html', vDados = vDados, vParam = vParam, vArranjo = vArranjo)
        
    else:
        
        return redirect(f'/parametros?id={id}&erro=True')



@app.route('/upload', methods=['POST'])
def reg():
    if request.method == 'POST':

        data = []
       
        data.append(request.form.get('id_parametros_proj'))
        data.append(request.form.get('cargas'))
        data.append(request.form.get('potencia'))
        data.append(request.form.get('tensao'))
        data.append(request.form.get('fator_corrente'))
        data.append(request.form.get('corrente_total'))
        data.append(request.form.get('queda_maxima'))
        data.append(request.form.get('fator_potencia'))
        data.append(request.form.get('potencia_trafo'))
        data.append(request.form.get('impedancia_trafo'))
        data.append(request.form.get('corrente_cc_sistema'))
        data.append(request.form.get('corrente_cc_barramento'))
        data.append(request.form.get('corrente_cc_barramento_calc'))
        data.append(request.form.get('corrente_cc_fase_terra'))
        data.append(request.form.get('isolacao'))
        data.append(request.form.get('material'))
        data.append(request.form.get('classe'))
        data.append(request.form.get('comp_cabo_fase'))
        data.append(request.form.get('num_cabo_fase'))
        data.append(request.form.get('diametro_blindagem'))
        data.append(request.form.get('tempo_cc'))
        data.append(request.form.get('temp_ambiente'))
        data.append(request.form.get('profundidade_cabo'))
        data.append(request.form.get('resistividade_solo')) 
        data.append(request.form.get('num_dutos_F1')) 
        data.append(request.form.get('espaco_eletrodutos')) 
        data.append(request.form.get('num_dutos_G1')) 
        data.append(request.form.get('espaco_cabos')) 
        data.append(request.form.get('arranjo')) 
        data.append(request.form.get('metodo_install')) 
        data.append(request.form.get('metodo'))
        data.append(request.form.get('diametro_cabo'))
        data.append(request.form.get('m_instal_id'))

        param = '?,' * 32
        
        conn.cursor.execute(f"DELETE FROM TB_PARAM_PROJETO WHERE id_parametros_proj = {data[0]}").rowcount
        conn.cnxn.commit()
        
        conn.cursor.execute(f"INSERT INTO TB_PARAM_PROJETO VALUES ({param}?)", data ).rowcount
        conn.cnxn.commit()
        
        hUpdate = datetime.datetime.now()
        
        conn.cursor.execute(f""" UPDATE TB_PROJETOS SET data_atualizacao = '{hUpdate}' WHERE ID = {data[0]} """)
        
        conn.cnxn.commit()

        return redirect(f'/relatorio?id={data[0]}')
    



def gerarPdf( vDados, vParam, vArranjo ):
      
    options = {
        "enable-local-file-access": "",
        "orientation": "portrait",
        "page-size": "A4",
        "margin-top": "1.0cm",
        "margin-right": "1.0cm",
        "margin-bottom": "1.0cm",
        "margin-left": "1.0cm",
        "encoding": "UTF-8",
    }
    
    pdf_content = render_template('relatorioPdf.html', vDados = vDados, vParam = vParam, vArranjo = vArranjo)
    
    config = pdfkit.configuration(wkhtmltopdf=rf'{pastaApp}\pdfkit\wkhtmltopdf.exe') 

    pdf_file = pdfkit.from_string(pdf_content, False, configuration=config, options=options)


    pdfFileName = re.sub('[^A-Za-z0-9]+', '', vDados[1])

    out = open(fr'{pastaApp}\pdfkit\{pdfFileName}.pdf', 'wb')

    out.write(pdf_file)

    out.close()

    return (fr'{pastaApp}\pdfkit\{pdfFileName}.pdf')

    

app.run(host='localhost', port=8080, debug=True)

# import logging
# log = logging.getLogger('werkzeug')
# log.setLevel(logging.ERROR)
# log.disabled = True

# if __name__ == "__main__":
#     print("Software de Dimensionamento de cabos inicializado com sucesso \n Acesse no navegador http://localhost:8080 ")
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080, threads=100)