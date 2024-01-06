Drop FUNCTION IF EXISTS fnreport0017;
CREATE OR REPLACE FUNCTION fnreport0017(
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
pParPessoaPtoIdenfTipo varchar default null,
pParPessoaPtoIdenf varchar default null,
pParCentro1Id varchar default null,
pParCentro1Nome varchar default null,
pParCentro1Ativo varchar default null,
pParCentroSubTipoId varchar default null,
pParCentroSubTipoNome varchar default null,
pParCentro2Id varchar default null,
pParCentro2Sigla varchar default null,
pParCentro2Nome varchar default null,
pParCentro2Ativo varchar default null,
pParFrenteTrabalhoId varchar default null,
pParFrenteTrabalhoNome varchar default null,
pParFrenteTrabalhoSigla varchar default null,
pParFrenteTrabalhoAtivo varchar default null,
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
vPar3 varchar :='';
r record;

begin
	
	if pParPessoaPtoIdenfTipo != '' then
		vPar1 := vPar1||'Tipo de Indenficação do Ponto ['||pParPessoaPtoIdenfTipo||']'||chr(13)||chr(10);
	else
		vPar1 := vPar1||'Tipo de Indenficação do Ponto []'||chr(13)||chr(10);
	end if;
	
	if pParPessoaPtoIdenf != '' then
		vPar1 := vPar1||'Indenficação Ponto ['||pParPessoaPtoIdenf||']'||chr(13)||chr(10);
	else
		vPar1 := vPar1||'Indenficação Ponto []'||chr(13)||chr(10);
	end if;
	
	if pParCentro1Id != '' then
			vPar1 := vPar1||'Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Id||'''')||'] '||chr(13)||chr(10);
	else
			vPar1 := vPar1||'Centro 1 []'||chr(13)||chr(10);
	end if;
	
	if pParCentro1Nome != '' then
			vPar1 := vPar1||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
	else
			vPar1 := vPar1||'Nome Centro 1 []'||chr(13)||chr(10);
	end if;
	
	if pParCentro1Ativo != '' then
		vPar1 := vPar1||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
	else
		vPar1 := vPar1||'Centro 1 Ativo []'||chr(13)||chr(10);
	end if;
	
	If pParCentroSubTipoId != '' then
		vPar1 := vPar1||'SubTipo ['||fnreport_sigla(pParUnitId,'ope_centro_subtipo','nome','id',''''||pParCentroSubTipoId||'''')||'] '||chr(13)||chr(10);
	else
		vPar1 := vPar1||'SubTipo []'||chr(13)||chr(10);
	end if;
	
	If pParCentroSubTipoNome != '' then
		vPar1 := vPar1||'Nome SubTipo ['||pParCentroSubTipoNome||']'||chr(13)||chr(10);
	else
		vPar1 := vPar1||'Nome SubTipo []'||chr(13)||chr(10);
	end if;
	
		If pParCentro2Id != '' then
		vPar2 := vPar2||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
	else
			vPar2 := vPar2||'Centro 2 []'||chr(13)||chr(10);
	end if;
	
	If pParCentro2Sigla != '' then
			vPar2 := vPar2||'Centro 2 Sigla['||pParCentro2Sigla||'] '||chr(13)||chr(10);
	else
			vPar2 := vPar2||'Centro 2 Sigla[]'||chr(13)||chr(10);
	end if;
	
		If pParCentro2Nome != '' then
			vPar2 := vPar2||'Nome Centro 2 ['||pParCentro2Nome||'] '||chr(13)||chr(10);
	else
			vPar2 := vPar2||'Nome Centro 2 []'||chr(13)||chr(10);
	end if;
	
	If pParCentro2Ativo != '' then
			vPar2 := vPar2||'Centro 2 Ativo['||pParCentro2Ativo||'] '||chr(13)||chr(10);
	else
			vPar2 := vPar2||'Centro 2 Ativo[]'||chr(13)||chr(10);
	end if;	
	
	if pParFrenteTrabalhoId != '' then
				vPar2 := vPar2||'Frente Trabalho ['||fnreport_sigla(pParUnitId,'ope_frente_trabalho','sigla_frente_trabalho','id',''''||pParFrenteTrabalhoId||'''')||'] '||chr(13)||chr(10);
	else
			vPar2 := vPar2||'Frente Trabalho []'||chr(13)||chr(10);
	end if;
	
	if pParFrenteTrabalhoNome != '' then
				vPar2 := vPar2||'Nome Frente Trabalho ['||pParFrenteTrabalhoNome||'] '||chr(13)||chr(10);
	else
				vPar2 := vPar2||'Nome Frente Trabalho []'||chr(13)||chr(10);
	end if;
	
	if pParFrenteTrabalhoSigla != '' then
			vPar3 := vPar3||'Sigla Frente Trabalho ['||pParFrenteTrabalhoSigla||'] '||chr(13)||chr(10);
	else
			vPar3 := vPar3||'Sigla Frente Trabalho []'||chr(13)||chr(10);
	end if;
	
	if pParFrenteTrabalhoAtivo != '' then
			vPar3 := vPar3||'Frente Trabalho Ativo ['||pParFrenteTrabalhoAtivo||'] '||chr(13)||chr(10);
	else
			vPar3 := vPar3||'Frente Trabalho Ativo []'||chr(13)||chr(10);
	end if;
	
	if pParLogUserIns != '' then
			vPar3 := vPar3||'Log Usuario Inserção ['||pParLogUserIns||'] '||chr(13)||chr(10);
	else
			vPar3 := vPar3||'Log Usuario Inserção []'||chr(13)||chr(10);
	end if;
	
	if pParLogUserUpd != '' then
			vPar3 := vPar3||'Log Usuario Alteração ['||pParLogUserUpd||'] '||chr(13)||chr(10);
	else
			vPar3 := vPar3||'Log Usuario Alteração []'||chr(13)||chr(10);
	end if;
	
	if pParLogDateInsIni != '' and pParLogDateInsFin != ''then
			vPar3 := vPar3||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
	else
			vPar3 := vPar3||'Data Inserção de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParLogDateUpdIni != '' and pParLogDateUpdFin != ''then
			vPar3 := vPar3||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
	else
			vPar3 := vPar3||'Data Alteração de [] até []'||chr(13)||chr(10);
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
	
	
		vSql = vSql ||',
				count(1) as valor_01
				from vwope_centro2_pessoa t1 where 1=1';
		
		
		IF pParUnitId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro1_unit_id' || ' in(''' ||pParUnitId||''')';
		END IF;
		
		IF pParPessoaPtoIdenfTipo != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_pessoa_pto_idenf_tipo' || ' like ''' ||pParPessoaPtoIdenfTipo||'''';
		END IF;
		
		IF pParPessoaPtoIdenf != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_pessoa_pto_idenf' || ' like ''' ||pParPessoaPtoIdenf||'''';
		END IF;
		
		IF pParCentro1Id != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro1_id' || ' in(''' ||pParCentro1Id||''')';
		END IF;
	
		IF pParCentro1Nome != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro1_nome' || ' like '|| '''%' || pParCentro1Nome || '%'' ';
		END IF;
		
		IF pParCentro1Ativo != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro1_ativo_desc' || ' like '|| '''%' || pParCentro1Ativo || '%'' ';
		END IF;
		
		IF pParCentroSubTipoId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_id' || ' in(''' ||pParCentroSubTipoId||''')';
		END IF;
			
		IF pParCentroSubTipoNome != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_nome' || ' like '|| '''%' || pParCentroSubTipoNome || '%'' ';
		END IF;
		
		IF pParCentro2Id != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';
		END IF;
	
		IF pParCentro2Sigla != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_sigla' || ' like '|| '''%' ||pParCentro2Sigla|| '%'' ';
		END IF;
		
		IF pParCentro2Nome != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '|| '''%' ||pParCentro2Nome|| '%'' ';
		END IF;
		IF pParCentro2Ativo != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_ativo_desc' || ' like '|| '''%' ||pParCentro2Ativo|| '%'' ';
		END IF;
		
		IF pParFrenteTrabalhoId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id' || ' in(''' ||pParFrenteTrabalhoId||''')';
		END IF;

		IF pParFrenteTrabalhoNome != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_nome' || ' like '|| '''%' ||pParFrenteTrabalhoNome|| '%'' ';
		END IF;

		IF pParFrenteTrabalhoSigla != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_sigla' || ' like '|| '''%' ||pParFrenteTrabalhoSigla|| '%'' ';
		END IF;

		IF pParFrenteTrabalhoAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_ativo_desc' || ' like '|| '''%' ||pParFrenteTrabalhoAtivo|| '%'' ';
		END IF;

		IF pParLogUserIns != '' THEN
			vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
		END IF;
		
		IF pParLogDateInsIni != '' and pParLogDateInsFin != '' THEN
		  vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
		END IF;
		
		IF pParLogUserUpd != '' THEN
			vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
		END IF;		

		IF pParLogDateUpdIni != '' and pParLogDateUpdFin != '' THEN
		  vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
		END IF;

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
	
	
	FOR r IN EXECUTE vSql loop
	
		ind_rel_id := pParIndRelId;
		ind_rel_par1 := vPar1;
		ind_rel_par2 := vPar2;
		ind_rel_par3 := vPar3;
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
		
	RETURN NEXT;
	
END loop;
raise notice'vSql :%',vSql;
		
		
end;
$BODY$
  LANGUAGE plpgsql VOLATILE;
	