# EXEMPLO EXECUÇÃO - report

## (FIN) - SUMARIO DE PAGAMENTOS E RECEBIMENTOS
       uuid:
       nome_tecnico: report0009.
	   
	   #Atualizar Parametros
	   
       parametros: pParUnitId,pParIndRelId ,pVart01, pVard01, pVart02, pVard02, pVart03, pVard03, pVart04, pVard04, pVart05, pVard05, 
       pParGerEmpresaId, pParFinPagRecES, pParFinCondPagrecId, pParFinTipoId, pParGerPessoaNome, pParGerPessoaId, pParGerPessoaPagrecNome,
       pParGerPessoaPagrecId, pParFinDocTipoId, pParFinPagrecDataMovIni, pParFinPagrecDataMovFin, pParFinPagrecNumeroDocPagrec,
       pParFinPagrecParcValorPagrecIni, pParFinPagrecParcValorPagrecFin, pParFinPagrecParcValorJuroIni, pParFinPagrecParcValorJuroFin,
       pParFinPagrecParcValorDescontoIni, pParFinPagrecParcValorDescontoFin, pParFinPagrecParcValorMultaIni, pParFinPagrecParcValorMultaFin
       pParFinPagrecParcDataVencIni, pParFinPagrecParcDataVencFin, pParLogUserIns, pParLogDateInsIni, pParLogDateInsFin, pParLogUserUpd,
       pParLogDateUpdIni, pParLogDateUpdFin
       #Guia Dados Teste (Execução)
              pParUnitId =  f3996813-838e-49af-9649-8dc44e24bc75
			  pParIndRelId = 623a4735-18f1-4a6e-b596-ef0235737973
              pVart01 = ger_pessoa_desc
              pVard01 = Pessoa
              pVart02 = ger_pessoa_pagrec_desc
              pVard02 = Pessoa P/R
              pVart03 = fin_pagrec_data_mov
              pVard03 = Dt.Mov
			  vars_01 = S
			  vars_02 = S
			  vars_03 = N
			  vars_04 = N
			  vars_05 = N
              
       #SQL
          select * from fnreport0009('f3996813-838e-49af-9649-8dc44e24bc75','623a4735-18f1-4a6e-b596-ef0235737973','ger_pessoa_desc','Pessoa',
                                    'ger_pessoa_pagrec_desc','Pessoa P/R',
                                    'fin_pagrec_data_mov','Dt.Mov')


## (GER) - PAIS > FEDERAÇÃO > CIDADE
       uuid: 0ac2032f-fc44-41c9-9bf9-833e1647be5b
       nome_tecnico: report0002.
       parametros: pParUnitId, pParPaisId, pParPaisNome, pParPaisNome, pParPaisSigla, pParPaisAtivo,
       pParUfId, pParUfNome ,pParUfAtivo, pParUfSigla, pParCidId, pParCidNome, pParCidAtivo, pParTitleReport
       #Guia Dados Teste (Execução)
              pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
              pParPaisId = 99c4bfa5-06bd-40b2-8432-61d284af7586
              pParPaisNome = Brasil
              pParPaisSigla = BRA
              pParPaisAtivo = S
              pParUfId = 498594ad-4218-42f9-aa24-510de57ae1a2
              pParUfNome = São Paulo
              pParUfAtivo = S
              pParUfSigla = SP
              pParCidId = 5da3855f-9103-476b-84ba-f7cd84bcb2b5
              pParCidNome = São Joaquim da Barra
              pParCidAtivo = S


## (SYS) - USUÁRIOS > UNIDADE
       uuid: 2a46c160-47e7-4bc7-9477-fab5b82e346a
       nome_tecnico: report0003.
       parametros:  pParUserId, pParUserName, pParUserEmail, pParUserActive, pParUnitName, pParUnitSigla, pParUnitId ,pParTitleReport
       #Guia Dados Teste (Execução)
               pParUserId = 7448e100-8b3c-4cc3-ba78-18b230339005
               pParUserName = admin
               pParUserEmail = suporte@resultfacil.com.br
               pParUserActive = S
               pParUnitName = Exemplo(PADRAO)
               pParUnitSigla = EXEMPLO
               pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
    
## (GER) - PESSOAS > ENDEREÇO > CONTA BANCÁRIA
      uuid: 02ad9cdb-2ff9-47ea-9248-abdfbe857d5a
      nome_tecnico: report0005.
      parametros: pParUnitId, pParPessoaNome, pParPessoaSigla, pParPessoaAtivo, pParpessoaId
      #Guia Dados Teste (Execução)
            pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
            pParpessoaId = 5e27d766-dd40-4be4-815b-8b455ecba37b
            pParPessoaNome = %Cli%
            pParPessoaSigla = %
            pParPessoaAtivo = %
            

## (GER) - MARCA > MODELO
      uuid: 5fc557d4-89ec-4804-b55a-3f1f31b91e8d
      nome_tecnico: report0007.
      parametros: pParUnitId, pParMarcaId, pParMarcaNome, pParMarcaAtivo, pParModeloId, pParModeloNome, pParModeloAtivo, pParTitleReport
      #Guia Dados Teste (Execução)
            pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
            pParMarcaId = d11e15fc-8b22-4d00-8c93-65e8b5f0c2ad
            pParMarcaNome = %
            pParMarcaAtivo = %
            pParModeloId = %
            pParModeloNome = %
            pParModeloAtivo = S

