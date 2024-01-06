Drop FUNCTION IF EXISTS fnreport0025;
CREATE OR REPLACE FUNCTION fnreport0025(
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
pParOpeAreaQntAreaProd varchar default null,
pParOpeAreaQntAreaImprod varchar default null,
pParOpeAreaQntPlantEstand varchar default null,
pParOpeAreaBlocoCol varchar default null,
pParOpeAreaDtIniPlan varchar default null,
pParOpeAreaDtIniPlanFin varchar default null,
pParOpeAreaDtFinPlanIni varchar default null,
pParOpeAreaDtFinPlan varchar default null,
pParOpeAreaDtUltPlanIni varchar default null,
pParOpeAreaDtUltPlanFin varchar default null,
pParOpeAreaDtIniCol varchar default null,
pParOpeAreaDtIniColFin varchar default null,
pParOpeAreaDtFinColIni varchar default null,
pParOpeAreaDtFinCol varchar default null,
pParOpeAreaDtUltColIni varchar default null,
pParOpeAreaDtUltColFin varchar default null,
pParOpeAreaDtFlorada1Ini varchar default null,
pParOpeAreaDtFlorada1Fin varchar default null,
pParOpeAreaDtEmergIni varchar default null,
pParOpeAreaDtEmergFin varchar default null,
pParOpeAreaUmedidaNome varchar default null,
pParOpeAreaUmedidaSigla varchar default null,
pParCentro2Nome varchar default null,
pParCentro2Sigla varchar default null,
pParCentro2Ativo varchar default null,
pParCentro2TipoDestinacao varchar default null,
pParCentro2TipoProp varchar default null,
pParCentro1Nome varchar default null,
pParCentro1Ativo varchar default null,
pParCentro1Sigla varchar default null,
pParAreaSistemaCultNome varchar default null,
pParAreaSistemaCultSigla varchar default null,
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


	if pParOcorMovNr != '' THEN
		vPar1 = vPar1||'Número do Movimento ['||pParOcorMovNr||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Número do Movimento [] '||chr(13)||chr(10);
	end if;
	
	if pParGerEmpresaNome != '' THEN
		vPar1 = vPar1||'Empresa ['||pParGerEmpresaNome||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Empresa []'||chr(13)||chr(10);
	end if;

	if pParGerEmpresaAtivo != '' THEN	
		vPar1 = vPar1||'Empresa Ativo ['||pParGerEmpresaAtivo||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Empresa Ativo []'||chr(13)||chr(10);
	end if;
	
	if pParGerEmpresaDocCnpj != '' THEN	
		vPar1 = vPar1||'CNPJ Empresa ['||pParGerEmpresaDocCnpj||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'CNPJ Empresa []'||chr(13)||chr(10);
	end if;
	
	if pParGerEmpresaDocCpf != '' THEN	
		vPar1 = vPar1||'CPF Empresa ['||pParGerEmpresaDocCpf||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'CPF Empresa []'||chr(13)||chr(10);
	end if;
	if pParGerPessoaEnderecoLograd != '' THEN	
		vPar1 = vPar1||'Endereço ['||pParGerPessoaEnderecoLograd||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Endereço []'||chr(13)||chr(10);
	end if;

	if pParGerPessoaEnderecoLogradNr != '' THEN	
		vPar1 = vPar1||'Nº Endereço ['||pParGerPessoaEnderecoLogradNr||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Nº Endereço []'||chr(13)||chr(10);
	end if;
	
	if pParGerCidadeNome != '' THEN	
		vPar1 = vPar1||'Cidade ['||pParGerCidadeNome||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Cidade []'||chr(13)||chr(10);
	end if;	

	if pParUfNome != '' THEN	
		vPar1 = vPar1||'Estado ['||pParUfNome||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Estado []'||chr(13)||chr(10);
	end if;	

	if pParOcorTipoNome != '' THEN	
		vPar1 = vPar1||'Nome Tipo Ocorrência ['||pParOcorTipoNome||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Nome Tipo Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParOcorTipoAtivo != '' THEN	
		vPar1 = vPar1||'Tipo Ocorrência Ativo ['||pParOcorTipoAtivo||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Tipo Ocorrência Ativo []'||chr(13)||chr(10);
	end if;
	
	if pParOcorTipoSigla != '' THEN	
		vPar1 = vPar1||'Sigla Tipo Ocorrência ['||pParOcorTipoSigla||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Sigla Tipo Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorTipoObrigCompart != '' THEN	
		vPar1 = vPar1||'Tipo Ocorrência Obrigatorio ['||pParOcorTipoObrigCompart||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Tipo Ocorrência Obrigatorio []'||chr(13)||chr(10);
	end if;

	if pParOcorTipoTp != '' THEN	
		vPar1 = vPar1||'Tipo Ocorrência ['||pParOcorTipoTp||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Tipo Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorMovDetQntOcor != '' THEN	
		vPar1 = vPar1||'Quantidade da Ocorrência ['||pParOcorMovDetQntOcor||']'||chr(13)||chr(10);
	else
		vPar1 = vPar1||'Quantidade da Ocorrência []'||chr(13)||chr(10);
	end if;
	if pParOcorMovDetQntOcorCalc != '' THEN	
		vPar2 = vPar2||'Quantidade Cálculada da Ocorrência ['||pParOcorMovDetQntOcorCalc||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Quantidade Cálculada da Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParOcorNome != '' THEN	
		vPar2 = vPar2||'Ocorrência ['||pParOcorNome||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParOcorAtivo != '' THEN	
		vPar2 = vPar2||'Ocorrência Ativa ['||pParOcorAtivo||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Ocorrência Ativa []'||chr(13)||chr(10);
	end if;
	
	if pParOcorSigla != '' THEN	
		vPar2 = vPar2||'Sigla Ocorrência ['||pParOcorSigla||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Sigla Ocorrência []'||chr(13)||chr(10);
	end if;
	if pParOcorTipo != '' THEN	
		vPar2 = vPar2||'Tipo Ocorrência ['||pParOcorTipo||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Tipo Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorTipoLanc != '' THEN	
		vPar2 = vPar2||'Tipo Lancamento Ocorrência ['||pParOcorTipoLanc||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Tipo Lancamento Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorGrupoNome != '' THEN	
		vPar2 = vPar2||'Grupo de Ocorrência ['||pParOcorGrupoNome||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Grupo de Ocorrência []'||chr(13)||chr(10);
	end if;
	
	if pParOcorGrupoAtivo != '' THEN	
		vPar2 = vPar2||'Grupo de Ocorrência Ativo ['||pParOcorGrupoAtivo||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Grupo de Ocorrência Ativo []'||chr(13)||chr(10);
	end if;
	if pParOcorGrupoSigla != '' THEN	
		vPar2 = vPar2||'Sigla Grupo de Ocorrência ['||pParOcorGrupoSigla||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Sigla Grupo de Ocorrência []'||chr(13)||chr(10);
	end if;

	if pParGerUmedidaNome != '' THEN	
		vPar2 = vPar2||'U. Medida Ocorrência ['||pParGerUmedidaNome||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'U. Medida Ocorrência []'||chr(13)||chr(10);
	end if;
	if pParGerUmedidaAtivo != '' THEN	
		vPar2 = vPar2||'U. Medida Ocorrência Ativo ['||pParGerUmedidaAtivo||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'U. Medida Ocorrência Ativo []'||chr(13)||chr(10);
	end if;
	
	if pParGerUmedidaSigla != '' THEN	
		vPar2 = vPar2||'Sigla U. Medida Ocorrência ['||pParGerUmedidaSigla||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Sigla U. Medida Ocorrência []'||chr(13)||chr(10);
	end if;	

	if pParOcorStatusNome != '' THEN	
		vPar2 = vPar2||'Status da Ocorrência ['||pParOcorStatusNome||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Status da Ocorrência []'||chr(13)||chr(10);
	end if;	
	if pParOcorStatusAtivo != '' THEN	
		vPar2 = vPar2||'Status da Ocorrência Ativo ['||pParOcorStatusAtivo||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Status da Ocorrência Ativo []'||chr(13)||chr(10);
	end if;	

	if pParOcorStatusSigla != '' THEN	
		vPar2 = vPar2||'Sigla Status da Ocorrência ['||pParOcorStatusSigla||']'||chr(13)||chr(10);
	else
		vPar2 = vPar2||'Sigla Status da Ocorrência []'||chr(13)||chr(10);
	end if;	
	if pParOcorStatusTipo != '' THEN	
		vPar3 = vPar3||'Tipo Status da Ocorrência ['||pParOcorStatusTipo||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Tipo Status da Ocorrência []'||chr(13)||chr(10);
	end if;	

	if pParOpeAreaQntAreaProd != '' THEN
		vPar3 = vPar3||'Qnt Area Produtiva ['||pParOpeAreaQntAreaProd||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Qnt Area Produtiva []'||chr(13)||chr(10);
	end if;

	if pParOpeAreaQntAreaImprod != '' THEN
		vPar3 = vPar3||'Qntd. Area Improdutiva ['||pParOpeAreaQntAreaImprod||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Qntd. Area Improdutiva []'||chr(13)||chr(10);
	end if;		

	if pParOpeAreaQntPlantEstand != '' THEN
		vPar3 = vPar3||'Qntd. de Plantas Estande ['||pParOpeAreaQntPlantEstand||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Qntd. de Plantas Estande []'||chr(13)||chr(10);
	end if;

	if pParOpeAreaBlocoCol != '' THEN
		vPar3 = vPar3||'Bloco de Colheita ['||pParOpeAreaBlocoCol||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Bloco de Colheita []'||chr(13)||chr(10);
	end if;

	if pParOpeAreaUmedidaNome != '' THEN
		vPar3 = vPar3||'U. Medida Área ['||pParOpeAreaUmedidaNome||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'U. Medida Área []'||chr(13)||chr(10);
	end if;
	
	if pParOpeAreaUmedidaSigla != '' THEN
		vPar3 = vPar3||'Sigla U. Medida Área ['||pParOpeAreaUmedidaSigla||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Sigla U. Medida Área []'||chr(13)||chr(10);
	end if;

	if pParCentro2Nome != '' THEN
		vPar3 = vPar3||'Nome Centro 2 ['||pParCentro2Nome||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Nome Centro 2 []'||chr(13)||chr(10);
	end if;

	if pParCentro2Sigla != '' THEN
		vPar3 = vPar3||'Sigla Centro 2 ['||pParCentro2Sigla||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Sigla Centro 2 []'||chr(13)||chr(10);
	end if;

	if pParCentro2Ativo != '' THEN
		vPar3 = vPar3||'Centro 2 Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Centro 2 Ativo []'||chr(13)||chr(10);
	end if;

	if pParCentro2TipoDestinacao != '' THEN
		vPar3 = vPar3||'Tipo Destinação Centro 2 ['||pParCentro2TipoDestinacao||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Tipo Destinação Centro 2 []'||chr(13)||chr(10);
	end if;

	if pParCentro2TipoProp != '' THEN
		vPar3 = vPar3||'Tipo Proprietário ['||pParCentro2TipoProp||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Tipo Proprietário []'||chr(13)||chr(10);
	end if;

	if pParCentro1Nome != '' THEN
		vPar3 = vPar3||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Nome Centro 1 []'||chr(13)||chr(10);
	end if;

	if pParCentro1Ativo != '' THEN
		vPar3 = vPar3||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Centro 1 Ativo []'||chr(13)||chr(10);
	end if;

	if pParCentro1Sigla != '' THEN
		vPar3 = vPar3||'Sigla Centro 1 ['||pParCentro1Sigla||']'||chr(13)||chr(10);
	else
		vPar3 = vPar3||'Sigla Centro 1 []'||chr(13)||chr(10);
	end if;

	if pParAreaSistemaCultNome != '' THEN
		vPar4 = vPar4||'Sistema Atividade Cultivo ['||pParAreaSistemaCultNome||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Sistema Atividade Cultivo []'||chr(13)||chr(10);
	end if;

	if pParAreaSistemaCultSigla != '' THEN
		vPar4 = vPar4||'Sigla Sistema Atividade Cultivo ['||pParAreaSistemaCultSigla||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Sigla Sistema Atividade Cultivo []'||chr(13)||chr(10);
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


	if pParOpeAreaDtIniPlan != '' and pParOpeAreaDtIniPlanFin != '' THEN
		vPar4 = vPar4||'Data Inicial Plantio de ['||pParOpeAreaDtIniPlan||'] até ['||pParOpeAreaDtIniPlanFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Inicial Plantio de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParOpeAreaDtFinPlanIni != '' and pParOpeAreaDtFinPlan != '' THEN
		vPar4 = vPar4||'Data Final Plantio de ['||pParOpeAreaDtFinPlanIni||'] até ['||pParOpeAreaDtFinPlan||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Final Plantio de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParOpeAreaDtUltPlanIni != '' and pParOpeAreaDtUltPlanFin != '' THEN
		vPar4 = vPar4||'Data Último Plantio de ['||pParOpeAreaDtUltPlanIni||'] até ['||pParOpeAreaDtUltPlanFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Último Plantio de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParOpeAreaDtIniCol != '' and pParOpeAreaDtIniColFin != '' THEN
		vPar4 = vPar4||'Data Inicial Colheita de ['||pParOpeAreaDtIniCol||'] até ['||pParOpeAreaDtIniColFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Inicial Colheita de [] até []'||chr(13)||chr(10);
	end if;
	

	if pParOpeAreaDtFinColIni != '' and pParOpeAreaDtFinCol != '' THEN
		vPar4 = vPar4||'Data Final Colheita de ['||pParOpeAreaDtFinColIni||'] até ['||pParOpeAreaDtFinCol||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Final Colheita de [] até []'||chr(13)||chr(10);
	end if;


	if pParOpeAreaDtUltColIni != '' and pParOpeAreaDtUltColFin != '' THEN
		vPar4 = vPar4||'Data Última Colheita de ['||pParOpeAreaDtUltColIni||'] até ['||pParOpeAreaDtUltColFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Última Colheita de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParOpeAreaDtFlorada1Ini != '' and pParOpeAreaDtFlorada1Fin != '' THEN
		vPar4 = vPar4||'Data 1º Florada de ['||pParOpeAreaDtFlorada1Ini||'] até ['||pParOpeAreaDtFlorada1Fin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data 1º Florada de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParOpeAreaDtEmergIni != '' and pParOpeAreaDtEmergFin != '' THEN
		vPar4 = vPar4||'Data Emergência de ['||pParOpeAreaDtEmergIni||'] até ['||pParOpeAreaDtEmergFin||']'||chr(13)||chr(10);
	else
		vPar4 = vPar4||'Data Emergência de [] até []'||chr(13)||chr(10);
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
		from vwope_ocor_mov_dest_area t1 where 1=1 ';
		
		if pParUnitId != '' then
			vSql = vSql || 'and ' || ' t1.unit_id' || ' in(''' ||pParUnitId||''')';
		end if;
		
		if pParOcorMovNr != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_mov_numero' || ' like '||'''' ||pParOcorMovNr||'''';
		end if;

		if pParGerEmpresaNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_nome' || ' like ' ||'''' ||pParGerEmpresaNome||'''';
		end if;

		if pParGerEmpresaAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_ativo' || ' like '||'''' ||pParGerEmpresaAtivo||'''';
		end if;

		if pParGerEmpresaDocCnpj != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cnpj' || ' like ' ||'''' ||pParGerEmpresaDocCnpj||'''';
		end if;
		
		if pParGerEmpresaDocCpf != '' then
			vSql = vSql || 'and ' || ' t1.ger_empresa_doc_cpf' || ' like ' ||'''' ||pParGerEmpresaDocCpf||'''';
		end if;

		if pParGerPessoaEnderecoLograd != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco' || ' like ' ||'''' ||pParGerPessoaEnderecoLograd||'''';
		end if;
		
		if pParGerPessoaEnderecoLogradNr != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nr' || ' like ' ||'''' ||pParGerPessoaEnderecoLogradNr||'''';
		end if;

		if pParGerCidadeNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_nome_cidade' || ' like ' ||'''' ||pParGerCidadeNome||'''';
		end if;
		
		if pParUfNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_uf' || ' like ' ||'''' ||pParUfNome||'''';
		end if;

		if pParOcorTipoNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_nome' || ' like ' ||'''' ||pParOcorTipoNome||'''';
		end if;

		if pParOcorTipoAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_ativo' || ' like ' ||'''' ||pParOcorTipoAtivo||'''';
		end if;
		
		if pParOcorTipoSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_sigla' || ' like ' ||'''' ||pParOcorTipoSigla||'''';
		end if;		

		if pParOcorTipoTp != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_tp' || ' like ' ||'''' ||pParOcorTipoTp||'''';
		end if;

		if pParOcorTipoObrigCompart != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_obrig' || ' like '||'''' ||pParOcorTipoObrigCompart||'''';
		end if;

		if pParOcorMovDetQntOcor != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor::text' || ' like ' ||'''' ||pParOcorMovDetQntOcor||'''';
		end if;

		if pParOcorMovDetQntOcorCalc != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_mov_det_qnt_ocor_calc::text' || ' like ' ||'''' ||pParOcorMovDetQntOcorCalc||'''';
		end if;
		
		if pParOcorNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_nome' || ' like ' ||'''' ||pParOcorNome||'''';
		end if;		

		if pParOcorAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_ativo' || ' like ' ||'''' ||pParOcorAtivo||'''';
		end if;

		if pParOcorSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_sigla' || ' like ' ||'''' ||pParOcorSigla||'''';
		end if;

		if pParOcorTipo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo' || ' like ' ||'''' ||pParOcorTipo||'''';
		end if;

		if pParOcorTipoLanc != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_tipo_lanc' || ' like ' ||'''' ||pParOcorTipoLanc||'''';
		end if;

		if pParOcorGrupoNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_nome' || ' like ' ||'''' ||pParOcorGrupoNome||'''';
		end if;

		if pParOcorGrupoAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_ativo' || ' like ' ||'''' ||pParOcorGrupoAtivo||'''';
		end if;	

		if pParOcorGrupoSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_grupo_sigla' || ' like '||'''' ||pParOcorGrupoSigla||'''';
		end if;
		
		if pParGerUmedidaNome != '' then
			vSql = vSql || 'and ' || ' t1.ger_umedida_nome' || ' like '||'''' ||pParGerUmedidaNome||'''';
		end if;

		if pParGerUmedidaAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ger_umedida_ativo' || ' like ' ||'''' ||pParGerUmedidaAtivo||'''';
		end if;

		if pParGerUmedidaSigla != '' then
			vSql = vSql || 'and ' || ' t1.ger_umedida_sigla' || ' like '||'''' ||pParGerUmedidaSigla||'''';
		end if;

		if pParOcorStatusNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_nome' || ' like ' ||'''' ||pParOcorStatusNome||'''';
		end if;

		if pParOcorStatusAtivo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_ativo' || ' like ' ||'''' ||pParOcorStatusAtivo||'''';
		end if;
		
		if pParOcorStatusSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_sigla' || ' like ' ||'''' ||pParOcorStatusSigla||'''';
		end if;

		if pParOcorStatusTipo != '' then
			vSql = vSql || 'and ' || ' t1.ope_ocor_status_tipo_status' || ' like '||'''' ||pParOcorStatusTipo||'''';
		end if;

		if pParOpeAreaQntAreaProd != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_area_qnt_area_prod::text' || ' like '||'''' ||pParOpeAreaQntAreaProd||'''';
		end if;

		if pParOpeAreaQntAreaImprod != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_area_qnt_area_improd::text' || ' like '||'''' ||pParOpeAreaQntAreaImprod||'''';
		end if;
		
		if pParOpeAreaQntPlantEstand != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_area_qnt_plantas_estande::text' || ' like '||'''' ||pParOpeAreaQntPlantEstand||'''';
		end if;

		if pParOpeAreaBlocoCol != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_area_bloco_col' || ' like ' ||'''' ||pParOpeAreaBlocoCol||'''';
		end if;

		if pParOpeAreaUmedidaNome != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_area_umedida_nome' || ' like ' ||'''' ||pParOpeAreaUmedidaNome||'''';
		end if;

		if pParOpeAreaUmedidaSigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_area_umedida_sigla' || ' like '||'''' ||pParOpeAreaUmedidaSigla||'''';
		end if;

		if pParCentro2Nome != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_nome' || ' like '||'''' ||pParCentro2Nome||'''';
		end if;

		if pParCentro2Sigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_sigla' || ' like '||'''' ||pParCentro2Sigla||'''';
		end if;

		if pParCentro2Ativo != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_ativo' || ' like '||'''' ||pParCentro2Ativo||'''';
		end if;

		if pParCentro2TipoDestinacao != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_tipo_destinacao' || ' like '||'''' ||pParCentro2TipoDestinacao||'''';
		end if;

		if pParCentro2TipoProp != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_tipo_prop' || ' like '||'''' ||pParCentro2TipoProp||'''';
		end if;

		if pParCentro1Nome != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro1_nome' || ' like '||'''' ||pParCentro1Nome||'''';
		end if;

		if pParCentro1Ativo != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro1_ativo' || ' like '||'''' ||pParCentro1Ativo||'''';
		end if;
		
		if pParCentro1Sigla != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro1_sigla' || ' like '||'''' ||pParCentro1Sigla||'''';
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
		 
		if pParOcorMovDataMovIni != '' and pParOcorMovDataMovFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' >= ''' || pParOcorMovDataMovIni|| '''' || ' and  CAST(t1.ope_ocor_mov_data_mov AS DATE)' || ' <= ''' || pParOcorMovDataMovFin || '''';
		end if;
		
		if pParOcorMovDetDtStatusIni != '' and pParOcorMovDetDtStatusFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' >= ''' || pParOcorMovDetDtStatusIni|| '''' || ' and  CAST(t1.ope_ocor_mov_det_data_status AS DATE)' || ' <= ''' || pParOcorMovDetDtStatusFin || '''';
		end if;

		if pParOpeAreaDtIniPlan != '' and pParOpeAreaDtIniPlanFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' >= ''' || pParOpeAreaDtIniPlan|| '''' || ' and  CAST(t1.ope_centro2_area_data_ini_plan AS DATE)' || ' <= ''' || pParOpeAreaDtIniPlanFin || '''';
		end if;

		if pParOpeAreaDtFinPlanIni != '' and pParOpeAreaDtFinPlan != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' >= ''' || pParOpeAreaDtFinPlanIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_fin_plan AS DATE)' || ' <= ''' || pParOpeAreaDtFinPlan || '''';
		end if;
		
		if pParOpeAreaDtUltPlanIni != '' and pParOpeAreaDtUltPlanFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' >= ''' || pParOpeAreaDtUltPlanIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_ult_plan AS DATE)' || ' <= ''' || pParOpeAreaDtUltPlanFin || '''';
		end if;

		if pParOpeAreaDtIniCol != '' and pParOpeAreaDtIniColFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' >= ''' || pParOpeAreaDtIniCol|| '''' || ' and  CAST(t1.ope_centro2_area_data_ini_col AS DATE)' || ' <= ''' || pParOpeAreaDtIniColFin || '''';
		end if;

		if pParOpeAreaDtFinColIni != '' and pParOpeAreaDtFinCol != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' >= ''' || pParOpeAreaDtFinColIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_fin_col AS DATE)' || ' <= ''' || pParOpeAreaDtFinCol || '''';
		end if;

		if pParOpeAreaDtUltColIni != '' and pParOpeAreaDtUltColFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' >= ''' || pParOpeAreaDtUltColIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_ult_col AS DATE)' || ' <= ''' || pParOpeAreaDtUltColFin || '''';
		end if;
		
		if pParOpeAreaDtFlorada1Ini != '' and pParOpeAreaDtFlorada1Fin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' >= ''' || pParOpeAreaDtFlorada1Ini|| '''' || ' and  CAST(t1.ope_centro2_area_data_florada_1 AS DATE)' || ' <= ''' || pParOpeAreaDtFlorada1Fin || '''';
		end if;

		if pParOpeAreaDtEmergIni != '' and pParOpeAreaDtEmergFin != '' then
			vSql = vSql || ' and ' || 'CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' >= ''' || pParOpeAreaDtEmergIni|| '''' || ' and  CAST(t1.ope_centro2_area_data_emerg AS DATE)' || ' <= ''' ||pParOpeAreaDtEmergFin|| '''';
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