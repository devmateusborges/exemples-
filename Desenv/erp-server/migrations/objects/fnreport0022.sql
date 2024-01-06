Drop FUNCTION IF EXISTS fnreport0022;
CREATE OR REPLACE FUNCTION fnreport0022(
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
pParItemServId varchar default null,
pParItemServNome varchar default null,
pParItemServAtivo varchar default null,
pParItemServTipo varchar default null,
pParItemServOrigemFiscal varchar default null,
pParItemServTipoComposi varchar default null,
pParItemServTipoCtbComp varchar default null,
pParItemServDocCnaeNfs varchar default null,
pParItemServSubGrupoId varchar default null,
pParItemServSubGrupoNome varchar default null,
pParItemServSubGrupoAtivo varchar default null,

pParItemServGrupoId varchar default null,
pParItemServGrupoNome varchar default null,
pParItemServGrupoAtivo varchar default null,
pParFisNcmId varchar default null,
pParFisNcmNome varchar default null,
pParFisNcmAtivo varchar default null,
pParFisNcmDataValidadeIni varchar default null,
pParFisNcmDataValidadeFin varchar default null,
pParFisNcmNumero varchar default null,
pParUnidadeMedId varchar default null,
pParUnidadeMedNome varchar default null,
pParUnidadeMedAtivo varchar default null,

pParFisCestId varchar default null,
pParFisCestNome varchar default null,
pParFisCestAtivo varchar default null,
pParFisCestDataValidadeIni varchar default null,
pParFisCestDataValidadeFin varchar default null,
pParFisCestNumero varchar default null,
pParFisNbsId varchar default null,
pParFisNbsNome varchar default null,
pParFisNbsAtivo varchar default null,
pParFisNbsDataValidadeIni varchar default null,
pParFisNbsDataValidadeFin varchar default null,
pParFisNbsNumero varchar default null,
pParCtbId varchar default null,
pParCtbNome varchar default null,
pParCtbAtivo varchar default null,
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
r record;

begin

	if pParItemServId != '' then
		vPar1 :=vPar1||'Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv','sigla_itemserv','id',''''||pParItemServId||'''')||'] '||chr(13)||chr(10);
	else
		vPar1 :=vPar1||'Item/Serviço []'||chr(13)||chr(10);
	end if;
	
	if pParItemServNome != '' then
		vPar1 :=vPar1||'Nome Item/Serviço ['||pParItemServNome||']'||chr(13)||chr(10);	
	else
		vPar1 :=vPar1||'Nome Item/Serviço []'||chr(13)||chr(10);		
	end if;
	
	if pParItemServAtivo != '' then
		vPar1 :=vPar1||'Item/Serviço Ativo ['||pParItemServAtivo||']'||chr(13)||chr(10);		
	else
		vPar1 :=vPar1||'Item/Serviço Ativo []'||chr(13)||chr(10);			
	end if;
	
	if pParItemServTipo != '' then
		vPar1 :=vPar1||'Tipo Item/Serviço ['||pParItemServTipo||']'||chr(13)||chr(10);		
	else
		vPar1 :=vPar1||'Tipo Item/Serviço []'||chr(13)||chr(10);			
	end if;
	
	if pParItemServOrigemFiscal != '' then
		vPar1 :=vPar1||'Origem Fiscal Item/Serviço ['||pParItemServOrigemFiscal||']'||chr(13)||chr(10);			
	else
		vPar1 :=vPar1||'Origem Fiscal Item/Serviço []'||chr(13)||chr(10);				
	end if;
	
	if pParItemServTipoComposi != '' then
		vPar1 :=vPar1||'Tipo de Composição Item/Serviço ['||pParItemServTipoComposi||']'||chr(13)||chr(10);				
	else
		vPar1 :=vPar1||'Tipo de Composição Item/Serviço []'||chr(13)||chr(10);					
	end if;

	if pParItemServTipoCtbComp != '' then
		vPar1 :=vPar1||'Tipo Componente Contábil Item/Serviço ['||pParItemServTipoCtbComp||']'||chr(13)||chr(10);				
	else
		vPar1 :=vPar1||'Tipo Componente Contábil Item/Serviço []'||chr(13)||chr(10);					
	end if;
	
 if pParItemServDocCnaeNfs!= '' then
		vPar1 :=vPar1||'Documento Cnae da NFS Item/Serviço ['||pParItemServDocCnaeNfs||']'||chr(13)||chr(10);	 
 else
		vPar1 :=vPar1||'Documento Cnae da NFS Item/Serviço []'||chr(13)||chr(10);	  
 end if;

	if pParItemServSubGrupoId != '' then
		vPar1 :=vPar1||'SubGrupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_subgrupo','nome','id',''''||pParItemServSubGrupoId||'''')||'] '||chr(13)||chr(10);
	else
		vPar1 :=vPar1||'SubGrupo Item/Serviço []'||chr(13)||chr(10);
	end if;

 if pParItemServSubGrupoNome != '' then
		vPar1 :=vPar1||'Nome SubGrupo Item/Serviço ['||pParItemServSubGrupoNome||']'||chr(13)||chr(10);	 
 else
		vPar1 :=vPar1||'Nome SubGrupo Item/Serviço []'||chr(13)||chr(10);	  
 end if;


 if pParItemServSubGrupoAtivo != '' then
		vPar1 :=vPar1||'SubGrupo Item/Serviço Ativo ['||pParItemServSubGrupoAtivo||']'||chr(13)||chr(10);	 
 else
		vPar1 :=vPar1||'SubGrupo Item/Serviço Ativo []'||chr(13)||chr(10);	  
 end if;

	if pParItemServGrupoId != '' then
		vPar1 :=vPar1||'Grupo Item/Serviço ['||fnreport_sigla(pParUnitId,'ger_itemserv_grupo','nome','id',''''||pParItemServGrupoId||'''')||'] '||chr(13)||chr(10);
	else
		vPar1 :=vPar1||'Grupo Item/Serviço []'||chr(13)||chr(10);
	end if;

 if pParItemServGrupoNome != '' then
		vPar1 :=vPar1||'Nome Grupo Item/Serviço ['||pParItemServGrupoNome||']'||chr(13)||chr(10);	 
 else
		vPar1 :=vPar1||'Nome Grupo Item/Serviço []'||chr(13)||chr(10);	  
 end if;

 if pParItemServGrupoAtivo != '' then
		vPar2 :=vPar2||'Grupo Item/Serviço Ativo ['||pParItemServGrupoAtivo||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Grupo Item/Serviço Ativo []'||chr(13)||chr(10);	  
 end if;

	if pParFisNcmId != '' then
		vPar2 :=vPar2||'NCM ['||fnreport_sigla(pParUnitId,'fis_ncm','nome','id',''''||pParFisNcmId||'''')||'] '||chr(13)||chr(10);
	else
		vPar2 :=vPar2||'NCM []'||chr(13)||chr(10);
	end if;

 if pParFisNcmNome != '' then
		vPar2 :=vPar2||'Nome NCM ['||pParFisNcmNome||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Nome NCM []'||chr(13)||chr(10);	  
 end if;

 if pParFisNcmAtivo != '' then
		vPar2 :=vPar2||'NCM Ativo ['||pParFisNcmAtivo||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'NCM Ativo []'||chr(13)||chr(10);	  
 end if;

 if pParFisNcmDataValidadeIni != '' and pParFisNcmDataValidadeFin != '' then
		vPar2 :=vPar2||'Data Validade NCM de ['||pParFisNcmDataValidadeIni||'] até ['||pParFisNcmDataValidadeFin||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Data Validade NCM de [] até []'||chr(13)||chr(10);	  
 end if;

 if pParFisNcmNumero != '' then
		vPar2 :=vPar2||'Nº NCM ['||pParFisNcmNumero||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Nº NCM []'||chr(13)||chr(10);	  
 end if;

 if pParUnidadeMedId != '' then
		vPar2 :=vPar2||'Unidade de Medida ['||fnreport_sigla(pParUnitId,'ger_umedida','sigla_umedida','id',''''||pParUnidadeMedId||'''')||'] '||chr(13)||chr(10);
	else
		vPar2 :=vPar2||'Unidade de Medida []'||chr(13)||chr(10);
	end if;

 if pParUnidadeMedNome != '' then
		vPar2 :=vPar2||'Nome Unidade de Medida ['||pParUnidadeMedNome||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Nome Unidade de Medida []'||chr(13)||chr(10);	  
 end if;

 if pParUnidadeMedAtivo != '' then
		vPar2 :=vPar2||'Unidade de Medida Ativo ['||pParUnidadeMedAtivo||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Unidade de Medida Ativo []'||chr(13)||chr(10);	  
 end if;

 if pParFisCestId != '' then
		vPar2 :=vPar2||'CEST ['||fnreport_sigla(pParUnitId,'fis_cest','nome','id',''''||pParFisCestId||'''')||'] '||chr(13)||chr(10);
	else
		vPar2 :=vPar2||'CEST []'||chr(13)||chr(10);
	end if;

 if pParFisCestNome != '' then
		vPar2 :=vPar2||'Nome CEST ['||pParFisCestNome||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Nome CEST []'||chr(13)||chr(10);	  
 end if;
 
 if pParFisCestAtivo != '' then
		vPar2 :=vPar2||'CEST Ativo ['||pParFisCestAtivo||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'CEST Ativo []'||chr(13)||chr(10);	  
 end if;

 if pParFisCestDataValidadeIni != '' and pParFisCestDataValidadeFin != '' then
		vPar2 :=vPar2||'Data Validade CEST de ['||pParFisCestDataValidadeIni||'] até ['||pParFisCestDataValidadeFin||']'||chr(13)||chr(10);	 
 else
		vPar2 :=vPar2||'Data Validade CEST de [] até []'||chr(13)||chr(10);	  
 end if;

 if pParFisCestNumero != '' then
		vPar3 :=vPar3||'Nº CEST ['||pParFisCestNumero||']'||chr(13)||chr(10);	 
 else
		vPar3 :=vPar3||'Nº CEST []'||chr(13)||chr(10);	  
 end if;

 if pParFisNbsId != '' then
		vPar3 :=vPar3||'NBS ['||fnreport_sigla(pParUnitId,'fis_nbs','nome','id',''''||pParFisNbsId||'''')||'] '||chr(13)||chr(10);
	else
		vPar3 :=vPar3||'NBS []'||chr(13)||chr(10);
	end if;

 if pParFisNbsNome != '' then
		vPar3 :=vPar3||'Nome NBS ['||pParFisNbsNome||']'||chr(13)||chr(10);	 
 else
		vPar3 :=vPar3||'Nome NBS []'||chr(13)||chr(10);	  
 end if;

 if pParFisNbsAtivo != '' then
		vPar3 :=vPar3||'NBS Ativo ['||pParFisNbsAtivo||']'||chr(13)||chr(10);	 
 else
		vPar3 :=vPar3||'NBS Ativo []'||chr(13)||chr(10);	  
 end if;

 if pParFisNbsDataValidadeIni != '' and pParFisNbsDataValidadeFin != '' then
		vPar3 :=vPar3||'Data Validade NBS de ['||pParFisNbsDataValidadeIni||'] até ['||pParFisNbsDataValidadeFin||']'||chr(13)||chr(10);	 
 else
		vPar3 :=vPar3||'Data Validade NBS de [] até []'||chr(13)||chr(10);	  
 end if;

 if pParFisNbsNumero != '' then
		vPar3 :=vPar3||'Nº NBS ['||pParFisNbsNumero||']'||chr(13)||chr(10);	 
 else
		vPar3 :=vPar3||'Nº NBS []'||chr(13)||chr(10);	  
 end if;

 if pParCtbId != '' then
		vPar3 :=vPar3||'Componente Contábil ['||fnreport_sigla(pParUnitId,'ctb_comp','sigla_comp','id',''''||pParCtbId||'''')||'] '||chr(13)||chr(10);
	else
		vPar3 :=vPar3||'Componente Contábil []'||chr(13)||chr(10);
	end if;

 if pParCtbNome != '' then
		vPar3 :=vPar3||'Nome Componente Contábil ['||pParCtbNome||']'||chr(13)||chr(10);	 
 else
		vPar3 :=vPar3||'Nome Componente Contábil []'||chr(13)||chr(10);	  
 end if;

 if pParCtbAtivo != '' then
		vPar3 :=vPar3||'Componente Contábil Ativo ['||pParCtbAtivo||']'||chr(13)||chr(10);	 
 else
		vPar3 :=vPar3||'Componente Contábil Ativo []'||chr(13)||chr(10);	  
 end if;

	if pParLogUserIns != '' then
		vPar3 :=vPar3||'Log Usuario Inserção ['||pParLogUserIns||']'||chr(13)||chr(10);
	else
		vPar3 :=vPar3||'Log Usuario Inserção []'||chr(13)||chr(10);
	end if;

	if pParLogUserUpd != '' then
		vPar3 :=vPar3||'Log Usuario Alteração ['||pParLogUserUpd||']'||chr(13)||chr(10);
	else
		vPar3 :=vPar3||'Log Usuario Alteração []'||chr(13)||chr(10);
	end if;

	if pParLogDateInsIni != '' and pParLogDateInsFin != '' then
		vPar3 :=vPar3||'Data Inserção de ['||pParLogDateInsIni||'] até ['||pParLogDateInsFin||']'||chr(13)||chr(10);
	else
		vPar3 :=vPar3||'Data Inserção de [] até []'||chr(13)||chr(10);
	end if;

	if pParLogDateUpdIni != '' and pParLogDateUpdFin != '' then
		vPar3 :=vPar3||'Data Alteração de ['||pParLogDateUpdIni||'] até ['||pParLogDateUpdFin||']'||chr(13)||chr(10);
	else
		vPar3 :=vPar3||'Data Alteração de [] até []'||chr(13)||chr(10);
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
			from vwger_itemserv t1 where 1=1';



		IF pParUnitId != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_unitid' || ' in(''' ||pParUnitId||''')';
		END IF;
		
		IF pParItemServId != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_id' || ' in(''' ||pParItemServId||''')';
		END IF;
		
		IF pParItemServNome != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_nome' || ' like '|| '''%' || pParItemServNome || '%'' ';	
		END IF;
		
		IF pParItemServAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_ativo_desc' || ' like '|| '''%' || pParItemServAtivo || '%'' ';	
		END IF;

		IF pParItemServTipo != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_tipo' || ' like '|| '''%' || pParItemServTipo || '%'' ';	
		END IF;
		
		IF pParItemServOrigemFiscal != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_origem_fiscal' || ' = '|| '''' || pParItemServOrigemFiscal || ''' ';	
		END IF;		
		
		IF pParItemServTipoComposi != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_tipo_composicao ' || ' like '|| '''%' || pParItemServTipoComposi || '%'' ';	
		END IF;			

		IF pParItemServTipoCtbComp != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_tipo_ctb_comp' || ' like '|| '''%' || pParItemServTipoCtbComp || '%'' ';	
		END IF;	
		
		IF pParItemServDocCnaeNfs != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_fis_doc_cnae_nfs' || ' like '|| '''%' || pParItemServDocCnaeNfs || '%'' ';	
		END IF;	
		
		IF pParItemServSubGrupoId != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_id' || ' in(''' ||pParItemServSubGrupoId||''')';
		END IF;	

		IF pParItemServSubGrupoNome != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_nome' || ' like '|| '''%' || pParItemServSubGrupoNome || '%'' ';	
		END IF;		
		
		IF pParItemServSubGrupoAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_subgrupo_ativo_desc' || ' like '|| '''%' || pParItemServSubGrupoAtivo || '%'' ';	
		END IF;			
		
		IF pParItemServGrupoId != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_id' || ' in(''' ||pParItemServGrupoId||''')';
		END IF;			
	
		IF pParItemServGrupoNome != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_nome' || ' like '|| '''%' || pParItemServGrupoNome || '%'' ';	
		END IF;		
		
		IF pParItemServGrupoAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_itemserv_grupo_ativo_desc' || ' like '|| '''%' || pParItemServGrupoAtivo || '%'' ';	
		END IF;		

		IF pParFisNcmId != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_ncm_id' || ' in(''' ||pParFisNcmId||''')';
		END IF;		

		IF pParFisNcmNome != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_ncm_nome' || ' like '|| '''%' || pParFisNcmNome || '%'' ';	
		END IF;		

		IF pParFisNcmAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_ncm_ativo_desc' || ' like '|| '''%' || pParFisNcmAtivo || '%'' ';	
		END IF;	

		IF pParFisNcmDataValidadeIni != '' and pParFisNcmDataValidadeFin != '' THEN
		  vSql = vSql || ' and ' || 'CAST(t1.fis_ncm_dt_validade AS DATE)' || ' >= ''' || pParFisNcmDataValidadeIni|| '''' || ' and  CAST(t1.fis_ncm_dt_validade AS DATE)' || ' <= ''' || pParFisNcmDataValidadeFin || '''';
		END IF;

		IF pParFisNcmNumero != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_ncm_nr_ncm' || ' like '|| '''%' || pParFisNcmNumero || '%'' ';	
		END IF;	

		IF pParUnidadeMedId != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_umedida_id' || ' in(''' ||pParUnidadeMedId||''')';
		END IF;	
		
		IF pParUnidadeMedNome != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_umedida_nome' || ' like '|| '''%' || pParUnidadeMedNome || '%'' ';	
		END IF;	
	
  	IF pParUnidadeMedAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.ger_umedida_ativo_desc' || ' like '|| '''%' || pParUnidadeMedAtivo || '%'' ';	
		END IF;	

		IF pParFisCestId != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_cest_id' || ' in(''' ||pParFisCestId||''')';
		END IF;	

  	IF pParFisCestNome != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_cest_nome' || ' like '|| '''%' || pParFisCestNome || '%'' ';	
		END IF;	

  	IF pParFisCestAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_cest_ativo_desc' || ' like '|| '''%' || pParFisCestAtivo || '%'' ';	
		END IF;	
		
		IF pParFisCestDataValidadeIni != '' and pParFisCestDataValidadeFin != '' THEN
		  vSql = vSql || ' and ' || 'CAST(t1.fis_cest_dt_validade AS DATE)' || ' >= ''' || pParFisCestDataValidadeIni|| '''' || ' and  CAST(t1.fis_cest_dt_validade AS DATE)' || ' <= ''' || pParFisCestDataValidadeFin || '''';
		END IF;


  	IF pParFisCestNumero != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_cest_nr_cest' || ' like '|| '''%' || pParFisCestNumero || '%'' ';	
		END IF;

		IF pParFisNbsId != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_nbs_id' || ' in(''' ||pParFisNbsId||''')';
		END IF;					

  	IF pParFisNbsNome != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_nbs_nome' || ' like '|| '''%' || pParFisNbsNome || '%'' ';	
		END IF;

  	IF pParFisNbsAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_nbs_ativo_desc' || ' like '|| '''%' || pParFisNbsAtivo || '%'' ';	
		END IF;

		IF pParFisNbsDataValidadeIni != '' and pParFisNbsDataValidadeFin != '' THEN
		  vSql = vSql || ' and ' || 'CAST(t1.fis_nbs_dt_validade AS DATE)' || ' >= ''' || pParFisNbsDataValidadeIni|| '''' || ' and  CAST(t1.fis_nbs_dt_validade AS DATE)' || ' <= ''' || pParFisNbsDataValidadeFin || '''';
		END IF;
		
  	IF pParFisNbsNumero != '' THEN
			vSql = vSql || 'and ' || ' t1.fis_nbs_nr_nbs' || ' like '|| '''%' || pParFisNbsNumero || '%'' ';	
		END IF;		
		
		IF pParCtbId != '' THEN
			vSql = vSql || 'and ' || ' t1.ctb_comp_id' || ' in(''' ||pParCtbId||''')';
		END IF;			
		
  	IF pParCtbNome != '' THEN
			vSql = vSql || 'and ' || ' t1.ctb_comp_nome' || ' like '|| '''%' || pParCtbNome || '%'' ';	
		END IF;		
		
  	IF pParCtbAtivo != '' THEN
			vSql = vSql || 'and ' || ' t1.ctb_comp_ativo_desc' || ' like '|| '''%' || pParCtbAtivo || '%'' ';	
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
		valor_01 := r.valor_01;

	RETURN NEXT;
	
END loop;
raise notice'vSql :%',vSql;



end;
$BODY$
  LANGUAGE plpgsql VOLATILE;
	