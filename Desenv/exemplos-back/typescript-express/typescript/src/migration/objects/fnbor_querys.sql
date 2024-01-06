-- DROP FUNCTION
-- DROP FUNCTION public.fnbor_querys(varchar,timestamptz,timestamptz,numeric,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,bool,varchar,varchar,varchar,varchar,varchar);
Drop FUNCTION IF EXISTS fnbor_querys;
CREATE OR REPLACE FUNCTION public.fnbor_querys(
    -- parâmetros obrigatórios
    pUnitId character varying, 
    pDataIni timestamptz,
    pdataFim timestamptz,
    pStatus numeric, -- 0=Todos / 1=Trabalhando / 2=Ocioso / 3=Desligado / 4=Suspeito
    -- opções de seleção dos dados
    pSelEmpresaId boolean DEFAULT false,
    pSelEquipamentoId boolean DEFAULT false,
    pSelOperadorId boolean DEFAULT false,
    pSelAtividadeId boolean DEFAULT false,
    pSelAreaId boolean DEFAULT false,
    pSelStatus boolean DEFAULT false,
    pSelRpmMin boolean DEFAULT false,
    pSelRpmAvg boolean DEFAULT false,
    pSelRpmMax boolean DEFAULT false,
    pSelHectaresTotal boolean DEFAULT false,
    pSelHectaresAvg boolean DEFAULT false,
    pSelHorasTotal boolean DEFAULT false,
    pSelHorasAvg boolean DEFAULT false,
    pSelVelocidadeMin boolean DEFAULT false,
    pSelVelocidadeAvg boolean DEFAULT false,
    pSelVelocidadeMax boolean DEFAULT false,
    -- opções de filtro da query
    pWhereEmpresaId character varying DEFAULT NULL::character varying,
    pWhereEquipamentoId character varying DEFAULT NULL::character varying,
    pWhereOperadorId character varying DEFAULT NULL::character varying,
    pWhereAtividadeId character varying DEFAULT NULL::character varying,
    pWhereAreaId character varying DEFAULT NULL::character varying)
 RETURNS TABLE( unit_id character varying,
                empresa_id character varying,
                equipamento_id character varying,
                operador_id character varying,
                atividade_id character varying,
                area_id character varying,
                status numeric,
                rpm_min numeric, 
                rpm_avg numeric, 
                rpm_max numeric,
                hectares_total numeric,
                hectares_avg numeric,
                horas_total numeric,
                horas_avg numeric,
                velocidade_min numeric,
                velocidade_avg numeric,
                velocidade_max numeric)
 LANGUAGE plpgsql
AS $function$
declare
  	vSql varchar;
  	r record;