## (FIN) - GRUPO > CLASSIFICAÇÃO
      uuid: 1d760ef1-57c4-4bce-a5aa-7627cb5848e9
      nome_tecnico: report0008.
      parametros: pParUnitId, pParAgrupNome, pParAgrupAtivo, pParGrupoId, pParGrupoNome, pParGrupoAtivo, pParFinClassSigla, pParFinClassNome,
      pParFinClassAtivo, pParAgrupId, pParFinClassId, pParTitleReport, pParGrupoSigla
      #Guia Dados Teste (Execução)
            pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
            pParAgrupId = 7e06adb1-bbb9-4a30-ae30-80592c0683c6
            pParAgrupNome = %
            pParAgrupAtivo = %
            pParGrupoId = f239c9cd-d1d7-43c6-b5b3-a784e69a7705
            pParGrupoNome = %
            pParGrupoAtivo = S
            pParGrupoSigla = %
            pParFinClassId =  593b77d5-0715-449d-9b84-8f4184125340
            pParFinClassSigla = %
            pParFinClassNome = %
            pParFinClassAtivo = %
            
            
## (FIN) - BANCO > CONTA
      uuid: ec2af668-7cda-4021-a7ad-320c5e93b703
      nome_tecnico: report0010
      parametros: pParUnitId, pParBancoNome, pParBancoNr, pParBancoAtivo, pParContaAgencia, pParContaNr, pParBancoId, pParContaId, pParContaAtivo,
      pParTitleReport
      #Guia Dados Teste (Execução)
            pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
            pParBancoId = f83897a1-dcc8-4890-8010-9e7dfec7fd8d
            pParBancoNome = 
            pParBancoAtivo =
            pParBancoNr = 
            pParContaId = e3a1ec7d-c831-4a40-83f5-330c32f8ba27
            pParContaAtivo =
            pParContaNr =
            pParContaAgencia =


## (OPE) ORDEM SERVIÇO
      uuid: fa54e176-e07e-416d-9150-0b708fd2451b
      nome_tecnico: report0011
      parametros: pParIdOrdem, pParUnitId
      #Guia Dados Teste (Execução)
            pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
            pParIdOrdem = 45ecc32e-08e2-46f8-95f5-866444e185e0 || 94ffbb47-a6ea-4e1d-8339-a3b98cff2a31
	

## (OPE) - ÁREA
	  uuid: 46c7b1bb-a8f8-4579-9b65-24d8ecc911b5
	  nome_tecnico: report0014OpeArea
	  parametros: nameReport,pParUser,pParTitleReport,pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,
	  pVart05,pVard05,pVart06,pVard06,pVart07,pVard07,pVart08,pVard08,pVart09,pVard09,pVart10,pVard10,pParCentro2AreaId,pParBlocoCol,pParTipoSoloId,
	  pParTipoSoloNome,pParEspacId,pParEspacNome,pParAtivSisPlanId,pParAtivSisPlanNome,pParAtivSisCultId,pParAtivSisCultNome,pParAtivSisColhId,pParAtivSisColhNome,
	  pParItemServId,pParItemServNome,pParItemServAtivo,pParDataIniPlan,pParDataIniPlanFin,pParDataFinPlanIni,pParDataFinPlan,pParDataUltPlanIni,pParDataUltPlanFin,
	  pParDataIniCol,pParDataIniColFin,pParDataFinColIni,pParDataFinCol,pParDataUltColIni,pParDataUltColFin,pParDataFloradaIni,pParDataFloradaFin,pParDataEmergIni,
	  pParDataEmergFin,pParUnidadeMedId,pParUnidadeMedNome,pParCentro1Id,pParCentro1Nome,pParCentro1Ativo,pParCentro2Id,pParCentro2Nome,pParCentro2Ativo,pParSubTipoId,
	  pParSubTipoNome,pParTipoId,pParTipoNome,pParRatTipoId,pParRatTipoNome,pParSubGrupoId,pParSubGrupoNome,pParGrupoId,pParGrupoNome,pParGrupoAtivo,pParPeriodoId,
	  pParPeriodoNome,pParPeriodoAtivo,pParPeriodoDataIni,pParPeriodoDataFin,pParLogUserIns,pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,
	  pParLogDateUpdFin,vars_01,vars_02,vars_03,vars_04,vars_05
      #Guia Dados Teste (Execução)
            pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
            pParIndRelId = 46c7b1bb-a8f8-4579-9b65-24d8ecc911b5
			pVart01 = ope_centro2_area_item_serv_ultimo_nome
			pVard01 = Item Serviço
			pVart02 = ope_centro2_area_tipo_solo_nome
			pVard02 = Tipo de Solo
			vars_01 = S
			vars_02 = S
			vars_03 = N
			vars_04 = N
			vars_05 = N
	 #SQL
		select * from fnreport0014('f3996813-838e-49af-9649-8dc44e24bc75','46c7b1bb-a8f8-4579-9b65-24d8ecc911b5','ope_centro2_area_tipo_solo_nome'
		,'Tipo Solo','','','','','','','','','','','','','','','','','','','','' , '',
		'','','','','','','','','','','','','','','','','','','','','','','','',
		'','','','','','','','','','','','','','','','','','','','','','','S','','','',
		'2020-04-01','2021-03-31','admin','','','','','')
		

