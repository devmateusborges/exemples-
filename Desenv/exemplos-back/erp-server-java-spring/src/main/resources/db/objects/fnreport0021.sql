DROP FUNCTION IF EXISTS fnreport0021;
CREATE OR REPLACE FUNCTION fnreport0021(
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
pParOrdRecIId varchar default null,
pParOrdRecQntRendIni varchar default null,
pParOrdRecQntRendFin varchar default null,
pParOrdRecPercUtilIni varchar default null,
pParOrdRecPercUtilFin varchar default null,
pParOrdRecQntTotUtilIni varchar default null,
pParOrdRecQntTotUtilFin varchar default null,
pParOrdRecVrUnitUtilIni varchar default null,
pParOrdRecVrUnitUtilFin varchar default null,
pParOrdRecVrTotUtilIni varchar default null,
pParOrdRecVrTotUtilFin varchar default null,
pParCentro1Id varchar default null,
pParCentro1Nome varchar default null,
pParCentro1Ativo varchar default null,
pParCentro2Id varchar default null,
pParCentro2Nome varchar default null,
pParCentro2Ativo varchar default null,
pParCtbId varchar default null,
pParCtbNome varchar default null,
pParCtbAtivo varchar default null,
pParPessoaEnderecoId varchar default null,
pParPessoaEnderecoAtivo varchar default null,
pParPessoaEnderecoTipo varchar default null,
pParPessoaEnderecoPadrao varchar default null,
pParPessoaEnderecoLograd varchar default null,
pParPessoaEnderecoNr varchar default null,
pParCentro1Imp01Id varchar default null,
pParCentro1Imp01Nome varchar default null,
pParCentro1Imp01Ativo varchar default null,
pParCentro2Imp01Id varchar default null,
pParCentro2Imp01Nome varchar default null,
pParCentro2Imp01Ativo varchar default null,
pParSubTipoId varchar default null,
pParSubTipoNome varchar default null,
pParTipoId varchar default null,
pParTipoNome varchar default null,
pParSubGrupoId varchar default null,
pParSubGrupoNome varchar default null,
pParSubGrupoAtivo varchar default null,
pParGrupoId varchar default null,
pParGrupoNome varchar default null,
pParGrupoAtivo varchar default null,
pParCentro2OrdId varchar default null,
pParCentro2OrdDtIniExec varchar default null,
pParCentro2OrdDtIniExecFin varchar default null,
pParCentro2OrdDtFinExecIni varchar default null,
pParCentro2OrdDtFinExec varchar default null,
pParCentro2OrdDtIniExecPrev varchar default null,
pParCentro2OrdDtIniExecPrevFin varchar default null,
pParCentro2OrdDtFinExecPrevIni varchar default null,
pParCentro2OrdDtFinExecPrev varchar default null,
pParCentro2OrdNr varchar default null,
pParEmpresaOrdId varchar default null,
pParEmpresaOrdNome varchar default null,
pParEmpresaOrdAtivo varchar default null,
pParEmpresaOrdCpf varchar default null,
pParEmpresaOrdCnpj varchar default null,
pParPeriodoOrdId varchar default null,
pParPeriodoOrdNome varchar default null,
pParPeriodoOrdAtivo varchar default null,
pParPeriodoOrdDataIni varchar default null,
pParPeriodoOrdDataIniFin varchar default null,
pParPeriodoOrdDataFinIni varchar default null,
pParPeriodoOrdDataFin varchar default null,
pParGerPessoaId varchar default null,
pParGerPessoaNome varchar default null,
pParGerPessoaAtivo varchar default null,
pParGerPessoaDoc varchar default null,
pParCentro2OrdTipoId varchar default null,
pParCentro2OrdTipoNome varchar default null,
pParCentro2OrdTipoAtivo varchar default null,
pParFrentTrabId varchar default null,
pParFrentTrabNome varchar default null,
pParFrentTrabAtivo varchar default null,
pParStatusId varchar default null,
pParStatusNome varchar default null,
pParStatusAtivo varchar default null,
pParStatusTipo varchar default null,
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
declare
vSql varchar;
vPar1 varchar :='';
vPar2 varchar :='';
vPar3 varchar :='';
vPar4 varchar :='';
r record;

begin

	
	if pParOrdRecQntRendIni != '' and pParOrdRecQntRendFin != '' then
	 vPar1 := vPar1||'Rendimento / Dosagem de ['||pParOrdRecQntRendIni||'] até ['||pParOrdRecQntRendFin||']'||chr(13)||chr(10);
	 
 else
		vPar1 := vPar1||'Rendimento / Dosagem de [] até []'||chr(13)||chr(10);
	end if;
	
	if pParOrdRecPercUtilIni != '' and pParOrdRecPercUtilFin != '' then
	 vPar1 := vPar1||'Percentual Utilização de ['||pParOrdRecPercUtilIni||'] até ['||pParOrdRecPercUtilFin||']'||chr(13)||chr(10);
	 
 else
		vPar1 := vPar1||'Percentual Utilização de [] até []'||chr(13)||chr(10);
 end if;	
	
	if pParOrdRecQntTotUtilIni != '' and pParOrdRecQntTotUtilFin != '' then
	 vPar1 := vPar1||'Quantidade Total Utilização de ['||pParOrdRecQntTotUtilIni||'] até ['||pParOrdRecQntTotUtilFin||']'||chr(13)||chr(10);
	 
 else
		vPar1 := vPar1||'Quantidade Total Utilização de [] até []'||chr(13)||chr(10);
 end if;
	if pParOrdRecVrUnitUtilIni != '' and pParOrdRecVrUnitUtilFin != '' then
		vPar1 := vPar1||'Valor Unitário Utilização de ['||pParOrdRecVrUnitUtilIni||'] até ['||pParOrdRecVrUnitUtilFin||']'||chr(13)||chr(10);
 else
		vPar1 := vPar1||'Valor Unitário Utilização de [] até []'||chr(13)||chr(10);
 end if;

	if pParOrdRecVrTotUtilIni != '' and pParOrdRecVrTotUtilFin != '' then
		vPar1 := vPar1||'Valor Total Utilização de ['||pParOrdRecVrTotUtilIni||'] até ['||pParOrdRecVrTotUtilFin||']'||chr(13)||chr(10);
 else
		vPar1 := vPar1||'Valor Total Utilização  de [] até []'||chr(13)||chr(10);
 end if;	
	
 if pParCentro2Id != '' then
		 vPar1 := vPar1||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
	else
		 vPar1 := vPar1||'Centro 2 [] '||chr(13)||chr(10);
	end if;
	
	if pParCentro2Nome != '' then
		 vPar1 := vPar1||'Nome Centro 2 ['||pParCentro2Nome||'] '||chr(13)||chr(10);
	else
		 vPar1 := vPar1||'Nome Centro 2 [] '||chr(13)||chr(10);	
	end if;
	
	if pParCentro2Ativo != '' then
		 vPar1 := vPar1||'Centro 2 Ativo ['||pParCentro2Ativo||'] '||chr(13)||chr(10);	
	else
		 vPar1 := vPar1||'Centro 2 Ativo [] '||chr(13)||chr(10);
	end if;
	
	if pParCentro1Id != '' then
		 vPar1 := vPar1||'Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Id||'''')||'] '||chr(13)||chr(10);	
	else
		vPar1 := vPar1||'Centro 1 [] '||chr(13)||chr(10);
	end if;

	if pParCentro1Nome != '' then
		vPar1 := vPar1||'Nome Centro 1 ['||pParCentro1Nome||'] '||chr(13)||chr(10);	
	else
		vPar1 := vPar1||'Nome Centro 1 [] '||chr(13)||chr(10);
	end if;
	
	if pParCentro1Ativo != '' then
		vPar1 := vPar1||'Centro 1 Ativo ['||pParCentro1Ativo||'] '||chr(13)||chr(10);		
	else
		vPar1 := vPar1||'Centro 1 Ativo [] '||chr(13)||chr(10);	
	end if;
	
		if pParCtbId != '' then
			vPar1 := vPar1||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCtbId||'''')||'] '||chr(13)||chr(10);	
	else
			vPar1 := vPar1||'Componente Contábil [] '||chr(13)||chr(10);	
	end if;
	
	if pParCtbNome != '' then
		vPar1 := vPar1||'Nome Componente Contábil ['||pParCtbNome||'] '||chr(13)||chr(10);	
	else
		vPar1 := vPar1||'Nome Componente Contábil [] '||chr(13)||chr(10);	
	end if;

	if pParCtbAtivo != '' then
			vPar1 := vPar1||'Componente Contábil Ativo ['||pParCtbAtivo||'] '||chr(13)||chr(10);	
	else
			vPar1 := vPar1||'Componente Contábil Ativo [] '||chr(13)||chr(10);
	end if;

	if pParPessoaEnderecoAtivo != '' then
		vPar1 := vPar1||'Pessoa Endereco Ativo ['||pParPessoaEnderecoAtivo||']'||chr(13)||chr(10);
	else
		vPar1 := vPar1||'Pessoa Endereco Ativo []'||chr(13)||chr(10);
	end if;
	

	if pParPessoaEnderecoTipo != '' then
		vPar1 := vPar1||'Pessoa Endereco Tipo ['||pParPessoaEnderecoTipo||']'||chr(13)||chr(10);
	else
		vPar1 := vPar1||'Pessoa Endereco Tipo []'||chr(13)||chr(10);	
	end if;
	
	if pParPessoaEnderecoPadrao != '' then
		vPar1 := vPar1||'Pessoa Endereco Padrão ['||pParPessoaEnderecoPadrao||']'||chr(13)||chr(10);	
	else
		vPar1 := vPar1||'Pessoa Endereco Padrão []'||chr(13)||chr(10);	
	end if;
	
	if pParPessoaEnderecoLograd !='' then
		vPar1 := vPar1||'Pessoa Endereco Logradouro ['||pParPessoaEnderecoLograd||']'||chr(13)||chr(10);	
	else
		vPar1 := vPar1||'Pessoa Endereco Logradouro []'||chr(13)||chr(10);	
	end if;
	
	if pParPessoaEnderecoNr !='' then
		vPar2 := vPar2||'Pessoa Nº Endereco ['||pParPessoaEnderecoNr||']'||chr(13)||chr(10);			
	else
		vPar2 := vPar2||'Pessoa Nº Endereco []'||chr(13)||chr(10);	
	end if;
	
	if pParCentro1Imp01Id != '' then
		 vPar2 := vPar2||'Implemento Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Imp01Id||'''')||'] '||chr(13)||chr(10);		
	else
		 vPar2 := vPar2||'Implemento Centro 1 [] '||chr(13)||chr(10);	
	end if;	
	if pParCentro1Imp01Nome != '' then
		vPar2 := vPar2||'Nome Implemento Centro 1 ['||pParCentro1Imp01Nome||'] '||chr(13)||chr(10);		
	else
		vPar2 := vPar2||'Nome Implemento Centro 1 [] '||chr(13)||chr(10);			
	end if;
	
	if pParCentro1Imp01Ativo != '' then
		vPar2 := vPar2||'Implemento Centro 1 Ativo ['||pParCentro1Imp01Ativo||'] '||chr(13)||chr(10);			
	else
		vPar2 := vPar2||'Implemento Centro 1 Ativo [] '||chr(13)||chr(10);				
	end if;	
	
	
	
	if pParCentro2Imp01Id != '' then
		 vPar2 := vPar2||'Implemento Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Imp01Id||'''')||'] '||chr(13)||chr(10);	
	else
		 vPar2 := vPar2||'Implemento Centro 2 [] '||chr(13)||chr(10);		
	end if;	
	
	if pParCentro2Imp01Nome != '' then
		vPar2 := vPar2||'Nome Implemento Centro 2 ['||pParCentro2Imp01Nome||'] '||chr(13)||chr(10);				
	else
		vPar2 := vPar2||'Nome Implemento Centro 2 [] '||chr(13)||chr(10);						
	end if;	

	if pParCentro2Imp01Ativo != '' then
		vPar2 := vPar2||'Implemento Centro 2 Ativo ['||pParCentro2Imp01Ativo||'] '||chr(13)||chr(10);			
	else
		vPar2 := vPar2||'Implemento Centro 2 Ativo [] '||chr(13)||chr(10);					
	end if;

	if pParSubTipoId != '' then
		vPar2 := vPar2||'SubTipo ['||fnreport_sigla(pParUnitId,'ope_centro_subtipo','nome','id',''''||pParSubTipoId||'''')||'] '||chr(13)||chr(10);		 		
	else
		vPar2 := vPar2||'SubTipo [] '||chr(13)||chr(10);		 			
	end if;
	
	if pParSubTipoNome != '' then
		vPar2 := vPar2||'Nome SubTipo ['||pParSubTipoNome||'] '||chr(13)||chr(10);
	else
		vPar2 := vPar2||'Nome SubTipo [] '||chr(13)||chr(10);	
	end if;
	
	if pParTipoId != '' then
		vPar2 := vPar2||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro_tipo','nome','id',''''||pParTipoId||'''')||'] '||chr(13)||chr(10);		 			
	else
		vPar2 := vPar2||'Tipo [] '||chr(13)||chr(10);
	end if;
	
	if pParTipoNome != '' then
		vPar2 := vPar2||'Nome Tipo ['||pParTipoNome||'] '||chr(13)||chr(10);	
	else
		vPar2 := vPar2||'Nome Tipo [] '||chr(13)||chr(10);	
	end if;

	if pParSubGrupoId != '' then
		 vPar2 := vPar2||'SubGrupo ['||fnreport_sigla(pParUnitId,'ope_centro_subgrupo','sigla_centro_subgrupo','id',''''||pParSubGrupoId||'''')||'] '||chr(13)||chr(10);
	else
		 vPar2 := vPar2||'SubGrupo [] '||chr(13)||chr(10);	
	end if;
	
	if pParSubGrupoNome != '' then
		 vPar2 := vPar2||'Nome SubGrupo ['||pParSubGrupoNome||'] '||chr(13)||chr(10);		
	else
		 vPar2 := vPar2||'Nome SubGrupo [] '||chr(13)||chr(10);		
	end if;
	
	if pParSubGrupoAtivo != '' then
		 vPar2 := vPar2||'SubGrupo Ativo ['||pParSubGrupoAtivo||'] '||chr(13)||chr(10);			
	else
		 vPar2 := vPar2||'SubGrupo Ativo [] '||chr(13)||chr(10);	
	end if;
	
	if pParGrupoId != '' then
		vPar2 := vPar2||'Grupo ['||fnreport_sigla(pParUnitId,'ope_centro_grupo','sigla_centro_grupo','id',''''||pParGrupoId||'''')||'] '||chr(13)||chr(10);		 
	else
		vPar2 := vPar2||'Grupo [] '||chr(13)||chr(10);
	end if;
	
	if pParGrupoNome != '' then
		vPar2 := vPar2||'Nome Grupo ['||pParGrupoNome||'] '||chr(13)||chr(10);
	else
		vPar2 := vPar2||'Nome Grupo [] '||chr(13)||chr(10);
	end if;
	
	if pParGrupoAtivo != '' then
		vPar3 := vPar3||'Grupo Ativo ['||pParGrupoAtivo||'] '||chr(13)||chr(10);	
	else
		vPar3 := vPar3||'Grupo Ativo [] '||chr(13)||chr(10);	
	end if;
	
	if pParCentro2OrdDtIniExec != '' and pParCentro2OrdDtIniExecFin != '' then
		vPar3 := vPar3||'Data Inicial Execução de ['||pParCentro2OrdDtIniExec||'] até ['|| pParCentro2OrdDtIniExecFin||']'||chr(13)||chr(10);
	else
		vPar3 := vPar3||'Data Inicial Execução de [] até []'||chr(13)||chr(10);
	end if;
	
 if pParCentro2OrdDtFinExecIni != '' and pParCentro2OrdDtFinExec != '' then
		vPar3 := vPar3||'Data Final Execução de ['||pParCentro2OrdDtFinExecIni||'] até ['|| pParCentro2OrdDtFinExec||']'||chr(13)||chr(10);
	else
		vPar3 := vPar3||'Data Final Execução de [] até []'||chr(13)||chr(10);
	end if;

	if pParCentro2OrdDtIniExecPrev!= '' and pParCentro2OrdDtIniExecPrevFin != '' then
		vPar3 := vPar3||'Data Inicial Execução Prévia de ['||pParCentro2OrdDtIniExecPrev||'] até ['|| pParCentro2OrdDtIniExecPrevFin||']'||chr(13)||chr(10);	
	else
		vPar3 := vPar3||'Data Inicial Execução Prévia de [] até []'||chr(13)||chr(10);		
	end if;
	
	if pParCentro2OrdDtFinExecPrevIni != '' and pParCentro2OrdDtFinExecPrev != '' then
		vPar3 := vPar3||'Data Final Execução Prévia de ['||pParCentro2OrdDtFinExecPrevIni||'] até ['|| pParCentro2OrdDtFinExecPrev||']'||chr(13)||chr(10);		
	else
		vPar3 := vPar3||'Data Final Execução Prévia de [] até []'||chr(13)||chr(10);		
	end if;
	
	if pParCentro2OrdNr != '' then
		vPar3 := vPar3||'Nº Ordem ['||pParCentro2OrdNr||']'||chr(13)||chr(10);
	else
		vPar3 := vPar3||'Nº Ordem []'||chr(13)||chr(10);
	end if;	


	if pParEmpresaOrdId != '' then
			vPar3 := vPar3||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||pParEmpresaOrdId||'''')||'] '||chr(13)||chr(10);	
	else
			vPar3 := vPar3||'Empresa []'||chr(13)||chr(10);		
	end if;
	
	if pParEmpresaOrdNome != '' then
			vPar3 := vPar3||'Nome Empresa ['||pParEmpresaOrdNome||']'||chr(13)||chr(10);			
	else
			vPar3 := vPar3||'Nome Empresa []'||chr(13)||chr(10);			
	end if;

	if pParEmpresaOrdAtivo != '' then
			vPar3 := vPar3||'Empresa Ativo ['||pParEmpresaOrdAtivo||']'||chr(13)||chr(10);			
	else
			vPar3 := vPar3||'Empresa Ativo []'||chr(13)||chr(10);			
	end if;
	
	if pParEmpresaOrdCpf != '' then
			vPar3 := vPar3||'Empresa Cpf ['||pParEmpresaOrdCpf||']'||chr(13)||chr(10);			
	else
			vPar3 := vPar3||'Empresa Cpf []'||chr(13)||chr(10);			
	end if;
	
	if pParEmpresaOrdCnpj != '' then
			vPar3 := vPar3||'Empresa CNPJ ['||pParEmpresaOrdCnpj||']'||chr(13)||chr(10);			
	else
			vPar3 := vPar3||'Empresa CNPJ []'||chr(13)||chr(10);			
	end if;
	
	if pParPeriodoOrdId != '' then
		 vPar3 := vPar3||'Período  ['||fnreport_sigla(pParUnitId,'ope_periodo','sigla_periodo','id',''''||pParPeriodoOrdId||'''')||'] '||chr(13)||chr(10);				
	else
		 vPar3 := vPar3||'Período []'||chr(13)||chr(10);			
	end if;	

	if pParPeriodoOrdNome != '' then
			vPar3 := vPar3||'Nome Período ['||pParPeriodoOrdNome||']'||chr(13)||chr(10);			
	else
			vPar3 := vPar3||'Nome Período []'||chr(13)||chr(10);			
	end if;	

	if pParPeriodoOrdAtivo != '' then
			vPar3 := vPar3||'Período Ativo ['||pParPeriodoOrdAtivo||']'||chr(13)||chr(10);			
	else
			vPar3 := vPar3||'Período Ativo []'||chr(13)||chr(10);			
	end if;	
	
	if pParPeriodoOrdDataIni != '' and pParPeriodoOrdDataIniFin != '' then
		vPar3 := vPar3||'Data Inicial do Período de ['||pParPeriodoOrdDataIni||'] até ['|| pParPeriodoOrdDataIniFin||']'||chr(13)||chr(10);	
	else
		vPar3 := vPar3||'Data Inicial do Período de [] até []'||chr(13)||chr(10);		
	end if;
	
	if pParPeriodoOrdDataFinIni != '' and pParPeriodoOrdDataFin != '' then
		vPar3 := vPar3||'Data Final do Período de ['||pParPeriodoOrdDataFinIni||'] até ['|| pParPeriodoOrdDataFin||']'||chr(13)||chr(10);		
	else
		vPar3 := vPar3||'Data Final do Período de [] até []'||chr(13)||chr(10);		
	end if;
		if pParGerPessoaId != '' then
		vPar4 := vPar4||'Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','nome','id',''''||pParGerPessoaId||'''')||'] '||chr(13)||chr(10);		
	else
		vPar4 := vPar4||'Pessoa [] '||chr(13)||chr(10);			
	end if;

	if pParGerPessoaNome != '' then
		vPar4 := vPar4||'Nome Pessoa ['||pParGerPessoaNome||'] '||chr(13)||chr(10);			
	else
		vPar4 := vPar4||'Nome Pessoa [] '||chr(13)||chr(10);	
	end if;

	if pParGerPessoaAtivo != '' then
		vPar4 := vPar4||'Pessoa Ativo ['||pParGerPessoaAtivo||'] '||chr(13)||chr(10);				
	else
		vPar4 := vPar4||'Pessoa Ativo [] '||chr(13)||chr(10);	
	end if;

	if pParGerPessoaDoc != '' then
		vPar4 := vPar4||'Doc Pessoa ['||pParGerPessoaDoc||'] '||chr(13)||chr(10);	
	else
		vPar4 := vPar4||'Doc Pessoa [] '||chr(13)||chr(10);	
	end if;

	if pParCentro2OrdTipoId != '' then
		vPar4 := vPar4||'Tipo Ord ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_tipo','sigla_ord_tipo','id',''''||pParCentro2OrdTipoId||'''')||'] '||chr(13)||chr(10);
	else
		vPar4 := vPar4||'Tipo Ord [] '||chr(13)||chr(10);
	end if;
	
	if pParCentro2OrdTipoNome != '' then
		vPar4 := vPar4||'Nome Tipo Ord ['||pParCentro2OrdTipoNome||'] '||chr(13)||chr(10);
	else
		vPar4 := vPar4||'Nome Tipo Ord [] '||chr(13)||chr(10);	
	end if;
	
	if pParCentro2OrdTipoAtivo != '' then
		vPar4 := vPar4||'Tipo Ativo Ord ['||pParCentro2OrdTipoAtivo||'] '||chr(13)||chr(10);
	else
		vPar4 := vPar4||'Tipo Ativo Ord [] '||chr(13)||chr(10);	
	end if;
	
	if pParFrentTrabId != '' then
		 vPar4 := vPar4||'Frente Trabalho ['||fnreport_sigla(pParUnitId,'ope_frente_trabalho','sigla_frente_trabalho','id',''''||pParFrentTrabId||'''')||'] '||chr(13)||chr(10);
	else
		 vPar4 := vPar4||'Frente Trabalho [] '||chr(13)||chr(10);	
	end if;
	
	if pParFrentTrabNome != '' then
		 vPar4 := vPar4||'Nome Frente Trabalho ['||pParFrentTrabNome||'] '||chr(13)||chr(10);		
	else
		 vPar4 := vPar4||'Nome Frente Trabalho [] '||chr(13)||chr(10);		
	end if;
	
	
	if pParFrentTrabAtivo != '' then
		 vPar4 := vPar4||'Frente Trabalho Ativo ['||pParFrentTrabAtivo||'] '||chr(13)||chr(10);	
	else
		 vPar4 := vPar4||'Frente Trabalho Ativo [] '||chr(13)||chr(10);		
	end if;	
	
	if pParStatusId != '' then
		 vPar4 := vPar4||'Status ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_status','sigla_ord_status','id',''''||pParStatusId||'''')||'] '||chr(13)||chr(10);	
	else
		 vPar4 := vPar4||'Status [] '||chr(13)||chr(10);	
	end if;
	
	if pParStatusNome != '' then
		 vPar4 := vPar4||'Nome Status ['||pParStatusNome||'] '||chr(13)||chr(10);
	else
		vPar4 := vPar4||'Nome Status [] '||chr(13)||chr(10);
	end if;
		
	if pParStatusAtivo != '' then
		vPar4 := vPar4||'Status Ativo ['||pParStatusAtivo||'] '||chr(13)||chr(10);
	else
		vPar4 := vPar4||'Status Ativo [] '||chr(13)||chr(10);
	end if;
	
	if pParStatusTipo != '' then
		vPar4 := vPar4||'Tipo Status ['||pParStatusTipo||'] '||chr(13)||chr(10);	
	else
		vPar4 := vPar4||'Tipo Status [] '||chr(13)||chr(10);		
	end if;
	
		if pParLogUserIns != '' then
		vPar4 := vPar4||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
	else
		vPar4 := vPar4||'Log Usuario Inserção []'||chr(13)||chr(10);
	end if;

	if pParLogUserUpd != '' then
		vPar4 := vPar4||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
	else
		vPar4 := vPar4||'Log Usuario Alteração []'||chr(13)||chr(10);
	end if;

	if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
		vPar4 := vPar4||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
	else
				vPar4 := vPar4||'Data Inserção de [] até []'||chr(13)||chr(10);
	end if;

	if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
		vPar4 := vPar4||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
	else
			vPar4 := vPar4||'Data Alteração de [] até []'||chr(13)||chr(10);
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
		,sum(t1.ope_centro2_ord_rec_qnt_rend) as valor_01
		,sum(t1.ope_centro2_ord_rec_perc_util) as valor_02
		,sum(t1.ope_centro2_ord_rec_qnt_total_util) as valor_03
		,sum(t1.ope_centro2_ord_rec_valor_unit_util) as valor_04
		,sum(t1.ope_centro2_ord_rec_valor_total_util) as valor_05
		from vwope_centro2_ord_rec t1 where 1=1
		';
		
		if pParUnitId != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_ord_rec_unitid' || ' in(''' ||pParUnitId||''')';
		end if;
		
		if pParOrdRecIId != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_ord_rec_id' || ' in(''' ||pParOrdRecIId||''')';
		end if;
	
	 if pParOrdRecQntRendIni != ''  and pParOrdRecQntRendFin != '' then
			vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_qnt_rend' || ' >= ''' || pParOrdRecQntRendIni|| '''' || ' and t1.ope_centro2_ord_rec_qnt_rend' || ' <= ''' || pParOrdRecQntRendFin|| ''''; 
	 end if;
	
	 if pParOrdRecPercUtilIni != ''  and pParOrdRecPercUtilFin != '' then
			vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_perc_util' || ' >= ''' || pParOrdRecPercUtilIni|| '''' || ' and  t1.ope_centro2_ord_rec_perc_util' || ' <= ''' || pParOrdRecPercUtilFin|| ''''; 
	 end if;
	 
	 if pParOrdRecQntTotUtilIni != ''  and pParOrdRecQntTotUtilFin != '' then
			vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_qnt_total_util ' || ' >= ''' || pParOrdRecQntTotUtilIni|| '''' || ' and  t1.ope_centro2_ord_rec_qnt_total_util' || ' <= ''' || pParOrdRecQntTotUtilFin|| ''''; 
	 end if;

	 if pParOrdRecVrUnitUtilIni != ''  and pParOrdRecVrUnitUtilFin != '' then
			vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_valor_unit_util' || ' >= ''' || pParOrdRecVrUnitUtilIni|| '''' || ' and  t1.ope_centro2_ord_rec_valor_unit_util' || ' <= ''' || pParOrdRecVrUnitUtilFin|| ''''; 
	 end if;

	 if pParOrdRecVrTotUtilIni != ''  and pParOrdRecVrTotUtilFin != '' then
			vSql = vSql || ' and ' || 't1.ope_centro2_ord_rec_valor_total_util' || ' >= ''' || pParOrdRecVrTotUtilIni|| '''' || ' and t1.ope_centro2_ord_rec_valor_total_util' || ' <= ''' || pParOrdRecVrTotUtilFin|| ''''; 
	 end if;
	 
	 if pParCentro1Id != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro1_id' || ' in(''' ||pParCentro1Id||''')';	 
	 end if;
	 
	if pParCentro1Nome != '' then
		vSql = vSql ||' and '||'t1.ope_centro1_nome'||' like'||'''%'||pParCentro1Nome||'%'' ';
	end if;
	
	if pParCentro1Ativo != '' then
		vSql = vSql ||' and '||'t1.ope_centro1_ativo_desc'||' like'||'''%'||pParCentro1Ativo||'%'' ';	
	end if;
	
	
	if pParCentro2Id != '' then
			vSql = vSql || 'and ' || ' t1.ope_centro2_id' || ' in(''' ||pParCentro2Id||''')';	 	
	end if;
	
	if pParCentro2Nome != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_nome'||' like'||'''%'||pParCentro2Nome||'%'' ';	
	end if;
	
	if pParCentro2Ativo != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_ativo_desc'||' like'||'''%'||pParCentro2Ativo||'%'' ';	
	end if;
	
	if pParCtbId != '' then
		 vSql = vSql || 'and ' || ' t1.ctb_id' || ' in(''' ||pParCtbId||''')';
	end if;

	if pParCtbNome != '' then
		vSql = vSql ||' and '||'t1.ctb_nome'||' like'||'''%'||pParCtbNome||'%'' ';		
	end if;

	if pParCtbAtivo != '' then
		vSql = vSql ||' and '||'t1.ctb_ativo_desc'||' like'||'''%'||pParCtbAtivo||'%'' ';		
	end if;
	
	
	--
	if pParPessoaEnderecoId != '' then
		 vSql = vSql || 'and ' || ' t1.ger_pessoa_endereco_id' || ' in(''' ||pParPessoaEnderecoId||''')';
	end if;
	
	if pParPessoaEnderecoAtivo != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_endereco_ativo_desc'||' like'||'''%'||pParPessoaEnderecoAtivo||'%'' ';				
	end if;
	
	if pParPessoaEnderecoTipo != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_endereco_tipo'||' like'||'''%'||pParPessoaEnderecoTipo||'%'' ';				
	end if;	
	
	if pParPessoaEnderecoPadrao != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_endereco_padrao'||' like'||'''%'||pParPessoaEnderecoPadrao||'%'' ';				
	end if;		
	

	if pParPessoaEnderecoLograd != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_endereco_logradouro'||' like'||'''%'||pParPessoaEnderecoLograd||'%'' ';				
	end if;		
	
	if pParPessoaEnderecoNr != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_endereco_loradouro_nr'||' like'||'''%'||pParPessoaEnderecoNr||'%'' ';				
	end if;	
	
	
	if pParCentro1Imp01Id != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro1_imp01_id' || ' in(''' ||pParCentro1Imp01Id||''')';	
	end if;
	
	if pParCentro1Imp01Nome != '' then
		vSql = vSql ||' and '||'t1.ope_centro1_imp01_nome'||' like'||'''%'||pParCentro1Imp01Nome||'%'' ';	
	end if; 
	
	if pParCentro1Imp01Ativo != '' then
		vSql = vSql ||' and '||'t1.ope_centro1_imp01_ativo_desc'||' like'||'''%'||pParCentro1Imp01Ativo||'%'' ';		
	end if;
	
	
	if pParCentro2Imp01Id != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro2_imp01_id' || ' in(''' ||pParCentro2Imp01Id||''')';	
	end if;
	
	if pParCentro2Imp01Nome != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_imp01_nome'||' like'||'''%'||pParCentro2Imp01Nome||'%'' ';	
	end if; 
	
	if pParCentro2Imp01Ativo != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_imp01_id_ativo_desc'||' like'||'''%'||pParCentro2Imp01Ativo||'%'' ';		
	end if;
	
	
	if pParSubTipoId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro_subtipo_id' || ' in(''' ||pParSubTipoId||''')';
	end if;
	
	if pParSubTipoNome != '' then
		vSql = vSql ||' and '||'t1.ope_centro_subtipo_nome'||' like'||'''%'||pParSubTipoNome||'%'' ';	
	end if;
	
	if pParTipoId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro_tipo_id' || ' in(''' ||pParTipoId||''')';
	end if;	
	
	if pParTipoNome != '' then
		vSql = vSql ||' and '||'t1.ope_centro_tipo_nome'||' like'||'''%'||pParTipoNome||'%'' ';	
	end if;
	 
	if pParSubGrupoId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro_subgrupo_id' || ' in(''' ||pParSubGrupoId||''')';
	end if;	
	
	if pParSubGrupoNome != '' then
		vSql = vSql ||' and '||'t1.ope_centro_subgrupo_nome'||' like'||'''%'||pParSubGrupoNome||'%'' ';	
	end if;	

	if pParSubGrupoAtivo != '' then
		vSql = vSql ||' and '||'t1.ope_centro_subgrupo_ativo_desc'||' like'||'''%'||pParSubGrupoAtivo||'%'' ';	
	end if;
	
	if pParGrupoId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro_grupo_id' || ' in(''' ||pParGrupoId||''')';
	end if;	
	
	if pParGrupoNome != '' then
		vSql = vSql ||' and '||'t1.ope_centro_grupo_nome'||' like'||'''%'||pParGrupoNome||'%'' ';	
	end if;	
	
	if pParGrupoAtivo != '' then
		vSql = vSql ||' and '||'t1.ope_centro_grupo_ativo_desc'||' like'||'''%'||pParGrupoAtivo||'%'' ';	
	end if;
	
	
	if pParCentro2OrdId != '' then
			 vSql = vSql || 'and ' || ' t1.ope_centro2_ord_id' || ' in(''' ||pParCentro2OrdId||''')';
	end if;
	
	
	
	if pParCentro2OrdDtIniExec != '' and pParCentro2OrdDtIniExecFin != '' then
		vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_ini_exec AS DATE)' || ' >= ''' || pParCentro2OrdDtIniExec|| '''' || ' and  CAST(t1.ope_centro2_ord_data_ini_exec AS DATE)' || ' <= ''' || pParCentro2OrdDtIniExecFin|| '''';		
	end if;

	if pParCentro2OrdDtFinExecIni != '' and pParCentro2OrdDtFinExec != '' then
		vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_fin_exec AS DATE)' || ' >= ''' || pParCentro2OrdDtFinExecIni|| '''' || ' and  CAST(t1.ope_centro2_ord_data_fin_exec AS DATE)' || ' <= ''' || pParCentro2OrdDtFinExec|| '''';		
	end if;

	if pParCentro2OrdDtIniExecPrev != '' and pParCentro2OrdDtIniExecPrevFin != '' then
		vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_ini_exec_prev AS DATE)' || ' >= ''' || pParCentro2OrdDtIniExecPrev|| '''' || ' and  CAST(t1.ope_centro2_ord_data_ini_exec_prev AS DATE)' || ' <= ''' || pParCentro2OrdDtIniExecPrevFin|| '''';
	end if;
	
	if pParCentro2OrdDtFinExecPrevIni != '' and pParCentro2OrdDtFinExecPrev != '' then
		vSql = vSql || ' and ' ||'CAST(t1.ope_centro2_ord_data_fin_exec_prev AS DATE)' || ' >= ''' || pParCentro2OrdDtFinExecPrevIni|| '''' || ' and  CAST(t1.ope_centro2_ord_data_fin_exec_prev AS DATE)' || ' <= ''' || pParCentro2OrdDtFinExecPrev|| '''';	
	end if;

	if pParCentro2OrdNr != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_ord_numero_ord'||' like'||'''%'||pParCentro2OrdNr||'%'' ';	
	end if;


		if pParEmpresaOrdId != '' then
		 vSql = vSql || 'and ' || ' t1.ger_empresa_id_ord' || ' in(''' ||pParEmpresaOrdId||''')';	
	end if;
	
	if pParEmpresaOrdNome != '' then
		vSql = vSql ||' and '||'t1.ger_empresa_nome_ord'||' like'||'''%'||pParEmpresaOrdNome||'%'' ';	
	end if;	
		
	if pParEmpresaOrdAtivo != '' then
		vSql = vSql ||' and '||'t1.ger_empresa_ativo_desc_ord'||' like'||'''%'||pParEmpresaOrdAtivo||'%'' ';	
	end if;		
	
	if pParEmpresaOrdCpf != '' then
		vSql = vSql ||' and '||'t1.ger_empresa_doc_cpf_ord'||' like'||'''%'||pParEmpresaOrdCpf||'%'' ';	
	end if;					
	
	if pParEmpresaOrdCnpj != '' then
		vSql = vSql ||' and '||'t1.ger_empresa_doc_cnpj_ord'||' like'||'''%'||pParEmpresaOrdCnpj||'%'' ';	
	end if;
	
	
	if pParPeriodoOrdId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_periodo_id_ord' || ' in(''' ||pParPeriodoOrdId||''')';		
	end if;

	if pParPeriodoOrdNome != '' then
		vSql = vSql ||' and '||'t1.ope_periodo_nome_ord'||' like'||'''%'||pParPeriodoOrdNome||'%'' ';	
	end if;

	if pParPeriodoOrdAtivo != '' then
		vSql = vSql ||' and '||'t1.ope_periodo_ativo_ord_desc'||' like'||'''%'||pParPeriodoOrdAtivo||'%'' ';	
	end if;

	if pParPeriodoOrdDataIni != '' and pParPeriodoOrdDataIniFin != '' then
		vSql = vSql || ' and ' ||'CAST(t1.ope_periodo_data_ini_ord AS DATE)' || ' >= ''' || pParPeriodoOrdDataIni|| '''' || ' and CAST(t1.ope_periodo_data_ini_ord AS DATE)' || ' <= ''' || pParPeriodoOrdDataIniFin|| '''';	
	end if;

	if pParPeriodoOrdDataFinIni != '' and pParPeriodoOrdDataFin != '' then
		vSql = vSql || ' and ' ||'CAST(t1.ope_periodo_data_fin_ord AS DATE)' || ' >= ''' || pParPeriodoOrdDataFinIni|| '''' || ' and CAST(t1.ope_periodo_data_fin_ord AS DATE)' || ' <= ''' || pParPeriodoOrdDataFin|| '''';	
	end if;
	
	
	if pParGerPessoaId != '' then
		 vSql = vSql || 'and ' || ' t1.ger_pessoa_id_ord' || ' in(''' ||pParGerPessoaId||''')';
	end if;

	if pParGerPessoaNome != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_nome_ord'||' like'||'''%'||pParGerPessoaNome||'%'' ';		
	end if;
	
	if pParGerPessoaAtivo != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_ativo_desc_ord'||' like'||'''%'||pParGerPessoaAtivo||'%'' ';		
	end if;

	if pParGerPessoaDoc != '' then
		vSql = vSql ||' and '||'t1.ger_pessoa_doc_cpf_cnpj_ord'||' like'||'''%'||pParGerPessoaDoc||'%'' ';		
	end if;
	
	
	if pParCentro2OrdTipoId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro2_ord_tipo_id' || ' in(''' ||pParCentro2OrdTipoId||''')';
	end if;
	

	if pParCentro2OrdTipoNome != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_ord_tipo_nome'||' like'||'''%'||pParCentro2OrdTipoNome||'%'' ';				
	end if;	

	if pParCentro2OrdTipoAtivo != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_ord_tipo_ativo_desc'||' like'||'''%'||pParCentro2OrdTipoAtivo||'%'' ';				
	end if;	
	
	if pParFrentTrabId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_frente_trabalho_id_ord' || ' in(''' ||pParFrentTrabId||''')';
	end if;	
	
	if pParFrentTrabNome != '' then
		vSql = vSql ||' and '||'t1.ope_frente_trabalho_nome_ord'||' like'||'''%'||pParFrentTrabNome||'%'' ';	
	end if;
	
	if pParFrentTrabAtivo != '' then
		vSql = vSql ||' and '||'t1.ope_frente_trabalho_ativo_desc_ord'||' like'||'''%'||pParFrentTrabAtivo||'%'' ';	
	end if;	
	
	if pParStatusId != '' then
		 vSql = vSql || 'and ' || ' t1.ope_centro2_ord_status_id' || ' in(''' ||pParStatusId||''')';
	end if;
	
	if pParStatusNome != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_ord_status_nome'||' like'||'''%'||pParStatusNome||'%'' ';	
	end if;

	if pParStatusAtivo != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_ord_status_ativo_desc'||' like'||'''%'||pParStatusAtivo||'%'' ';	
	end if;
	
	if pParStatusTipo != '' then
		vSql = vSql ||' and '||'t1.ope_centro2_ord_status_tipo_status'||' like'||'''%'||pParStatusTipo||'%'' ';	
	end if;	
	
	if pParLogUserIns != '' then
			vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
	end if;
		
		if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
		  vSql = vSql || ' and ' || 'CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
		end if;
		
		if pParLogUserUpd != '' then
			vSql = vSql || 'and ' || ' t1.log_user_upd' || ' like '|| '''%' ||pParLogUserUpd|| '%'' ';
		end if;		

		if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
		  vSql = vSql || ' and ' || 'CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
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
		valor_02 := r.valor_02;
		valor_03 := r.valor_03;
		valor_04 := r.valor_04;
		valor_05 := r.valor_05;

	RETURN NEXT;
	
	END loop;
Raise notice 'Sql :%',vSql;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE;
