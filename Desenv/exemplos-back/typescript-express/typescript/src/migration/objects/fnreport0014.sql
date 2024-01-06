Drop FUNCTION IF EXISTS fnreport0014;
CREATE 	OR REPLACE FUNCTION fnreport0014(
pParUnitId VARCHAR,
pParIndRelId VARCHAR,
pVart01 VARCHAR,
pVard01 VARCHAR,
pVart02 VARCHAR DEFAULT NULL,
pVard02 VARCHAR DEFAULT NULL,
pVart03 VARCHAR DEFAULT NULL,
pVard03 VARCHAR DEFAULT NULL,
pVart04 VARCHAR DEFAULT NULL,
pVard04 VARCHAR DEFAULT NULL,
pVart05 VARCHAR DEFAULT NULL,
pVard05 VARCHAR DEFAULT NULL,
pVart06 VARCHAR DEFAULT NULL,
pVard06 VARCHAR DEFAULT NULL,
pVart07 VARCHAR DEFAULT NULL,
pVard07 VARCHAR DEFAULT NULL,
pVart08 VARCHAR DEFAULT NULL,
pVard08 VARCHAR DEFAULT NULL,
pVart09 VARCHAR DEFAULT NULL,
pVard09 VARCHAR DEFAULT NULL,
pVart10 VARCHAR DEFAULT NULL,
pVard10 VARCHAR DEFAULT NULL,
pParCentro2AreaId VARCHAR DEFAULT NULL,
pParBlocoCol VARCHAR DEFAULT NULL,
pParTipoSoloId VARCHAR DEFAULT NULL,
pParTipoSoloNome VARCHAR DEFAULT NULL,
pParEspacId VARCHAR DEFAULT NULL,
pParEspacNome VARCHAR DEFAULT NULL,
pParAtivSisPlanId VARCHAR DEFAULT NULL,
pParAtivSisPlanNome VARCHAR DEFAULT NULL,
pParAtivSisCultId VARCHAR DEFAULT NULL,
pParAtivSisCultNome VARCHAR DEFAULT NULL,
pParAtivSisColhId VARCHAR DEFAULT NULL,
pParAtivSisColhNome VARCHAR DEFAULT NULL,
pParItemServId VARCHAR DEFAULT NULL,
pParItemServNome VARCHAR DEFAULT NULL,
pParItemServAtivo VARCHAR DEFAULT NULL,
pParDataIniPlan VARCHAR DEFAULT NULL,
pParDataIniPlanFin VARCHAR DEFAULT NULL,
pParDataFinPlanIni VARCHAR DEFAULT NULL,
pParDataFinPlan VARCHAR DEFAULT NULL,

pParDataUltPlanIni VARCHAR DEFAULT NULL,
pParDataUltPlanFin VARCHAR DEFAULT NULL,

pParDataIniCol VARCHAR DEFAULT NULL,
pParDataIniColFin VARCHAR DEFAULT NULL,
pParDataFinColIni VARCHAR DEFAULT NULL,
pParDataFinCol VARCHAR DEFAULT NULL,

pParDataUltColIni VARCHAR DEFAULT NULL,
pParDataUltColFin VARCHAR DEFAULT NULL,


pParDataFloradaIni VARCHAR DEFAULT NULL,
pParDataFloradaFin VARCHAR DEFAULT NULL,


pParDataEmergIni VARCHAR DEFAULT NULL,
pParDataEmergFin VARCHAR DEFAULT NULL,

pParUnidadeMedId VARCHAR DEFAULT NULL,
pParUnidadeMedNome VARCHAR DEFAULT NULL,
pParCentro1Id VARCHAR DEFAULT NULL,
pParCentro1Nome VARCHAR DEFAULT NULL,
pParCentro1Ativo VARCHAR DEFAULT NULL,
pParCentro2Id VARCHAR DEFAULT NULL,
pParCentro2Nome VARCHAR DEFAULT NULL,
pParCentro2Ativo VARCHAR DEFAULT NULL,
pParSubTipoId VARCHAR DEFAULT NULL,
pParSubTipoNome VARCHAR DEFAULT NULL,
pParTipoId VARCHAR DEFAULT NULL,
pParTipoNome VARCHAR DEFAULT NULL,
pParRatTipoId VARCHAR DEFAULT NULL,
pParRatTipoNome VARCHAR DEFAULT NULL,
pParSubGrupoId VARCHAR DEFAULT NULL,
pParSubGrupoNome VARCHAR DEFAULT NULL,
pParGrupoId VARCHAR DEFAULT NULL,
pParGrupoNome VARCHAR DEFAULT NULL,
pParGrupoAtivo VARCHAR DEFAULT NULL,
pParPeriodoId VARCHAR DEFAULT NULL,
pParPeriodoNome VARCHAR DEFAULT NULL,
pParPeriodoAtivo VARCHAR DEFAULT NULL,
pParPeriodoDataIni VARCHAR DEFAULT NULL,
pParPeriodoDataFin VARCHAR DEFAULT NULL,
pParLogUserIns VARCHAR DEFAULT NULL,
pParLogDateInsIni VARCHAR DEFAULT NULL, 
pParLogDateInsFin VARCHAR DEFAULT NULL, 
pParLogUserUpd VARCHAR DEFAULT NULL,
pParLogDateUpdIni VARCHAR DEFAULT NULL,
pParLogDateUpdFin VARCHAR DEFAULT NULL		
	) 
		RETURNS TABLE (
		ind_rel_id VARCHAR,
		ind_rel_par1 VARCHAR,
		ind_rel_par2 VARCHAR,
		ind_rel_par3 VARCHAR,
		vart_01 VARCHAR,
		vard_01 VARCHAR,
		vart_02 VARCHAR,
		vard_02 VARCHAR,
		vart_03 VARCHAR,
		vard_03 VARCHAR,
		vart_04 VARCHAR,
		vard_04 VARCHAR,
		vart_05 VARCHAR,
		vard_05 VARCHAR,
		vart_06 VARCHAR,
		vard_06 VARCHAR,
		vart_07 VARCHAR,
		vard_07 VARCHAR,
		vart_08 VARCHAR,
		vard_08 VARCHAR,
		vart_09 VARCHAR,
		vard_09 VARCHAR,
		vart_10 VARCHAR,
		vard_10 VARCHAR,
		valor_01 NUMERIC,
		valor_02 NUMERIC,
		valor_03 NUMERIC,
		valor_04 NUMERIC,
		valor_05 NUMERIC,
		valor_06 NUMERIC,
		valor_07 NUMERIC,
		valor_08 NUMERIC,
		valor_09 NUMERIC,
		valor_10 NUMERIC 
	) AS $BODY$ DECLARE
	vSql VARCHAR;