## (OPE) - Equipamento
	  uuid: ca30de82-cd90-4fe4-8ee1-887dff83b59a
	  nome_tecnico: report0016OpeEquip
	  parametros:pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,pVart06,pVard06,pVart07,pVard07,
		pVart08,pVard08,pVart09,pVard09,pVart10,pVard10,pParEquipId,pParEquipTipoRodado,pParEquipTipoCarroceria,pParEquipCidId,pParEquipCidNome,
		pParEquipAtivo,pParUfId,pParUfNome,pParEquipPlaca,pParEquipRenavam,pParEquipTara,pParEquipCapacidKg,pParEquipCapacidM3,pParEquipPotenc,
		pParEquipNrChassi,pParEquipNrSerie,pParEquipLiberadoAbastec,pParEquipLargura,pParEquipAltur,pParEquipNrRegEstadual,pParEquipTipoTracao,pParEquipTipoTranspAutCarga,
		pParCentro1Id,pParCentro1Nome,pParCentro1Ativo,pParCentro2Id,pParCentro2Nome,pParCentro2Ativo,pParFrentTrabId,pParFrentTrabNome,pParFrentTrabAtivo,
		pParMarcaModeloId,pParMarcaModeloNome,pParMarcaModeloAtivo,pParMarcaId,pParMarcaNome,pParMarcaAtivo,pParSubGrupId,pParSubGrupoNome,pParSubGrupoAtivo,
		pParGrupoId,pParGrupoNome,pParGrupoAtivo,pParProprietarioId,pParProprietarioNome,pParProprietarioAtivo,pParProprietarioDoc,pParLogUserIns,pParLogDateInsIni,
		pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,pParLogDateUpdFin
	  #Guia Dados Teste (Execução)
		pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
        pParIndRelId = ca30de82-cd90-4fe4-8ee1-887dff83b59a
		pVart01 = ope_centro2_equip_cidade_nome
		pVard01 = Cidade
		pVart02 = ope_frente_trabalho_nome
		pVard02 = Frente
		pVart03 = ope_centro2_nome
		pVard03 = Equipamento
	  
	  #SQL
		select * from fnreport0016('f3996813-838e-49af-9649-8dc44e24bc75','ca30de82-cd90-4fe4-8ee1-887dff83b59a','ope_centro2_equip_cidade_nome',
		'Cidade','ope_frente_trabalho_nome','Frente','ope_centro2_nome','Equipamento');

## (OPE) - Pessoa
	  uuid: 18d16cfe-436e-4a56-bd1d-9d25a281d3e1
	  nome_tecnico: report0017OpePessoa
	  parametros: pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,pParCentro2PessoaId,
		pParPessoaPtoIdenfTipo,pParPessoaPtoIdenf,pParCentro1Id,pParCentro1Nome,pParCentro1Ativo,pParCentroSubTipoId,pParCentroSubTipoNome,
		pParCentro2Id,pParCentro2Sigla,pParCentro2Nome,pParCentro2Ativo,pParFrenteTrabalhoId,pParFrenteTrabalhoNome,pParFrenteTrabalhoSigla,
		pParFrenteTrabalhoAtivo,pParLogUserIns,pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,pParLogDateUpdFin
	  #Guia Dados Teste (Execução)
		pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
		pParIndRelId = 18d16cfe-436e-4a56-bd1d-9d25a281d3e1
		pVart01 = ope_frente_trabalho_nome
		pVard01 = Frente
		pVart02 = ope_centro2_nome
		pVard02 = Pessoa

## (OPE) - Estoque
	  uuid: 3378e747-b2a9-46ed-a3f0-172043f95800
	  nome_tecnico: report0018OpeEstoque
	  parametros: pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,pParEstoqId,
		pParEstoqTipo,pParCentro2Id,pParCentro2Nome,pParCentro2Ativo,pParCentro2Sigla,pParCentro2TipoDestinacao,pParCentro2TipoCtbComp,
		pParCentro2CtbCompId,pParLogUserIns,pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,pParLogDateUpdFin
	  #Guia Dados Teste (Execução)
		pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
        pParIndRelId = 3378e747-b2a9-46ed-a3f0-172043f95800
		pVart01 = ope_centro2_estoque_tipo
		pVard01 = Tipo
		pVart02 = ope_centro2_nome
		pVard02 = Centro 2

