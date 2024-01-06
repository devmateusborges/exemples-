CREATE OR REPLACE FUNCTION public.fnreport_list(pparunitid character varying, pparindrelid character varying, pparparams text)
 RETURNS TABLE(ind_rel_id character varying, ind_rel_par1 character varying, ind_rel_reportname character varying, ind_f1 character varying, ind_f2 character varying, ind_f3 character varying, ind_f4 character varying, ind_f5 character varying, ind_f6 character varying, ind_f7 character varying, ind_f8 character varying, ind_f9 character varying, ind_f10 character varying, ind_fd1 character varying, ind_fd2 character varying, ind_fd3 character varying, ind_fd4 character varying, ind_fd5 character varying, ind_fd6 character varying, ind_fd7 character varying, ind_fd8 character varying, ind_fd9 character varying, ind_fd10 character varying, ind_fl1 character varying, ind_fl2 character varying, ind_fl3 character varying, ind_fl4 character varying, ind_fl5 character varying, ind_fl6 character varying, ind_fl7 character varying, ind_fl8 character varying, ind_fl9 character varying, ind_fl10 character varying)
 LANGUAGE plpgsql
AS $function$
       declare
       vMsg text := '';
       vSql text;
       vPar1 varchar := '';
       r record;
       l record;
       pJ json;
       pJNv json;
       vParBuscaTabela varchar;
       vParBuscaCampoNome varchar;
       vParBuscaCampoId varchar;
       vParNome varchar;
       vParNomeTec varchar;
       vColNomeTec varchar;
       vColNomeTecPrefixo varchar;
       vParValor varchar;
       vParValorDec varchar;
       vParParams varchar;
       vNameReport varchar;
       vParRelVar varchar := '';
       vIdxCol integer := 1;
       pParCampos varchar[];
       
       begin
       
           vMsg = 'Posição 1';
        vParParams = REPLACE(pParParams,'%22',chr(34));
       
        vMsg = 'Posição 3B'||vParParams;		
        select vParParams::json 
           into pJ;
       
       
        vMsg = 'Posição 2';
        select r2.config_ftd::json->>'query'::text, r1.nome as nome
          into vSql
        from ind_rel r1,
             ind_ftd r2
        where r1.ind_ftd_id = r2.id
          and r1.id = pParIndRelId;
            
           vMsg = 'Posição 3';
           SELECT
               r1.nome INTO vNameReport 
           FROM
               ind_rel r1 
           WHERE
               r1.ID = pParIndRelId;
               
           vMsg = 'Posição 4';
         for pJNv in select  * from json_array_elements((pJ->>'cols')::json)
             loop
                   
                   vColNomeTec = pJNv->>'colNomeTec';
                   vColNomeTecPrefixo = pJNv->>'colNomeTecPrefixo';
       
                   if vIdxCol = 1 then
                       vParRelVar = vParRelVar||' '||vColNomeTecPrefixo||'.'||vColNomeTec||' as f'||vIdxCol;
                       
                   else
                       vParRelVar = vParRelVar||' ,'||vColNomeTecPrefixo||'.'||vColNomeTec||' as f'||vIdxCol;
                   end if;			
                   
                   vParRelVar = vParRelVar||' ,(Select r1.var_nome_descritivo as fd'||vIdxCol||'  from ind_rel_var r1 where r1.ind_rel_id = '''||pParIndRelId||''' and r1.var_nome_tecnico = '''||vColNomeTec||''' limit 1 )  ';
               
                   vMsg = 'Posição 14';		
                   vParRelVar = vParRelVar|| ',(Select r1.largura as fl'||vIdxCol||' from ind_rel_var r1 where r1.ind_rel_id = '''||pParIndRelId||''' and r1.var_nome_tecnico = '''||vColNomeTec||''' limit 1)  ';
                   vIdxCol := vIdxCol+1;
                   
          end loop;
        
        
            for x in vIdxCol..10 loop
                       vMsg = 'Posição 14';	
                   
                       vParRelVar = vParRelVar||' ,(Select null as f'||x||') ';
                       vParRelVar = vParRelVar||' ,(Select null as fd'||x||') ';
                       vParRelVar = vParRelVar||' ,(Select null as fl'||x||') ';
                           
       
            end loop;
       
       vMsg = 'Posição 24';		
        vSql = replace(vSql,' /*FIELDS*/ ',vParRelVar);
       
        vMsg = 'Posição 25';		
        vSql = replace(vSql,'${pParUnitId}',''''||pParUnitId||'''');
           
           vMsg = 'Posição 27';		
           for pJNv in select  * from json_array_elements((pJ->>'params')::json)
           loop
                   vParNomeTec := pJNv->>'parNomeTec';
                   vParValor := pJNv->>'parValor';
                   vParValor := REPLACE((vParValor),'%20',chr(32));
                   vParValor := REPLACE((vParValor),'%C3%AD',chr(237));
                   vParValor := REPLACE((vParValor),'%22',chr(34));
               vMsg = 'Posição 28';				
                 if vParValor is null then
       -- 			vSql = replace(vSql,'${'||vParNomeTec||'}',);
                       vSql = replace(vSql,'${'||vParNomeTec||'}',null);
                   else
                       vSql = replace(vSql,'${'||vParNomeTec||'}',''''||vParValor||'''');
                   end if;
                   RAISE NOTICE 'NomeValor % %', pJNv->>'parNomeTec', vParValor;
                   
                   --Busca campos para montar siglas dos parametros
                   vParBuscaTabela := '';
                   vParBuscaCampoNome := '';
                   vParBuscaCampoId := '';
                   vParNome := '';
                   vParValorDec := '';
                   vMsg = 'Posição 28';		
                   select p1.busca_tabela, p1.busca_campo_nome,  p1.busca_campo_id, p1.nome
                       into vParBuscaTabela, vParBuscaCampoNome, vParBuscaCampoId, vParNome
                       from ind_prm p1
                       join ind_rel_relac_prm p2 on(p1.id = p2.ind_prm_id)
                    where p2.ind_rel_id = pParIndRelId
                        and p1.nome_tecnico = vParNomeTec;
                   vMsg = 'Posição 29';		
                       
               if vParBuscaTabela != '' and vParBuscaCampoNome != '' and vParBuscaCampoId != '' and vParValorDec != '' then
               vMsg = 'Posição 30';		
                        vParValorDec := fnreport_decodeuri(vParValor);
                        vPar1 := vPar1||' ['||fnreport_sigla(pParUnitId,vParBuscaTabela,vParBuscaCampoNome,			 	vParBuscaCampoId,vParValorDec)||'] '||chr(13)||chr(10);
       -- 					raise notice 'Parametros 1 % ',vPar1;
                else
                       if vParNome != null or vParNome != '' then
                               vPar1 := vPar1||vParNome||' ['||vParValor||'] '||chr(13)||chr(10);
                       end if;
       -- 			 raise notice 'ParNome 1 % ',vParNome;
                end if;
               
           end loop;
       
        vMsg = 'Posição 30A '||vSql;
        raise notice '%',vMsg;
        
       for r in EXECUTE vSql loop
           vMsg = 'Posição 31';			 
           ind_rel_id := pParIndRelId;
           ind_rel_par1 := vPar1;
           ind_rel_reportname := vNameReport;
           ind_f1 := r.f1;
           ind_f2 := r.f2;
           ind_f3 := r.f3;
           ind_f4 := r.f4;
           ind_f5 := r.f5;
           ind_f6 := r.f6;
           ind_f7 := r.f7;
           ind_f8 := r.f8;
           ind_f9 := r.f9;
           ind_f10 := r.f10;
           
           ind_fd1 := r.fd1;
           ind_fd2 := r.fd2;
            ind_fd3 := r.fd3;
           ind_fd4 := r.fd4;
            ind_fd5 := r.fd5;
            ind_fd6 := r.fd6;
           ind_fd7 := r.fd7;
           ind_fd8 := r.fd8;
           ind_fd9 := r.fd9;
           ind_fd10 := r.fd10;
           
            ind_fl1 := r.fl1;
           ind_fl2 := r.fl2;
           ind_fl3 := r.fl3;
           ind_fl4 := r.fl4;
           ind_fl5 := r.fl5;
           ind_fl6 := r.fl6;
           ind_fl7 := r.fl7;
           ind_fl8 := r.fl8;
           ind_fl9 := r.fl9;
           ind_fl10 := r.fl10;
           return next;
           
       end loop;
       
       return;
       
       
       EXCEPTION WHEN others THEN		
           Raise EXCEPTION ' % % ', vMsg, SQLERRM;
       
       end;
       $function$
;
