drop FUNCTION if EXISTS fnreport0016;
CREATE OR REPLACE FUNCTION fnreport0016(
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
pParEquipId VARCHAR DEFAULT NULL,	
pParEquipTipoRodado VARCHAR DEFAULT NULL,	
pParEquipTipoCarroceria VARCHAR DEFAULT NULL,	
pParEquipCidId VARCHAR DEFAULT NULL,	
pParEquipCidNome VARCHAR DEFAULT NULL,
pParEquipCidAtivo VARCHAR DEFAULT NULL,	
pParUfId VARCHAR DEFAULT NULL,	
pParUfNome VARCHAR DEFAULT NULL,	
pParEquipPlaca VARCHAR DEFAULT NULL,pParEquipRenavam VARCHAR DEFAULT NULL,
pParEquipTara VARCHAR DEFAULT NULL,
pParEquipCapacidKg VARCHAR DEFAULT NULL,
pParEquipCapacidM3 VARCHAR DEFAULT NULL,
pParEquipPotenc VARCHAR DEFAULT NULL,
pParEquipNrChassi VARCHAR DEFAULT NULL,
pParEquipNrSerie VARCHAR DEFAULT NULL,
pParEquipLiberadoAbastec VARCHAR DEFAULT NULL,
pParEquipLargura VARCHAR DEFAULT NULL,
pParEquipAltur VARCHAR DEFAULT NULL,
pParEquipNrRegEstadual VARCHAR DEFAULT NULL,
pParEquipTipoTracao VARCHAR DEFAULT NULL,
pParCentro1Id VARCHAR DEFAULT NULL,
pParCentro1Nome VARCHAR DEFAULT NULL,
pParCentro1Ativo VARCHAR DEFAULT NULL,
pParCentro2Id VARCHAR DEFAULT NULL,
pParCentro2Nome VARCHAR DEFAULT NULL,
pParCentro2Ativo VARCHAR DEFAULT NULL,
pParFrentTrabId VARCHAR DEFAULT NULL,
pParFrentTrabNome VARCHAR DEFAULT NULL,
pParFrentTrabAtivo VARCHAR DEFAULT NULL,
pParMarcaModeloId VARCHAR DEFAULT NULL,
pParMarcaModeloNome VARCHAR DEFAULT NULL,
pParMarcaModeloAtivo VARCHAR DEFAULT NULL,
pParMarcaId VARCHAR DEFAULT NULL,
pParMarcaNome VARCHAR DEFAULT NULL,
pParMarcaAtivo VARCHAR DEFAULT NULL,
pParSubGrupId VARCHAR DEFAULT NULL,
pParSubGrupoNome VARCHAR DEFAULT NULL,
pParSubGrupoAtivo VARCHAR DEFAULT NULL,
pParGrupoId VARCHAR DEFAULT NULL,
pParGrupoNome VARCHAR DEFAULT NULL,
pParGrupoAtivo VARCHAR DEFAULT NULL,
pParProprietarioId VARCHAR DEFAULT NULL,
pParProprietarioNome VARCHAR DEFAULT NULL,
pParProprietarioAtivo VARCHAR DEFAULT NULL,
pParProprietarioDoc VARCHAR DEFAULT NULL,
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
ind_rel_par4 VARCHAR,
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
valor_01 integer,
valor_02 integer,
valor_03 integer,
valor_04 integer,
valor_05 integer,
valor_06 integer,
valor_07 integer,
valor_08 integer,
valor_09 integer,
valor_10 integer
) AS $BODY$ 
DECLARE
vSql text;
vPar1 VARCHAR := '';
vPar2 VARCHAR := '';
vPar3 VARCHAR := '';
vPar4 VARCHAR := '';
r record;


BEGIN

-- Param 1
if pParCentro1Nome != ''  then
vPar1 := vPar1|| 'Nome Centro 1 [' ||pParCentro1Nome|| '] ' || chr(13) || chr(10);
else
vPar1 := vPar1|| 'Nome Centro 1 [] ' || chr(13) || chr(10);
end if;