## (OPE) - ORD DEST
	  uuid: 311efc68-9d31-4aed-8e23-40863b9f8983
	  nome_tecnico: report0019OpeOrdDest
	  parametros: pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,
	  pParOrdDestId,pParOrdDestQntPrevObjIni,pParOrdDestQntPrevObjFin,pParOrdDestVrUnitPrevIni,pParOrdDestVrUnitPrevFin,pParOrdDestVrTotPrevIni,
	  pParOrdDestVrTotPrevFin,pParOrdDestQntObjIni,pParOrdDestQntObjFin,pParOrdDestVrUnitIni,pParOrdDestVrUnitFin,pParOrdDestVrTotalIni,pParOrdDestVrTotalFin,
	  pParOrdDataIniExecIni,pParOrdDataIniExecFin,pParOrdDataFinExecIni,pParOrdDataFinExecFin,pParOrdDataStatusIni,pParOrdDataStatusFin,pParOrdDataIniExecPrevIni,
	  pParOrdDataIniExecPrevFin,pParOrdDataFinExecPrevIni,pParOrdDataFinExecPrevFin,pParCentro2Id,pParCentro2Nome,pParCentro2Ativo,pParCtbId,pParCtbNome,pParCtbAtivo,
	  pParGerUmedidaId,pParGerUmedidaNome,pParGerUmedidaAtivo,pParCentro1Id,pParCentro1Nome,pParCentro1Ativo,pParSubGrupoId,pParSubGrupoNome,pParSubGrupoAtivo,pParGrupoId,
	  pParGrupoNome,pParGrupoAtivo,pParSubTipoId,pParSubTipoNome,pParTipoId,pParTipoNome,pParGerEmpresaId,pParGerEmpresaNome,pParGerEmpresaAtivo,pParGerEmpresaDocCnpj,pParGerEmpresaDocCpf,
	  pParPeriodoId,pParPeriodoNome,pParPeriodoAtivo,pParPeriodoDataIni,pParPeriodoDataIniFin,pParPeriodoDataFinIni,pParPeriodoDataFin,pParCentro2PessoaId,pParCentro2PessoaNome,
	  pParGerPessoaEnderecoId,pParGerPessoaEnderecoAtivo,pParGerPessoaEnderecoTipo,pParGerPessoaEnderecoPadrao,pParGerPessoaEnderecoLograd,pParGerPessoaEnderecoLogradNr,
	  pParGerPessoaEnderecoLogradBairro,pParGerPessoaId,pParGerPessoaNome,pParGerPessoaAtivo,pParGerPessoaDoc,pParOrdTipoId,pParOrdTipoNome,pParOrdCentro2Id,
	  pParOrdCentro2Nome,pParOrdCentro2Ativo,pParFrenteTrabalhoId,pParFrenteTrabalhoNome,pParFrenteTrabalhoAtivo,pParStatusId,pParStatusNome,pParStatusAtivo,
	  pParStatusTipo,pParLogUserIns,pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,pParLogDateUpdFin
	  #Guia Dados Teste (Execução)
	  	pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
        pParIndRelId = 311efc68-9d31-4aed-8e23-40863b9f8983 
		pVart01 = ger_empresa_nome_ord	
		pVard01 = Empresa
		pVart02 = ope_centro2_nome
		pVard02 = Destinação
		
## (OPE) - ORD ITEM/SERV
	  uuid: dde3a09a-9f51-4113-83d1-b3f0fd27ed35
	  nome_tecnico: report0020OpeOrdItemServ
	  parametros:  pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,
	  pParItemServId,pParQntRendIni,pParQntRendFin,pParPercUtilIni,pParPercUtilFin,pParQntTotUtilIni,pParQntTotUtilFin,pParVrUnitUtilIni,pParVrUnitUtilFin,
	  pParVrTotUtilIni,pParVrTotUtilFin,pParAtivOrdExec,pParAtivOrdTipoExec,pParItemServNome,pParItemServAtivo,pParItemServTipo,pParAtivId,pParAtivNome,pParAtivAtivo,
	  pParCentro2OrdId,pParCentro2OrdDtIniExec,pParCentro2OrdDtIniExecFin,pParCentro2OrdDtFinExecIni,pParCentro2OrdDtFinExec,pParCentro2OrdDtIniExecPrev,pParCentro2OrdDtIniExecPrevFin,
	  pParCentro2OrdDtFinExecPrevIni,pParCentro2OrdDtFinExecPrev,pParCentro2OrdNr,pParEmpresaOrdId,pParEmpresaOrdNome,pParEmpresaOrdAtivo,pParEmpresaOrdCpf,pParEmpresaOrdCnpj,
	  pParPeriodoOrdId,pParPeriodoOrdNome,pParPeriodoOrdAtivo,pParPeriodoOrdDataIni,pParPeriodoOrdDataIniFin,pParPeriodoOrdDataFinIni,pParPeriodoOrdDataFin,pParCtbId,pParCtbNome,
	  pParCtbAtivo,pParGerPessoaId,pParGerPessoaNome,pParGerPessoaAtivo,pParGerPessoaDoc,pParPessoaEnderecoId,pParPessoaEnderecoAtivo,pParPessoaEnderecoTipo,pParPessoaEnderecoPadrao,
	  pParPessoaEnderecoLograd,pParPessoaEnderecoNr,pParCentro2OrdTipoId,pParCentro2OrdTipoNome,pParCentro2OrdTipoAtivo,pParCentro2Id,pParCentro2Nome,pParCentro2Ativo,pParCentro1Id,
	  pParCentro1Nome,pParCentro1Ativo,pParFrentTrabId,pParFrentTrabNome,pParFrentTrabAtivo,pParStatusId,pParStatusNome,pParStatusAtivo,pParStatusTipo,pParSubGrupoId,pParSubGrupoNome,
	  pParSubGrupoAtivo,pParGrupoId,pParGrupoNome,pParGrupoAtivo,pParSubTipoId,pParSubTipoNome,pParTipoId,pParTipoNome,pParLogUserIns,pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,
	  pParLogDateUpdIni,pParLogDateUpdFin
	   #Guia Dados Teste (Execução)	  
	  	 pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
         pParIndRelId = 311efc68-9d31-4aed-8e23-40863b9f8983
		 pVart01 = ope_atividade_nome
		 pVard01 = Atividade
		 pVart02 = ger_itemserv_nome
		 pVard02 = Item/Serv
		 
