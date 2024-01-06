CREATE OR REPLACE FUNCTION public.fnreport0019(pparunitid character varying, pparindrelid character varying, pvart01 character varying, pvard01 character varying, pvart02 character varying DEFAULT NULL::character varying, pvard02 character varying DEFAULT NULL::character varying, pvart03 character varying DEFAULT NULL::character varying, pvard03 character varying DEFAULT NULL::character varying, pvart04 character varying DEFAULT NULL::character varying, pvard04 character varying DEFAULT NULL::character varying, pvart05 character varying DEFAULT NULL::character varying, pvard05 character varying DEFAULT NULL::character varying, pparorddestid character varying DEFAULT NULL::character varying, pparorddestqntprevobjini character varying DEFAULT NULL::character varying, pparorddestqntprevobjfin character varying DEFAULT NULL::character varying, pparorddestvrunitprevini character varying DEFAULT NULL::character varying, pparorddestvrunitprevfin character varying DEFAULT NULL::character varying, pparorddestvrtotprevini character varying DEFAULT NULL::character varying, pparorddestvrtotprevfin character varying DEFAULT NULL::character varying, pparorddestqntobjini character varying DEFAULT NULL::character varying, pparorddestqntobjfin character varying DEFAULT NULL::character varying, pparorddestvrunitini character varying DEFAULT NULL::character varying, pparorddestvrunitfin character varying DEFAULT NULL::character varying, pparorddestvrtotalini character varying DEFAULT NULL::character varying, pparorddestvrtotalfin character varying DEFAULT NULL::character varying, pparorddatainiexecini character varying DEFAULT NULL::character varying, pparorddatainiexecfin character varying DEFAULT NULL::character varying, pparorddatafinexecini character varying DEFAULT NULL::character varying, pparorddatafinexecfin character varying DEFAULT NULL::character varying, pparorddatastatusini character varying DEFAULT NULL::character varying, pparorddatastatusfin character varying DEFAULT NULL::character varying, pparorddatainiexecprevini character varying DEFAULT NULL::character varying, pparorddatainiexecprevfin character varying DEFAULT NULL::character varying, pparorddatafinexecprevini character varying DEFAULT NULL::character varying, pparorddatafinexecprevfin character varying DEFAULT NULL::character varying, pparcentro2id character varying DEFAULT NULL::character varying, pparcentro2nome character varying DEFAULT NULL::character varying, pparcentro2ativo character varying DEFAULT NULL::character varying, pparctbid character varying DEFAULT NULL::character varying, pparctbnome character varying DEFAULT NULL::character varying, pparctbativo character varying DEFAULT NULL::character varying, ppargerumedidaid character varying DEFAULT NULL::character varying, ppargerumedidanome character varying DEFAULT NULL::character varying, ppargerumedidaativo character varying DEFAULT NULL::character varying, pparcentro1id character varying DEFAULT NULL::character varying, pparcentro1nome character varying DEFAULT NULL::character varying, pparcentro1ativo character varying DEFAULT NULL::character varying, pparsubgrupoid character varying DEFAULT NULL::character varying, pparsubgruponome character varying DEFAULT NULL::character varying, pparsubgrupoativo character varying DEFAULT NULL::character varying, ppargrupoid character varying DEFAULT NULL::character varying, ppargruponome character varying DEFAULT NULL::character varying, ppargrupoativo character varying DEFAULT NULL::character varying, pparsubtipoid character varying DEFAULT NULL::character varying, pparsubtiponome character varying DEFAULT NULL::character varying, ppartipoid character varying DEFAULT NULL::character varying, ppartiponome character varying DEFAULT NULL::character varying, ppargerempresaid character varying DEFAULT NULL::character varying, ppargerempresanome character varying DEFAULT NULL::character varying, ppargerempresaativo character varying DEFAULT NULL::character varying, ppargerempresadoccnpj character varying DEFAULT NULL::character varying, ppargerempresadoccpf character varying DEFAULT NULL::character varying, pparperiodoid character varying DEFAULT NULL::character varying, pparperiodonome character varying DEFAULT NULL::character varying, pparperiodoativo character varying DEFAULT NULL::character varying, pparperiododataini character varying DEFAULT NULL::character varying, pparperiododatainifin character varying DEFAULT NULL::character varying, pparperiododatafinini character varying DEFAULT NULL::character varying, pparperiododatafin character varying DEFAULT NULL::character varying, pparcentro2pessoaid character varying DEFAULT NULL::character varying, pparcentro2pessoanome character varying DEFAULT NULL::character varying, ppargerpessoaenderecoid character varying DEFAULT NULL::character varying, ppargerpessoaenderecoativo character varying DEFAULT NULL::character varying, ppargerpessoaenderecotipo character varying DEFAULT NULL::character varying, ppargerpessoaenderecopadrao character varying DEFAULT NULL::character varying, ppargerpessoaenderecolograd character varying DEFAULT NULL::character varying, ppargerpessoaenderecologradnr character varying DEFAULT NULL::character varying, ppargerpessoaenderecologradbairro character varying DEFAULT NULL::character varying, ppargerpessoaid character varying DEFAULT NULL::character varying, ppargerpessoanome character varying DEFAULT NULL::character varying, ppargerpessoaativo character varying DEFAULT NULL::character varying, ppargerpessoadoc character varying DEFAULT NULL::character varying, pparordtipoid character varying DEFAULT NULL::character varying, pparordtiponome character varying DEFAULT NULL::character varying, pparordcentro2id character varying DEFAULT NULL::character varying, pparordcentro2nome character varying DEFAULT NULL::character varying, pparordcentro2ativo character varying DEFAULT NULL::character varying, pparfrentetrabalhoid character varying DEFAULT NULL::character varying, pparfrentetrabalhonome character varying DEFAULT NULL::character varying, pparfrentetrabalhoativo character varying DEFAULT NULL::character varying, pparstatusid character varying DEFAULT NULL::character varying, pparstatusnome character varying DEFAULT NULL::character varying, pparstatusativo character varying DEFAULT NULL::character varying, pparstatustipo character varying DEFAULT NULL::character varying, pparloguserins character varying DEFAULT NULL::character varying, pparlogdateinsini character varying DEFAULT NULL::character varying, pparlogdateinsfin character varying DEFAULT NULL::character varying, pparloguserupd character varying DEFAULT NULL::character varying, pparlogdateupdini character varying DEFAULT NULL::character varying, pparlogdateupdfin character varying DEFAULT NULL::character varying)
 RETURNS TABLE(ind_rel_id character varying, ind_rel_par1 character varying, ind_rel_par2 character varying, ind_rel_par3 character varying, ind_rel_par4 character varying, vart_01 character varying, vard_01 character varying, vart_02 character varying, vard_02 character varying, vart_03 character varying, vard_03 character varying, vart_04 character varying, vard_04 character varying, vart_05 character varying, vard_05 character varying, valor_01 numeric, valor_02 numeric, valor_03 numeric, valor_04 numeric, valor_05 numeric, valor_06 numeric, valor_07 numeric, valor_08 numeric, valor_09 numeric, valor_10 numeric)
 LANGUAGE plpgsql