if pParCentro1Ativo != ''  then
vPar1 := vPar1|| 'Centro 1 Ativo [' ||pParCentro1Ativo|| '] ' || chr(13) || chr(10);
else
vPar1 := vPar1|| 'Centro 1 Ativo [] ' || chr(13) || chr(10);
end if;
 
if pParCentro2Nome != '' then
vPar1 := vPar1|| 'Centro 2 Nome [' ||pParCentro2Nome|| '] ' || chr(13) || chr(10);
else
vPar1 := vPar1|| 'Centro 2 Nome [] ' || chr(13) || chr(10);
end if;

if pParCentro2Ativo != ''  then
vPar1 := vPar1|| 'Centro 2 Ativo [' ||pParCentro2Ativo|| '] ' || chr(13) || chr(10);
else
vPar1 := vPar1|| 'Centro 2 Ativo [] ' || chr(13) || chr(10);
end if;
 
 if pParEquipCidNome != ''  then
	vPar1 := vPar1 || 'Cidade Nome [' || pParEquipCidNome || '] ' || chr(13) || chr(10);
 else
	vPar1 := vPar1 || 'Cidade Nome [] ' || chr(13) || chr(10);
 end if;
 
	if pParUfNome != '' then
	vPar1 := vPar1 || 'Estado Nome [' || pParUfNome || '] ' || chr(13) || chr(10);
	else
	vPar1 := vPar1 || 'Estado Nome []' || chr(13) || chr(10);
	end if;
  
	if pParEquipCidAtivo != '' then
	vPar1 := vPar1 || 'Equipamento Ativo [' || pParEquipCidAtivo || '] ' || chr(13) || chr(10);
	else
	vPar1 := vPar1 || 'Equipamento Ativo []' || chr(13) || chr(10);
	end if;
	
	if pParEquipTipoRodado != '' then
		vPar1 := vPar1||'Tipo Rodadado [' || pParEquipTipoRodado || '] ' || chr(13) || chr(10);
	else 
		vPar1 := vPar1||'Tipo Rodadado [] ' || chr(13) || chr(10);
	end if;

	if pParEquipTipoCarroceria != '' then
		vPar1 := vPar1|| 'Tipo Carroceira [' || pParEquipTipoCarroceria || '] ' || chr(13) || chr(10);
	else
		vPar1 := vPar1|| 'Tipo Carroceira [] ' || chr(13) || chr(10);
	end if;

	if pParEquipPlaca != '' then
	vPar1 := vPar1 || 'Placa Equipamento [' ||pParEquipPlaca|| '] ' || chr(13) || chr(10);
	else
	vPar1 := vPar1 || 'Placa Equipamento []' || chr(13) || chr(10);
	end if;

	if pParEquipRenavam != '' then
	vPar1 := vPar1 || 'Reg Nacional de Veículos Automotores [' ||pParEquipRenavam|| '] ' || chr(13) || chr(10);
	else
	vPar1 := vPar1 || 'Reg Nacional de Veículos Automotores [] ' || chr(13) || chr(10);
	end if;

