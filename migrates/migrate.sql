

create table TB_PARAM_PROJETO (
id_parametros_proj INTEGER REFERENCES TB_PROJETOS(ID) ON UPDATE CASCADE,
cargas varchar(200),
potencia varchar(200),
tensao varchar(200),
fator_corrente varchar(200),
corrente_total varchar(200),
queda_maxima varchar(200),
fator_potencia varchar(200),
potencia_trafo varchar(200),
impedancia_trafo varchar(200),
corrente_cc_sistema varchar(200),
corrente_cc_barramento varchar(200),
corrente_cc_barramento_calc varchar(200),
corrente_cc_fase_terra varchar(200),
isolacao varchar(200),
material varchar(200),
classe varchar(200),
comp_cabo_fase varchar(200),
num_cabo_fase varchar(200),
diametro_blindagem varchar(200),
tempo_cc varchar(200),
temp_ambiente varchar(200),
profundidade_cabo float,
resistividade_solo float,
num_dutos_F1 integer,
espaco_eletrodutos varchar(10),
num_dutos_G1 integer,
espaco_cabos varchar(100),
arranjo varchar(100),
metodo_install varchar(100))


data.append(request.form.get('cargas'))
data.append(request.form.get('potencia'))
data.append(request.form.get('tensao'))
data.append(request.form.get('fator_corrente'))
data.append(request.form.get('corrente_total  '))
data.append(request.form.get('queda_maxima'))
data.append(request.form.get('fator_potencia'))
data.append(request.form.get('potencia_trafo'))
data.append(request.form.get('impedancia_trafo'))
data.append(request.form.get('corrente_cc_sistema'))
data.append(request.form.get('corrente_cc_barramento'))
data.append(request.form.get('corrente_cc_barramento_calc'))
data.append(request.form.get('corrente_cc_fase_terra'))
data.append(request.form.get('comp_cabo_fase'))
data.append(request.form.get('num_cabo_fase'))
data.append(request.form.get('diametro_blindagem '))
data.append(request.form.get('tempo_cc'))