AS $function$
       declare
       vSql varchar;
       vPar1 varchar :='';
       vPar2 varchar :='';
       vPar3 varchar :='';
       vPar4 varchar :='';
       r record;
       
       begin
           if  pParOrdDestQntPrevObjIni != '' and pParOrdDestQntPrevObjFin != '' then
             vPar1 := vPar1||'Qntd - Prevista - Objeto de ['||pParOrdDestQntPrevObjIni||'] até ['||pParOrdDestQntPrevObjFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Qntd - Prevista - Objeto de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestVrUnitPrevIni != '' and pParOrdDestVrUnitPrevFin != '' then
               vPar1 := vPar1 ||'Valor Unitário - Previsto de ['||pParOrdDestVrUnitPrevIni||'] até ['||pParOrdDestVrUnitPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1 ||'Valor Unitário - Previsto de [] até []'||chr(13)||chr(10);
           end if;
           if pParOrdDestVrTotPrevIni != '' and pParOrdDestVrTotPrevFin != '' then
               vPar1 := vPar1 ||'Valor Total - Previsto de ['||pParOrdDestVrTotPrevIni||'] até ['||pParOrdDestVrTotPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1 ||'Valor Total - Previsto de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestQntObjIni != '' and pParOrdDestQntObjFin != '' then
               vPar1 := vPar1 ||'Qntd - Real - Objeto de ['||pParOrdDestQntObjIni||'] até ['||pParOrdDestQntObjFin||']'||chr(13)||chr(10);
           else 
               vPar1 := vPar1||'Qntd - Real - Objeto de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestVrUnitIni != '' and pParOrdDestVrUnitFin != '' then
               vPar1 := vPar1||'Valor Unitário - Real de['||pParOrdDestVrUnitIni||'] até ['||pParOrdDestVrUnitFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Valor Unitário - Real de[] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDestVrTotalIni != '' and pParOrdDestVrTotalFin != '' then
               vPar1 := vPar1||'Valor Total - Real de ['||pParOrdDestVrTotalIni||'] até ['||pParOrdDestVrTotalFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Valor Total - Real de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataIniExecIni != '' and pParOrdDataIniExecFin != '' then
               vPar1 := vPar1||'Data Inicial Execução de ['||pParOrdDataIniExecIni||'] até ['||pParOrdDataIniExecFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Inicial Execução de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataFinExecIni != '' and pParOrdDataFinExecFin != '' then
               vPar1 := vPar1||'Data Final Execução de ['||pParOrdDataFinExecIni||'] até ['||pParOrdDataFinExecFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Final Execução de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataStatusIni != '' and pParOrdDataStatusFin != '' then
               vPar1 := vPar1||'Data Status de ['||pParOrdDataStatusIni||'] até ['||pParOrdDataStatusFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Status de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParOrdDataIniExecPrevIni != '' and pParOrdDataIniExecPrevFin != '' then
               vPar1 := vPar1||'Data Inicial Execução Prev de ['||pParOrdDataIniExecPrevIni||'] até ['||pParOrdDataIniExecPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Inicial Execução Prev de [] até []'||chr(13)||chr(10);
           end if;
       
           if pParOrdDataFinExecPrevIni != '' and pParOrdDataFinExecPrevFin != '' then
               vPar1 := vPar1||'Data Final Execução Prev de ['||pParOrdDataFinExecPrevIni||'] até ['||pParOrdDataFinExecPrevFin||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Data Final Execução Prev de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2Id != '' then
                   vPar1 := vPar1||'Centro 2 ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParCentro2Id||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Centro 2 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2Nome != '' then
               vPar1:= vPar1||'Nome Centro 2 ['||pParCentro2Nome||']'||chr(13)||chr(10);
           else
               vPar1:= vPar1||'Nome Centro 2 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2Ativo != '' then
               vPar1:= vPar1||'Centro 2 Ativo ['||pParCentro2Ativo||']'||chr(13)||chr(10);
           else 
               vPar1:= vPar1||'Centro 2 Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParCtbId != '' then
                   vPar1 := vPar1||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCtbId||'''')||'] '||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Componente Contábil []'||chr(13)||chr(10);
           end if;
           
           if pParCtbNome != '' then
               vPar1 := vPar1||'Nome Componente Contábil ['||pParCtbNome||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Nome Componente Contábil []'||chr(13)||chr(10);
           end if;
           
           if pParCtbAtivo != '' then
               vPar1 := vPar1||'Componente Contábil Ativo ['||pParCtbAtivo||']'||chr(13)||chr(10);
           else
               vPar1 := vPar1||'Componente Contábil Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaId != '' then
                   vPar2 := vPar2||'Unidade Medida ['||fnreport_sigla(pParUnitId,'ger_umedida','sigla_umedida','id',''''||pParGerUmedidaId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Unidade Medida []'||chr(13)||chr(10);
           end if;	
           
           if pParGerUmedidaNome != '' then
               vPar2 := vPar2||'Nome Unidade Medida ['||pParGerUmedidaNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Unidade Medida []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaAtivo != '' then
               vPar2 := vPar2||'Unidade Medida Ativo ['||pParGerUmedidaAtivo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Unidade Medida Ativo[]'||chr(13)||chr(10);
           end if;
           
           if pParCentro1Id != '' then
                   vPar2 := vPar2||'Centro 1 ['||fnreport_sigla(pParUnitId,'ope_centro1','sigla_centro1','id',''''||pParCentro1Id||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Centro 1 []'||chr(13)||chr(10);
           end if;
           
           if pParCentro1Nome != '' then
               vPar2 := vPar2||'Nome Centro 1 ['||pParCentro1Nome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Centro 1 []'||chr(13)||chr(10);
           end if;
       
           if pParCentro1Ativo != '' then
               vPar2 := vPar2||'Centro 1 Ativo ['||pParCentro1Ativo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Centro 1 Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParSubGrupoId != '' then
                   vPar2 := vPar2||'SubGrupo ['||fnreport_sigla(pParUnitId,'ope_centro_subgrupo','sigla_centro_subgrupo','id',''''||pParSubGrupoId||'''')||'] '||chr(13)||chr(10);
           else
                   vPar2 := vPar2||'SubGrupo []'||chr(13)||chr(10);
           end if;
           if pParSubGrupoNome != '' then
               vPar2 := vPar2||'Nome SubGrupo ['||pParSubGrupoNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome SubGrupo []'||chr(13)||chr(10);
           end if;
           
           if pParSubGrupoAtivo != '' then
               vPar2 := vPar2||'SubGrupo Ativo ['||pParSubGrupoAtivo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'SubGrupo Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGrupoId != '' then
               vPar2 := vPar2||'Grupo ['||fnreport_sigla(pParUnitId,'ope_centro_grupo','sigla_centro_grupo','id',''''||pParGrupoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Grupo []'||chr(13)||chr(10);
           end if;
           
           if pParGrupoNome != '' then
               vPar2 := vPar2||'Nome Grupo ['||pParGrupoNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Grupo []'||chr(13)||chr(10);
           end if;
           
           if pParGrupoAtivo != '' then
               vPar2 := vPar2||'Grupo Ativo ['||pParGrupoAtivo||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Grupo Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParSubTipoId != '' then
               vPar2 := vPar2||'SubTipo ['||fnreport_sigla(pParUnitId,'ope_centro_subtipo','nome','id',''''||pParSubTipoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'SubTipo []'||chr(13)||chr(10);	
           end if;
           
           if pParSubTipoNome != '' then
               vPar2 := vPar2||'Nome SubTipo ['||pParSubTipoNome||']'||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Nome SubTipo []'||chr(13)||chr(10);	
           end if;
           
           if pParTipoId != '' then
               vPar2 := vPar2||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro_tipo','nome','id',''''||pParTipoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParTipoNome != '' then
               vPar2 := vPar2||'Nome Tipo ['||pParTipoNome||']'||chr(13)||chr(10);	
           else
               vPar2 := vPar2||'Nome Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParGerEmpresaId != '' then
               vPar2 := vPar2||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||pParGerEmpresaId||'''')||'] '||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Empresa []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaNome != '' then
               vPar2 := vPar2||'Nome Empresa ['||pParGerEmpresaNome||']'||chr(13)||chr(10);
           else
               vPar2 := vPar2||'Nome Empresa []'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaAtivo != '' then
               vPar3 := vPar3||'Empresa Ativo['||pParGerEmpresaAtivo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Empresa Ativo[]'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCnpj != '' then
               vPar3 := vPar3||'Empresa Doc Cnpj['||pParGerEmpresaDocCnpj||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Empresa Doc Cnpj[]'||chr(13)||chr(10);
           end if;
           
           if pParGerEmpresaDocCpf != '' then
               vPar3 := vPar3||'Empresa Doc Cpf['||pParGerEmpresaDocCpf||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Empresa Doc Cpf[]'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoId != '' then
               vPar3 := vPar3||'Período ['||fnreport_sigla(pParUnitId,'ope_periodo','sigla_periodo','id',''''||pParPeriodoId||'''')||'] '||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Período []'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoNome != '' then
               vPar3 := vPar3||'Nome Período ['||pParPeriodoNome||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Nome Período []'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoAtivo != '' then
               vPar3 := vPar3||'Período Ativo['||pParPeriodoAtivo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Período Ativo[]'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoDataIni != '' and pParPeriodoDataIniFin != '' then
                vPar3 := vPar3||'Data Inicial Período de ['||pParPeriodoDataIni||'] até ['||pParPeriodoDataIniFin||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Data Inicial Período de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParPeriodoDataFinIni != '' and pParPeriodoDataFin !='' then
               vPar3 := vPar3||'Data Final Período de ['||pParPeriodoDataFinIni||'] até ['||pParPeriodoDataFin||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Data Final Período de [] até []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2PessoaId != '' then
               vPar3 := vPar3||'Centro 2 Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParCentro2PessoaId||'''')||'] '||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Centro 2 Pessoa []'||chr(13)||chr(10);
           end if;
           
           if pParCentro2PessoaNome != '' then
               vPar3 := vPar3||'Centro 2 Nome Pessoa ['||pParCentro2PessoaNome||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Centro 2 Nome Pessoa []'||chr(13)||chr(10);
           end if;
           
           if pParGerPessoaEnderecoAtivo != '' then
               vPar3 := vPar3||'Pessoa Endereco Ativo ['||pParGerPessoaEnderecoAtivo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Pessoa Endereco Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerPessoaEnderecoTipo != '' then
               vPar3 := vPar3||'Pessoa Endereco Tipo ['||pParGerPessoaEnderecoTipo||']'||chr(13)||chr(10);
           else
               vPar3 := vPar3||'Pessoa Endereco Tipo []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoPadrao != '' then
               vPar3 := vPar3||'Pessoa Endereco Padrão ['||pParGerPessoaEnderecoPadrao||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Endereco Padrão []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoLograd !='' then
               vPar3 := vPar3||'Pessoa Endereco Logradouro ['||pParGerPessoaEnderecoLograd||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Endereco Logradouro []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoLogradNr !='' then
               vPar3 := vPar3||'Pessoa Nº Endereco ['||pParGerPessoaEnderecoLogradNr||']'||chr(13)||chr(10);			
           else
               vPar3 := vPar3||'Pessoa Nº Endereco []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaEnderecoLogradBairro != '' then
               vPar3 := vPar3||'Pessoa Bairro ['||pParGerPessoaEnderecoLogradBairro||']'||chr(13)||chr(10);	
           else
               vPar3 := vPar3||'Pessoa Bairro []'||chr(13)||chr(10);	
           end if;
           
           if pParGerPessoaId != '' then
               vPar3 := vPar3||'Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParCentro2PessoaId||'''')||'] '||chr(13)||chr(10);		
           else
               vPar3 := vPar3||'Pessoa []'||chr(13)||chr(10);		
           end if;
           
           if pParGerPessoaNome != '' then
               vPar3 := vPar3||'Nome Pessoa ['||pParGerPessoaNome||']'||chr(13)||chr(10);		
           else
               vPar3 := vPar3||'Nome Pessoa []'||chr(13)||chr(10);		
           end if;
           
           if pParGerPessoaAtivo != '' then
               vPar4 := vPar4||'Pessoa Ativo ['||pParGerPessoaAtivo||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Pessoa Ativo []'||chr(13)||chr(10);		
           end if;
           
           if pParGerPessoaDoc != '' then
               vPar4 := vPar4||'Pessoa Doc ['||pParGerPessoaDoc||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Pessoa Doc []'||chr(13)||chr(10);
           end if;
           
           if pParOrdTipoId != '' then
               vPar4 := vPar4||'Tipo ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_tipo','sigla_ord_tipo','id',''''||pParOrdTipoId||'''')||'] '||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Tipo []'||chr(13)||chr(10);
           end if;
           
           if pParOrdTipoNome != '' then
               vPar4 := vPar4||'Nome Tipo ['||pParOrdTipoNome||']'||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Nome Tipo []'||chr(13)||chr(10);
           end if;
           
           
           if pParOrdCentro2Id != '' then
               vPar4 := vPar4||'Centro 2 Ord ['||fnreport_sigla(pParUnitId,'ope_centro2','sigla_centro2','id',''''||pParOrdCentro2Id||'''')||'] '||chr(13)||chr(10);				
           else
               vPar4 := vPar4||'Centro 2 Ord []'||chr(13)||chr(10);			
           end if;
           
           if pParOrdCentro2Nome != '' then
               vPar4 := vPar4||'Nome Centro 2 Ord ['||pParOrdCentro2Nome||']'||chr(13)||chr(10);				
           else
               vPar4 := vPar4||'Nome Centro 2 Ord []'||chr(13)||chr(10);			
           end if;
           
           
           if pParOrdCentro2Ativo != '' then
               vPar4 := vPar4||'Centro 2 Ord Ativo ['||pParOrdCentro2Ativo||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Centro 2 Ord Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParFrenteTrabalhoId != '' then
               vPar4 := vPar4||'Frente Trabalho ['||fnreport_sigla(pParUnitId,'ope_frente_trabalho','sigla_frente_trabalho','id',''''||pParFrenteTrabalhoId||'''')||'] '||chr(13)||chr(10);		
           else
               vPar4 := vPar4||'Frente Trabalho []'||chr(13)||chr(10);
           end if;
           
           if pParFrenteTrabalhoNome != '' then
               vPar4 := vPar4||'Nome Frente Trabalho ['||pParFrenteTrabalhoNome||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome Frente Trabalho []'||chr(13)||chr(10);
           end if;
       
           if pParFrenteTrabalhoAtivo != '' then
               vPar4 := vPar4||'Frente Trabalho Ativo['||pParFrenteTrabalhoAtivo||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Frente Trabalho Ativo[]'||chr(13)||chr(10);	
           end if;
           
           if pParStatusId != '' then
               vPar4 := vPar4||'Status ['||fnreport_sigla(pParUnitId,'ope_centro2_ord_status','sigla_ord_status','id',''''||pParStatusId||'''')||']'||chr(13)||chr(10);			
           else
               vPar4 := vPar4||'Status []'||chr(13)||chr(10);
           end if;
           
           if pParStatusNome != '' then
               vPar4 := vPar4||'Nome Status ['||pParStatusNome||']'||chr(13)||chr(10);
           else
               vPar4 := vPar4||'Nome Status []'||chr(13)||chr(10);	
           end if;
       
           if pParStatusAtivo != '' then
               vPar4 := vPar4||'Status Ativo ['||pParStatusAtivo||']'||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Status Ativo []'||chr(13)||chr(10);		
           end if;
       
           if pParStatusTipo != '' then
               vPar4 := vPar4||'Status Tipo ['||pParStatusTipo||']'||chr(13)||chr(10);	
           else
               vPar4 := vPar4||'Status Tipo []'||chr(13)||chr(10);	
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
                   ,sum(t1.ope_centro2_ord_dest_qnt_prev_obj)  as valor_01
                   ,sum(t1.ope_centro2_ord_dest_valor_unit_prev) as valor_02
                   ,sum(t1.ope_centro2_ord_dest_valor_total_prev) as valor_03
                   ,sum(t1.ope_centro2_ord_dest_qnt_obj) as valor_04
                   ,sum(t1.ope_centro2_ord_dest_valor_unit) as valor_05
                   ,sum(t1.ope_centro2_ord_dest_valor_total) as valor_06
               from vwope_centro2_ord_dest t1 
               where 1=1 ';
                   
               
               
           if pParUnitId != '' then
               vSql = vSql || ' and  t1.ope_centro2_ord_dest_unit_id in(''' ||pParUnitId||''')';
           end if;
           
           if pParOrdDestId != '' then
               vSql = vSql || ' and  t1.ope_centro2_ord_dest_id in(''' ||pParOrdDestId||''')';
           end if;
           
           if pParOrdDestQntPrevObjIni != '' and pParOrdDestQntPrevObjFin != '' then
               vSql = vSql ||' and t1.ope_centro2_ord_dest_qnt_prev_obj >= '''||pParOrdDestQntPrevObjIni||''''||
            ' and t1.ope_centro2_ord_dest_qnt_prev_obj  <= '''||pParOrdDestQntPrevObjFin||''''; 
           end if;
           
           if pParOrdDestVrUnitPrevIni != '' and pParOrdDestVrUnitPrevFin != '' then
                   vSql = vSql ||' and t1.ope_centro2_ord_dest_valor_unit_prev >= '''||pParOrdDestVrUnitPrevIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_unit_prev  <= '''||pParOrdDestVrUnitPrevFin||''''; 
           end if;
           
           if pParOrdDestVrTotPrevIni != '' and 	pParOrdDestVrTotPrevFin != '' then
                   vSql = vSql ||' and t1.ope_centro2_ord_dest_valor_total_prev >= '''||pParOrdDestVrTotPrevIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_total_prev  <= '''||pParOrdDestVrTotPrevFin||''''; 		
           end if;
       
           if pParOrdDestVrTotPrevIni != '' and 	pParOrdDestVrTotPrevFin != '' then
                   vSql = vSql ||' and t1.ope_centro2_ord_dest_valor_total_prev >= '''||pParOrdDestVrTotPrevIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_total_prev  <= '''||pParOrdDestVrTotPrevFin||''''; 		
           end if;
           
               
           if pParOrdDestQntObjIni != '' and 	pParOrdDestQntObjFin != '' then
                   vSql = vSql ||' and t1.ope_centro2_ord_dest_qnt_obj >= '''||pParOrdDestQntObjIni||''''||
            ' and t1.ope_centro2_ord_dest_qnt_obj  <= '''||pParOrdDestQntObjFin||''''; 		
           end if;
           
           if pParOrdDestVrUnitIni != '' and 	pParOrdDestVrUnitFin != '' then
               vSql = vSql ||' and t1.ope_centro2_ord_dest_valor_unit >= '''||pParOrdDestVrUnitIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_unit  <= '''||pParOrdDestVrUnitFin||''''; 		
           end if;
               
           if pParOrdDestVrTotalIni != '' and 	pParOrdDestVrTotalFin != '' then
               vSql = vSql ||' and t1.ope_centro2_ord_dest_valor_total >= '''||pParOrdDestVrTotalIni||''''||
            ' and t1.ope_centro2_ord_dest_valor_total  <= '''||pParOrdDestVrTotalFin||''''; 		
           end if;
           
           if pParOrdDataIniExecIni != '' and 	pParOrdDataIniExecFin != '' then
               vSql = vSql ||' and t1.ope_centro2_ord_data_ini_exec >= '''||pParOrdDataIniExecIni||''''||
            ' and t1.ope_centro2_ord_data_ini_exec  <= '''||pParOrdDataIniExecFin||''''; 		
           end if;
           
           if pParOrdDataFinExecIni != '' and 	pParOrdDataFinExecFin != '' then
               vSql = vSql ||' and t1.ope_centro2_ord_data_fin_exec >= '''||pParOrdDataFinExecIni||''''||
            ' and t1.ope_centro2_ord_data_fin_exec  <= '''||pParOrdDataFinExecFin||''''; 		
           end if;
           
           if pParOrdDataStatusIni != '' and 	pParOrdDataStatusFin != '' then
               vSql = vSql ||' and t1.ope_centro2_ord_data_status >= '''||pParOrdDataStatusIni||''''||
            ' and t1.ope_centro2_ord_data_status  <= '''||pParOrdDataStatusFin||''''; 		
           end if;
           
           if pParOrdDataIniExecPrevIni != '' and 	pParOrdDataIniExecPrevFin != '' then
               vSql = vSql ||' and t1.ope_centro2_ord_data_ini_exec_prev >= '''||pParOrdDataIniExecPrevIni||''''||
            ' and t1.ope_centro2_ord_data_ini_exec_prev  <= '''||pParOrdDataIniExecPrevFin||''''; 		
           end if;
           
           if pParOrdDataFinExecPrevIni != '' and 	pParOrdDataFinExecPrevFin != '' then
                vSql = vSql ||' and t1.ope_centro2_ord_data_fin_exec_prev >= '''||pParOrdDataFinExecPrevIni||''''||
            ' and t1.ope_centro2_ord_data_fin_exec_prev  <= '''||pParOrdDataFinExecPrevFin||''''; 		
           end if;	
           
           if pParCentro2Id != '' then
                   vSql = vSql || ' and  t1.ope_centro2_id in(''' ||pParCentro2Id||''')';
           end if;
           
           if pParCentro2Nome != '' then
                   vSql = vSql ||' and t1.ope_centro2_nome like'||'''%'||pParCentro2Nome||'%'' ';
           end if;
       
           if pParCentro2Ativo != '' then
                   vSql = vSql ||' and t1.ope_centro2_ativo_desc like'||'''%'||pParCentro2Ativo||'%'' ';
           end if;
           
           if pParCtbId != '' then
                   vSql = vSql || ' and  t1.ctb_id in(''' ||pParCtbId||''')';
           end if;
           
           if pParCtbNome != '' then
                   vSql = vSql ||' and t1.ctb_nome like'||'''%'||pParCtbNome||'%'' ';
           end if;
           
           if pParCtbAtivo != '' then
                   vSql = vSql ||' and t1.ctb_ativo_desc like'||'''%'||pParCtbAtivo||'%'' ';
           end if;
           
       
           if pParGerUmedidaId != '' then
                   vSql = vSql || ' and  t1.ger_umedida_id in(''' ||pParGerUmedidaId||''')';
           end if;
       
           if pParGerUmedidaNome != '' then
                   vSql = vSql ||' and t1.ger_umedida_nome like'||'''%'||pParGerUmedidaNome||'%'' ';
           end if;
           
           if pParGerUmedidaAtivo != '' then
                   vSql = vSql ||' and t1.ger_umedida_ativo_desc like'||'''%'||pParGerUmedidaAtivo||'%'' ';
           end if;
           
           if pParCentro1Id != '' then
                   vSql = vSql || ' and  t1.ope_centro1_id in(''' ||pParCentro1Id||''')';
           end if;	
           
           if pParCentro1Nome != '' then
                   vSql = vSql ||' and t1.ope_centro1_nome_dest like'||'''%'||pParCentro1Nome||'%'' ';
           end if;
       
           if pParCentro1Ativo != '' then
                   vSql = vSql ||' and t1.ope_centro1_ativo_desc like'||'''%'||pParCentro1Ativo||'%'' ';
           end if;
       
           if pParSubGrupoId != '' then
                   vSql = vSql || ' and  t1.ope_centro_subgrupo_id in(''' ||pParSubGrupoId||''')';
           end if;	
           
           if pParSubGrupoNome != '' then
                   vSql = vSql ||' and t1.ope_centro_subgrupo_nome like'||'''%'||pParSubGrupoNome||'%'' ';
           end if;
           
           if pParSubGrupoAtivo != '' then
                   vSql = vSql ||' and t1.ope_centro_subgrupo_ativo_desc like'||'''%'||pParSubGrupoAtivo||'%'' ';
           end if;
       
           if pParGrupoId != '' then
                   vSql = vSql || ' and  t1.ope_centro_grupo_id in(''' ||pParGrupoId||''')';
           end if;	
           
           if pParGrupoNome != '' then
                   vSql = vSql ||' and t1.ope_centro_grupo_nome like'||'''%'||pParGrupoNome||'%'' ';
           end if;
       
           if pParGrupoAtivo != '' then
                   vSql = vSql ||' and t1.ope_centro_grupo_ativo_desc like'||'''%'||pParGrupoAtivo||'%'' ';
           end if;
           
           if pParSubTipoId != '' then
                   vSql = vSql || ' and  t1.ope_centro_subtipo_id in(''' ||pParSubTipoId||''')';
           end if;	
           
           if pParSubTipoNome != '' then
                   vSql = vSql ||' and t1.ope_centro_subtipo_nome like'||'''%'||pParSubTipoNome||'%'' ';
           end if;	
       
           if pParTipoId != '' then
                   vSql = vSql || ' and  t1.ope_centro_tipo_id in(''' ||pParTipoId||''')';
           end if;	
           
           if pParTipoNome != '' then
                   vSql = vSql ||' and t1.ope_centro_tipo_nome like'||'''%'||pParTipoNome||'%'' ';
           end if;	
           
           if pParGerEmpresaId != '' then
                   vSql = vSql || ' and  t1.ger_empresa_id_ord in(''' ||pParGerEmpresaId||''')';
           end if;		
           
           if pParGerEmpresaNome != '' then
               vSql = vSql ||' and t1.ger_empresa_nome_ord like'||'''%'||pParGerEmpresaNome||'%'' ';
           end if;
           
           if pParGerEmpresaAtivo != '' then
               vSql = vSql ||' and t1.ger_empresa_ativo_ord_desc like'||'''%'||pParGerEmpresaAtivo||'%'' ';
           end if;
       
           if pParGerEmpresaDocCnpj != '' then
               vSql = vSql ||' and t1.ger_empresa_doc_cnpj_ord like'||'''%'||pParGerEmpresaDocCnpj||'%'' ';
           end if;
       
           if pParGerEmpresaDocCpf != '' then
               vSql = vSql ||' and t1.ger_empresa_doc_cpf_ord like'||'''%'||pParGerEmpresaDocCpf||'%'' ';
           end if;	
       
           if pParPeriodoId != '' then
                   vSql = vSql || ' and  t1.ope_periodo_id_ord in(''' ||pParPeriodoId||''')';
           end if;
           
           if pParPeriodoNome != '' then
               vSql = vSql||' and t1.ope_periodo_nome_ord like'||'''%'||pParPeriodoNome||'%'' ';
           end if;
           
           if pParPeriodoAtivo != '' then
               vSql = vSql||' and t1.ope_periodo_ativo_ord_desc like'||'''%'||pParPeriodoAtivo||'%'' ';
           end if;	
           
           if pParPeriodoDataIni != '' and pParPeriodoDataIniFin != '' then
                   vSql = vSql ||' and t1.ope_periodo_data_ini_ord >= '''||pParPeriodoDataIni||''''||
            ' and t1.ope_periodo_data_ini_ord  <= '''||pParPeriodoDataIniFin||''''; 
           end if;	
           
           if pParPeriodoDataFinIni != '' and pParPeriodoDataFin != '' then
                   vSql = vSql ||' and t1.ope_periodo_data_fin_ord >= '''||pParPeriodoDataFinIni||''''||
            ' and t1.ope_periodo_data_fin_ord  <= '''||pParPeriodoDataFin||''''; 
           end if;	
           
           if pParCentro2PessoaId != '' then
                   vSql = vSql || ' and  t1.ope_centro2_pessoa_id_ord in(''' ||pParCentro2PessoaId||''')';
           end if;
           
           if pParCentro2PessoaNome != '' then
               vSql = vSql||' and t1.ope_centro2_nome_pessoa_ord like'||'''%'||pParCentro2PessoaNome||'%'' ';
           end if;	
       
           if pParGerPessoaEnderecoId != '' then
                   vSql = vSql || ' and  t1.ger_pessoa_endereco_id_ord in(''' ||pParGerPessoaEnderecoId||''')';
           end if;
           
           if pParGerPessoaEnderecoAtivo != '' then
               vSql = vSql||' and t1.ger_pessoa_endereco_ativo_ord_desc like'||'''%'||pParGerPessoaEnderecoAtivo||'%'' ';
           end if;	
           
           if pParGerPessoaEnderecoTipo != '' then
               vSql = vSql||' and t1.ger_pessoa_endereco_tipo_ord like'||'''%'||pParGerPessoaEnderecoTipo||'%'' ';
           end if;		
           
           if pParGerPessoaEnderecoPadrao != '' then
               vSql = vSql||' and t1.ger_pessoa_endereco_padrao_ord like'||'''%'||pParGerPessoaEnderecoPadrao||'%'' ';
           end if;	
           
       
           if pParGerPessoaEnderecoLograd != '' then
               vSql = vSql||' and t1.ger_pessoa_endereco_end_logradouro_ord like'||'''%'||pParGerPessoaEnderecoLograd||'%'' ';
           end if;
           
           if pParGerPessoaEnderecoLogradNr != '' then
               vSql = vSql||' and t1.ger_pessoa_endereco_end_logradouro_nr_ord like'||'''%'||pParGerPessoaEnderecoLogradNr||'%'' ';
           end if;
           
           if pParGerPessoaEnderecoLogradBairro != '' then
               vSql = vSql||' and t1.ger_pessoa_endereco_end_bairro_ord like'||'''%'||pParGerPessoaEnderecoLogradBairro||'%'' ';
           end if;	
           
           if pParGerPessoaId != '' then
                   vSql = vSql || ' and  t1.ger_pessoa_id_ord in(''' ||pParGerPessoaId||''')';
           end if;	
           
           if pParGerPessoaNome != '' then
               vSql = vSql||' and t1.ger_pessoa_nome_ord like'||'''%'||pParGerPessoaNome||'%'' ';
           end if;
           
           if pParGerPessoaAtivo != '' then
                   vSql = vSql||' and t1.ger_pessoa_ativo_ord_desc like'||'''%'||pParGerPessoaAtivo||'%'' ';
           end if;	
           
           if pParGerPessoaDoc != '' then
                   vSql = vSql||' and t1.ger_pessoa_doc_cpf_cnpj_ord like'||'''%'||pParGerPessoaDoc||'%'' ';
           end if;	
       
           if pParOrdTipoId != '' then
                   vSql = vSql || ' and  t1.ope_centro2_ord_tipo_id_ord in(''' ||pParOrdTipoId||''')';
           end if;
       
           if pParOrdTipoNome != '' then
                   vSql = vSql||' and t1.ope_centro2_ord_tipo_nome_ord like'||'''%'||pParOrdTipoNome||'%'' ';
           end if;	
           
           if pParOrdCentro2Id != '' then
                   vSql = vSql || ' and  t1.ope_centro2_id_ord in(''' ||pParOrdCentro2Id||''')';
           end if;
           
           if pParOrdCentro2Nome != '' then
                   vSql = vSql||' and t1.ope_centro2_nome_ord like'||'''%'||pParOrdCentro2Nome||'%'' ';
           end if;	
           
           if pParOrdCentro2Ativo != '' then
                   vSql = vSql||' and t1.ope_centro2_ativo_desc_ord like'||'''%'||pParOrdCentro2Ativo||'%'' ';
           end if;
           
           if pParFrenteTrabalhoId != '' then
                   vSql = vSql || ' and  t1.ope_frente_trabalho_id_ord in(''' ||pParFrenteTrabalhoId||''')';
           end if;
           
           if pParFrenteTrabalhoNome != '' then
                   vSql = vSql||' and t1.ope_frente_trabalho_nome_ord like'||'''%'||pParFrenteTrabalhoNome||'%'' ';
           end if;	
           
           if pParFrenteTrabalhoAtivo != '' then
                   vSql = vSql||' and t1.ope_frente_trabalho_ativo_desc like'||'''%'||pParFrenteTrabalhoAtivo||'%'' ';
           end if;	
       
           if pParStatusId != '' then
                   vSql = vSql || ' and  t1.ope_centro2_ord_status_id_ord in(''' ||pParStatusId||''')';
           end if;
           
           if pParStatusNome != '' then
                   vSql = vSql||' and t1.ope_centro2_ord_status_nome_ord like'||'''%'||pParStatusNome||'%'' ';
           end if;	
           
           if pParStatusAtivo != '' then
                   vSql = vSql||' and t1.ope_centro2_ord_status_ativo_ord_desc like'||'''%'||pParStatusAtivo||'%'' ';
           end if;	
           
           if pParStatusTipo != '' then
                   vSql = vSql||' and t1.ope_centro2_tipo_status_ord like'||'''%'||pParStatusTipo||'%'' ';
           end if;
           
           if pParLogUserIns != '' then
                   vSql = vSql || ' and t1.log_user_ins like '|| '''%' ||pParLogUserIns|| '%'' ';
           end if;
               
               if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
                 vSql = vSql || ' and CAST(t1.log_date_ins AS DATE)' || ' >= ''' || pParLogDateInsIni|| '''' || ' and  CAST(t1.log_date_ins AS DATE)' || ' <= ''' || pParLogDateInsFin || '''';
               end if;
               
               if pParLogUserUpd != '' then
                   vSql = vSql || ' and  t1.log_user_upd like '|| '''%' ||pParLogUserUpd|| '%'' ';
               end if;		
       
               if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
                 vSql = vSql || ' and CAST(t1.log_date_upd AS DATE)' || ' >= ''' || pParLogDateUpdIni|| '''' || ' and  CAST(t1.log_date_upd AS DATE)' || ' <= ''' || pParLogDateUpdFin || '''';
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
               valor_06 := r.valor_06;
       
           RETURN NEXT;
           
           END loop;
       raise notice 'SQl:% ',vSql; 
       end;
       $function$
;
