-- SQLite


-- create table TABELA_34_FATORES_CORRECAO_CABOS_UNIPOLARES_REF_A1 (
-- GRUPO VARCHAR(200),
-- ESQUEMA_ILUSTRATIVO VARCHAR(500),
-- ESPACAMENTO_A_B VARCHAR(100),
-- FATOR_CORRECAO FLOAT     
-- );



-- create table TABELA_35_FATORES_CORRECAO_CABOS_TRIPOLARES_REF_A1 (
-- GRUPO VARCHAR(200),
-- ESQUEMA_ILUSTRATIVO VARCHAR(500),
-- ESPACAMENTO_A_B VARCHAR(100),
-- FATOR_CORRECAO FLOAT     
-- ) ;


CREATE TABLE TABELA_36_FATOR_CORRECAO_F1
(
[Número de dutos] integer,
[Seção condutor mm2] varchar(100),
Encostados float,
[200] float,
[400] float,
[600] float,
[800] float
);


insert into TABELA_36_FATOR_CORRECAO_F1 select 	2,'10 a 150',0.8,0.84,0.88,0.91,0.93;	
insert into TABELA_36_FATOR_CORRECAO_F1 select 		2		,'185 a 1000'	,	0.8	,	0.8	,	0.85	,	0.88,		0.9	 ;
insert into TABELA_36_FATOR_CORRECAO_F1 select 		3		,'10 a 150'	,	0.68	,	0.74	,	0.8	,	0.84,		0.87	 ;
insert into TABELA_36_FATOR_CORRECAO_F1 select 		3		,'185 a 1000'	,	0.68	,	0.69	,	0.75	,	0.8,		0.83	;
insert into TABELA_36_FATOR_CORRECAO_F1 select 		4		,'10 a 150'	,	0.62	,	0.69	,	0.76	,	0.81,		0.84	;
insert into TABELA_36_FATOR_CORRECAO_F1 select 		4		,'185 a 1000'	,	0.62	,	0.64	,	0.71	,	0.76,		0.8	;

CREATE TABLE TABELA_37_FATOR_CORRECAO_F2
([Seção condutor mm2] varchar(100),
[2] float,
[3] float,
[4] float);

insert into TABELA_37_FATOR_CORRECAO_F2 select 	'10 a 150'	,0.84	,			0.73		,		0.65	;		
insert into TABELA_37_FATOR_CORRECAO_F2 select 	'185 a 1000'	,0.81	,			0.69		,		0.61	;		


CREATE TABLE TABELA_38_FATOR_CORRECAO_G1
([Número de dutos] integer,
[Seção condutor mm2] varchar(100),
[200] float,
[400] float,
[600] float,
[800] float);

insert into TABELA_38_FATOR_CORRECAO_G1 select 3      	, '10_50', 			1.06	,	1.1	,	1.12	,	1.14	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 3     	, '70_150', 			1	,	1.01	,	1.02	,	1.02	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 3      	, '185_400', 			0.97	,	0.93	,	0.92	,	0.92	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 3      	, '500_1000', 			0.97	,	0.92	,	0.89	,	0.88	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 6		, '10_50', 	 			0.92	,	1	,	1.05	,	1.09	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 6		, '70_150',  			0.86	,	0.91	,	0.95	,	0.97	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 6		, '185_400',  			0.82	,	0.83	,	0.85	,	0.86	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 6		, '500_1000', 			0.82	,	0.81	,	0.81	,	0.82	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 9		, '10_50', 			0.85	,	0.95	,	1.02	,	1.07	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 9		, '70_150', 		0.79	,	0.87	,	0.91	,	0.95	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 9		, '185_400', 		0.75	,	0.79	,	0.82	,	0.84	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 9		, '500_1000',		0.74	,	0.76	,	0.78	,	0.8	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 12		, '10_50', 				0.81	,	0.93	,	1	,	1.05	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 12		, '70_150', 			0.75	,	0.84	,	0.9	,	0.93	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 12		, '185_400',  			0.71	,	0.77	,	0.8	,	0.83	;
insert into TABELA_38_FATOR_CORRECAO_G1 select 12		, '500_1000', 			0.7	,	0.74	,	0.77	,	0.78	;
																				
					