vPar1 VARCHAR := '';
vPar2 VARCHAR := '';
vPar3 VARCHAR = '';
r record;
vRelAgric BOOLEAN;

BEGIN

	if pParSubTipoId = 'f4053f31-1832-4653-ac41-99c06edc3cac' then
			vRelAgric = true;
	else
			vRelAgric = false;
	end if;
		
	if pParCentro1Nome != '' then
	vPar1 = vPar1 || 'Centro 1 Nome [' || pParCentro1Nome || '] ' || chr(13) || chr(10);
	else
	vPar1 = vPar1 || 'Centro 1 Nome [] ' || chr(13) || chr(10);
	end if;
	
	if pParCentro1Ativo != '' then
	vPar1 = vPar1 || 'Centro 1 Ativo [' || pParCentro1Ativo || '] ' || chr(13) || chr(10);
	else
	vPar1 = vPar1 || 'Centro 1 Ativo [] ' || chr(13) || chr(10);
	end if;
	
	if pParCentro2Nome != '' then
	 vPar1 = vPar1 || 'Centro 2 Nome [' || pParCentro2Nome || '] ' || chr(13) || chr(10);
	else
	 vPar1 = vPar1 || 'Centro 2 Nome [] ' || chr(13) || chr(10);
	end if;
	
	if  pParCentro2Ativo != '' then
	vPar1 = vPar1|| 'Centro 2 Ativo [' || pParCentro2Ativo || '] ' || chr(13) || chr(10);
	
	else
	vPar1 = vPar1 || 'Centro 2 Ativo [] ' || chr(13) || chr(10);
	end if;
		
	if pParTipoSoloNome != '' then
	vPar1 = vPar1 ||'Nome Solo [' || pParTipoSoloNome || '] ' || chr(13) || chr(10);
	else
	vPar1 = vPar1 ||'Nome Solo [] ' || chr(13) || chr(10);
	end if;
	
	if pParUnidadeMedNome != '' then
	vPar1 = vPar1 || 'Nome Unidade Medida [' || pParUnidadeMedNome || '] ' || chr(13) || chr(10);
	else
	vPar1 = vPar1 || 'Nome Unidade Medida [] ' || chr(13) || chr(10);
	end if;
	
	if pParRatTipoNome != '' then
	 vPar1 := vPar1 || 'Nome Tipo de Rateio [' || pParRatTipoNome || '] ' || chr(13) || chr(10);
	else
		vPar1 := vPar1 || 'Nome Tipo de Rateio [] ' || chr(13) || chr(10);
	end if;
	
	if pParTipoNome!= '' then
	vPar1 := vPar1 || 'Nome Centro Tipo [' || pParTipoNome || '] ' || chr(13) || chr(10);
	else
	vPar1 := vPar1 || 'Nome Centro Tipo [] ' || chr(13) || chr(10);
	end if;
		
	if pParSubTipoNome != '' then
	vPar1 := vPar1 || 'Nome Centro SubTipo [' || pParSubTipoNome || '] ' || chr(13) || chr(10);
	else
	vPar1 := vPar1|| 'Nome Centro SubTipo [] ' || chr(13) || chr(10);
	end if;
	
	if  pParEspacNome != '' then
		vPar1 := vPar1 || 'Nome Espaçamento [' || pParEspacNome || '] ' || chr(13) || chr(10);
	else
		vPar1 := vPar1|| 'Nome Espaçamento [] ' || chr(13) || chr(10);
	end if;
	
	if pParAtivSisPlanNome != '' then
	vPar1 := vPar1 || 'Nome Atividade Plantio [' || pParAtivSisPlanNome || '] ' || chr(13) || chr(10);
	else
	vPar1 := vPar1|| 'Nome Atividade Plantio [] ' || chr(13) || chr(10);
	end if;
	
	------Param 2
	if pParAtivSisCultNome != '' then
	vPar2 = vPar2 || 'Nome Atividade Cultura [' || pParAtivSisCultNome || '] ' || chr(13) || chr(10);
	else
	vPar2 = vPar2 || 'Nome Atividade Cultura [] ' || chr(13) || chr(10);
	end if;
		
	if pParPeriodoNome  != ''  then
		vPar2 := vPar2  || 'Nome Periodo [' || pParPeriodoNome || '] ' || chr(13) || chr(10);
	else
		vPar2 := vPar2  || 'Nome Periodo [] ' || chr(13) || chr(10);
	end if;
	

	---Param 3
	if pParPeriodoAtivo != '' then
		vPar2 = vPar2|| 'Periodo Ativo [' || pParPeriodoAtivo || '] ' || chr(13) || chr(10);
	else
		vPar2 = vPar2|| 'Periodo Ativo [] ' || chr(13) || chr(10);
	end if;
	
	if pParAtivSisColhNome != '' then
	vPar2 = vPar2|| 'Nome Atividade Colheita [' || pParAtivSisColhNome || '] ' || chr(13) || chr(10);
	else
	vPar2 = vPar2|| 'Nome Atividade Colheita [] ' || chr(13) || chr(10);
	end if;
	
	if pParItemServNome != '' then
	vPar2 = vPar2||'Nome Item de Serviço [' || pParItemServNome || '] ' || chr(13) || chr(10);
	else
	vPar2 = vPar2||'Nome Item de Serviço [] ' || chr(13) || chr(10);
	end if;
	
	if pParItemServAtivo!= '' then
	vPar2 = vPar2|| 'Item de Serviço Ativo [' || pParItemServAtivo || '] ' || chr(13) || chr(10);
	else
	vPar2 = vPar2|| 'Item de Serviço Ativo [] ' || chr(13) || chr(10);
	end if;
	
	if  pParGrupoNome != ''  then
	vPar2 = vPar2 || 'Nome Grupo [' || pParGrupoNome || '] ' || chr(13) || chr(10);
	else
	vPar2 = vPar2 || 'Nome Grupo [] ' || chr(13) || chr(10);
	end if;
	if pParGrupoAtivo != ''  then
	vPar2 = vPar2 || 'Ativo Grupo [' || pParGrupoAtivo || '] ' || chr(13) || chr(10);
	else
	vPar2 = vPar2 || 'Ativo Grupo [] ' || chr(13) || chr(10);
	end if;
	
	if pParSubGrupoNome != ''  then
		vPar2 = vPar2 || 'Nome SubGrupo [' || pParSubGrupoNome || '] ' || chr(13) || chr(10);
	else
		vPar2 = vPar2 || 'Nome SubGrupo [] ' || chr(13) || chr(10);
	end if;
	
	
	if pParBlocoCol != '' then
		vPar2 = vPar2  ||'Bloco de Colheita [' || pParBlocoCol || '] ' || chr(13) || chr(10);
	else
		vPar2 = vPar2  ||'Bloco de Colheita [] ' || chr(13) || chr(10);
	end if;

	--Param 4
	if pParLogUserIns != '' then
		vPar2 = vPar2 || 'Log Usuario Inserção [' ||pParLogUserIns|| '] ' || chr(13) || chr(10);
	else
		vPar2 = vPar2 || 'Log Usuario Inserção [] ' || chr(13) || chr(10);
	end if;
	
	if pParLogUserUpd != '' then
		vPar3 := vPar3 || 'Log Usuario Alteração [' ||pParLogUserUpd|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Log Usuario Alteração [] ' || chr(13) || chr(10);
	end if;
