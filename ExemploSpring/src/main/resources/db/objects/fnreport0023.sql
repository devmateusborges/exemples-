CREATE OR REPLACE FUNCTION public.fnreport0023(pparunitid character varying, pparindrelid character varying, pvart01 character varying, pvard01 character varying, pvart02 character varying DEFAULT NULL::character varying, pvard02 character varying DEFAULT NULL::character varying, pvart03 character varying DEFAULT NULL::character varying, pvard03 character varying DEFAULT NULL::character varying, pvart04 character varying DEFAULT NULL::character varying, pvard04 character varying DEFAULT NULL::character varying, pvart05 character varying DEFAULT NULL::character varying, pvard05 character varying DEFAULT NULL::character varying, pvart06 character varying DEFAULT NULL::character varying, pvard06 character varying DEFAULT NULL::character varying, pvart07 character varying DEFAULT NULL::character varying, pvard07 character varying DEFAULT NULL::character varying, pvart08 character varying DEFAULT NULL::character varying, pvard08 character varying DEFAULT NULL::character varying, pvart09 character varying DEFAULT NULL::character varying, pvard09 character varying DEFAULT NULL::character varying, pvart10 character varying DEFAULT NULL::character varying, pvard10 character varying DEFAULT NULL::character varying, pparmovid character varying DEFAULT NULL::character varying, pparmovserie character varying DEFAULT NULL::character varying, ppardatamovini character varying DEFAULT NULL::character varying, ppardatamovfin character varying DEFAULT NULL::character varying, pparnrmov character varying DEFAULT NULL::character varying, ppardataentregamovini character varying DEFAULT NULL::character varying, ppardataentregamovfin character varying DEFAULT NULL::character varying, pparmovoperacaoid character varying DEFAULT NULL::character varying, pparmovoperacaonome character varying DEFAULT NULL::character varying, pparmovoperacaoativo character varying DEFAULT NULL::character varying, pparmovoperacaosigla character varying DEFAULT NULL::character varying, pparmovoperacaotipoes character varying DEFAULT NULL::character varying, pparmovtipoid character varying DEFAULT NULL::character varying, pparmovtiponome character varying DEFAULT NULL::character varying, pparmovtipoativo character varying DEFAULT NULL::character varying, pparmovtiposigla character varying DEFAULT NULL::character varying, pparmovtipomov character varying DEFAULT NULL::character varying, ppargernumeracaoid character varying DEFAULT NULL::character varying, ppargernumeracaonome character varying DEFAULT NULL::character varying, ppargernumeracaoativo character varying DEFAULT NULL::character varying, ppargernumeracaoserie character varying DEFAULT NULL::character varying, pparmovstatusid character varying DEFAULT NULL::character varying, pparmovstatusnome character varying DEFAULT NULL::character varying, pparmovstatusativo character varying DEFAULT NULL::character varying, pparmovstatussigla character varying DEFAULT NULL::character varying, pparmovstatustipo character varying DEFAULT NULL::character varying, ppargerempresaid character varying DEFAULT NULL::character varying, ppargerempresanome character varying DEFAULT NULL::character varying, ppargerempresaativo character varying DEFAULT NULL::character varying, ppargerempresasigla character varying DEFAULT NULL::character varying, ppargerpessoaid character varying DEFAULT NULL::character varying, ppargerpessoanome character varying DEFAULT NULL::character varying, ppargerpessoaativo character varying DEFAULT NULL::character varying, ppargerpessoasigla character varying DEFAULT NULL::character varying, ppargerpessoaenderecoativo character varying DEFAULT NULL::character varying, ppargerpessoaenderecolograd character varying DEFAULT NULL::character varying, ppargerpessoaenderecologradnr character varying DEFAULT NULL::character varying, ppargerpessoaenderecologradbairro character varying DEFAULT NULL::character varying, ppargerpessoaentregid character varying DEFAULT NULL::character varying, ppargerpessoaentregnome character varying DEFAULT NULL::character varying, ppargerpessoaentregativo character varying DEFAULT NULL::character varying, ppargerpessoaentregenderecoativo character varying DEFAULT NULL::character varying, ppargerpessoaentregenderecolograd character varying DEFAULT NULL::character varying, ppargerpessoaentregenderecologradnr character varying DEFAULT NULL::character varying, ppargerpessoaentregenderecologradbairro character varying DEFAULT NULL::character varying, pparmovitemservid character varying DEFAULT NULL::character varying, pparitemservid character varying DEFAULT NULL::character varying, pparitemservnome character varying DEFAULT NULL::character varying, pparitemservativo character varying DEFAULT NULL::character varying, pparitemservsigla character varying DEFAULT NULL::character varying, pparitemservtipo character varying DEFAULT NULL::character varying, pparitemservsubgrupoid character varying DEFAULT NULL::character varying, pparitemservsubgruponome character varying DEFAULT NULL::character varying, pparitemservsubgrupoativo character varying DEFAULT NULL::character varying, pparitemservgrupoid character varying DEFAULT NULL::character varying, pparitemservgruponome character varying DEFAULT NULL::character varying, pparitemservgrupoativo character varying DEFAULT NULL::character varying, ppargerumedidaid character varying DEFAULT NULL::character varying, ppargerumedidanome character varying DEFAULT NULL::character varying, ppargerumedidaativo character varying DEFAULT NULL::character varying, ppargerumedidasigla character varying DEFAULT NULL::character varying, pparfiscfopid character varying DEFAULT NULL::character varying, pparfiscfopnr character varying DEFAULT NULL::character varying, pparfiscfopnome character varying DEFAULT NULL::character varying, pparfiscfopativo character varying DEFAULT NULL::character varying, pparfiscfopdatavalidini character varying DEFAULT NULL::character varying, pparfiscfopdatavalidfin character varying DEFAULT NULL::character varying, pparloguserins character varying DEFAULT NULL::character varying, pparlogdateinsini character varying DEFAULT NULL::character varying, pparlogdateinsfin character varying DEFAULT NULL::character varying, pparloguserupd character varying DEFAULT NULL::character varying, pparlogdateupdini character varying DEFAULT NULL::character varying, pparlogdateupdfin character varying DEFAULT NULL::character varying)
 RETURNS TABLE(ind_rel_id character varying, ind_rel_par1 character varying, ind_rel_par2 character varying, ind_rel_par3 character varying, ind_rel_par4 character varying, vart_01 character varying, vard_01 character varying, vart_02 character varying, vard_02 character varying, vart_03 character varying, vard_03 character varying, vart_04 character varying, vard_04 character varying, vart_05 character varying, vard_05 character varying, vart_06 character varying, vard_06 character varying, vart_07 character varying, vard_07 character varying, vart_08 character varying, vard_08 character varying, vart_09 character varying, vard_09 character varying, vart_10 character varying, vard_10 character varying, valor_01 numeric, valor_02 numeric, valor_03 numeric, valor_04 numeric, valor_05 numeric, valor_06 numeric, valor_07 numeric, valor_08 numeric, valor_09 numeric, valor_10 numeric, valor_11 numeric, valor_12 numeric, valor_13 numeric, valor_14 numeric, valor_15 numeric, valor_16 numeric, valor_17 numeric, valor_18 numeric)
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
       
       
       
           if pParMovSerie != '' then
               vPar1 = vPar1||'Serie do Movimento ['||pParMovSerie||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Serie do Movimento [] '||chr(13)||chr(10);
           end if;
       
       
           if pParDataMovIni != '' and pParDataMovFin != '' then
               vPar1 := vPar1 || 'Data do Movimento de ['||pParDataMovIni||'] até ['||pParDataMovFin||']'|| chr(13) || chr(10);
           else
               vPar1 := vPar1 || 'Data do Movimento de [] até []'|| chr(13) || chr(10);	
           end if;
       
       
           if pParNrMov != '' then
               vPar1 := vPar1 ||'Nº do Movimento ['||pParNrMov||']'|| chr(13) || chr(10);
           else
               vPar1 := vPar1 ||'Nº do Movimento []'|| chr(13) || chr(10);	
           end if;
       
       
           if pParDataEntregaMovIni != '' and  pParDataEntregaMovFin != '' then
               vPar1 := vPar1 || 'Data Entrega do Movimento de ['||pParDataEntregaMovIni||'] até ['||pParDataEntregaMovFin||']'|| chr(13) || chr(10);
           else
               vPar1 := vPar1 || 'Data Entrega do Movimento de [] até []'|| chr(13) || chr(10);
           end if;
       
       
           if pParMovOperacaoId != '' then
               vPar1 = vPar1||'Operação do Movimento ['||fnreport_sigla(pParUnitId,'mov_operacao','sigla_mov_operacao','id',''''||pParMovOperacaoId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Operação do Movimento []'||chr(13)||chr(10);				
           end if;
       
           if pParMovOperacaoNome != '' then
               vPar1 = vPar1||'Nome Operação do Movimento ['||pParMovOperacaoNome||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Nome Operação do Movimento [] '||chr(13)||chr(10);
           end if;
       
           if pParMovOperacaoAtivo != '' then
               vPar1 = vPar1||'Operação do Movimento Ativo ['||pParMovOperacaoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Operação do Movimento Ativo [] '||chr(13)||chr(10);
           end if;
       
           if pParMovOperacaoSigla != '' then
               vPar1 = vPar1||'Sigla Operação do Movimento ['||pParMovOperacaoSigla||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Sigla Operação do Movimento [] '||chr(13)||chr(10);
           end if;
               
           if pParMovOperacaoTipoES != '' then
               vPar1 = vPar1||'Operação do Movimento Tipo E/S ['||pParMovOperacaoTipoES||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Operação do Movimento Tipo E/S [] '||chr(13)||chr(10);
           end if;	
            
       
           if pParMovTipoId != '' then
               vPar1 = vPar1||'Tipo de Movimento ['||fnreport_sigla(pParUnitId,'mov_tipo','sigla_mov_tipo','id',''''||pParMovTipoId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Tipo de Movimento []'||chr(13)||chr(10);	
           end if;
       
       
           if pParMovTipoNome != '' then
                   vPar1 = vPar1||'Nome Tipo de Movimento ['||pParMovTipoNome||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Nome Tipo de Movimento [] '||chr(13)||chr(10);		
           end if;
       
           if pParMovTipoAtivo != '' then
                   vPar1 = vPar1||'Tipo de Movimento Ativo ['||pParMovTipoAtivo||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Tipo de Movimento Ativo[] '||chr(13)||chr(10);	
           end if;
           
           if pParMovTipoSigla != '' then
                   vPar1 = vPar1||'Sigla Tipo de Movimento ['||pParMovTipoSigla||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Sigla Tipo de Movimento [] '||chr(13)||chr(10);	
           end if;	
           
           if pParMovTipoMov != '' then
                   vPar1 = vPar1||'Tipo do Movimento ['||pParMovTipoMov||'] '||chr(13)||chr(10);	
           else
                   vPar1 = vPar1||'Tipo do Movimento [] '||chr(13)||chr(10);	
           end if;	
           
           if pParGerNumeracaoId != '' then
               vPar1 = vPar1||'Numeração ['||fnreport_sigla(pParUnitId,'ger_numeracao','nome','id',''''||pParGerNumeracaoId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Numeração []'||chr(13)||chr(10);
           end if;	
           
           if pParGerNumeracaoNome != '' then
               vPar1 = vPar1||'Nome da Numeração ['||pParGerNumeracaoNome||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Nome da Numeração []'||chr(13)||chr(10);
           end if;		
       
           if pParGerNumeracaoAtivo != '' then
               vPar1 = vPar1||'Numeração Ativo ['||pParGerNumeracaoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar1 = vPar1||'Numeração Ativo[]'||chr(13)||chr(10);
           end if;	
       
           if pParGerNumeracaoSerie != '' then
               vPar2 = vPar2||'Série Numeração ['||pParGerNumeracaoSerie||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Série Numeração []'||chr(13)||chr(10);
           end if;	
       
           if pParMovStatusId != '' then
               vPar2 = vPar2||'Status da Movimentação ['||fnreport_sigla(pParUnitId,'mov_status','sigla_mov_status','id',''''||pParMovStatusId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Status da Movimentação []'||chr(13)||chr(10);
           end if;	
           
           if pParMovStatusNome != '' then
               vPar2 = vPar2||'Nome Status da Movimentação ['||pParMovStatusNome||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Nome Status da Movimentação []'||chr(13)||chr(10);
           end if;	
           
           if pParMovStatusAtivo != '' then
               vPar2 = vPar2||'Status da Movimentação Ativo ['||pParMovStatusAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Status da Movimentação Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParMovStatusSigla != '' then
               vPar2 = vPar2||'Sigla Status da Movimentação ['||pParMovStatusSigla||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Sigla Status da Movimentação []'||chr(13)||chr(10);
           end if;
       
           if pParMovStatusTipo != '' then
               vPar2 = vPar2||'Tipo Status da Movimentação ['||pParMovStatusTipo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Tipo Status da Movimentação []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaId != '' then
               vPar2 = vPar2||'Empresa ['||fnreport_sigla(pParUnitId,'ger_empresa','sigla_empresa','id',''''||pParGerEmpresaId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Empresa []'||chr(13)||chr(10);
           end if;	
       
           if pParGerEmpresaNome != '' then
               vPar2 = vPar2||'Nome Empresa ['||pParGerEmpresaNome||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Nome Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaAtivo != '' then
               vPar2 = vPar2||'Empresa Ativo ['||pParGerEmpresaAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Empresa Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerEmpresaSigla != '' then
               vPar2 = vPar2||'Sigla Empresa ['||pParGerEmpresaSigla||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Sigla Empresa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaId != '' then
               vPar2 = vPar2||'Pessoa ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParGerPessoaId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Pessoa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaNome != ''  then
               vPar2 = vPar2||'Nome Pessoa ['||pParGerPessoaNome||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Nome Pessoa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaAtivo != ''  then
               vPar2 = vPar2||'Pessoa Ativo ['||pParGerPessoaAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Pessoa Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaSigla != ''  then
               vPar2 = vPar2||'Sigla Pessoa ['||pParGerPessoaSigla||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Sigla Pessoa []'||chr(13)||chr(10);
           end if;
           
               
           if pParGerPessoaEnderecoAtivo != ''  then
               vPar2 = vPar2||'Endereço Pessoa Ativo ['||pParGerPessoaEnderecoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Endereço Pessoa Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLograd != ''  then
               vPar2 = vPar2||'Endereço Pessoa Logradouro ['||pParGerPessoaEnderecoLograd||'] '||chr(13)||chr(10);			
           else
               vPar2 = vPar2||'Endereço Pessoa Logradouro []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLogradNr != ''  then
               vPar3 = vPar3||'Nº Endereço Pessoa ['||pParGerPessoaEnderecoLogradNr||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nº Endereço Pessoa []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEnderecoLogradBairro != ''  then
               vPar3 = vPar3||'Bairro Endereço Pessoa ['||pParGerPessoaEnderecoLogradBairro||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Bairro Endereço Pessoa []'||chr(13)||chr(10);
           end if;	
           
           if pParGerPessoaEntregId != '' then
               vPar3 = vPar3||'Pessoa Entrega ['||fnreport_sigla(pParUnitId,'ger_pessoa','sigla_pes','id',''''||pParGerPessoaEntregId||'''' ) ||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Pessoa Entrega []'||chr(13)||chr(10);
           end if;		
       
           if pParGerPessoaEntregNome != ''  then
               vPar3 = vPar3||'Nome Pessoa Entrega ['||pParGerPessoaEntregNome||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nome Pessoa Entrega []'||chr(13)||chr(10);
           end if;	
       
           if pParGerPessoaEntregAtivo != ''  then
               vPar3 = vPar3||'Pessoa Entrega Ativo ['||pParGerPessoaEntregAtivo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Pessoa Entrega Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEntregEnderecoAtivo != ''  then
               vPar3 = vPar3||'Endereço Pessoa Entrega Ativo ['||pParGerPessoaEntregEnderecoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Endereço Pessoa Entrega Ativo []'||chr(13)||chr(10);
           end if;
           
           if pParGerPessoaEntregEnderecoLograd != ''  then
               vPar3 = vPar3||'Endereço Pessoa Entrega Logradouro ['||pParGerPessoaEntregEnderecoLograd||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Endereço Pessoa Entrega Logradouro []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEntregEnderecoLogradNr != ''  then
               vPar3 = vPar3||'Nº Endereço Pessoa Entrega ['||pParGerPessoaEntregEnderecoLogradNr||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nº Endereço Pessoa Entrega []'||chr(13)||chr(10);
           end if;
       
           if pParGerPessoaEntregEnderecoLogradBairro != ''  then
               vPar3 = vPar3||'Bairro Endereço Pessoa Entrega ['||pParGerPessoaEntregEnderecoLogradBairro||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Bairro Endereço Pessoa Entrega []'||chr(13)||chr(10);
           end if;
       
           if pParItemServId != '' then
               vPar3 = vPar3||'Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv','sigla_itemserv','id',''''||pParItemServId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar3 = vPar3||'Item/Serviço []'||chr(13)||chr(10);
           end if;	
       
           if pParItemServNome != ''  then
               vPar3 = vPar3||'Nome Item/Serviço ['||pParItemServNome||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nome Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServAtivo != ''  then
               vPar3 = vPar3||'Item/Serviço Ativo ['||pParItemServAtivo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Item/Serviço Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParItemServSigla != ''  then
               vPar3 = vPar3||'Sigla Item/Serviço ['||pParItemServSigla||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Sigla Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServTipo != ''  then
               vPar3 = vPar3||'Tipo Item/Serviço ['||pParItemServTipo||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Tipo Item/Serviço []'||chr(13)||chr(10);
           end if;
           if pParItemServSubGrupoId != '' then
               vPar3 = vPar3||'SubGrupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_subgrupo','nome','id',''''||pParItemServSubGrupoId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar3 = vPar3||'SubGrupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServSubGrupoNome != ''  then
               vPar3 = vPar3||'Nome SubGrupo Item/Serviço ['||pParItemServSubGrupoNome||'] '||chr(13)||chr(10);			
           else
               vPar3 = vPar3||'Nome SubGrupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServSubGrupoAtivo != ''  then
               vPar4 = vPar4||'SubGrupo Item/Serviço Ativo ['||pParItemServSubGrupoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'SubGrupo Item/Serviço Ativo []'||chr(13)||chr(10);
           end if;
       
       
           if pParItemServGrupoId != '' then
               vPar4 = vPar4||'Grupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_grupo','nome','id',''''||pParItemServGrupoId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Grupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServGrupoNome != ''  then
               vPar4 = vPar4||'Nome Grupo Item/Serviço ['||pParItemServGrupoNome||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nome Grupo Item/Serviço []'||chr(13)||chr(10);
           end if;
       
           if pParItemServGrupoAtivo != ''  then
               vPar4 = vPar4||'Grupo Item/Serviço Ativo ['||pParItemServGrupoAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Grupo Item/Serviço Ativo []'||chr(13)||chr(10);
           end if;
       
           if pParGerUmedidaId != '' then
               vPar4 = vPar4||'Unidade de Medida ['||fnreport_sigla(pParUnitId,'ger_umedida','sigla_umedida','id',''''||pParGerUmedidaId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Unidade de Medida []'||chr(13)||chr(10);
           end if;
           
           if pParGerUmedidaNome != '' then
               vPar4 = vPar4||'Nome Unidade de Medida ['||pParGerUmedidaNome||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nome Unidade de Medida []'||chr(13)||chr(10);
           end if;	
       
           if pParGerUmedidaAtivo != '' then
               vPar4 = vPar4||'Unidade de Medida Ativo ['||pParGerUmedidaAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Unidade de Medida Ativo []'||chr(13)||chr(10);
           end if;	
       
           if pParGerUmedidaSigla != '' then
               vPar4 = vPar4||'Sigla Unidade de Medida ['||pParGerUmedidaSigla||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Sigla Unidade de Medida []'||chr(13)||chr(10);
           end if;
       
           if pParFisCfopId != '' then
               vPar4 = vPar4||'Cfop ['||fnreport_sigla(pParUnitId,'fis_cfop','nome','id',''''||pParFisCfopId||'''' ) ||'] '||chr(13)||chr(10);
           else
               vPar4 = vPar4||'Cfop []'||chr(13)||chr(10);
           end if;
       
           if pParFisCfopNR != '' then
               vPar4 = vPar4||'Nº Cfop ['||pParFisCfopNR||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nº Cfop []'||chr(13)||chr(10);
           end if;
       
           if pParFisCfopNome != '' then
               vPar4 = vPar4||'Nome Cfop ['||pParFisCfopNome||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Nome Cfop []'||chr(13)||chr(10);
           end if;
           
           if pParFisCfopAtivo != '' then
               vPar4 = vPar4||'Cfop Ativo ['||pParFisCfopAtivo||'] '||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Cfop Ativo []'||chr(13)||chr(10);
           end if;
       
       
           if pParFisCfopDataValidIni != '' and  pParFisCfopDataValidFin != '' then
               vPar4 = vPar4||'Data Validade Cfop de ['||pParFisCfopDataValidIni||'] até ['||pParFisCfopDataValidFin||']'||chr(13)||chr(10);			
           else
               vPar4 = vPar4||'Data Validade Cfop de [] até []'||chr(13)||chr(10);
           end if;
       
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
               
               if  pVart06 != ''  THEN
                vSql = vSql || ','  || pVart06 ||'   as vart_06 '||
                          ','''|| pVard06 ||''' as vard_06 ';
               else 
                  vSql = vSql || ',null as vart_06'||
                                      ',null as vard_06';
               end if;
       
               if  pVart07 != ''  THEN
                vSql = vSql || ','  || pVart07 ||'   as vart_07 '||
                          ','''|| pVard07 ||''' as vard_07 ';
               else 
                  vSql = vSql || ',null as vart_07'||
                                      ',null as vard_07';
               end if;
               
               if  pVart08 != ''  THEN
                vSql = vSql || ','  || pVart08 ||'   as vart_08 '||
                          ','''|| pVard08 ||''' as vard_08 ';
               else 
                  vSql = vSql || ',null as vart_08'||
                                      ',null as vard_08';
               end if;
       
               if  pVart09 != ''  THEN
                vSql = vSql || ','  || pVart09 ||'   as vart_09 '||
                          ','''|| pVard09 ||''' as vard_09 ';
               else 
                  vSql = vSql || ',null as vart_09'||
                                      ',null as vard_09';
               end if;
       
       --- 
               if  pVart10 != ''  THEN
                vSql = vSql || ','  || pVart10 ||'   as vart_10 '||
                          ','''|| pVard10 ||''' as vard_10 ';
               else 
                  vSql = vSql || ',null as vart_10'||
                                      ',null as vard_10';
               end if;
       
               vSql = vSql ||',
                   sum(t1.mov_itemserv_qnt_devolvida) as valor_01,
                   sum(t1.mov_itemserv_qnt_orig) as valor_02,
                   t1.mov_itemserv_valor_unit_orig as valor_03,
                   sum(t1.mov_itemserv_valor_bruto) as valor_04,
                   sum(t1.mov_itemserv_valor_liquido) as valor_05,
                   sum(t1.mov_itemserv_qnt_conv) as valor_06,
                   t1.mov_itemserv_valor_unit_conv as valor_07,
                   sum(t1.mov_itemserv_valor_desconto) as valor_08,
                   sum(t1.mov_itemserv_valor_acrecimo) as valor_09,
                   sum(t1.mov_itemserv_valor_outros) as valor_10,
                   sum(t1.mov_itemserv_valor_frete) as valor_11,
                   sum(t1.mov_itemserv_valor_seguro) as valor_12,
                   sum(t1.mov_itemserv_valor_tributo_retido) as valor_13,
                   sum(t1.mov_itemserv_valor_tributo_total) as valor_14,
                   sum(t1.mov_itemserv_valor_outros_tributo_ret) as valor_15,
                   sum(t1.mov_itemserv_valor_desconto_cond) as valor_16,
                   sum(t1.mov_itemserv_valor_desconto_incond) as valor_17,
                   sum(t1.mov_itemserv_valor_deducao) as valor_18
                   from vwmov_mov_itemserv t1 
                   inner join vwmov_mov t2
                   on t1.mov_id = t2.mov_id
                   where 1=1 ';
                   
                   
                   
               IF pParUnitId != '' THEN
                   vSql = vSql || 'and ' || ' t1.mov_itemserv_unit_id' || ' in(''' ||pParUnitId||''')';
               END IF;
       
               IF pParMovId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_id ' || ' in(''' ||pParMovId||''')';		
               END IF;
               
               IF pParMovSerie != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_serie_mov ' ||' like'||'''%'||pParMovSerie||'%'' ';
               END IF;
               
               IF pParDataMovIni != '' and pParDataMovFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t2.mov_data_mov AS DATE)' || ' >= ''' || pParDataMovIni|| '''' || ' and  CAST(t2.mov_data_mov AS DATE)' || ' <= ''' || pParDataMovFin || '''';	
               END IF;
       
               IF pParNrMov != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_numero_mov ' ||' = '||''||pParNrMov||'';
               END IF;
       
               IF pParDataEntregaMovIni != '' and pParDataEntregaMovFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t2.mov_data_entrega AS DATE)' || ' >= ''' || pParDataEntregaMovIni|| '''' || ' and  CAST(t2.mov_data_entrega AS DATE)' || ' <= ''' || pParDataEntregaMovFin || '''';
               END IF;
       
               IF pParMovOperacaoId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_operacao_id ' || ' in(''' ||pParMovOperacaoId||''')';	
               END IF;
       
               IF pParMovOperacaoNome != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_nome'||' like'||'''%'||pParMovOperacaoNome||'%'' ';
               END IF;
       
               IF pParMovOperacaoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_ativo'||' like'||'''%'||pParMovOperacaoAtivo||'%'' ';
               END IF;
       
               IF pParMovOperacaoSigla != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_sigla'||' like'||'''%'||pParMovOperacaoSigla||'%'' ';
               END IF;
       
               IF pParMovOperacaoTipoES != '' THEN
                   vSql = vSql ||' and '||'t2.mov_operacao_tipo_es'||' like'||'''%'||pParMovOperacaoTipoES||'%'' ';
               END IF;
               
               IF pParMovTipoId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_tipo_id ' || ' in(''' ||pParMovTipoId||''')';
               END IF;		
               
               IF pParMovTipoNome != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_nome'||' like'||'''%'||pParMovTipoNome||'%'' ';
               END IF;		
           
               IF pParMovTipoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_ativo'||' like'||'''%'||pParMovTipoAtivo||'%'' ';
               END IF;	
               
               IF pParMovTipoSigla != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_sigla'||' like'||'''%'||pParMovTipoSigla||'%'' ';
               END IF;
       
               IF pParMovTipoMov != '' THEN
                   vSql = vSql ||' and '||'t2.mov_tipo_tipo_mov'||' like'||'''%'||pParMovTipoMov||'%'' ';		
               END IF;
               
               IF pParGerNumeracaoId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_numeracao_id ' || ' in(''' ||pParGerNumeracaoId||''')';
               END IF;		
       
               IF pParGerNumeracaoNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_numeracao_nome'||' like'||'''%'||pParGerNumeracaoNome||'%'' ';
               END IF;		
       
               IF pParGerNumeracaoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_numeracao_ativo'||' like'||'''%'||pParGerNumeracaoAtivo||'%'' ';
               END IF;	
       
               IF pParGerNumeracaoSerie != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_numeracao_serie ' ||' like'||'''%'||pParGerNumeracaoSerie||'%'' ';
               END IF;	
       
               IF pParMovStatusId != '' THEN
                   vSql = vSql || 'and ' || ' t2.mov_status_id ' || ' in(''' ||pParMovStatusId||''')';		
               END IF;	
       
               IF pParMovStatusNome != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_nome'||' like'||'''%'||pParMovStatusNome||'%'' ';
               END IF;	
       
               IF pParMovStatusAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_ativo'||' like'||'''%'||pParMovStatusAtivo||'%'' ';
               END IF;	
       
               IF pParMovStatusSigla != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_sigla'||' like'||'''%'||pParMovStatusSigla||'%'' ';
               END IF;
       
               IF pParMovStatusTipo != '' THEN
                   vSql = vSql ||' and '||'t2.mov_status_tipo_status'||' like'||'''%'||pParMovStatusTipo||'%'' ';
               END IF;
               
               IF pParGerEmpresaId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_empresa_id ' || ' in(''' ||pParGerEmpresaId||''')';
               END IF;
       
               IF pParGerEmpresaNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_empresa_nome'||' like'||'''%'||pParGerEmpresaNome||'%'' ';
               END IF;
       
               IF pParGerEmpresaAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_empresa_ativo'||' like'||'''%'||pParGerEmpresaAtivo||'%'' ';
               END IF;
       
               IF pParGerEmpresaSigla != '' THEN
                   vSql = vSql ||' and '||'t2.ger_empresa_sigla'||' like'||'''%'||pParGerEmpresaSigla||'%'' ';
               END IF;
       
               IF pParGerPessoaId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_pessoa_id ' || ' in(''' ||pParGerPessoaId||''')';
               END IF;
       
               IF pParGerPessoaNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_nome'||' like'||'''%'||pParGerPessoaNome||'%'' ';
               END IF;
       
               IF pParGerPessoaAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_ativo'||' like'||'''%'||pParGerPessoaAtivo||'%'' ';
               END IF;
       
               IF pParGerPessoaSigla != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_sigla_pes'||' like'||'''%'||pParGerPessoaSigla||'%'' ';
               END IF;
       
               IF pParGerPessoaEnderecoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_ativo'||' like'||'''%'||pParGerPessoaEnderecoAtivo||'%'' ';
               END IF;
       
               IF pParGerPessoaEnderecoLograd != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_end_lograd'||' like'||'''%'||pParGerPessoaEnderecoLograd||'%'' ';		
               END IF;
       
               IF pParGerPessoaEnderecoLogradNr != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_lograd_nr'||' like'||'''%'||pParGerPessoaEnderecoLogradNr||'%'' ';		
               END IF;
       
               IF pParGerPessoaEnderecoLogradBairro != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_end_bairro'||' like'||'''%'||pParGerPessoaEnderecoLogradBairro||'%'' ';			
               END IF;
               
               IF pParGerPessoaEntregId != '' THEN
                   vSql = vSql || 'and ' || ' t2.ger_pessoa_entrega_id ' || ' in(''' ||pParGerPessoaEntregId||''')';
               END IF;
       
               IF pParGerPessoaEntregNome != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_entrega_nome'||' like'||'''%'||pParGerPessoaEntregNome||'%'' ';
               END IF;
       
               IF pParGerPessoaEntregAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_entrega_ativo'||' like'||'''%'||pParGerPessoaEntregAtivo||'%'' ';
               END IF;
       
               IF pParGerPessoaEntregEnderecoAtivo != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_ativo'||' like'||'''%'||pParGerPessoaEntregEnderecoAtivo||'%'' ';		
               END IF;
       
               IF pParGerPessoaEntregEnderecoLograd != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_end_lograd'||' like'||'''%'||pParGerPessoaEntregEnderecoLograd||'%'' ';		
               END IF;
       
               IF pParGerPessoaEntregEnderecoLogradNr != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_end_lograd_nr'||' like'||'''%'||pParGerPessoaEntregEnderecoLogradNr||'%'' ';				
               END IF;
       
               IF pParGerPessoaEntregEnderecoLogradBairro != '' THEN
                   vSql = vSql ||' and '||'t2.ger_pessoa_endereco_entrega_end_bairro'||' like'||'''%'||pParGerPessoaEntregEnderecoLogradBairro||'%'' ';		
               END IF;
       
               -- Analisar forma item/serv ou mov/item/serv
               
               IF pParMovItemServId != '' THEN
                   vSql = vSql || 'and ' || ' t1.mov_itemserv_id ' || ' in(''' ||pParMovItemServId||''')';
               END IF;
               
               IF pParItemServId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_item_serv_id ' || ' in(''' ||pParItemServId||''')';
               END IF;
       
               IF pParItemServNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_nome'||' like'||'''%'||pParItemServNome||'%'' ';
               END IF;
       
               IF pParItemServAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_ativo'||' like'||'''%'||pParItemServAtivo||'%'' ';
               END IF;
       
               IF pParItemServSigla != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_sigla'||' like'||'''%'||pParItemServSigla||'%'' ';
               END IF;
       
               IF pParItemServTipo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_item_serv_tipo'||' like'||'''%'||pParItemServTipo||'%'' ';
               END IF;
       
               IF pParItemServSubGrupoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_id ' || ' in(''' ||pParItemServSubGrupoId||''')';
               END IF;
       
               IF pParItemServSubGrupoNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_subgrupo_nome'||' like'||'''%'||pParItemServSubGrupoNome||'%'' ';
               END IF;
       
               IF pParItemServSubGrupoAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_subgrupo_ativo'||' like'||'''%'||pParItemServSubGrupoAtivo||'%'' ';
               END IF;
       
               IF pParItemServGrupoId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_id ' || ' in(''' ||pParItemServGrupoId||''')';
               END IF;
               
               IF pParItemServGrupoNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_grupo_nome'||' like'||'''%'||pParItemServGrupoNome||'%'' ';		
               END IF;
       
               IF pParItemServGrupoAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_itemserv_grupo_ativo'||' like'||'''%'||pParItemServGrupoAtivo||'%'' ';
               END IF;
       
               IF pParGerUmedidaId != '' THEN
                   vSql = vSql || 'and ' || ' t1.ger_umedida_id ' || ' in(''' ||pParGerUmedidaId||''')';
               END IF;
       
               IF pParGerUmedidaNome != '' THEN
                   vSql = vSql ||' and '||'t1.ger_umedida_nome'||' like'||'''%'||pParGerUmedidaNome||'%'' ';
               END IF;
       
               IF pParGerUmedidaAtivo != '' THEN
                   vSql = vSql ||' and '||'t1.ger_umedida_ativo'||' like'||'''%'||pParGerUmedidaAtivo||'%'' ';
               END IF;
       
               IF pParGerUmedidaSigla != '' THEN
                   vSql = vSql ||' and '||'t1.ger_umedida_sigla'||' like'||'''%'||pParGerUmedidaSigla||'%'' ';
               END IF;
       
               IF pParFisCfopId != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_id ' || ' in(''' ||pParFisCfopId||''')';
               END IF;
       
               IF pParFisCfopNR != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_nr_cfop ' ||' like'||'''%'||pParFisCfopNR||'%'' ';
               END IF;
               
               IF pParFisCfopNome != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_nome ' ||' like'||'''%'||pParFisCfopNome||'%'' ';
               END IF;
       
               IF pParFisCfopAtivo != '' THEN
                   vSql = vSql || 'and ' || ' t1.fis_cfop_ativo ' ||' like'||'''%'||pParFisCfopAtivo||'%'' ';
               END IF;
               
               IF pParFisCfopDataValidIni != '' and pParFisCfopDataValidFin != '' THEN
                 vSql = vSql || ' and ' || 'CAST(t1.fis_cfop_data_validade AS DATE)' || ' >= ''' ||pParFisCfopDataValidIni|| '''' || ' and  CAST(t1.fis_cfop_data_validade AS DATE)' || ' <= ''' ||pParFisCfopDataValidFin || '''';		
               END IF;
       
               IF pParLogUserIns != '' THEN
                       vSql = vSql || 'and ' || ' t1.log_user_ins' || ' like '|| '''%' ||pParLogUserIns|| '%'' ';
               END IF;
                   
               IF pParLogDateInsIni != '' AND pParLogDateInsFin != '' THEN
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
               vSql = vSql||' group by valor_03, valor_07, '|| pVart01;
       
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
           
               if  pVart06 != ''  THEN
                vSql = vSql||  ','|| pVart06;
               end if;
       
               if  pVart07 != ''  THEN
                vSql = vSql||  ','|| pVart07;
               end if;
       
               if  pVart08 != ''  THEN
                vSql = vSql||  ','|| pVart08;
               end if;		
               
               if  pVart09 != ''  THEN
                vSql = vSql||  ','|| pVart09;
               end if;	
               
               if  pVart10 != ''  THEN
                vSql = vSql||  ','|| pVart10;
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
               
           if  pVart06 != ''  THEN
                vSql = vSql||  ','|| pVart06;
               end if;
       
           if  pVart07 != ''  THEN
                vSql = vSql||  ','|| pVart07;
               end if;
       
           if  pVart08 != ''  THEN
                vSql = vSql||  ','|| pVart08;
               end if;
       
           if  pVart09 != ''  THEN
                vSql = vSql||  ','|| pVart09;
               end if;
           
               if  pVart10 != ''  THEN
                vSql = vSql||  ','|| pVart10;
               end if;
       
       
               raise notice 'vSql :%', vSql;
       
       
       
               for r in EXECUTE vSql loop
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
                    valor_07 := r.valor_07;
                    valor_08 := r.valor_08;
                    valor_09 := r.valor_09;
                    valor_10 := r.valor_10;
                    valor_11 := r.valor_11;
                    valor_12 := r.valor_12;
                    valor_13 := r.valor_13;
                    valor_14 := r.valor_14;
                    valor_15 := r.valor_15;
                    valor_16 := r.valor_16;
                    valor_17 := r.valor_17;
                    valor_18 := r.valor_18;
                    
                   return next;
                   raise notice 'vSql :%', vSql;
               end loop;
               return;
       
       
       
       end;
       $function$
;