-- Param 2
	if pParEquipTara != '' then
	vPar2 := vPar2 || 'Peso Veículo em Ordem de Marcha [' ||pParEquipTara|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2 || 'Peso Veículo em Ordem de Marcha []' || chr(13) || chr(10);
	end if;

	if pParEquipCapacidKg != '' then
	vPar2 := vPar2 || 'Capacidade Kg Equipamento [' ||pParEquipCapacidKg|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2 || 'Capacidade Kg Equipamento [] ' || chr(13) || chr(10);
	end if;

	if pParEquipCapacidKg != '' then
	vPar2 := vPar2 || 'Capacidade Kg Equipamento [' ||pParEquipCapacidKg|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2 || 'Capacidade Kg Equipamento []' || chr(13) || chr(10);
	end if;

	if pParEquipCapacidM3 != '' then
	vPar2 := vPar2 || 'Capacidade M3 Equipamento [' ||pParEquipCapacidM3|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2 || 'Capacidade M3 Equipamento []' || chr(13) || chr(10);
	end if;

	if pParEquipPotenc != '' then
	vPar2 := vPar2|| 'Potência do Equipamento [' ||pParEquipPotenc|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2 || 'Potência do Equipamento []' || chr(13) || chr(10);
	end if;

	if pParEquipNrChassi != '' then
	vPar2 := vPar2 || 'Nº Chassi do Equipamento [' ||pParEquipNrChassi|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2 || 'Nº Chassi do Equipamento []' || chr(13) || chr(10);
	end if;

	if pParEquipNrSerie != '' then
	vPar2 := vPar2 || 'Nº Série  do Equipamento [' ||pParEquipNrSerie|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2 || 'Nº Série  do Equipamento [] ' || chr(13) || chr(10);
	end if;
	
	if pParEquipNrRegEstadual != '' then
	vPar2 := vPar2|| 'Nº Registro Estadual do Equipamento [' ||pParEquipNrRegEstadual|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2|| 'Nº Registro Estadual do Equipamento [] ' || chr(13) || chr(10);
	end if;

	if pParEquipLiberadoAbastec != '' then
	vPar3 := vPar3|| 'Equipamento Liberado para Abastecimento [' ||pParEquipLiberadoAbastec|| '] ' || chr(13) || chr(10);
	else
	vPar2 := vPar2|| 'Equipamento Liberado para Abastecimento []' || chr(13) || chr(10);
	end if;

-- Param 3
	if pParEquipLargura != '' then
	vPar3 := vPar3|| 'Largura do Equipamento [' ||pParEquipLargura|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Largura do Equipamento []' || chr(13) || chr(10);
	end if;

	if pParEquipAltur != '' then
	vPar3 := vPar3|| 'Altura do Equipamento [' ||pParEquipAltur|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Altura do Equipamento [] ' || chr(13) || chr(10);
	end if;

	if pParEquipTipoTracao != '' then
	vPar3 := vPar3|| 'Tipo de Tração Equipamento [' ||pParEquipTipoTracao|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Tipo de Tração Equipamento [] ' || chr(13) || chr(10);
	end if;
 
 if pParFrentTrabNome != '' then
	vPar3 := vPar3|| 'Nome Frente de Trabalho [' ||pParFrentTrabNome|| '] ' || chr(13) || chr(10);
 else
	vPar3 := vPar3|| 'Nome Frente de Trabalho [] ' || chr(13) || chr(10);
 end if;

	if pParFrentTrabAtivo != ''  then
	vPar3 := vPar3|| 'Frente de Trabalho Ativo [' ||pParFrentTrabAtivo|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Frente de Trabalho Ativo [] ' || chr(13) || chr(10);
	end if;
 
	if pParMarcaModeloNome != '' then
		vPar3 := vPar3|| 'Modelo Nome [' ||pParMarcaModeloNome|| '] ' || chr(13) || chr(10);
	else
		vPar3 := vPar3|| 'Modelo Nome []' || chr(13) || chr(10);
	end if;

	if pParMarcaModeloAtivo != '' then
	vPar3 := vPar3|| 'Modelo Ativo [' ||pParMarcaModeloAtivo|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Modelo Ativo [] ' || chr(13) || chr(10);
	end if;


	 if pParMarcaNome!= '' then
	vPar3 := vPar3|| 'Nome Marca [' ||pParMarcaNome|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Nome Marca [] ' || chr(13) || chr(10);
	end if;

	if pParMarcaAtivo != '' then
	vPar3 := vPar3|| 'Ativo Marca [' ||pParMarcaAtivo|| '] ' || chr(13) || chr(10);
	else
	vPar3 := vPar3|| 'Ativo Marca [] ' || chr(13) || chr(10);
	end if;
