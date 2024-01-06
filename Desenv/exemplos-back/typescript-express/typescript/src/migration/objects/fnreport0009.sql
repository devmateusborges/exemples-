Drop FUNCTION IF EXISTS fnreport0009;
CREATE OR REPLACE FUNCTION fnreport0009(
pParUnitId varchar, 
pParIndRelId varchar, 
pVart01 varchar, 
pVard01 varchar, 
pVart02 varchar default null,
pVard02 varchar default null,
pVart03 varchar default null,
pVard03 varchar default null,
pVart04 varchar default null,
pVard04 varchar default null,
pVart05 varchar default null,
pVard05 varchar default null,
pParFinPagRecES varchar default null,
pParGerPessoaNome varchar default null,
pParGerPessoaPagRecNome varchar default null,
pParFinPagRecDataMovIni varchar default null,
pParFinPagRecDataMovFin varchar default null,
pParFinPagRecNumeroDocPagRec varchar default null,
pParFinPagRecParcValorPagRecIni varchar default null,
pParFinPagRecParcValorPagRecFin varchar default null,
pParFinPagRecParcValorJuroIni varchar default null,
pParFinPagRecParcValorJuroFin  varchar default null,
pParFinPagRecParcValorDescontoIni varchar default null,
pParFinPagRecParcValorDescontoFin varchar default null,
pParFinPagRecParcValorMultaIni varchar default null,
pParFinPagRecParcValorMultaFin varchar default null,
pParFinPagRecParcDataVencIni varchar default null,
pParFinPagRecParcDataVencFin varchar default null,
pParFinPagRecDataBaixaIni varchar default null,
pParFinPagRecDataBaixaFin varchar default null,
pParLogUserIns varchar default null,
pParLogDateInsIni varchar default null,
pParLogDateInsFin varchar default null,
pParLogUserUpd varchar default null,
pParLogDateUpdIni varchar default null,
pParLogDateUpdFin varchar default null


)
RETURNS TABLE(
 ind_rel_id varchar,
 ind_rel_par1 varchar,
 ind_rel_par2 varchar,
 ind_rel_par3 varchar,
 vart_01 varchar,
 vard_01 varchar,
 vart_02 varchar,
 vard_02 varchar,
 vart_03 varchar,
 vard_03 varchar,
 vart_04 varchar,
 vard_04 varchar,
 vart_05 varchar,
 vard_05 varchar,
 valor_01 numeric,
 valor_02 numeric,
 valor_03 numeric,
 valor_04 numeric,
 valor_05 numeric,
 valor_06 numeric,
 valor_07 numeric,
 valor_08 numeric,
 valor_09 numeric,
 valor_10 numeric) AS $BODY$
declare
vSql varchar;
vPar1 varchar :='';
vPar2 varchar :='';
r record;
begin
		

	
	 if pParFinPagRecES != '' then
		 vPar1 = vPar1||' Entrada/Saída ['||pParFinPagRecES||']'||chr(13)||chr(10);
	 else
			vPar1 = vPar1||' Entrada/Saída []'||chr(13)||chr(10);
	 end if;
	 
	 if pParGerPessoaNome != '' then
		 vPar1 = vPar1||' Nome da Pessoa(s) ['||pParGerPessoaNome||']'||chr(13)||chr(10);
	 else
			vPar1 = vPar1||' Nome da Pessoa(s) []'||chr(13)||chr(10);
	 end if;
	 
	 if pParGerPessoaPagRecNome != '' then
		vPar1 = vPar1||' Nome Pessoa Pag/Rec ['||pParGerPessoaPagRecNome||']'||chr(13)||chr(10);
	 else 
		vPar1 = vPar1||' Nome Pessoa Pag/Rec []'||chr(13)||chr(10);
	 end if;

	 if pParFinPagRecNumeroDocPagRec != '' then
		vPar1 = vPar1||' Numero Documento Pag/Rec ['||pParFinPagRecNumeroDocPagRec||']'||chr(13)||chr(10);
	else 
		vPar1 = vPar1||' Numero Documento Pag/Rec []'||chr(13)||chr(10);
	end if;
	
	if pParLogUserIns != '' then
		vPar1 = vPar1||' Usuario(s) de inserção ['||pParLogUserIns||'] '||chr(13)||chr(10);
	else
			vPar1 = vPar1||' Usuario(s) de inserção [] '||chr(13)||chr(10);
	end if;
	 
	if pParLogUserUpd != '' then
		vPar1 = vPar1||' Usuario(s) de alteração ['||pParLogUserUpd||'] '||chr(13)||chr(10);
	else
		vPar1 = vPar1||' Usuario(s) de alteração [] '||chr(13)||chr(10);	
	end if;
	 

	if pParFinPagRecParcDataVencIni != '' and pParFinPagRecParcDataVencFin != '' then
		vPar1 = vPar1||' Data Vencimento ['||pParFinPagRecParcDataVencIni ||'] até ['||pParFinPagRecParcDataVencFin||'] '||chr(13)||chr(10);
	else
		vPar1 = vPar1||' Data Vencimento [] até [] '||chr(13)||chr(10);
	end if;
	
	------------------------------------------------------------------------------
 if pParFinPagRecDataMovIni != '' and pParFinPagRecDataMovFin != '' then
		vPar2 = vPar2|| 'Data Movimento ['||pParFinPagRecDataMovIni ||'] até ['||pParFinPagRecDataMovFin||'] '||chr(13)||chr(10);
	else
	vPar2 = vPar2|| 'Data Movimento [] até []'||chr(13)||chr(10);
	end if;
	
	
	
	 if pParFinPagRecParcValorPagRecIni != '' and pParFinPagRecParcValorPagRecFin != ''   then
		vPar2 = vPar2|| 'Valor Inicial Pag/Rec ['||pParFinPagRecParcValorPagRecIni ||'] até ['||pParFinPagRecParcValorPagRecFin||'] '||chr(13)||chr(10);
	else
	vPar2 = vPar2|| 'Valor Inicial Pag/Rec [] até [] '||chr(13)||chr(10);
	end if;

	if pParFinPagRecParcValorJuroIni != '' and pParFinPagRecParcValorJuroFin != ''  then
		vPar2 = vPar2|| 'Valor De Juros Inicial Pag/Rec  ['||pParFinPagRecParcValorJuroIni ||'] até ['||pParFinPagRecParcValorJuroFin||'] '||chr(13)||chr(10);