## (OPE) - ORD REC
	  uuid: 7ce1666f-4df4-4e17-8376-ce7305ee6d6e
	  nome_tecnico: report0021OpeOrdRec
	  parametros: pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,
	  pParOrdRecIId,pParOrdRecQntRendIni,pParOrdRecQntRendFin,pParOrdRecPercUtilIni,pParOrdRecPercUtilFin,pParOrdRecQntTotUtilIni,pParOrdRecQntTotUtilFin,pParOrdRecVrUnitUtilIni,
	  pParOrdRecVrUnitUtilFin,pParOrdRecVrTotUtilIni,pParOrdRecVrTotUtilFin,pParCentro1Id,pParCentro1Nome,pParCentro1Ativo,pParCentro2Id,pParCentro2Nome,pParCentro2Ativo,
	  pParCtbId,pParCtbNome,pParCtbAtivo,pParPessoaEnderecoId,pParPessoaEnderecoAtivo,pParPessoaEnderecoTipo,pParPessoaEnderecoPadrao,pParPessoaEnderecoLograd,pParPessoaEnderecoNr,
	  pParCentro1Imp01Id,pParCentro1Imp01Nome,pParCentro1Imp01Ativo,pParCentro2Imp01Id,pParCentro2Imp01Nome,pParCentro2Imp01Ativo,pParSubTipoId,pParSubTipoNome,pParTipoId,pParTipoNome,
	  pParSubGrupoId,pParSubGrupoNome,pParSubGrupoAtivo,pParGrupoId,pParGrupoNome,pParGrupoAtivo,pParCentro2OrdId,pParCentro2OrdDtIniExec,pParCentro2OrdDtIniExecFin,pParCentro2OrdDtFinExecIni,
	  pParCentro2OrdDtFinExec,pParCentro2OrdDtIniExecPrev,pParCentro2OrdDtIniExecPrevFin,pParCentro2OrdDtFinExecPrevIni,pParCentro2OrdDtFinExecPrev,pParCentro2OrdNr,pParEmpresaOrdId,pParEmpresaOrdNome,
	  pParEmpresaOrdAtivo,pParEmpresaOrdCpf,pParEmpresaOrdCnpj,pParPeriodoOrdId,pParPeriodoOrdNome,pParPeriodoOrdAtivo,pParPeriodoOrdDataIni,pParPeriodoOrdDataIniFin,pParPeriodoOrdDataFinIni,pParPeriodoOrdDataFin,
	  pParGerPessoaId,pParGerPessoaNome,pParGerPessoaAtivo,pParGerPessoaDoc,pParCentro2OrdTipoId,pParCentro2OrdTipoNome,pParCentro2OrdTipoAtivo,pParFrentTrabId,pParFrentTrabNome,pParFrentTrabAtivo,pParStatusId,
	  pParStatusNome,pParStatusAtivo,pParStatusTipo,pParLogUserIns,pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,pParLogDateUpdFin
	   #Guia Dados Teste (Execução)	  	  
	  	 pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
         pParIndRelId = 7ce1666f-4df4-4e17-8376-ce7305ee6d6e
		 pVart01 = ope_frente_trabalho_nome_ord
		 pVard01 = Frente Trabalho
		 pVart02 = ope_centro2_nome
		 pVard02 = Recurso
		 
## (GER) - ITEM/SERVIÇO
	  uuid: 0f0dc5f0-6e33-4674-a3e5-025fc02a42bd
	  nome_tecnico: report0022GerItemServ
	  parametros: pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,
	  pParItemServId,pParItemServNome,pParItemServAtivo,pParItemServTipo,pParItemServOrigemFiscal,pParItemServTipoComposi,pParItemServTipoCtbComp,pParItemServDocCnaeNfs,
	  pParItemServSubGrupoId,pParItemServSubGrupoNome,pParItemServSubGrupoAtivo,pParItemServGrupoId,pParItemServGrupoNome,pParItemServGrupoAtivo,pParFisNcmId,pParFisNcmNome,
      pParFisNcmAtivo,pParFisNcmDataValidadeIni,pParFisNcmDataValidadeFin,pParFisNcmNumero,pParUnidadeMedId,pParUnidadeMedNome,pParUnidadeMedAtivo,pParFisCestId,pParFisCestNome,
	  pParFisCestAtivo,pParFisCestDataValidadeIni,pParFisCestDataValidadeFin,pParFisCestNumero,pParFisNbsId,pParFisNbsNome,pParFisNbsAtivo,pParFisNbsDataValidadeIni,pParFisNbsDataValidadeFin,
	  pParFisNbsNumero,pParCtbId,pParCtbNome,pParCtbAtivo,pParLogUserIns,pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,pParLogDateUpdFin
	   #Guia Dados Teste (Execução)	  	  
	  	 pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
         pParIndRelId = 7ce1666f-4df4-4e17-8376-ce7305ee6d6e
		 pVart01 = ger_itemserv_grupo_nome
		 pVard01 = Grupo
		 pVart02 = ger_itemserv_nome
		 pVard02 = Item/Serviço
		 
		 