-- Param 4

  if pParGrupoNome != '' then
		vPar4 := vPar4|| 'Grupo Nome [' ||pParGrupoNome|| '] ' || chr(13) || chr(10);
	else
		vPar4 := vPar4|| 'Grupo Nome [] ' || chr(13) || chr(10);
	end if;

	if pParGrupoAtivo != ''  then
	vPar4 := vPar4|| 'Grupo Ativo [' ||pParGrupoAtivo|| '] ' || chr(13) || chr(10);
	else
	vPar4 := vPar4|| 'Grupo Ativo [] ' || chr(13) || chr(10);
	end if;

	if pParSubGrupoNome != '' then
	vPar4 := vPar4|| 'Nome SubGrupo [' ||pParSubGrupoNome|| '] ' || chr(13) || chr(10);
	else
	vPar4 := vPar4|| 'Nome SubGrupo [] ' || chr(13) || chr(10);
	end if;

	if pParSubGrupoAtivo != '' then
	vPar4 := vPar4|| 'SubGrupo Ativo [' ||pParSubGrupoAtivo|| '] ' || chr(13) || chr(10);
	else
	vPar4 := vPar4|| 'SubGrupo Ativo [] ' || chr(13) || chr(10);
	end if;

 if pParProprietarioNome != '' then
	vPar4 := vPar4|| 'Nome do Proprietario [' ||pParProprietarioNome|| '] ' || chr(13) || chr(10);
 else
	vPar4 := vPar4|| 'Nome do Proprietario [] ' || chr(13) || chr(10);
 end if;

	if pParProprietarioAtivo != '' then
	vPar4 := vPar4|| 'Proprietário Ativo [' ||pParProprietarioAtivo|| '] ' || chr(13) || chr(10);
	else
	vPar4 := vPar4|| 'Proprietário Ativo []' || chr(13) || chr(10);
	end if;

	if pParProprietarioDoc != '' then
	vPar4 := vPar4|| 'Documento Proprietário [' ||pParProprietarioDoc|| '] ' || chr(13) || chr(10);
	else
	vPar4 := vPar4|| 'Documento Proprietário [] ' || chr(13) || chr(10);
	end if;

-- Param 3
	if pParLogUserIns != '' then
		vPar4 := vPar4 || 'Log Usuario Inserção [' ||pParLogUserIns|| '] ' || chr(13) || chr(10);
	else 
		vPar4 := vPar4 || 'Log Usuario Inserção []' || chr(13) || chr(10);
	end if;
	
	if pParLogUserUpd != ''  then
		vPar4 := vPar4 || 'Log Usuario Alteração [' ||pParLogUserUpd|| '] ' || chr(13) || chr(10);
	else 
		vPar4 := vPar4 || 'Log Usuario Alteração [] ' || chr(13) || chr(10);
	end if;
	
	if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
	vPar4 := vPar4 || 'Log Data Inserção de [' ||pParLogDateInsIni|| '] até ['||pParLogDateInsFin||']'|| chr(13) || chr(10);
	else
	vPar4 := vPar4 || 'Log Data Inserção de [] até []' || chr(13) || chr(10);
	end if;
	
	if pParLogDateUpdIni != '' and pParLogDateUpdIni != '' then
	vPar4 := vPar4 || 'Log Data Alteração de [' || pParLogDateUpdIni || '] até [' ||pParLogDateUpdFin||']'|| chr(13) || chr(10);
	else
	vPar4 := vPar4 || 'Log Data Alteração de [] até []' || chr(13) || chr(10);
	end if;
	

