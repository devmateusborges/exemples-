Drop FUNCTION IF EXISTS fnreport0026;
CREATE OR REPLACE FUNCTION fnreport0026(
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
pParCentro1Nome varchar default null,
pParCentro1Sigla varchar default null,
pParCentro1Ativo varchar default null,
pParCentro2Nome varchar default null,
pParCentro2Ativo varchar default null,
pParCentro2Sigla varchar default null,
pParCentro2EquipTipoRodad varchar default null,
pParCentro2EquipTipoCarroc varchar default null,
pParCentro2EquipCid varchar default null,
pParCentro2EquipUf varchar default null,
pParCentro2EquipPlaca varchar default null,
pParCentro2EquipRenavam varchar default null,
pParCentro2EquipTara varchar default null,
pParCentro2EquipCapacidKg varchar default null,
pParCentro2EquipCapacidM3 varchar default null,
pParCentro2EquipPotenc varchar default null,
pParCentro2EquipNrChassi varchar default null,
pParCentro2EquipNrSerie varchar default null,
pParCentro2EquipLiberadoAbastec varchar default null,
pParCentro2EquipNrRegisEstadual varchar default null,
pParCentro2EquipTipoTracao varchar default null,
pParCentro2EquipTranspAutoCarg varchar default null,
pParCompartNome varchar default null,
pParCompartAtivo varchar default null,
pParCompartSigla varchar default null,
pParCompartCapacid varchar default null,
pParCompartValidItemServ varchar default null,
pParCompartDtAquisicaoIni varchar default null,
pParCompartDtAquisicaoFin varchar default null,
pParCompartVrAquisicao varchar default null,
pParCompartNrSerie varchar default null,
pParOcorMovDataMovIni varchar default null,
pParOcorMovDataMovFin varchar default null,
pParOcorMovNr varchar default null,
pParGerEmpresaNome varchar default null,
pParGerEmpresaAtivo varchar default null,
pParGerEmpresaDocCnpj varchar default null,
pParGerEmpresaDocCpf varchar default null,
pParGerPessoaEnderecoLograd varchar default null,
pParGerPessoaEnderecoLogradNr varchar default null,
pParGerCidadeNome varchar default null,
pParUfNome varchar default null,
pParOcorTipoNome varchar default null,
pParOcorTipoAtivo varchar default null,
pParOcorTipoSigla varchar default null,
pParOcorTipoObrigCompart varchar default null,
pParOcorTipoTp varchar default null,
pParOcorMovDetQntOcor varchar default null,
pParOcorMovDetQntOcorCalc varchar default null,
pParOcorMovDetDtStatusIni varchar default null,
pParOcorMovDetDtStatusFin varchar default null,
pParOcorNome varchar default null,
pParOcorAtivo varchar default null,
pParOcorSigla varchar default null,
pParOcorTipo varchar default null,
pParOcorTipoLanc varchar default null,
pParOcorGrupoNome varchar default null,
pParOcorGrupoAtivo varchar default null,
pParOcorGrupoSigla varchar default null,
pParGerUmedidaNome varchar default null,
pParGerUmedidaAtivo varchar default null,
pParGerUmedidaSigla varchar default null,
pParOcorStatusNome varchar default null,
pParOcorStatusAtivo varchar default null,
pParOcorStatusSigla varchar default null,
pParOcorStatusTipo varchar default null,
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
 ind_rel_par4 varchar,
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
DECLARE
vSql varchar;
vPar1 varchar :='';
vPar2 varchar :='';
vPar3 varchar :='';
vPar4 varchar :='';
r record;
begin
	
	if pParCentro1Nome != '' THEN
		vPar1 = vPar1||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Nome Centro 1 [] '||chr(13)||chr(10);
	end if;

	if pParCentro1Ativo != '' THEN
		vPar1 = vPar1||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Centro 1 Ativo [] '||chr(13)||chr(10);
	end if;

	if pParCentro1Sigla != '' THEN
		vPar1 = vPar1||'Sigla Centro 1 ['||pParCentro1Sigla||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Sigla Centro 1 [] '||chr(13)||chr(10);
	end if;

	if pParCentro2Nome != '' THEN
		vPar1 = vPar1||'Equipamento ['||pParCentro2Nome||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Equipamento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2Ativo != '' THEN
		vPar1 = vPar1||'Equipamento Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Equipamento Ativo [] '||chr(13)||chr(10);
	end if;

	if pParCentro2Sigla != '' THEN
		vPar1 = vPar1||'Sigla Equipamento ['||pParCentro2Sigla||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Sigla Equipamento [] '||chr(13)||chr(10);
	end if;
	if pParCentro2EquipTipoRodad != '' THEN
		vPar1 = vPar1||'Tipo Rodado Equipamento ['||pParCentro2EquipTipoRodad||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Tipo Rodado Equipamento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2EquipTipoCarroc != '' THEN
		vPar1 = vPar1||'Tipo Carroceria Equipamento ['||pParCentro2EquipTipoCarroc||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Tipo Carroceria Equipamento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2EquipCid != '' THEN
		vPar1 = vPar1||'Equipamento Cidade ['||pParCentro2EquipCid||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Equipamento Cidade [] '||chr(13)||chr(10);
	end if;
	if pParCentro2EquipUf != '' THEN
		vPar1 = vPar1||'Estado Equipamento ['||pParCentro2EquipUf||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Estado Equipamento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2EquipPlaca != '' THEN
		vPar1 = vPar1||'Placa Equipamento ['||pParCentro2EquipPlaca||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Placa Equipamento [] '||chr(13)||chr(10);
	end if;
	if pParCentro2EquipRenavam != '' THEN
		vPar1 = vPar1||'Renavam Equipamento ['||pParCentro2EquipRenavam||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Renavam Equipamento [] '||chr(13)||chr(10);
	end if;
	if pParCentro2EquipTara != '' THEN
		vPar1 = vPar1||'Tara Equipamento ['||pParCentro2EquipTara||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Tara Equipamento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2EquipCapacidM3 != '' THEN
		vPar1 = vPar1||'Capacidade M³ Equipamento ['||pParCentro2EquipCapacidM3||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Capacidade M³ Equipamento [] '||chr(13)||chr(10);
	end if;
	if pParCentro2EquipPotenc != '' THEN
		vPar1 = vPar1||'Potência Equipamento ['||pParCentro2EquipPotenc||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Potência Equipamento [] '||chr(13)||chr(10);
	end if;
	
	if pParCentro2EquipNrChassi != '' THEN
		vPar1 = vPar1||'Nº Chassi Equipamento ['||pParCentro2EquipNrChassi||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Nº Chassi Equipamento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2EquipNrSerie != '' THEN
		vPar2 = vPar2||'Nº Serie Equipamento ['||pParCentro2EquipNrSerie||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Nº Serie Equipamento [] '||chr(13)||chr(10);
	end if;
	if pParCentro2EquipLiberadoAbastec != '' THEN
		vPar2 = vPar2||'Equipamento Liberado Abastecimento ['||pParCentro2EquipLiberadoAbastec||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Equipamento Liberado Abastecimento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2EquipNrRegisEstadual != '' THEN
		vPar2 = vPar2||'Nº Registro Estadual Equipamento ['||pParCentro2EquipNrRegisEstadual||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Nº Registro Estadual Equipamento [] '||chr(13)||chr(10);
	end if;
	if pParCentro2EquipTipoTracao != '' THEN
		vPar2 = vPar2||'Tipo Tração Equipamento ['||pParCentro2EquipTipoTracao||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Tipo Tração Equipamento [] '||chr(13)||chr(10);
	end if;

	if pParCentro2EquipTranspAutoCarg != '' THEN
		vPar2 = vPar2||'Tipo Transp. Automo Carga  ['||pParCentro2EquipTranspAutoCarg||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Tipo Transp. Automo Carga  [] '||chr(13)||chr(10);
	end if;
	if pParCompartNome != '' THEN
		vPar2 = vPar2||'Nome Compartimento ['||pParCompartNome||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Nome Compartimento [] '||chr(13)||chr(10);
	end if;
	if pParCompartAtivo != '' THEN
		vPar2 = vPar2||'Compartimento Ativo ['||pParCompartAtivo||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Compartimento Ativo [] '||chr(13)||chr(10);
	end if;

	if pParCompartSigla != '' THEN
		vPar2 = vPar2||'Sigla Compartimento ['||pParCompartSigla||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Sigla Compartimento [] '||chr(13)||chr(10);
	end if;
	
	if pParCompartCapacid != '' THEN
		vPar2 = vPar2||'Capacidade Compartimento ['||pParCompartCapacid||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Capacidade Compartimento [] '||chr(13)||chr(10);
	end if;	

	if pParCompartValidItemServ != '' THEN
		vPar2 = vPar2||'Valida Item/Serviço ['||pParCompartValidItemServ||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Valida Item/Serviço [] '||chr(13)||chr(10);
	end if;
	if pParCompartVrAquisicao != '' THEN
		vPar2 = vPar2||'Valor Aquisição Compartimento ['||pParCompartVrAquisicao||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Valor Aquisição Compartimento [] '||chr(13)||chr(10);
	end if;
	if pParCompartNrSerie != '' THEN
		vPar2 = vPar2||'Nº Serie Compartimento ['||pParCompartNrSerie||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Nº Serie Compartimento [] '||chr(13)||chr(10);
	end if;
	
	if pParOcorMovNr != '' THEN
		vPar2 = vPar2||'Número do Movimento ['||pParOcorMovNr||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Número do Movimento [] '||chr(13)||chr(10);
	end if;

	if pParGerEmpresaNome != '' THEN
		vPar2 = vPar2||'Empresa ['||pParGerEmpresaNome||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Empresa []'||chr(13)||chr(10);
	end if;

	if pParGerEmpresaAtivo != '' THEN	
		vPar2 = vPar2||'Empresa Ativo ['||pParGerEmpresaAtivo||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Empresa Ativo []'||chr(13)||chr(10);
	end if;
	
	if pParGerEmpresaDocCnpj != '' THEN	
		vPar2 = vPar2||'CNPJ Empresa ['||pParGerEmpresaDocCnpj||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'CNPJ Empresa []'||chr(13)||chr(10);
	end if;
	
	if pParGerEmpresaDocCpf != '' THEN	
		vPar3 = vPar3||'CPF Empresa ['||pParGerEmpresaDocCpf||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'CPF Empresa []'||chr(13)||chr(10);
	end if;

	if pParGerPessoaEnderecoLograd != '' THEN	
		vPar3 = vPar3||'Endereço ['||pParGerPessoaEnderecoLograd||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Endereço []'||chr(13)||chr(10);
	end if;

	if pParGerPessoaEnderecoLogradNr != '' THEN	
		vPar3 = vPar3||'Nº Endereço ['||pParGerPessoaEnderecoLogradNr||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Nº Endereço []'||chr(13)||chr(10);
	end if;
	
	if pParGerCidadeNome != '' THEN	
		vPar3 = vPar3||'Cidade ['||pParGerCidadeNome||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Cidade []'||chr(13)||chr(10);
	end if;	

	if pParUfNome != '' THEN	
		vPar3 = vPar3||'Estado ['||pParUfNome||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Estado []'||chr(13)||chr(10);
	end if;		
	
	if pParOcorTipoNome != '' THEN	
		vPar3 = vPar3||'Nome Tipo Ocorrência ['||pParOcorTipoNome||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Nome Tipo Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParOcorTipoAtivo != '' THEN	
		vPar3 = vPar3||'Tipo Ocorrência Ativo ['||pParOcorTipoAtivo||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Tipo Ocorrência Ativo []'||chr(13)||chr(10);
	end if;
	
	if pParOcorTipoSigla != '' THEN	
		vPar3 = vPar3||'Sigla Tipo Ocorrência ['||pParOcorTipoSigla||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Sigla Tipo Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorTipoObrigCompart != '' THEN	
		vPar3 = vPar3||'Tipo Ocorrência Obrigatorio ['||pParOcorTipoObrigCompart||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Tipo Ocorrência Obrigatorio []'||chr(13)||chr(10);
	end if;

	if pParOcorTipoTp != '' THEN	
		vPar3 = vPar3||'Tipo Ocorrência ['||pParOcorTipoTp||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Tipo Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorMovDetQntOcor != '' THEN	
		vPar3 = vPar3||'Quantidade da Ocorrência ['||pParOcorMovDetQntOcor||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Quantidade da Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParOcorMovDetQntOcorCalc != '' THEN	
		vPar3 = vPar3||'Quantidade Cálculada da Ocorrência ['||pParOcorMovDetQntOcorCalc||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Quantidade Cálculada da Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorNome != '' THEN	
		vPar3 = vPar3||'Ocorrência ['||pParOcorNome||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParOcorAtivo != '' THEN	
		vPar3 = vPar3||'Ocorrência Ativa ['||pParOcorAtivo||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Ocorrência Ativa []'||chr(13)||chr(10);
	end if;
	
	if pParOcorSigla != '' THEN	
		vPar3 = vPar3||'Sigla Ocorrência ['||pParOcorSigla||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Sigla Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParOcorTipo != '' THEN	
		vPar3 = vPar3||'Tipo Ocorrência ['||pParOcorTipo||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Tipo Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorTipoLanc != '' THEN	
		vPar4 = vPar4||'Tipo Lancamento Ocorrência ['||pParOcorTipoLanc||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Tipo Lancamento Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorGrupoNome != '' THEN	
		vPar4 = vPar4||'Grupo de Ocorrência ['||pParOcorGrupoNome||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Grupo de Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorGrupoAtivo != '' THEN	
		vPar4 = vPar4||'Grupo de Ocorrência Ativo ['||pParOcorGrupoAtivo||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Grupo de Ocorrência Ativo []'||chr(13)||chr(10);
	end if;

	if pParOcorGrupoSigla != '' THEN	
		vPar4 = vPar4||'Sigla Grupo de Ocorrência ['||pParOcorGrupoSigla||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Sigla Grupo de Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParGerUmedidaNome != '' THEN	
		vPar4 = vPar4||'U. Medida Ocorrência ['||pParGerUmedidaNome||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'U. Medida Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParGerUmedidaAtivo != '' THEN	
		vPar4 = vPar4||'U. Medida Ocorrência Ativo ['||pParGerUmedidaAtivo||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'U. Medida Ocorrência Ativo []'||chr(13)||chr(10);
	end if;
	
	if pParGerUmedidaSigla != '' THEN	
		vPar4 = vPar4||'Sigla U. Medida Ocorrência ['||pParGerUmedidaSigla||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Sigla U. Medida Ocorrência []'||chr(13)||chr(10);
	end if;	

	if pParOcorStatusNome != '' THEN	
		vPar4 = vPar4||'Status da Ocorrência ['||pParOcorStatusNome||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Status da Ocorrência []'||chr(13)||chr(10);
	end if;	

	if pParOcorStatusAtivo != '' THEN	
		vPar4 = vPar4||'Status da Ocorrência Ativo ['||pParOcorStatusAtivo||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Status da Ocorrência Ativo []'||chr(13)||chr(10);
	end if;	

	if pParOcorStatusSigla != '' THEN	
		vPar4 = vPar4||'Sigla Status da Ocorrência ['||pParOcorStatusSigla||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Sigla Status da Ocorrência []'||chr(13)||chr(10);
	end if;	

	if pParOcorStatusTipo != '' THEN	
		vPar4 = vPar4||'Tipo Status da Ocorrência ['||pParOcorStatusTipo||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Tipo Status da Ocorrência []'||chr(13)||chr(10);
	end if;	
	
	if pParLogUserIns != '' then
		vPar4 = vPar4||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Log Usuario Inserção []'||chr(13)||chr(10);
	end if;

	if pParLogUserUpd != '' then
		vPar4 = vPar4||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Log Usuario Alteração []'||chr(13)||chr(10);
	end if;

-- Datas
	if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
		vPar4 = vPar4||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Inserção de [] até []'||chr(13)||chr(10);
	end if;

	if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
		vPar4 = vPar4||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Alteração de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParCompartDtAquisicaoIni != '' and pParCompartDtAquisicaoFin != '' THEN
		vPar4 = vPar4||'Data de Aquisição Compartimento de ['||pParCompartDtAquisicaoIni||'] até ['||pParCompartDtAquisicaoFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data de Aquisição Compartimento de [] até []'||chr(13)||chr(10);
	end if;
	if pParOcorMovDataMovIni != '' and pParOcorMovDataMovFin != '' THEN
		vPar4 = vPar4||'Data do Movimento de ['||pParOcorMovDataMovIni||'] até ['||pParOcorMovDataMovFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data do Movimento de [] até []'||chr(13)||chr(10);
	end if;

	if pParOcorMovDetDtStatusIni != '' and pParOcorMovDetDtStatusFin != '' THEN
		vPar4 = vPar4||'Data Status Ocorrência de ['||pParOcorMovDetDtStatusIni||'] até ['||pParOcorMovDetDtStatusFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Status Ocorrência de [] até []'||chr(13)||chr(10);
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
		
		vSql = vSql||' 
		,count(1) as valor_01
		from vwope_ocor_mov_dest_equip t1 where 1=1 ';
		
		if pParUnitId != '' then
			vSql = vSql || 'and ' || ' t1.unit_id' || ' in(''' ||pParUnitId||''')';
		end if;
		
		if pParCentro1Nome != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro1_nome' || ' like '||'''' ||pParCentro1Nome||'''';
		end if;
	
		if pParCentro1Sigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro1_sigla' || ' like '||'''' ||pParCentro1Sigla||'''';
		end if;

		if pParCentro1Ativo != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro1_ativo' || ' like '||'''' ||pParCentro1Ativo||'''';
		end if;

		if pParCentro2Nome != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '||'''' ||pParCentro2Nome||'''';
		end if;
		
		if pParCentro2Ativo != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_ativo' || ' like '||'''' ||pParCentro2Ativo||'''';
		end if;

		if pParCentro2Sigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_sigla' || ' like '||'''' ||pParCentro2Sigla||'''';
		end if;

		if pParCentro2EquipTipoRodad != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_rodado' || ' like '||'''' ||pParCentro2EquipTipoRodad||'''';
		end if;

		if pParCentro2EquipTipoCarroc != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_carroceria' || ' like '||'''' ||pParCentro2EquipTipoCarroc||'''';
		end if;

		if pParCentro2EquipCid != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_cidade_nome' || ' like '||'''' ||pParCentro2EquipCid||'''';
		end if;

		if pParCentro2EquipUf != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_uf_sigla' || ' like '||'''' ||pParCentro2EquipUf||'''';
		end if;

		if pParCentro2EquipPlaca != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_placa' || ' like '||'''' ||pParCentro2EquipPlaca||'''';
		end if;

		if pParCentro2EquipRenavam != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_renavam' || ' like '||'''' ||pParCentro2EquipRenavam||'''';
		end if;

		if pParCentro2EquipTara != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tara' || ' like '||'''' ||pParCentro2EquipTara||'''';
		end if;

		if pParCentro2EquipCapacidKg != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_capacidade_kg::text' || ' like '||'''' ||pParCentro2EquipCapacidKg||'''';
		end if;

		if pParCentro2EquipCapacidM3 != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_capacidade_m3::text' || ' like '||'''' ||pParCentro2EquipCapacidM3||'''';
		end if;

		if pParCentro2EquipPotenc != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_potencia' || ' like '||'''' ||pParCentro2EquipPotenc||'''';
		end if;

		if pParCentro2EquipNrChassi != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_nr_chassi' || ' like '||'''' ||pParCentro2EquipNrChassi||'''';
		end if;

		if pParCentro2EquipNrSerie != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_nr_serie' || ' like '||'''' ||pParCentro2EquipNrSerie||'''';
		end if;

		if pParCentro2EquipLiberadoAbastec != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_liberado_abastec' || ' like '||''''||pParCentro2EquipLiberadoAbastec||'''';
		end if;

		if pParCentro2EquipNrRegisEstadual != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_nr_registro_estadual' || ' like '||'''' ||pParCentro2EquipNrRegisEstadual||'''';
		end if;

		if pParCentro2EquipTipoTracao != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_tracao::text' || ' like '||'''' ||pParCentro2EquipTipoTracao||'''';
		end if;

		if pParCentro2EquipTranspAutoCarg != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_equip_tipo_transp_auto_carga::text' || ' like ' ||'''' ||pParCentro2EquipTranspAutoCarg||'''';
		end if;

		if pParCompartNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_nome' || ' like '||'''' ||pParCompartNome||'''';
		end if;

		if pParCompartAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_ativo' || ' like '||'''' ||pParCompartAtivo||'''';
		end if;

		if pParCompartSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_sigla' || ' like '||'''' ||pParCompartSigla||'''';
		end if;

		if pParCompartCapacid != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_capacidade' || ' like ' ||'''' ||pParCompartCapacid||'''';
		end if;

		if pParCompartValidItemServ != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_validade_itemserv' || ' like '||'''' ||pParCompartValidItemServ||'''';
		end if;

		if pParCompartValidItemServ != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_validade_itemserv' || ' like '||'''' ||pParCompartValidItemServ||'''';
		end if;

		if pParCompartVrAquisicao != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_vr_aquisicao' || ' like '||'''' ||pParCompartVrAquisicao||'''';
		end if;

		if pParCompartNrSerie != '' then
			vSql = vSql || 'and ' || ' t1.ope_compart_nr_serie' || ' like '||'''' ||pParCompartNrSerie||'''';
		end if;

		if pParOcorMovNr != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_mov_numero' || ' like '||'''' ||pParOcorMovNr||'''';
		end if;

---
		if pParGerEmpresaNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_nome' || ' like '||'''' ||pParGerEmpresaNome||'''';
		end if;

		if pParGerEmpresaAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_ativo' || ' like ' ||'''' ||pParGerEmpresaAtivo||'''';
		end if;

		if pParGerEmpresaDocCnpj != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cnpj' || ' like '||'''' ||pParGerEmpresaDocCnpj||'''';
		end if;
		
		if pParGerEmpresaDocCpf != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cpf' || ' like '||'''' ||pParGerEmpresaDocCpf||'''';
		end if;

		if pParGerPessoaEnderecoLograd != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco' || ' like '||'''' ||pParGerPessoaEnderecoLograd||'''';
		end if;
		
		if pParGerPessoaEnderecoLogradNr != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nr' || ' like '||'''' ||pParGerPessoaEnderecoLogradNr||'''';
		end if;

		if pParGerCidadeNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nome_cidade' || ' like '||'''' ||pParGerCidadeNome||'''';
		end if;
		
		if pParUfNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_uf' || ' like '||'''' ||pParUfNome||'''';
		end if;

		if pParOcorTipoNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_nome' || ' like '||'''' ||pParOcorTipoNome||'''';
		end if;

		if pParOcorTipoAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_ativo' || ' like '||'''' ||pParOcorTipoAtivo||'''';
		end if;
		
		if pParOcorTipoSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_sigla' || ' like '||'''' ||pParOcorTipoSigla||'''';
		end if;		

		if pParOcorTipoTp != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_tp' || ' like '||'''' ||pParOcorTipoTp||'''';
		end if;

		if pParOcorTipoObrigCompart != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_obrig' || ' like '||'''' ||pParOcorTipoObrigCompart||'''';
		end if;

		if pParOcorMovDetQntOcor != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor::text' || ' like '||'''' ||pParOcorMovDetQntOcor||'''';
		end if;

		if pParOcorMovDetQntOcorCalc != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor_calc::text' || ' like '||'''' ||pParOcorMovDetQntOcorCalc||'''';
		end if;
		
		if pParOcorNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_nome' || ' like '||'''' ||pParOcorNome||'''';
		end if;		

		if pParOcorAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_ativo' || ' like '||'''' ||pParOcorAtivo||'''';
		end if;

		if pParOcorSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_sigla' || ' like '||'''' ||pParOcorSigla||'''';
		end if;

		if pParOcorTipo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo' || ' like '||'''' ||pParOcorTipo||'''';
		end if;

		if pParOcorTipoLanc != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_lanc' || ' like '||'''' ||pParOcorTipoLanc||'''';
		end if;

		if pParOcorGrupoNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_nome' || ' like '||'''' ||pParOcorGrupoNome||'''';
		end if;

		if pParOcorGrupoAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_ativo' || ' like '||'''' ||pParOcorGrupoAtivo||'''';
		end if;	

		if pParOcorGrupoSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_sigla' || ' like '||'''' ||pParOcorGrupoSigla||'''';
		end if;
		
		if pParGerUmedidaNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_umedida_nome' || ' like '||'''' ||pParGerUmedidaNome||'''';
		end if;

		if pParGerUmedidaAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ger_umedida_ativo' || ' like '||'''' ||pParGerUmedidaAtivo||'''';
		end if;

		if pParGerUmedidaSigla != '' then
			vSql = vSql || 'and ' || ' t1.ger_umedida_sigla' || ' like '||'''' ||pParGerUmedidaSigla||'''';
		end if;

		if pParOcorStatusNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_nome' || ' like '||'''' ||pParOcorStatusNome||'''';
		end if;

		if pParOcorStatusAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_ativo' || ' like '||'''' ||pParOcorStatusAtivo||'''';
		end if;
		
		if pParOcorStatusSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_sigla' || ' like '||'''' ||pParOcorStatusSigla||'''';
		end if;

		if pParOcorStatusTipo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_tipo_status' || ' like '||'''' ||pParOcorStatusTipo||'''';
		end if;

		if pParLogUserIns != '' then 
			vSql = vSql ||' and '||'t1.log_user_ins'||' in(''' ||pParLogUserIns||''')';
		end if; 
		 
		if pParLogUserUpd != '' then 
			vSql = vSql ||' and '||'t1.log_user_upd'||' in(''' ||pParLogUserUpd||''')';
		end if;
		

		--data
		if pParLogDateInsIni != '' and pParLogDateInsFin != '' then 
			vSql = vSql ||' and '||' CAST(t1.log_date_ins AS DATE)'||' >= '''||pParLogDateInsIni||''''||'and CAST(t1.log_date_ins AS DATE)'||' <= '''||pParLogDateInsFin||'''';
		end if;		 
		
		if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then 
			vSql = vSql ||' and '||'CAST(t1.log_date_upd AS DATE)'||' >= '''||pParLogDateUpdIni||''''||' and  CAST(t1.log_date_upd AS DATE)'||' <= '''||pParLogDateUpdFin||'''';
		end if;	
		 
		if pParCompartDtAquisicaoIni != '' and pParCompartDtAquisicaoFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_compart_data_aquisicao AS DATE)' || ' >= ''' || pParCompartDtAquisicaoIni|| '''' || ' and  CAST(t1.ope_compart_data_aquisicao AS DATE)' || ' <= ''' || pParCompartDtAquisicaoFin || '''';
		end if;
		
		if pParOcorMovDataMovIni != '' and pParOcorMovDataMovFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' >= ''' || pParOcorMovDataMovIni|| '''' || ' and  CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' <= ''' || pParOcorMovDataMovFin || '''';
		end if;

		if pParOcorMovDetDtStatusIni != '' and pParOcorMovDetDtStatusFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' >= ''' || pParOcorMovDetDtStatusIni|| '''' || ' and  CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' <= ''' || pParOcorMovDetDtStatusFin || '''';
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
		valor_01 := r.valor_01;
	
	RETURN NEXT;
	
	END loop;



end;
$BODY$
LANGUAGE plpgsql VOLATILE;