begin
	vSql = 'select a.unit_id as unit_id ';

    --Columns--
    --==================================
    if (pSelEmpresaId) then
    	vSql = vSql || ', a.ger_empresa_id as empresa_id';
    end if;
    -- 
    if (pSelEquipamentoId) then
    	vSql = vSql || ', a.ope_centro2_equip_id_1 as equipamento_id';
    end if;
    --
    if (pSelOperadorId) then
    	vSql = vSql || ', a.ope_centro2_pessoa_id as operador_id';
    end if;
    --
    if (pSelAtividadeId) then
    	vSql = vSql || ', a.ope_atividade_id as atividade_id';
    end if;
    --
    if (pSelAreaId) then
    	vSql = vSql || ', a.ope_centro2_area_id as area_id';
    end if;
    --
    if (pSelStatus) then
    	vSql = vSql || ', case when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric > 0 and a.ope_atividade_id is not null) then 1 ';
		vSql = vSql || '       when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric <= 0) then 2 ';
		vSql = vSql || '       when (a.equipamento_ignicao != ''ON'') then 3 ';
		vSql = vSql || '       else 4 '; -- definir melhor a regra do "Suspeito"
		vSql = vSql || '  end as status ';
	end if;

   	--Agregates--
   	--==================================
   	if (pSelRpmMin) then
   		vSql = vSql || ', min(equipamento_rpm::numeric) as rpm_min ';
    end if;
    --
    if (pSelRpmAvg) then
   		vSql = vSql || ', round(avg(equipamento_rpm::numeric)) as rpm_avg ';
    end if;
    --
    if (pSelRpmMax) then
   		vSql = vSql || ', max(equipamento_rpm::numeric) as rpm_max ';
    end if;
    --
    if (pSelHectaresTotal) then
   		vSql = vSql || ', round(sum(qnt_ha_trab), 3) as hectares_total ';
    end if;
    --
    if (pSelHectaresAvg) then
   		vSql = vSql || ', round(avg(qnt_ha_trab), 3) as hectares_avg ';
    end if;
    --
    if (pSelHorasTotal) then
   		vSql = vSql || ', round(sum(duration), 3) as horas_total ';
    end if;
    --
    if (pSelHorasAvg) then
   		vSql = vSql || ', round(avg(duration), 3) as horas_avg ';
    end if;
    --
   	if (pSelVelocidadeMin) then
   		vSql = vSql || ', min(equipamento_veloc::numeric) as velocidade_min ';
    end if;
    --
    if (pSelVelocidadeAvg) then
    	vSql = vSql || ', round(avg(equipamento_veloc::numeric)) as velocidade_avg ';
    end if;
    --
    if (pSelVelocidadeMax) then
    	vSql = vSql || ', max(equipamento_veloc::numeric) as velocidade_max ';
    end if;
    
	vSql = vSql || '  from public.bor_mov a ';
    vSql = vSql || ' where a.unit_id = ''' || pUnitId || '''';
    vSql = vSql || '   and a.dthr_track between to_timestamp('''||to_char(pDataIni, 'dd/mm/yyyy hh24:mi:ss')||''', ''dd/mm/yyyy hh24:mi:ss'') ';
    vSql = vSql || '   and to_timestamp('''||to_char(pDataFim, 'dd/mm/yyyy hh24:mi:ss')||''', ''dd/mm/yyyy hh24:mi:ss'') ';
	--And--
	--===================================
	if (pStatus = 1) then -- trabalhando
		vSql = vSql || ' and (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric > 0 and a.ope_atividade_id is not null) ';
	end if;
	if (pStatus = 2) then -- ocioso
		vSql = vSql || ' and (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric <= 0) ';
	end if;
	if (pStatus = 3) then -- desligado
		vSql = vSql || ' and (a.equipamento_ignicao != ''ON'') ';
	end if;
	if (pStatus = 4) then -- suspeito
		--vSql = vSql || ' and (a.equipamento_ignicao != ''ON'') ';
	end if;
    if (pWhereEmpresaId is not null and pWhereEmpresaId != '') then
    	vSql = vSql || ' and (a.ger_empresa_id = '''|| pWhereEmpresaId ||''') ';
    end if;
    --
    if (pWhereEquipamentoId is not null and pWhereEquipamentoId != '') then
    	vSql = vSql || ' and (a.ope_centro2_equip_id_1 = '''|| pWhereEquipamentoId ||''') ';
    end if;
    --
    if (pWhereOperadorId is not null and pWhereOperadorId != '') then
    	vSql = vSql || ' and (a.ope_centro2_pessoa_id = '''|| pWhereOperadorId ||''') ';
    end if;
    --
    if (pWhereAtividadeId is not null and pWhereAtividadeId != '') then
    	vSql = vSql || ' and (a.ope_atividade_id = '''|| pWhereAtividadeId ||''') ';
    end if;
    --
    if (pWhereAreaId is not null and pWhereAreaId != '') then 
    	vSql = vSql || ' and (a.ope_centro2_id_area = '''|| pWhereAreaId ||''') ';
    end if;
    --
	

	--Group By
	--===================================
	vSql = vSql || ' group by a.unit_id ';
    if (pSelEmpresaId) then
    	vSql = vSql || ', a.ger_empresa_id';
    end if;
    -- 
    if (pSelEquipamentoId) then
    	vSql = vSql || ', a.ope_centro2_equip_id_1';
    end if;
   
    if (pSelOperadorId) then
    	vSql = vSql || ', a.ope_centro2_pessoa_id';
    end if;
    --
    if (pSelAtividadeId) then
    	vSql = vSql || ', a.ope_atividade_id';
    end if;
    --
    if (pSelAreaId) then
    	vSql = vSql || ', a.ope_centro2_area_id';
    end if;
    --
    if (pSelStatus) then
    	vSql = vSql || ', case when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric > 0 and a.ope_atividade_id is not null) then 1 ';
		vSql = vSql || '       when (a.equipamento_ignicao = ''ON'' and a.equipamento_veloc::numeric <= 0) then 2 ';
		vSql = vSql || '       when (a.equipamento_ignicao != ''ON'') then 3 ';
		vSql = vSql || '       else 4 '; -- definir melhor a regra do "Suspeito"
		vSql = vSql || '  end ';
    end if;
		
   
    --Query--
    --===================================
	raise notice 'vSql :%', vSql;
		
	for r in EXECUTE vSql loop
		unit_id = r.unit_id;
	    --
		if (pSelEmpresaId) then
    		empresa_id = r.empresa_id;
    	else 
    		empresa_id = null;
    	end if;
        --
        if (pSelEquipamentoId) then
    		equipamento_id = r.equipamento_id;
    	else 
    		equipamento_id = null;
    	end if;
        --
        if (pSelOperadorId) then
        	operador_id = r.operador_id;
    	else 
    		operador_id = null;
    	end if;
    	--
    	if (pSelAtividadeId) then
    		atividade_id = r.atividade_id;
    	else 
    		atividade_id = null;
    	end if;
    	--
    	if (pSelAreaId) then
    		area_id = r.area_id;
    	else 
    		area_id = null;
    	end if;
    	--
        if (pSelStatus) then
	        status = r.status;
        else
        	status = null;
        end if;
        
        --Agregates--
   		--==================================
   		if (pSelRpmMin) then
    		rpm_min = r.rpm_min;
    	else 
    		rpm_min = null; 
    	end if;
    	--
    	if (pSelRpmAvg) then
    		rpm_avg = r.rpm_avg;
    	else 
    		rpm_avg = null; 
    	end if;
    	--
    	if (pSelRpmMax) then
    		rpm_max = r.rpm_max;
    	else 
    		rpm_max = null; 
    	end if;
    	--
    	if (pSelHectaresTotal) then
    		hectares_total = r.hectares_total;
    	else 
    		hectares_total = null;
    	end if;
    	--
    	if (pSelHectaresAvg) then
    		hectares_avg = r.hectares_avg;
    	else 
    		hectares_avg = null;
    	end if;
    	--
    	if (pSelHorasTotal) then
    		horas_total = r.horas_total;
    	else 
    		horas_total = null;
    	end if;
    	--
    	if (pSelHorasAvg) then
    		horas_avg = r.horas_avg;
    	else 
    		horas_avg = null;
    	end if;
    	--
   		if (pSelVelocidadeMin) then
    		velocidade_min = r.velocidade_min;
    	else 
    		velocidade_min = null;
    	end if;
        --
        if (pSelVelocidadeAvg) then
    		velocidade_avg = r.velocidade_avg;
    	else 
    		velocidade_avg = null;
    	end if;
        -- 
        if (pSelVelocidadeMax) then
    		velocidade_max = r.velocidade_max;
    	else 
    		velocidade_max = null;
    	end if;
		--
        return next;
		--
	end loop;
	--
	return;
end;
$function$
;