else
		vPar2 = vPar2|| 'Valor De Juros Inicial Pag/Rec [] até [] '||chr(13)||chr(10);
end if;

	 if pParFinPagRecParcValorDescontoIni != '' and pParFinPagRecParcValorDescontoFin != ''  then
			vPar2 = vPar2|| 'Valor De Desconto Inicial ['||pParFinPagRecParcValorDescontoIni ||'] até ['||pParFinPagRecParcValorDescontoFin||'] '||chr(13)||chr(10);
	else
	vPar2 = vPar2|| 'Valor De Desconto Inicial [] até [] '||chr(13)||chr(10);
	end if;

if pParFinPagRecParcValorMultaIni != '' and pParFinPagRecParcValorMultaFin != '' then
		vPar2 = vPar2|| 'Valor Da Multa Inicial ['||pParFinPagRecParcValorMultaIni ||'] até ['||pParFinPagRecParcValorMultaFin||'] '||chr(13)||chr(10);
else
		vPar2 = vPar2|| 'Valor Da Multa Inicial [] até [] '||chr(13)||chr(10);
end if;

if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
		vPar2 = vPar2|| 'Data Inserção ['||pParLogDateInsIni ||'] até ['||pParLogDateInsFin||'] '||chr(13)||chr(10);
else
		vPar2 = vPar2|| 'Data Inserção [] até [] '||chr(13)||chr(10);
end if;

if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
		vPar2 = vPar2|| 'Data Alteração ['||pParLogDateUpdIni ||'] até ['||pParLogDateUpdFin||'] '||chr(13)||chr(10);
else
		vPar2 = vPar2|| 'Data Alteração [] até []'||chr(13)||chr(10);
end if;
	
		
if pParFinPagRecDataBaixaIni != '' and pParFinPagRecDataBaixaFin != '' then
		vPar2 = vPar2|| 'Data Baixa ['||pParFinPagRecDataBaixaIni ||'] até ['||pParFinPagRecDataBaixaFin||'] '||chr(13)||chr(10);
else
		vPar2 = vPar2|| 'Data Baixa [] até []'||chr(13)||chr(10);
end if;
	
	
		