vSql = 'select
	' || pVart01 || '   as vart_01 ' || ',''' || pVard01 || ''' as vard_01 ';
	
	IF pVart02 != '' THEN
			vSql = vSql || ',' || pVart02 || '   as vart_02 ' || ',''' || pVard02 || ''' as vard_02 ';
		ELSE
		vSql = vSql || ',null as vart_02' || ',null as vard_02';	
	END IF;
	IF pVart03 != '' THEN
			vSql = vSql || ',' || pVart03 || '   as vart_03 ' || ',''' || pVard03 || ''' as vard_03 ';
	ELSE 	
		vSql = vSql || ',null as vart_03' || ',null as vard_03';
	END IF;
	IF pVart04 != '' THEN
			vSql = vSql || ',' || pVart04 || '   as vart_04 ' || ',''' || pVard04 || ''' as vard_04 ';
	ELSE
	vSql = vSql || ',null as vart_04' || ',null as vard_04';
	END IF;
	
	IF pVart05 != '' THEN
			vSql = vSql || ',' || pVart05 || '   as vart_05 ' || ',''' || pVard05 || ''' as vard_05 ';
	ELSE 	
		vSql = vSql || ',null as vart_05' || ',null as vard_05';
	END IF;
	
	IF pVart06 != '' THEN
		vSql = vSql || ',' || pVart06 || '   as vart_06 ' || ',''' || pVard06 || ''' as vard_06 ';
	ELSE 
		vSql = vSql || ',null as vart_06' || ',null as vard_06';	
	END IF;
	
	IF pVart07 != '' THEN
			vSql = vSql || ',' || pVart07 || '   as vart_07 ' || ',''' || pVard07 || ''' as vard_07 ';
	ELSE
		vSql = vSql || ',null as vart_07' || ',null as vard_07';	
	END IF;
	
	IF pVart08 != '' THEN
			vSql = vSql || ',' || pVart08 || '   as vart_08 ' || ',''' || pVard08 || ''' as vard_08 ';
	ELSE 
		vSql = vSql || ',null as vart_08' || ',null as vard_08';	
	END IF;
	
	IF pVart09 != '' THEN
			vSql = vSql || ',' || pVart09 || '   as vart_09 ' || ',''' || pVard09 || ''' as vard_09 ';
	ELSE 
	vSql = vSql || ',null as vart_09' || ',null as vard_09';	
	END IF;
	
	IF pVart10 != '' THEN
			vSql = vSql || ',' || pVart09 || '   as vart_10 ' || ',''' || pVard09 || ''' as vard_10 ';
	ELSE 
		vSql = vSql || ',null as vart_10' || ',null as vard_10 ';
	END IF;
	
-- 	vSql = vSql ||',
-- 				count(1) as valor_01
-- 				t1.ope_centro2_sigla as valor_02,
-- 				t1.ope_centro2_ativo_desc as valor_03,
-- 				t1.ope_frente_trabalho_nome as valor_04,
-- 				t1.ope_frente_trabalho_sigla as valor_05,
-- 				t1.ope_frente_trabalho_ativo_desc as valor_06,
-- 				t1.ger_marca_modelo_nome as valor_07,
-- 				t1.ger_marca_nome as valor_08,
-- 				t1.ope_centro_grupo_nome as valor_09,
-- 				t1.ger_pessoa_proprietario_nome as valor_10
-- 				from vwope_centro2_equip t1 where 1=1';

	vSql = vSql ||',
				count(1) as valor_01
				from vwope_centro2_equip t1 where 1=1';
				
				
	IF pParEquipId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_id' || ' in(''' ||pParEquipId||''')';
	END IF;
	
	IF pParEquipTipoRodado != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_equip_tipo_rodado_desc' || ' like ' || '''%' || pParEquipTipoRodado || '%'' ';
	END IF;
	
	IF pParEquipTipoCarroceria != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_equip_tipo_carroceria_desc' || ' like ' || '''%' || pParEquipTipoCarroceria || '%'' ';
	END IF;
	IF pParEquipCidId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_cidade_id' || ' in(''' ||pParEquipCidId||''')';
	END IF;

	IF pParEquipCidNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_equip_cidade_nome' || ' like ' || '''%' || pParEquipCidNome || '%'' ';
	END IF;
	
	IF pParEquipCidAtivo != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_equip_cidade_ativo_desc' || ' like ' || '''%' || pParEquipCidAtivo || '%'' ';
	END IF;
	
	IF pParUfId != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro2_uf_id' || ' in(''' ||pParUfId||''')';
	END IF;
	
	IF pParUfNome != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_uf_nome' || ' like ' || '''%' || pParUfNome || '%'' ';
	END IF;
	
	IF pParEquipPlaca != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_equip_placa' || ' like ' || '''%' || pParEquipPlaca || '%'' ';
	END IF;
	
	IF pParEquipRenavam != '' THEN
		vSql = vSql || ' and ' || 't1.ope_centro2_equip_renavam' || ' like ' || '''%' || pParEquipRenavam || '%'' ';
	END IF;

IF pParEquipTara != '' THEN
      vSql = vSql || ' and ' || 't1.ope_centro2_equip_tara' || ' = ' || '''' || pParEquipTara || ''' ';