CREATE TABLE TABELA_39_FATOR_CORRECAO_G2
([Seção condutor mm2] varchar(100),
[6] float,
[3] float,
[9] float);

insert into TABELA_39_FATOR_CORRECAO_G2 select 	'10 a 120',	0.99	,0.78	,0.67;  
insert into TABELA_39_FATOR_CORRECAO_G2 select 	'150 a 300',	0.95	,0.71	,0.61;  
insert into TABELA_39_FATOR_CORRECAO_G2 select 	'400 a 1000',	0.94	,0.67	,0.57;  

CREATE TABLE TABELA_40_FATOR_CORRECAO_H	
([Seis condutores isolados] FLOAT,
[Nove condutores isolados] FLOAT,
[12 condutores isolados] float);


INSERT INTO TABELA_40_FATOR_CORRECAO_H SELECT 0.76, 0.65,0.58;			



CREATE TABLE TABELA_41_FATOR_CORRECAO_I	
([Espaçamento entre centros de cabos] varchar(100),
[Seção condutor mm2] varchar(100),
[Número de cabos 3] FLOAT,
[Número de cabos 6] FLOAT,
[Número de cabos 9] FLOAT,
[Número de cabos 12] FLOAT);


	
INSERT INTO TABELA_41_FATOR_CORRECAO_I SELECT '2·De',	'Todas'			,	1	,	0.78	,	0.68	,	0.61	 ;
INSERT INTO TABELA_41_FATOR_CORRECAO_I SELECT '200 mm',	'10 a 120'		,	1.06	,	0.9	,	0.82	,	0.78	 ;
INSERT INTO TABELA_41_FATOR_CORRECAO_I SELECT '200 mm',	'150 a 300'		,	0.97	,	0.81	,	0.74	,	0.7	 ;
INSERT INTO TABELA_41_FATOR_CORRECAO_I SELECT '200 mm',	'400 a 1000'		,	0.92	,	0.76	,	0.68	,	0.64	 ;


CREATE TABLE TABELA_42_MATERIAL(
[Material] VARCHAR(100),
[β (°C)] FLOAT,
[K (A.s1/2.mm–2)] FLOAT);


INSERT INTO TABELA_42_MATERIAL SELECT 'Cobre',	234.5,	226;
INSERT INTO TABELA_42_MATERIAL SELECT 'Alumínio',228,	148;

CREATE TABLE TABELA_43_TEMP_CURTO(
[Material da isolação] VARCHAR(100),
[Temperatura inicial °C] INTEGER,
[Temperatura final °C a] INTEGER);

INSERT INTO TABELA_43_TEMP_CURTO SELECT 'EPR e HEPR'	,			90	,				250;	
INSERT INTO TABELA_43_TEMP_CURTO SELECT 'EPR 105'	,			105	,				250;	
INSERT INTO TABELA_43_TEMP_CURTO SELECT 'XLPE e TR XLPE',			90	,				250;	


CREATE TABLE TABELA_44_TEMP_BLINDAGEM_CURTO(
[Material da cobertura] VARCHAR(100),	
[Temperatura final máxima °C a, b] INTEGER);


INSERT INTO TABELA_44_TEMP_BLINDAGEM_CURTO SELECT 'SE1/A, SHF2 e SE1/B c', 220;
INSERT INTO TABELA_44_TEMP_BLINDAGEM_CURTO SELECT 'ST3 c', 150;
INSERT INTO TABELA_44_TEMP_BLINDAGEM_CURTO SELECT 'SHF1 e ST7 c', 180;
INSERT INTO TABELA_44_TEMP_BLINDAGEM_CURTO SELECT 'ST1 e ST2 c', 200;

