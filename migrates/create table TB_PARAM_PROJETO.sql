create table TB_PARAM_PROJETO (
id_parametros_proj INTEGER REFERENCES TB_PROJETOS(ID) ON UPDATE CASCADE,
cargas int,
potencia float,
tensao float,
fator_corrente float,
corrente_total float,
queda_maxima float,
fator_potencia float,
potencia_trafo float,
impedancia_trafo float,
corrente_cc_sistema float,
corrente_cc_barramento float,
corrente_cc_barramento_calc float,
corrente_cc_fase_terra float,
isolacao varchar(200),
material varchar(200),
classe varchar(200),
comp_cabo_fase float,
num_cabo_fase int,
diametro_blindagem float,
tempo_cc float,
temp_ambiente float,
profundidade_cabo float,
resistividade_solo float,
num_dutos_F1 integer,
espaco_eletrodutos varchar(10),
num_dutos_G1 integer,
espaco_cabos varchar(100),
arranjo varchar(100),
metodo_install varchar(100),
mInstallRadio varchar(100),
diametro_cabo float);
--drop table TB_PARAM_PROJETO