END IF;

	IF pParEquipCapacidKg != '' THEN
			vSql = vSql || ' and ' || 't1.ope_centro2_equip_capacidade_kg' || ' = ' || '''' ||pParEquipCapacidKg|| ''' ';
	END IF;
	
	IF pParEquipCapacidM3 != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_capacidade_m3'|| ' = ' || '''' ||pParEquipCapacidM3|| ''' ';
	END IF;
	
	IF pParEquipPotenc != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_potencia'|| ' = ' || '''' ||pParEquipPotenc|| ''' ';
	END IF;
	
	IF pParEquipNrChassi != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_nr_chassi'|| ' = ' || '''' ||pParEquipNrChassi|| ''' ';
	END IF;
	
	IF pParEquipNrSerie != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_nr_serie'|| ' = ' || '''' ||pParEquipNrSerie|| ''' ';
	END IF;
	
	IF pParEquipLiberadoAbastec != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_liberado_abastec'|| ' like ' || '''%' ||pParEquipLiberadoAbastec|| '%'' ';
	END IF;
	IF pParEquipLargura != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_largura'|| ' = ' || '''' ||pParEquipLargura|| ''' ';
	END IF;
	
	IF pParEquipAltur != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_altura'|| ' = ' || '''' ||pParEquipAltur|| ''' ';
	END IF;
	
	IF pParEquipNrRegEstadual != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_nr_registro_estadual'|| ' = ' || '''' ||pParEquipNrRegEstadual|| ''' ';
	END IF;
	
	IF pParEquipTipoTracao != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_equip_tipo_tracao'|| ' = ' || '''' ||pParEquipTipoTracao|| ''' ';
 END IF;
 
 
	IF pParCentro1Id != '' THEN
			vSql = vSql || 'and ' || ' t1.ope_centro1_id' || ' in(''' ||pParCentro1Id||''')';
	END IF;
	
	IF pParCentro1Nome != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro1_nome'||' like ' || '''%' ||pParCentro1Nome|| '%'' ';
  END IF;
	
	IF pParCentro1Ativo != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro1_ativo_desc'||' like ' || '''%' ||pParCentro1Ativo|| '%'' ';
  END IF;
	
	IF pParCentro2Id != '' THEN
				vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';
  END IF;
	
	IF pParCentro2Nome != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_nome'||' like ' || '''%' ||pParCentro2Nome|| '%'' ';
  END IF;
	
	IF pParCentro2Ativo != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro2_ativo_desc'||' like ' || '''%' ||pParCentro2Ativo|| '%'' ';
  END IF;
	
	IF pParFrentTrabId != '' THEN
				vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id' || ' in(''' ||pParFrentTrabId||''')';
  END IF;	
	
	IF pParFrentTrabNome != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_frente_trabalho_nome'||' like ' || '''%' ||pParFrentTrabNome|| '%'' ';
  END IF;
	
	IF pParFrentTrabAtivo != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_frente_trabalho_ativo_desc'||' like ' || '''%' ||pParFrentTrabAtivo|| '%'' ';
  END IF;

	IF pParMarcaModeloId != '' THEN
				vSql = vSql || 'and ' || ' t1.ger_marca_modelo_id' || ' in(''' ||pParMarcaModeloId||''')';
  END IF;	
	
	IF pParMarcaModeloNome != '' THEN
			vSql = vSql || ' and ' ||'t1.ger_marca_modelo_nome'||' like ' || '''%' ||pParMarcaModeloNome|| '%'' ';
  END IF;	
	
	IF pParMarcaModeloAtivo != '' THEN
			vSql = vSql || ' and ' ||'t1.ger_marca_modelo_ativo_desc'||' like ' || '''%' ||pParMarcaModeloAtivo|| '%'' ';
	END IF;	
	
	IF pParMarcaId != '' THEN
				vSql = vSql || 'and ' || ' t1.ger_marca_id' || ' in(''' ||pParMarcaId||''')';
  END IF;	
	
	IF pParMarcaNome != '' THEN
			vSql = vSql || ' and ' ||'t1.ger_marca_nome'||' like ' || '''%' ||pParMarcaNome|| '%'' ';
  END IF;		
	
	IF pParMarcaAtivo != '' THEN
			vSql = vSql || ' and ' ||'t1.ger_marca_ativo_desc'||' like ' || '''%' ||pParMarcaAtivo|| '%'' ';
  END IF;	
		
	IF pParSubGrupId != '' THEN
				vSql = vSql || 'and ' || ' t1.ope_centro_subgrupo_id' || ' in(''' ||pParSubGrupId||''')';
  END IF;	
	
	IF pParSubGrupoNome != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro_subgrupo_nome'||' like ' || '''%' ||pParSubGrupoNome|| '%'' ';
  END IF;		
	
	IF pParSubGrupoAtivo != '' THEN
			vSql = vSql || ' and ' ||'t1.ope_centro_subgrupo_ativo_desc'||' like ' || '''%' ||pParSubGrupoAtivo|| '%'' ';
  END IF;
		
	IF pParGrupoId != '' THEN
				vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id' || ' in(''' ||pParGrupoId||''')';
  END IF;		
	
	IF pParGrupoNome != '' THEN
				vSql = vSql || ' and ' ||'t1.ope_centro_grupo_nome'||' like ' || '''%' ||pParGrupoNome|| '%'' ';
  END IF;		
	
	IF pParGrupoAtivo != '' THEN
				vSql = vSql || ' and ' ||'t1.ope_centro_grupo_ativo_desc'||' like ' || '''%' ||pParGrupoAtivo|| '%'' ';
  END IF;		
	
	IF pParProprietarioId != '' THEN
				vSql = vSql || 'and ' || ' t1.ger_pessoa_proprietario_id' || ' in(''' ||pParProprietarioId||''')';
  END IF;
	
	IF pParProprietarioNome != '' THEN
				vSql = vSql || ' and ' ||'t1.ger_pessoa_proprietario_nome'||' like ' || '''%' ||pParProprietarioNome|| '%'' ';
  END IF;		
	
	IF pParProprietarioAtivo != '' THEN
				vSql = vSql || ' and ' ||'t1.ger_pessoa_proprietario_ativo_desc'||' like ' || '''%' ||pParProprietarioAtivo|| '%'' ';
  END IF;			

	IF pParProprietarioDoc != '' THEN
				vSql = vSql || ' and ' ||'t1.ger_pessoa_proprietario_doc_cpf_cnpj_desc'||' like ' || '''%' ||pParProprietarioDoc|| '%'' ';
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


	
-- GROUP BY
-- 	vSql = vSql || ' group by valor_01,valor_02,valor_03,valor_04,valor_05,valor_06,valor_07,valor_08,valor_09,valor_10,' || pVart01;
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
	
	raise notice'vSql :%', vSql;
	
		FOR r IN EXECUTE vSql loop
	
		ind_rel_id := pParIndRelId;
		ind_rel_par1 := vPar1;
		ind_rel_par2 := vPar2;
		ind_rel_par3 := vPar3;
		ind_rel_par4 := vPar4;
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
-- 		valor_02 := r.valor_02;
-- 		valor_03 := r.valor_03;
-- 		valor_04 := r.valor_04;
-- 		valor_05 := r.valor_05;
-- 		valor_06 := r.valor_06;
-- 		valor_07 := r.valor_07;
-- 		valor_07 := r.valor_07;
-- 		valor_08 := r.valor_08;
-- 		valor_09 := r.valor_09;
-- 		valor_10 := r.valor_10;
		
	RETURN NEXT;
	
END loop;
raise notice'vSql :%',vSql;

END;
$BODY$ LANGUAGE plpgsql VOLATILE;