## (MOV) MOVIMENTAÇÃO DE ITENS
	  uuid: a26c642c-7396-4958-bbf6-633b4e008c13
	  nome_tecnico: report0023MovItemServ
	  parametros: pParUnitId,pParIndRelId,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,pVart06,pVard06,
	  pVart07,pVard07,pVart08,pVard08,pVart09,pVard09,pVart10,pVard10,pParMovId,pParMovSerie,pParDataMovIni,pParDataMovFin,pParNrMov,
	  pParDataEntregaMovIni,pParDataEntregaMovFin,pParMovOperacaoId,pParMovOperacaoNome,pParMovOperacaoAtivo,pParMovOperacaoSigla,pParMovOperacaoTipoES,
	  pParMovTipoId,pParMovTipoNome,pParMovTipoAtivo,pParMovTipoSigla,pParMovTipoMov,pParGerNumeracaoId,pParGerNumeracaoNome,pParGerNumeracaoAtivo,
	  pParGerNumeracaoSerie,pParMovStatusId,pParMovStatusNome,pParMovStatusAtivo,pParMovStatusSigla,pParMovStatusTipo,pParGerEmpresaId,pParGerEmpresaNome,
	  pParGerEmpresaAtivo,pParGerEmpresaSigla,pParGerPessoaId,pParGerPessoaNome,pParGerPessoaAtivo,pParGerPessoaSigla,pParGerPessoaEnderecoAtivo,
	  pParGerPessoaEnderecoLograd,pParGerPessoaEnderecoLogradNr,pParGerPessoaEnderecoLogradBairro,pParGerPessoaEntregId,pParGerPessoaEntregNome,
	  pParGerPessoaEntregAtivo,pParGerPessoaEntregEnderecoAtivo,pParGerPessoaEntregEnderecoLograd,pParGerPessoaEntregEnderecoLogradNr,pParGerPessoaEntregEnderecoLogradBairro,
	  pParMovItemServId,pParItemServId,pParItemServNome,pParItemServAtivo,pParItemServSigla,pParItemServTipo,pParItemServSubGrupoId,pParItemServSubGrupoNome,
	  pParItemServSubGrupoAtivo,pParItemServGrupoId,pParItemServGrupoNome,pParItemServGrupoAtivo,pParGerUmedidaId,pParGerUmedidaNome,pParGerUmedidaAtivo,
	  pParGerUmedidaSigla,pParFisCfopId,pParFisCfopNR,pParFisCfopNome,pParFisCfopAtivo,pParFisCfopDataValidIni,pParFisCfopDataValidFin,pParLogUserIns,
	  pParLogDateInsIni,pParLogDateInsFin,pParLogUserUpd,pParLogDateUpdIni,pParLogDateUpdFin
	   #Guia Dados Teste (Execução)	  	  
	  	 pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
         pParIndRelId = a26c642c-7396-4958-bbf6-633b4e008c13
		 pVart01 = ger_itemserv_grupo_nome
		 pVard01 = Grupo
		 pVart02 = ger_item_serv_nome
		 pVard02 = Item/Serviço
		 

## (MOV) - ANALISE DE COTAÇÃO
	  uuid: 0127bc7f-6c48-4206-bf27-3eb364c7a7ca
	  nome_tecnico: report0024MovCotacao
	  parametros: pParUnitId,pParTitleReport,pParIndRelId,pParMovId,pParDataMovIni,pParDataMovFin,pParNrMov,pParGerEmpresaNome,pParGerEmpresaSigla,pParSystemUser
	   #Guia Dados Teste (Execução)
		pParUnit = f3996813-838e-49af-9649-8dc44e24bc75
		pParIndRelId = 0127bc7f-6c48-4206-bf27-3eb364c7a7ca
		pParMovId = 4482d8dd-2fad-4216-927f-b11460794015
		dataMovIni = 2020-06-25
		dataMovFim = 2020-06-26
		pParNrMov = %
		pParGerEmpresaNome = %
		pParGerEmpresaSigla = %
		pParSystemUser = %

		
## (OPE) - OCORRENCIAS - ÁREA
	  uuid: bd99ce86-c4fe-4e15-b844-6565bc08d0d6
	  nome_tecnico: report0025OpeOcorMovDestArea
	  parametros:pParUnitId,pParIndRelId,pParTitleReport,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,pParOpeAreaQntAreaProd,
		pParOpeAreaQntAreaImprod,pParOpeAreaQntPlantEstand,pParOpeAreaBlocoCol,pParOpeAreaDtIniPlan,pParOpeAreaDtIniPlanFin,pParOpeAreaDtFinPlanIni,
		pParOpeAreaDtFinPlan,pParOpeAreaDtUltPlanIni,pParOpeAreaDtUltPlanFin,pParOpeAreaDtIniCol,pParOpeAreaDtIniColFin,pParOpeAreaDtFinColIni,pParOpeAreaDtFinCol,
		pParOpeAreaDtUltColIni,pParOpeAreaDtUltColFin,pParOpeAreaDtFlorada1Ini,pParOpeAreaDtFlorada1Fin,pParOpeAreaDtEmergIni,pParOpeAreaDtEmergFin,pParOpeAreaUmedidaNome,
		pParOpeAreaUmedidaSigla,pParCentro2Nome,pParCentro2Sigla,pParCentro2Ativo,pParCentro2TipoDestinacao,pParCentro2TipoProp,pParCentro1Nome,pParCentro1Ativo,
		pParCentro1Sigla,pParAreaSistemaCultNome,pParAreaSistemaCultSigla,pParOcorMovDataMovIni,pParOcorMovDataMovFin,pParOcorMovNr,pParGerEmpresaNome,pParGerEmpresaAtivo,
		pParGerEmpresaDocCnpj,pParGerEmpresaDocCpf,pParGerPessoaEnderecoLograd,pParGerPessoaEnderecoLogradNr,pParGerCidadeNome,pParUfNome,pParOcorTipoNome,
		pParOcorTipoAtivo,pParOcorTipoSigla,pParOcorTipoObrigCompart,pParOcorTipoTp,pParOcorMovDetQntOcor,pParOcorMovDetQntOcorCalc,pParOcorMovDetDtStatusIni,
		pParOcorMovDetDtStatusFin,pParOcorNome,pParOcorAtivo,pParOcorSigla,pParOcorTipo,pParOcorTipoLanc,pParOcorGrupoNome,pParOcorGrupoAtivo,pParOcorGrupoSigla,
		pParGerUmedidaNome,pParGerUmedidaAtivo,pParGerUmedidaSigla,pParOcorStatusNome,pParOcorStatusAtivo,pParOcorStatusSigla,pParOcorStatusTipo,pParLogUserIns,
		pParLogUserUpd,pParLogDateInsIni,pParLogDateInsFin,pParLogDateUpdIni,pParLogDateUpdFin,pParUser
	   #Guia Dados Teste (Execução)
		pParUnit = f3996813-838e-49af-9649-8dc44e24bc75
		pParIndRelId = bd99ce86-c4fe-4e15-b844-6565bc08d0d6
		pVart01 = ope_centro2_nome
		pVard01 = Área
		pVart02 = ope_ocor_mov_numero
		pVard02 = Nº Movimento
		

