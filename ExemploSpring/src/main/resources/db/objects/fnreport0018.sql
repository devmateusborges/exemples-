Drop FUNCTION IF EXISTS  fnreport0018;
CREATE OR REPLACE FUNCTION fnreport0018(
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
pParEstoqId  varchar default null,
pParEstoqTipo  varchar default null,
pParCentro2Id  varchar default null,
pParCentro2Nome  varchar default null,
pParCentro2Ativo  varchar default null,
pParCentro2Sigla  varchar default null,
pParCentro2TipoDestinacao  varchar default null,
pParCentro2TipoCtbComp  varchar default null,
pParCentro2CtbCompId varchar default null,
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


if pParEstoqTipo != '' then
	vPar1 := vPar1||'Tipo Estoque ['||pParEstoqTipo||']'||chr(13)||chr(10);
else
	vPar1 := vPar1||'Tipo Estoque []'||chr(13)||chr(10);
end if;

if pParCentro2Id != '' then
	vPar1 := vPar1||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
else
vPar1 := vPar1||'Centro 2 []'||chr(13)||chr(10);
end if;

if pParCentro2Nome != '' then
vPar1 := vPar1||'Nome Centro 2 ['||pParCentro2Nome||']'||chr(13)||chr(10);
else
vPar1 := vPar1||'Nome Centro 2 []'||chr(13)||chr(10);
end if;

if pParCentro2Ativo != '' then
vPar1 := vPar1||'Centro 2 Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
else
vPar1 := vPar1||'Centro 2 Ativo []'||chr(13)||chr(10);
end if;

if pParCentro2Sigla != '' then
vPar1 := vPar1||'Centro 2 Sigla ['||pParCentro2Sigla||']'||chr(13)||chr(10);
else
vPar1 := vPar1||'Centro 2 Sigla []'||chr(13)||chr(10);
end if;

if pParCentro2TipoDestinacao != '' then
vPar1 := vPar1||'Destinação ['||pParCentro2TipoDestinacao||']'||chr(13)||chr(10);
else
vPar1 := vPar1||'Destinação []'||chr(13)||chr(10);
end if;

if pParCentro2TipoCtbComp != '' then
vPar2 := vPar2||'Centro 2 Tipo Contabil ['||pParCentro2TipoCtbComp||']'||chr(13)||chr(10);
else
vPar2 := vPar2||'Centro 2 Tipo Contabil []'||chr(13)||chr(10);
end if;

if pParCentro2CtbCompId != '' then
	vPar2 := vPar2||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCentro2CtbCompId||'''')||'] '||chr(13)||chr(10);
else
vPar2 := vPar2||'Componente Contábil []'||chr(13)||chr(10);
end if;

if pParLogUserIns != '' then
vPar2 := vPar2||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
else
vPar2 := vPar2||'Log Usuario Inserção []'||chr(13)||chr(10);
end if;

if pParLogUserUpd != '' then
vPar2 := vPar2||'Log Usuario Alteração ['||pParLogUserIns||']'||chr(13)||chr(10);
else
vPar2 := vPar2||'Log Usuario Alteração []'||chr(13)||chr(10);
end if;

if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
	vPar2 := vPar2||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
else
			vPar2 := vPar2||'Data Inserção de [] até []'||chr(13)||chr(10);
end if;

	if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
		vPar2 := vPar2||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
	else
		vPar2 := vPar2||'Data Alteração de [] até []'||chr(13)||chr(10);
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
			from vwope_centro2_estoque t1 where 1=1';


		IF pParUnitId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_estoque_unit_id' || ' in(''' ||pParUnitId||''')';
		END IF;
		
		IF pParEstoqId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_estoque_id' || ' in(''' ||pParEstoqId||''')';
		END IF;
		
		IF pParEstoqTipo != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_estoque_tipo' || ' like '|| '''%' || pParEstoqTipo || '%'' ';			
		END IF;
		
		IF pParCentro2Id != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';			
		END IF;
		
		IF pParCentro2Nome != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '|| '''%' || pParCentro2Nome || '%'' ';	
		END IF;
		
		IF pParCentro2Ativo != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_ativo_desc' || ' like '|| '''%' || pParCentro2Ativo || '%'' ';	
		END IF;
		
		IF pParCentro2Sigla != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_sigla_centro2' || ' like '|| '''%' || pParCentro2Sigla || '%'' ';	
		END IF;
		
		IF pParCentro2TipoDestinacao != '' THEN
		  vSql = vSql|| 'and ' || ' t1.ope_centro2_tipo_destinacao' || ' like '|| '''%' || pParCentro2TipoDestinacao|| '%'' ';	
		END IF;
		
		IF pParCentro2TipoCtbComp != '' THEN
		  vSql = vSql|| 'and ' || ' t1.ope_centro2_tipo_ctb_comp' || ' like '|| '''%' || pParCentro2TipoCtbComp|| '%'' ';	
		END IF;
		
		IF pParCentro2TipoCtbComp != '' THEN
		  vSql = vSql|| 'and ' || ' t1.ope_centro2_tipo_ctb_comp' || ' like '|| '''%' || pParCentro2TipoCtbComp|| '%'' ';	
		END IF;

		IF pParCentro2CtbCompId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_ctb_comp_id' || ' in(''' ||pParCentro2CtbCompId||''')';			
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