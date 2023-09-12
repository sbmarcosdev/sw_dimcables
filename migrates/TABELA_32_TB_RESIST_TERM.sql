-- SQLite

create table TABELA_32_TB_RESIST_TERM 
(METODO VARCHAR(10),
[1.0] FLOAT,
[1.5] FLOAT,
[2.0] FLOAT,
[2.5] FLOAT,
[3.0] FLOAT,
[4.0] FLOAT);


INSERT INTO TABELA_32_TB_RESIST_TERM SELECT	'F1'    	,	1.24	,1.14	,1.06	,1	,0.93	,0.83	;
INSERT INTO TABELA_32_TB_RESIST_TERM SELECT	'F2'    	,	1.14	,1.09	,1.04	,1	,0.94	,0.85	;
INSERT INTO TABELA_32_TB_RESIST_TERM SELECT	'G1'    	,	1.31	,1.18	,1.08	,1	,0.93	,0.82	;
INSERT INTO TABELA_32_TB_RESIST_TERM SELECT	'G2'    	,	1.15	,1.09	,1.04	,1	,0.94	,0.85	;
INSERT INTO TABELA_32_TB_RESIST_TERM SELECT	'H'    		,	1.45	,1.23	,1.09	,1	,0.91	,0.8	;
INSERT INTO TABELA_32_TB_RESIST_TERM SELECT	'I'    		,	1.44	,1.23	,1.09	,1	,0.91	,0.8	;


-- DROP TABLE TB_RESIST_TERM;

--SELECT [3] FROM TABELA_32_TB_RESIST_TERM WHERE METODO = 'F1'