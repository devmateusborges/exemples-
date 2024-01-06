Drop FUNCTION IF EXISTS fnreport_par;
CREATE OR REPLACE FUNCTION fnreport_par(
pParUnitId varchar, 
pParIndRelId varchar,
pParParams text
)
RETURNS varchar

AS $BODY$
declare
vSql text;
vPar1 varchar;
r record;
pJ json;
pJNv json;
vParNome varchar;
vParNomeTec varchar;
vParValor varchar;
vParValorDec varchar;
vParParams varchar;
busca_tabela varchar;
busca_campo_nome varchar;
busca_campo_id varchar;
ind_rel_par1 varchar;
vSiglas varchar;
jsonKey varchar;
paramsrel VARCHAR;
existParam integer := 0;
paramVar varchar;
begin
			
		vParParams = REPLACE(pParParams,'%22',chr(34));
		vParParams = TRANSLATE(vParParams,chr(35),chr(34));
		ind_rel_par1 = '';
		
		select vParParams::json
    into pJ;
		
	
		
 		for pJNv in select  * from json_array_elements((pJ)::json) 
 		loop

		
 			select json_object_keys(pJNv::json) into jsonKey;
			
			vParValor := pJNv->>jsonKey;
			vParNomeTec := jsonKey;
	
			
			
		select id into paramVar from ind_prm where nome_tecnico = vParNomeTec;

		select count(*) into existParam from ind_rel_prm relac
		 where relac.ind_rel_id = pParIndRelId
		 and relac.ind_prm_id = paramVar;
		 
		 Raise Notice ' Variavel Id%',paramVar;
		 
			raise notice 'Return de Params % ', existParam;
			
			If (existParam > 0) Then
			
			RAISE NOTICE ' Parametro Existe Para Esse Relatorio %', existParam;	
			busca_tabela = '';
			busca_campo_nome = '';
			busca_campo_id = '';
			
	
			
			select indP.busca_tabela, indP.busca_campo_nome, indP.busca_campo_id, indP.nome
			  into busca_tabela, busca_campo_nome, busca_campo_id, vParNome
			  from ind_prm indP 
		  where indP.nome_tecnico = vParNomeTec;

			If busca_tabela Is Not Null Then
				
				vParValorDec := fnreport_decodeuri(vParValor);
				
				select fnreport_sigla(pParUnitId,busca_tabela,busca_campo_nome,busca_campo_id,vParValorDec)
				into vSiglas;
			 
			If vSiglas Is Null Then
		    vSiglas := '';	
		  End If;
			
			ind_rel_par1 := ind_rel_par1 || vParNome||' ['||vSiglas||'] '||chr(13)||chr(10);
			
			ELSE
			
			ind_rel_par1 := ind_rel_par1 || vParNome||' ['||vParValor||'] '||chr(13)||chr(10);
			
		  END IF;
			

			ELSE
			
				RAISE NOTICE ' Sem Parametros';	
			End If;
	
		End Loop;
	
	
		return ind_rel_par1;
end;
$BODY$
  LANGUAGE plpgsql VOLATILE;