## (OPE) - OCORRENCIAS - EQUIPAMENTOS
	  uuid: aaa91203-1662-4cb3-83e9-d1d337a88bc3
	  nome_tecnico: report0026OpeOcorMovDestEquip
	  parametros:pParUnitId,pParIndRelId,pParTitleReport,pVart01,pVard01,pVart02,pVard02,pVart03,pVard03,pVart04,pVard04,pVart05,pVard05,pParCentro1Nome,pParCentro1Sigla,
		pParCentro1Ativo,pParCentro2Nome,pParCentro2Ativo,pParCentro2Sigla,pParCentro2EquipTipoRodad,pParCentro2EquipTipoCarroc,pParCentro2EquipCid,
		pParCentro2EquipUf,pParCentro2EquipPlaca,pParCentro2EquipRenavam,pParCentro2EquipTara,pParCentro2EquipCapacidKg,pParCentro2EquipCapacidM3,
		pParCentro2EquipPotenc,pParCentro2EquipNrChassi,pParCentro2EquipNrSerie,pParCentro2EquipLiberadoAbastec,pParCentro2EquipNrRegisEstadual,
		pParCentro2EquipTipoTracao,pParCentro2EquipTranspAutoCarg,pParCompartNome,pParCompartAtivo,pParCompartSigla,pParCompartCapacid,pParCompartValidItemServ,
		pParCompartDtAquisicaoIni,pParCompartDtAquisicaoFin,pParCompartVrAquisicao,pParCompartNrSerie,pParOcorMovDataMovIni,pParOcorMovDataMovFin,pParOcorMovNr,
		pParGerEmpresaNome,pParGerEmpresaAtivo,pParGerEmpresaDocCnpj,pParGerEmpresaDocCpf,pParGerPessoaEnderecoLograd,pParGerPessoaEnderecoLogradNr,pParGerCidadeNome,
		pParUfNome,pParOcorTipoNome,pParOcorTipoAtivo,pParOcorTipoSigla,pParOcorTipoObrigCompart,pParOcorTipoTp,pParOcorMovDetQntOcor,pParOcorMovDetQntOcorCalc,
		pParOcorMovDetDtStatusIni,pParOcorMovDetDtStatusFin,pParOcorNome,pParOcorAtivo,pParOcorSigla,pParOcorTipo,pParOcorTipoLanc,pParOcorGrupoNome,pParOcorGrupoAtivo,
		pParOcorGrupoSigla,pParGerUmedidaNome,pParGerUmedidaAtivo,pParGerUmedidaSigla,pParOcorStatusNome,pParOcorStatusAtivo,pParOcorStatusSigla,pParOcorStatusTipo,
		pParLogUserIns,pParLogUserUpd,pParLogDateInsIni,pParLogDateInsFin,pParLogDateUpdIni,pParLogDateUpdFin,pParUser
	   #Guia Dados Teste (Execução)
		pParUnit = f3996813-838e-49af-9649-8dc44e24bc75
		pParIndRelId = aaa91203-1662-4cb3-83e9-d1d337a88bc3
		pVart01 = ope_centro2_nome
		pVard01 = Equipamento
		pVart02 = ope_ocor_mov_numero
		pVard02 = Nº Mov
	  
## (Varios) Reports List
	  - Para executar encode pParParams em Base64
      - nome_tecnico: reportlist.
      - parametros: pParUnitId, pParIndRelId, pParParams
## (GER) - EMPRESA
                pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
                pParIndRelId = c9b0c767-55de-4eaf-af26-14c76c731547
                pParParams = {%22params%22:[{%22parNomeTec%22:%22pParGerEmpresaId%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParGerEmpresaNome%22,%22parValor%22:%22Agro%20Petros%22},{%22parNomeTec%22:%22pParGerEmpresaSigla%22,%22parValor%22:%22%22},{%22parNomeTec%22:%22pParGerEmpresaAtivo%22,%22parValor%22:%22S%22},{%22parNomeTec%22:%22pParGerEmpresaDocCnpj%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParGerEmpresaDocCpf%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserIns%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserUpd%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsFin%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdFin%22,%22parValor%22:%22%%22}]}
				