-- 	--------------------------------------------------------------------------------------------------

-- Datas

	if pParDataIniPlan != '' and pParDataIniPlanFin != '' then
	vPar3 := vPar3 || 'Data Inicial do Plantio de [' || pParDataIniPlan || '] até [' || pParDataIniPlanFin || '] ' || chr(13) || chr(10);
 else
	vPar3 := vPar3 ||'Data Inicial do Plantio de [] até [] '|| chr(13) || chr(10);
 end if;

	if pParDataFinPlanIni != '' and pParDataFinPlan != '' then
	vPar3 := vPar3 || 'Data Final do Plantio de [' || pParDataFinPlanIni || '] até [' || pParDataFinPlan || '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Data Final do Plantio de [] até [] ' || chr(13) || chr(10);
	end if;
	
	if pParDataUltPlanIni != '' and pParDataUltPlanFin != '' then
	vPar3 := vPar3 || 'Data Ultimo Plantio de [' || pParDataUltPlanIni || '] até' ||'['||pParDataUltPlanFin||']'|| chr(13) || chr(10);
	else 
	vPar3 := vPar3 || 'Data Ultimo Plantio de [] até []' || chr(13) || chr(10);
	end if;
	
	if pParDataIniCol != '' and pParDataIniColFin != '' then
	vPar3 := vPar3 || 'Data Inicial de Colheita de [' || pParDataIniCol || '] até [' || pParDataIniColFin || '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Data Inicial de Colheita de [] até [] ' || chr(13) || chr(10);	
	end if;
	
	if pParDataFinCol != '' and pParDataFinColIni != '' then
	vPar3 := vPar3 || 'Data Final de Colheita de [' || pParDataFinCol || '] até [' || pParDataFinColIni || '] ' || chr(13) || chr(10);