vSql = 'select
    '  || pVart01 ||'   as vart_01 '||
		','''|| pVard01 ||''' as vard_01 ';
		
		if  pVart02 != ''  THEN
		 vSql = vSql || ','  || pVart02 ||'   as vart_02 '||
		           ','''|| pVard02 ||''' as vard_02 ';
		else 
		   vSql = vSql || ',null as vart_02'||
							   ',null as vard_02';
		end if;
    if  pVart03 != '' THEN
		 vSql = vSql || ','  || pVart03 ||'   as vart_03 '||
		           ','''|| pVard03 ||''' as vard_03 ';
		else 
		   vSql = vSql || ',null as vart_03'||
							   ',null as vard_03';
		end if;
    if  pVart04 != '' THEN
		 vSql = vSql || ','  || pVart04 ||'   as vart_04 '||
		           ','''|| pVard04 ||''' as vard_04 ';
		else 
		   vSql = vSql || ',null as vart_04'||
							   ',null as vard_04';
		end if;
    if  pVart05 != ''  THEN
		 vSql = vSql || ','  || pVart05 ||'   as vart_05 '||
		           ','''|| pVard05 ||''' as vard_05 ';
		else 
		   vSql = vSql || ',null as vart_05'||
							   ',null as vard_05';
		end if;
				
		vSql = vSql||' ,sum(t1.fin_pagrec_parc_valor_pagrec) as valor_01
									 ,sum(t1.fin_pagrec_parc_valor_juro)  as valor_02
									 ,sum(t1.fin_pagrec_parc_valor_desconto) as valor_03
									 ,sum(t1.fin_pagrec_parc_valor_multa) as valor_04
									 ,sum(COALESCE((select sum(s1.valor_pagrec) 
									                 from fin_pagrec_baixa s1 
																	 where s1.fin_pagrec_parc_id = t1.fin_pagrec_parc_id ';
									 	 if pParFinPagRecDataBaixaIni != '' and pParFinPagRecDataBaixaFin != ''then
												vSql = vSql ||' and '||'CAST(s1.data_baixa AS DATE)'||' >= '''||pParFinPagRecDataBaixaIni||''''||' 
												                and  CAST(s1.data_baixa AS DATE)'||' <= '''||pParFinPagRecDataBaixaFin||'''';
										end if;
									 
									 vSql = vSql||'),0)) as valor_05,	 
									 (SUM ( t1.fin_pagrec_parc_valor_pagrec )-sum(t1.fin_pagrec_parc_valor_desconto)+
									 SUM ( t1.fin_pagrec_parc_valor_juro )+
									 sum(t1.fin_pagrec_parc_valor_multa)-
								    sum(COALESCE((select sum(s1.valor_pagrec) 
																			 from fin_pagrec_baixa s1 
																			 where s1.fin_pagrec_parc_id = t1.fin_pagrec_parc_id ';
												 if pParFinPagRecDataBaixaIni != '' and pParFinPagRecDataBaixaFin != ''then
														vSql = vSql ||' and '||'CAST(s1.data_baixa AS DATE)'||' >= '''||pParFinPagRecDataBaixaIni||''''||' 
																						and  CAST(s1.data_baixa AS DATE)'||' <= '''||pParFinPagRecDataBaixaFin||'''';
												end if;
									 vSql = vSql||'),0))) as valor_06
							from vwfin_pagrec_geral t1 where 1=1 ';
		
		-- And--
		--===================================

	 if pParUnitId != '' then
			vSql = vSql ||' and t1.fin_pagrec_unit_id '||' in('''||pParUnitId||''')';
	 end if;
	 
	 if pParFinPagRecES != '' then 
		vSql = vSql ||' and '||' t1.fin_pagrec_tipo_es'||' like '||'''' ||pParFinPagRecES||''' ';
	 end if;
	 
	 if pParGerPessoaNome != '' then 
		vSql = vSql ||' and '||'t1.ger_pessoa_nome'||' like '||'''' ||pParGerPessoaNome||''' ';
	 end if;	 
	 
	 if pParGerPessoaPagRecNome != '' then 
		vSql = vSql ||' and '||'t1.ger_pessoa_pagrec_nome'||' like '||'''' ||pParGerPessoaPagRecNome||''' ';
	 end if;	 
	 
	 if pParFinPagRecDataMovIni != '' and pParFinPagRecDataMovFin != '' then 	
 		vSql = vSql ||' and '||'t1.fin_pagrec_data_mov'||' >= '''||pParFinPagRecDataMovIni||''''||' and t1.fin_pagrec_data_mov'||' <= '''||pParFinPagRecDataMovFin||'''';
 	 end if;
	 
	 if pParFinPagRecNumeroDocPagRec != '' then 
		vSql = vSql ||' and t1.fin_pagrec_numero_doc_pagrec like '||'''' ||pParFinPagRecNumeroDocPagRec||''' ';
	 end if;
		
	 if pParFinPagRecParcValorPagRecIni != '' and pParFinPagRecParcValorPagRecFin != '' then 
		vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_pagrec'||' >= '''||pParFinPagRecParcValorPagRecIni||''''||'and t1.fin_pagrec_parc_valor_pagrec'||' <= '''||pParFinPagRecParcValorPagRecFin||'''';
		end if;

	 if pParFinPagRecParcValorJuroIni != '' and pParFinPagRecParcValorJuroFin != '' then 
		vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_juro'||' >= '''||pParFinPagRecParcValorJuroIni||''''||'and t1.fin_pagrec_parc_valor_juro'||' <= '''||pParFinPagRecParcValorJuroFin||'''';
	 end if;
	 
	 if pParFinPagRecParcValorDescontoIni != '' and  pParFinPagRecParcValorDescontoFin != '' then 
	 vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_desconto'||' >= '''||pParFinPagRecParcValorDescontoIni||''''||'and t1.fin_pagrec_parc_valor_desconto'||' <= '''||pParFinPagRecParcValorDescontoFin||'''';
	 end if;	 
	 
	 if pParFinPagRecParcValorMultaIni != '' and pParFinPagRecParcValorMultaFin != '' then 
		vSql = vSql ||' and '||'t1.fin_pagrec_parc_valor_multa'||' >= '''||pParFinPagRecParcValorMultaIni||''''||' and '||'t1.fin_pagrec_parc_valor_multa'||' <= '''||pParFinPagRecParcValorMultaFin||'''';
	 end if;

	 if pParFinPagRecParcDataVencIni != '' and pParFinPagRecParcDataVencFin != '' then 
		vSql = vSql ||' and '||'t1.fin_pagrec_parc_data_venc'||' >= '''||pParFinPagRecParcDataVencIni||''''||
	 ' and t1.fin_pagrec_parc_data_venc'||' <= '''||pParFinPagRecParcDataVencFin||''''; 
	 end if;
	 
	 if pParLogUserIns != '' then 
		vSql = vSql ||' and '||'t1.log_user_ins'||' in('''||pParLogUserIns||''')';
	 end if; 
	 
	 if pParLogDateInsIni != '' and pParLogDateInsFin != '' then 
		vSql = vSql ||' and '||' CAST(t1.log_date_ins AS DATE)'||' >= '''||pParLogDateInsIni||''''||'and CAST(t1.log_date_ins AS DATE)'||' <= '''||pParLogDateInsFin||'''';
	 end if;		 
	 
	 if pParLogUserUpd != '' then 
		vSql = vSql ||' and '||'t1.log_user_upd'||' in('''||pParLogUserUpd||''')';
	 end if;
	 
	 if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then 
		vSql = vSql ||' and '||'CAST(t1.log_date_upd AS DATE)'||' >= '''||pParLogDateUpdIni||''''||' and  CAST(t1.log_date_upd AS DATE)'||' <= '''||pParLogDateUpdFin||'''';
	 end if;	
	 


	 
		-- Group By
	 -- ===================================
		vSql = vSql||' group by '|| pVart01;

		if  pVart02 != ''  THEN
		 vSql = vSql||  ','|| pVart02;
		end if;
		
    if  pVart03 != ''  THEN
		 vSql = vSql||  ','|| pVart03;
		end if;
		
    if  pVart04 != ''  THEN
		 vSql = vSql||  ','|| pVart04;
		end if;
		
    if  pVart05 != ''  THEN
		 vSql = vSql||  ','|| pVart05;
		end if;
		
	 -- Order By
	 -- ===================================
		vSql = vSql||' order by '|| pVart01;

		if  pVart02 != ''  THEN
		 vSql = vSql||  ','|| pVart02;
		end if;
		
    if  pVart03 != ''  THEN
		 vSql = vSql||  ','|| pVart03;
		end if;
		
    if  pVart04 != ''  THEN
		 vSql = vSql||  ','|| pVart04;
		end if;
		
    if  pVart05 != ''  THEN
		 vSql = vSql||  ','|| pVart05;
		end if;
		
		raise notice 'vSql2 :%', vSql;

for r in EXECUTE vSql loop
ind_rel_id := pParIndRelId;
ind_rel_par1 := vPar1;
ind_rel_par2 := vPar2;
 vart_01 := r.vart_01;
 vard_01 := r.vard_01;
 vart_02 := r.vart_02;
 vard_02 := r.vard_02;
 vart_03 := r.vart_03;
 vard_03 := r.vard_03;
 vart_04 := r.vart_04;
 vard_04 := r.vard_04;
 vart_05 := r.vart_05;
 vard_05 := r.vard_05;
 valor_01 := r.valor_01;
 valor_02 := r.valor_02;
 valor_03 := r.valor_03;
 valor_04 := r.valor_04;
 valor_05 := r.valor_05;
 valor_06 := r.valor_06;
return next;
end loop;
return;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE;
