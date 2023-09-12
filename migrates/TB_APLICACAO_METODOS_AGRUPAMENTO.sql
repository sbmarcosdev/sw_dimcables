-- SQLite

CREATE TABLE TB_APLICACAO_METODOS_AGRUPAMENTO

(ID INTEGER ,
FATOR FLOAT,
DESCRICAO_FATOR VARCHAR(200)) ;


INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 1,	1.00,'Fator de correção para grupos de cabos unipolares dispostos em trifólio ao ar livre (Tabela 34 - NBR:14039 - Métodos A1, A2, B1, B2)';
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 2,	0.00,'Fator de correção para grupos de cabos unipolares dispostos em trifólio ao ar livre (Tabela 35 - NBR:14039 - Métodos A1, A2, B1, B2)';										
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 3,	0.00,'Fator de correção espaçamento de eletrodutos (Tabela 36 - NBR:14039 - Método F1)';		
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 4,	0.00,'Fator de correção espaçamento de eletrodutos (Tabela 37 - NBR:14039 - Método F2)';										
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 5,	0.00,'Fator de correção espaçamento de eletrodutos (Tabela 38 - NBR:14039 - Método G1)';										
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 6,	0.00,'Fator de correção espaçamento de eletrodutos (Tabela 39 - NBR:14039 - Método G2)';										
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 7,	0.00,'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 40 - NBR:14039 - Método H)';
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 8,	0.00,'Fator de correção espaçamento de cabos diretamente enterrados (Tabela 41 - NBR:14039 - Método I)';										
INSERT INTO TB_APLICACAO_METODOS_AGRUPAMENTO SELECT 9,	1.00,'Sem fator de correção por agrupamento aplicado (cabo isolado).';										



