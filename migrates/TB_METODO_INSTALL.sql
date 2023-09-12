-- SQLite


create table TB_METODO_INSTALL (
TIPO VARCHAR(100),
[Seção do condutor mm2] integer,
A1  INTEGER,
A2  INTEGER,
B1  INTEGER,
B2  INTEGER,
C   INTEGER,
D   INTEGER,
E   INTEGER,
F1  INTEGER,
F2  INTEGER,
G1  INTEGER,
G2  INTEGER,
H   INTEGER,
I   INTEGER);


INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	10	,86	,70	,104	,94	,78	,93	,69	,59	,63	,66	,73	,64	,68   ;
INSERT INTO TB_METODO_INSTALL SELECT 	'COBRE_90', 	16	,113	,92	,136	,123	,101	,123	,90	,75	,81	,84	,93	,82	,87   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	25	,148	,120	,179	,162	,131	,164	,117	,97	,104	,107	,119	,105	,110  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	35	,180	,147	,219	,197	,159	,202	,142	,116	,124	,127	,142	,125	,131  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	50	,218	,177	,264	,238	,190	,246	,170	,137	,147	,149	,167	,147	,154  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	70	,272	,220	,329	,296	,236	,309	,211	,167	,179	,180	,202	,178	,187  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	95	,332	,269	,400	,360	,286	,379	,255	,200	,214	,213	,239	,211	,221  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	120	,384	,311	,461	,413	,328	,439	,294	,227	,243	,239	,269	,238	,249  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	150	,437	,352	,514	,460	,369	,492	,330	,251	,269	,256	,292	,262	,270  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	185	,498	,403	,583	,522	,419	,561	,375	,282	,301	,283	,324	,293	,300  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	240	,588	,474	,678	,605	,488	,656	,438	,324	,345	,319	,366	,334	,340  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	300	,670	,540	,767	,683	,551	,745	,494	,361	,383	,349	,403	,370	,375  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	400	,760	,618	,844	,750	,602	,823	,550	,394	,417	,360	,424	,401	,395  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	500	,856	,694	,943	,837	,669	,922	,615	,434	,458	,389	,461	,440	,429  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	630	,958	,776	,1048	,929	,736	,1028	,683	,475	,500	,416	,497	,478	,464  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	800	,1064	,858	,1152	,1018	,804	,1134	,755	,517	,541	,444	,532	,516	,497  ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_90', 	1000	,1161	,934	,1250	,1102	,862	,0	,817	,551	,575	,467	,560	,547	,525  ;

INSERT INTO TB_METODO_INSTALL SELECT 	'ALUMINIO_90' , 	10	, 66	,54	,80	,72	,60	,72	,53	,45	,49	,51	,56	,50	,52 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	16	, 87	,71	,106	,96	,78	,96	,70	,58	,63	,65	,72	,64	,67 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	25	, 115	,94	,139	,126	,102	,127	,91	,75	,81	,83	,93	,82	,86 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	35	, 140	,114	,170	,154	,124	,157	,110	,90	,96	,99	,110	,97	,102 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	50	, 169	,137	,206	,186	,148	,192	,132	,106	,114	,117	,130	,114	,120 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	70	, 212	,171	,257	,231	,184	,241	,164	,130	,139	,142	,158	,139	,146 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	95	, 258	,209	,313	,281	,222	,296	,198	,156	,166	,168	,188	,165	,173 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	120	, 300	,242	,362	,325	,255	,345	,229	,178	,189	,190	,213	,186	,196 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	150	, 340	,275	,407	,364	,288	,389	,259	,198	,211	,207	,233	,206	,215 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	185	, 391	,316	,465	,416	,328	,447	,296	,223	,238	,231	,261	,232	,241 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	240	, 463	,374	,545	,486	,385	,527	,349	,259	,275	,263	,298	,267	,275 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	300	, 532	,428	,621	,553	,438	,603	,397	,290	,308	,291	,331	,298	,306 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	400	, 621	,500	,703	,625	,496	,685	,453	,325	,344	,311	,359	,331	,333 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	500	, 716	,577	,799	,709	,574	,781	,517	,366	,386	,341	,396	,370	,368 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	630	, 822	,665	,905	,802	,633	,888	,587	,409	,431	,372	,436	,412	,405 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	800	, 931	,751	,1012	,894	,706	,996	,663	,455	,476	,404	,474	,454	,443 ;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_90' , 	1000	, 1038	,835	,1120	,987	,773	,0	,733	,496	,517	,431	,509	,492	,476 ;


INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       10	, 96	,83	,115	,107	,86	,106	,77	,64	,68	,71	,79	,69	,73    ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       16	, 126	,109	,151	,141	,112	,140	,100	,82	,88	,90	,101	,89	,93    ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       25	, 165	,142	,199	,184	,146	,186	,130	,105	,112	,115	,129	,113	,119   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       35	, 201	,173	,243	,225	,177	,229	,157	,126	,135	,137	,153	,134	,142   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       50	, 243	,210	,294	,272	,212	,278	,189	,149	,159	,161	,181	,158	,166   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       70	, 303	,261	,366	,339	,262	,349	,234	,181	,194	,195	,219	,192	,201   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       95	, 370	,319	,446	,412	,317	,428	,284	,217	,232	,231	,259	,228	,239   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       120	, 428	,369	,514	,474	,364	,495	,327	,247	,264	,260	,292	,257	,269   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       150	, 487	,419	,575	,530	,410	,555	,369	,273	,292	,279	,318	,283	,293   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       185	, 556	,480	,653	,601	,465	,633	,419	,307	,328	,309	,353	,317	,326   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       240	, 656	,565	,760	,699	,542	,741	,490	,353	,376	,349	,400	,362	,370   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       300	, 748	,646	,862	,791	,612	,842	,554	,394	,418	,383	,441	,402	,408   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       400	, 857	,738	,953	,874	,674	,934	,619	,431	,457	,397	,466	,437	,432   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       500	, 967	,832	,1067	,978	,749	,1049	,694	,477	,503	,430	,508	,480	,471   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       630	, 1086	,933	,1191	,1089	,828	,1173	,773	,523	,550	,462	,550	,523	,510   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       800	, 1207	,1035	,1311	,1197	,905	,0	,856	,570	,597	,494	,589	,566	,549   ;
INSERT INTO TB_METODO_INSTALL SELECT	'COBRE_105',       1000	, 1320	,1130	,1426	,1301	,971	,0	,928	,609	,635	,520	,623	,601	,580   ;



INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  10	,74	,64	,89	,82	,66	,81	,59	,49	,53	,55	,61	,53	,56	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  16	,97	,84	,117	,109	,87	,109	,77	,63	,68	,70	,78	,69	,72	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  25	,128	,110	,155	,143	,113	,144	,101	,81	,87	,90	,100	,88	,93	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  35	,156	,134	,189	,175	,137	,178	,122	,97	,104	,107	,119	,104	,110	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  50	,189	,163	,229	,212	,164	,217	,147	,115	,123	,126	,141	,123	,130	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  70	,235	,203	,286	,264	,204	,272	,182	,141	,151	,153	,171	,149	,157	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  95	,287	,248	,348	,322	,246	,334	,220	,169	,180	,182	,203	,177	,187	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  120	,333	,287	,403	,372	,283	,388	,254	,192	,205	,206	,230	,201	,212	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  150	,379	,326	,454	,418	,319	,438	,288	,215	,230	,225	,253	,223	,233	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  185	,435	,376	,519	,478	,364	,504	,330	,242	,259	,251	,283	,250	,261	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  240	,516	,445	,609	,560	,427	,593	,389	,281	,299	,287	,324	,288	,298	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  300	,593	,511	,695	,638	,484	,679	,444	,316	,336	,318	,360	,322	,332	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  400	,692	,597	,789	,724	,559	,773	,508	,355	,375	,341	,392	,359	,362	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  500	,800	,691	,899	,823	,638	,883	,580	,399	,422	,375	,435	,402	,402	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  630	,923	,795	,1021	,934	,726	,1006	,661	,448	,471	,410	,479	,448	,444	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  800	,1050	,900	,1144	,1045	,790	,1130	,747	,499	,522	,446	,523	,495	,486	;
INSERT INTO TB_METODO_INSTALL SELECT	'ALUMINIO_105',  1000	,1174	,1005	,1270	,1158	,866	,0	,828	,545	,568	,478	,562	,538	,524	;