else
	vPar3 := vPar3 || 'Data Final de Colheita de [] até [] ' || chr(13) || chr(10);
end if;

  if pParDataUltColIni != '' and pParDataUltColFin != '' then
	vPar3 := vPar3 || 'Data Ultima Colheita de [' || pParDataUltColIni || '] Até ' ||'[' || pParDataUltColFin||']'||  chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Data Ultima Colheita de [] até []' || chr(13) || chr(10);  end if;
	
	if pParDataFloradaIni != '' and pParDataFloradaFin != '' then
	vPar3 := vPar3 || 'Data 1º Florada de [' || pParDataFloradaIni || '] até'||'['||pParDataFloradaFin||']'|| chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Data 1º Florada de [] até []' || chr(13) || chr(10);
	end if;
	
	if pParDataEmergIni != '' and pParDataEmergFin != '' then
	vPar3 := vPar3 || 'Data de Emergencia de [' || pParDataEmergIni || '] até' ||'['||pParDataEmergFin||']'|| chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Data de Emergencia de [] até []' || chr(13) || chr(10);
	end if;
	
	if pParPeriodoDataIni != '' and pParPeriodoDataFin != '' then
	vPar3 := vPar3 || 'Data Inicial Periodo de [' || pParPeriodoDataIni || '] até [' || pParPeriodoDataFin || '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Data Inicial Periodo de [] até [] ' || chr(13) || chr(10);	
	end if;
	
	if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
	vPar3 := vPar3 || 'Data Log Inserção de [' ||pParLogDateInsIni|| '] até ['||pParLogDateInsFin||']'|| chr(13) || chr(10);
	else
	vPar3 := vPar3 || 'Data Log Inserção de [] até []' || chr(13) || chr(10);
	end if;
	
	if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
	vPar3 := vPar3 || 'Data Log Alteração de [' || pParLogDateUpdIni || '] até [' ||pParLogDateUpdFin||']'|| chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Data Log Alteração de [] até []' || chr(13) || chr(10);
	end if;
		
		
	vSql = 'select
	' || pVart01 || '   as vart_01 ' || ',''' || pVard01 || ''' as vard_01 ';
	IF
		pVart02 != '' THEN
			vSql = vSql || ',' || pVart02 || '   as vart_02 ' || ',''' || pVard02 || ''' as vard_02 ';
		ELSE vSql = vSql || ',null as vart_02' || ',null as vard_02';
		
	END IF;
	IF
		pVart03 != '' THEN
			vSql = vSql || ',' || pVart03 || '   as vart_03 ' || ',''' || pVard03 || ''' as vard_03 ';
		ELSE vSql = vSql || ',null as vart_03' || ',null as vard_03';
		
	END IF;
	IF
		pVart04 != '' THEN
			vSql = vSql || ',' || pVart04 || '   as vart_04 ' || ',''' || pVard04 || ''' as vard_04 ';
		ELSE vSql = vSql || ',null as vart_04' || ',null as vard_04';
		
	END IF;
	IF
		pVart05 != '' THEN
			vSql = vSql || ',' || pVart05 || '   as vart_05 ' || ',''' || pVard05 || ''' as vard_05 ';
		ELSE vSql = vSql || ',null as vart_05' || ',null as vard_05';
		
	END IF;
	IF
		pVart06 != '' THEN
			vSql = vSql || ',' || pVart06 || '   as vart_06 ' || ',''' || pVard06 || ''' as vard_06 ';
		ELSE vSql = vSql || ',null as vart_06' || ',null as vard_06';
		
	END IF;
	IF
		pVart07 != '' THEN
			vSql = vSql || ',' || pVart07 || '   as vart_07 ' || ',''' || pVard07 || ''' as vard_07 ';
		ELSE vSql = vSql || ',null as vart_07' || ',null as vard_07';
		
	END IF;
	IF
		pVart08 != '' THEN
			vSql = vSql || ',' || pVart08 || '   as vart_08 ' || ',''' || pVard08 || ''' as vard_08 ';
		ELSE vSql = vSql || ',null as vart_08' || ',null as vard_08';
		
	END IF;
	IF
		pVart09 != '' THEN
			vSql = vSql || ',' || pVart09 || '   as vart_09 ' || ',''' || pVard09 || ''' as vard_09 ';
		ELSE vSql = vSql || ',null as vart_09' || ',null as vard_09';
		
	END IF;
	IF
		pVart10 != '' THEN
			vSql = vSql || ',' || pVart09 || '   as vart_10 ' || ',''' || pVard09 || ''' as vard_10 ';
		ELSE vSql = vSql || ',null as vart_10' || ',null as vard_10 ';
		
	END IF;
	
	vSql = vSql || ',sum(t1.ope_centro2_area_qnt_area_prod) as valor_01,
	sum(t1.ope_centro2_area_qnt_area_improd) as valor_02,
	sum(t1.ope_centro2_area_qnt_plantas_estande) as valor_03
	from vwope_centro2_area t1 where 1=1 ';
	

	
	IF pParCentro2AreaId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_area_id' || ' in(''' || pParCentro2AreaId || ''')';
	END IF;
	
	IF pParBlocoCol != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_bloco_col' || ' like ' || '''%' || pParBlocoCol || '%'' ';
	END IF;
	
	IF pParTipoSoloId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_tipo_solo_id ' || ' in(''' || pParTipoSoloId ||''')';
	END IF;
	
	IF pParTipoSoloNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_tipo_solo_nome' || ' like ' || '''%' || pParTipoSoloNome || '%'' ';
	END IF;
	
	
		IF pParUnidadeMedId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_area_umedida_id' || ' in(''' || pParUnidadeMedId || ''')';
	END IF;
	
	IF pParUnidadeMedNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_umedida_nome' || ' like ' || '''%' || pParUnidadeMedNome || '%'' ';
	END IF;
	
	IF pParTipoId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro_tipo_id' || ' in(''' || pParTipoId || ''')';
	END IF;
	
	IF pParTipoNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro_tipo_nome' || ' like ' || '''%' || pParTipoNome || '%'' ';
	END IF;
	
	IF pParSubTipoId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro_subtipo_id' || ' in(''' || pParSubTipoId || ''')';
	END IF;
	
	IF pParSubTipoNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro_subtipo_nome' || ' like ' || '''%' || pParSubTipoNome || '%'' ';
	END IF;	
	
	IF pParEspacId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_area_espacamento_id' || ' in(''' || pParEspacId || ''')';
	END IF;
	
	IF pParEspacNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_espacamento_nome' || ' like ' || '''%' || pParEspacNome || '%'' ';
	END IF;
	
	IF pParAtivSisPlanId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_area_atividade_sistema_plan_id' || ' in(''' || pParAtivSisPlanId || ''')';
	END IF;
	
	IF pParAtivSisPlanNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_atividade_sistema_plan_nome' || ' like ' || '''%' || pParAtivSisPlanNome || '%'' ';		
	END IF;
	
	IF pParAtivSisCultId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_area_atividade_sistema_cult_id ' || ' in(''' || pParAtivSisCultId || ''')';
	END IF;
	
	IF pParAtivSisCultNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_atividade_sistema_cult_nome' || ' like ' || '''%' || pParAtivSisCultNome || '%'' ';
	END IF;
	
	IF pParAtivSisColhId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_area_atividade_sistema_col_id ' || ' in(''' || pParAtivSisColhId || ''')';
	END IF;
	
	IF pParAtivSisColhNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_atividade_sistema_col_nome' || ' like ' || '''%' || pParAtivSisColhNome || '%'' ';
	END IF;
	
	IF pParItemServId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_area_item_serv_id ' || ' in(''' || pParItemServId || ''')';
	END IF;
	
	IF pParItemServNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_item_serv_nome' || ' like ' || '''%' || pParItemServNome || '%'' ';
	END IF;
	
	IF pParItemServAtivo != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_area_item_serv_ativo_desc' || ' like ' || '''%' || pParItemServAtivo || '%'' ';
	END IF;
	
	-- Datas

	
	
	IF pParDataIniPlan != '' AND pParDataIniPlanFin != '' THEN
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' >= ''' || pParDataIniPlan || '''' || ' and  CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' <= ''' || pParDataIniPlanFin || '''';
	END IF;
	
	
	IF pParDataFinPlanIni != '' AND pParDataFinPlan != '' THEN
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' >= ''' || pParDataFinPlanIni || '''' || ' and  CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' <= ''' || pParDataFinPlan || '''';
	END IF;
	
	IF pParDataUltPlanIni != '' and pParDataUltPlanFin != '' THEN
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' >= ''' || pParDataUltPlanIni || '''' || ' and  CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' <= ''' || pParDataUltPlanFin || '''';
	END IF;

	IF pParDataIniCol != ''  AND pParDataIniColFin != '' THEN
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' >= ''' || pParDataIniCol || '''' || ' and  CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' <= ''' || pParDataIniColFin || '''';
	END IF;
	
	IF pParDataFinColIni != ''  AND pParDataFinCol != '' THEN
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' >= ''' || pParDataFinColIni || '''' || ' and  CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' <= ''' || pParDataFinCol || '''';
	END IF;
	
	IF pParDataUltColIni != '' and pParDataUltColFin != '' THEN			
	 vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' >= ''' || pParDataUltColIni || '''' || ' and  CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' <= ''' || pParDataUltColFin || '''';
  END IF;	

	
	IF pParDataFloradaIni != '' and pParDataFloradaFin != '' THEN
	vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' >= ''' || pParDataFloradaIni || '''' || ' and  CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' <= ''' || pParDataFloradaFin || '''';
	
	END IF;
	
	IF pParDataEmergIni != '' and  pParDataEmergFin != '' THEN
				vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' >= ''' || pParDataEmergIni || '''' || ' and  CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' <= ''' || pParDataEmergFin || '''';
				
	END IF;
	
	IF pParLogUserIns != '' THEN
				vSql = vSql || ' and ' ||'t1.log_user_ins'||' like ' || '''%' ||pParLogUserIns|| '%'' ';
  END IF;				

	IF pParLogDateInsIni != '' and pParLogDateInsFin != '' THEN
	 vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni || '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
  END IF;	
	
	IF pParLogUserUpd != '' THEN
				vSql = vSql || ' and ' ||'t1.log_user_upd'||' like ' || '''%' ||pParLogUserUpd|| '%'' ';
  END IF;				

	IF pParLogDateUpdIni != '' and  pParLogDateUpdFin != '' THEN
		 	 vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni || '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
  END IF;				




	-- fim datas
	
	IF pParCentro1Id != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro1_id ' || ' in(''' || pParCentro1Id || ''')';
	END IF;
	
	IF pParCentro1Nome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro1_nome' || ' like ' || '''%' || pParCentro1Nome || '%'' ';
	END IF;
	
	IF pParCentro1Ativo != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro1_ativo_desc' || ' like ' || '''%' || pParCentro1Ativo || '%'' ';
	END IF;
	
	IF pParCentro2Id != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro2_id ' || ' in(''' || pParCentro2Id || ''')';
	END IF;
	
	IF pParCentro2Nome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_nome' || ' like ' || '''%' || pParCentro2Nome || '%'' ';
	END IF;
	
	IF pParCentro2Ativo != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_ativo_desc ' || ' like ' || '''%' || pParCentro2Ativo || '%'' ';
	END IF;
	
	IF pParGrupoId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id ' || ' in(''' || pParGrupoId || ''')';
	END IF;
	
	IF pParGrupoNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro_grupo_nome' || ' like ' || '''%' || pParGrupoNome || '%'' ';
	END IF;
	
	IF pParGrupoAtivo != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro_grupo_ativo_desc' || ' like ' || '''%' || pParGrupoAtivo || '%'' ';
	END IF;
	
	IF pParSubGrupoId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro_subgrupo_id' || ' in(''' || pParSubGrupoId || ''')';
	END IF;
	
	IF pParSubGrupoNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro_subgrupo_nome' || ' like ' || '''%' || pParSubGrupoNome || '%'' ';
	END IF;	
	
	
	IF pParRatTipoId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_centro_rat_tipo_id' || ' in(''' || pParRatTipoId || ''')';
	END IF;
	
	IF pParRatTipoNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro_rat_tipo_nome' || ' like ' || '''%' || pParRatTipoNome || '%'' ';
	END IF;		
	
	IF pParPeriodoId != '' THEN
			vSql = vSql || ' and ' || ' t1.ope_periodo_id ' || ' in(''' || pParPeriodoId || ''')';
	END IF;
	
	IF pParPeriodoNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_periodo_nome' || ' like ' || '''%' || pParPeriodoNome || '%'' ';
	END IF;
	
	IF pParPeriodoAtivo != '' THEN
			vSql = vSql || ' and ' || 't1.ope_periodo_ativo_desc' || ' like ' || '''%' || pParPeriodoAtivo || '%'' ';
	END IF;
	
	IF pParPeriodoDataIni != '' AND pParPeriodoDataFin != '' THEN
			vSql = vSql || ' and ' || 'CAST(t1.ope_periodo_data_ini AS DATE)' || ' >= ''' || pParPeriodoDataIni || '''' || ' and  CAST(t1.ope_periodo_data_fin AS DATE)' || ' <= ''' || pParPeriodoDataFin || '''';
	END IF;
	
	if pParUnitId != '' then
		vSql = vSql|| ' and t1.ope_centro2_area_unit_id '||' in('''||pParUnitId||''')';
	end if;
	-- GROUP BY
	vSql = vSql || ' group by ' || pVart01;
	
	IF pVart02 != '' THEN
			vSql = vSql || ',' || pVart02;
	END IF;
	
	IF pVart03 != '' THEN
			vSql = vSql || ',' || pVart03;		
	END IF;
	
	IF pVart04 != '' THEN
			vSql = vSql || ',' || pVart04;	
	END IF;
	
	IF pVart05 != '' THEN
			vSql = vSql || ',' || pVart05;	
	END IF;
	
	IF pVart06 != '' THEN
			vSql = vSql || ',' || pVart06;	
	END IF;
	
	IF pVart07 != '' THEN
			vSql = vSql || ',' || pVart07;	
	END IF;
	
	IF pVart08 != '' THEN
			vSql = vSql || ',' || pVart08;	
	END IF;
	
	IF pVart09 != '' THEN
			vSql = vSql || ',' || pVart09;
	END IF;
	
	IF pVart10 != '' THEN
			vSql = vSql || ',' || pVart10;	
	END IF;
	
-- Order By
-- ===================================
	vSql = vSql || ' order by ' || pVart01;
	IF pVart02 != '' THEN
			vSql = vSql || ',' || pVart02;	
	END IF;
	
	IF pVart03 != '' THEN
			vSql = vSql || ',' || pVart03;	
	END IF;
	
	IF pVart04 != '' THEN
			vSql = vSql || ',' || pVart04;	
	END IF;
	
	IF pVart05 != '' THEN
			vSql = vSql || ',' || pVart05;	
	END IF;
	
	IF pVart06 != '' THEN
			vSql = vSql || ',' || pVart06;	
	END IF;
	
	IF pVart07 != '' THEN
			vSql = vSql || ',' || pVart07;	
	END IF;
	
	IF pVart08 != '' THEN
			vSql = vSql || ',' || pVart08;	
	END IF;
	
	IF pVart09 != '' THEN
			vSql = vSql || ',' || pVart09;	
	END IF;
	
	IF pVart10 != '' THEN
			vSql = vSql || ',' || pVart10;	
	END IF;
	
-- 	raise notice'vSql :%', vSql;
	
	raise notice 'Param 2 :%',vPar2;
	raise notice 'Param 3 :%',vPar3;
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
		vart_06 := r.vart_06;
		vard_06 := r.vard_06;
		vart_07 := r.vart_07;
		vard_07 := r.vard_07;
		vart_08 := r.vart_08;
		vard_08 := r.vard_08;
		vart_09 := r.vart_09;
		vard_09 := r.vard_09;
		vart_10 := r.vart_10;
		vard_10 := r.vard_10;
		valor_01 := r.valor_01;
		valor_02 := r.valor_02;
		valor_03 := r.valor_03;
	RETURN NEXT;
	
END loop;
raise notice'vSql :%',vSql;
RETURN;

END;
$BODY$ LANGUAGE plpgsql VOLATILE;