## (FIN) - TIPO VARIAÇÃO
               pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
               pParIndRelId = 31e0bf5f-8cb4-4b03-91e2-ad3b464dd38e
               pParParams = {%22params%22:[{%22parNomeTec%22:%22pParFinTipoVariacaoId%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinTipoVariacaoNome%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinTipoVariacaoAtivo%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinTipoBaixa%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinTipoVariacaoVrPositivo%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserIns%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserUpd%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsFin%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdFin%22,%22parValor%22:%22%%22}]}
      

## (FIN) - LOTE
              pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
              pParIndRelId = bc0729af-2d4d-4d90-864a-413cda82adc1
              pParParams = {%22params%22:[{%22parNomeTec%22:%22pParFinLoteId%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinLoteNome%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinLoteDateIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinLoteDateFin%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserIns%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserUpd%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsFin%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdFin%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdIni%22,%22parValor%22:%22%%22}]}
    
## (FIN) - CONDIÇÃO DE PAGAMENTO
              pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
              pParIndRelId = d0037aa1-1260-4272-9d7c-6f73db3cb0a0
              pParParams =  {%22params%22:[{%22parNomeTec%22:%22pParFinCondPagRecId%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinCondPagRecNome%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinCondPagRecSigla%22,%22parValor%22:%22%22},{%22parNomeTec%22:%22pParFinCondPagRecAtivo%22,%22parValor%22:%22S%22},{%22parNomeTec%22:%22pParConsidFeriado%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParConsidFDS%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParTipoPrazo%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserIns%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserUpd%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsFin%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdFin%22,%22parValor%22:%22%%22}]}

## (FIN) - TIPO DOCUMENTO
              pParUnitId = f3996813-838e-49af-9649-8dc44e24bc75
              pParIndRelId = da7751b9-a905-4e89-8392-7490c66c5a93
              pParParams = {%22params%22:[{%22parNomeTec%22:%22pParFinDocTipoId%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinDocTipoNome%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinDocTipoAtivo%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParFinCondPagRecNDoc%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserIns%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogUserUpd%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateInsFin%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdIni%22,%22parValor%22:%22%%22},{%22parNomeTec%22:%22pParLogDateUpdFin%22,%22parValor%22:%22%%22}]}


# EXEMPLO - report

## FONTE DE DADOS
http://localhost:3001/v1/report/generator/generatorDataReport/U2FsdGVkX19t6cGtvPzWnBqXb2gFsWeTesgoyzE2VCI9yh0lNHNtj4%2BnsMAYPWELj13LJMqirX%2B1Li90cxertu4v3npK97Kn2M1QE1K6Ejzm5h8stVtvl4UFas3GGn9Oto6lNRf06q01ImpGiuz9tA%3D%3D?pParAtivo=N&pParGerCidadeNome=%


# CONFIGURAÇÃO PADRAO DOS RELATÓRIOS

## Fonte
```
    Fonte-Padrão: SansSerif
    Para Labels Master {
        Tamanho : 9
        h(eigth): 12px    
    }
    Para Labels Detail{
        Tamanho : 9
        h(eigth): 12px    
    }
    Para Labels SubDetail{
       LabelTitleDados:{
        Tamanho : 9
        h(eigth): 12px    
       }
       LabelDados:{
        Tamanho : 8
        h(eigth): 12px    
       }
    }
```


## Cabecalho: Landscape(Paisagem)
```
     Title:
       label-title:
         x: 0px
         y: 0px
         w(idth): 560px
         h(eigth): 20px
         Alinhamento: Esquerda

       label-usuario:
         x: 560px
         y: 0px
         w(idth): 232px
         h(eigth): 20px
         Alinhamento: Esquerda

     Detail:
       Parâmetros:
         x: 0px
         y: 10px
         w(idth): 792px
         h(eigth): 50px
         Alinhamento: Esquerda
```
## Cabecalho: Portrait(Retrato)
```
     Title:
       label-title:
         x: 0px
         y: 0px
         w(idth): 450px
         h(eigth): 20px
         Alinhamento: Esquerda

       label-usuario:
         x: 450px
         y: 0px
         w(idth): 145px
         h(eigth): 20px
         Alinhamento: Esquerda

     Detail:
       Parâmetros:
         x: 0px
         y: 10px
         w(idth): 595px
         h(eigth): 50px
         Alinhamento: Esquerda
```
## Rodapé: Landscape(Paisagem)
```
     Page-Footer:
       Image:
         x: 2px
         y: 4px
         w(idth): 23px
         h(eigth): 12px
       Name-Report:
         x: 25px
         y: 0px
         w(idth): 737px
         h(eigth): 18px
```
## Rodapé: Portrait(Retrato)
```
     Page-Footer:
       Image:
         x: 2px
         y: 4px
         w(idth): 23px
         h(eigth): 12px
       Name-Report:
         x: 25px
         y: 0px
         w(idth): 530px
         h(eigth): 18px
```		 

## Orientação: Portrait(Retrato)
```
     (Group Header): Configuração Primeira Banda Mestre(Pai)
        label 1:
          x: 0px
          y: 0px
          w(idth): 30px
          h(eigth): 12px
     
     (Group Header): Configuração Segunda Banda Detalhe(Filho)
        label 1:
          x: 10px
          y: 0px
          w(idth): 50px
          h(eigth): 12px

     (GroupHeaderBand): Se ouver uma terceira banda(Neto)
        label 1:
          x: 10px
          y: 0px
          w(idth): 50px
          h(eigth): 12px
     
     Data e Flags:
          Alinhamento: Centro
     
     Valores Numericos:
          Alinhamento: Direita
```		  