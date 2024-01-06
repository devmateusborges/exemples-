--=======================================================
--Desabilita Trigger para evitar disparos 
--=======================================================
declare
  vScript varchar2(1000);
begin
  for f1 in(select 'ALTER TRIGGER '||t.trigger_name||' DISABLE ' as script
              from user_triggers t
              where  t.status = 'ENABLED'
              and t.table_name in('TFICHA','TFICHA_CONTAS','TFICHA_END_COBRA','TFICHA_END_ENTREGA')
            )

  loop 
    vScript := f1.script;
    execute immediate f1.script;
  end loop;
  
exception
when others then
     dbms_output.put_line('Erro ['||vScript||'] ['||SQLERRM||']');
end;

--=======================================================
--Cria função de UUID
--=======================================================
create or replace function random_uuid return VARCHAR2 is
  v_uuid VARCHAR2(40);
begin
  select lower(regexp_replace(rawtohex(sys_guid()), '([A-F0-9]{8})([A-F0-9]{4})([A-F0-9]{4})([A-F0-9]{4})([A-F0-9]{12})', '\1-\2-\3-\4-\5')) into v_uuid from dual;
  return v_uuid;
end random_uuid;




alter table tficha add zuuid varchar(36);
create unique index idx_tficha_zuuid on tficha (zuuid);
alter table tficha_contas add zuuid varchar(36);
create unique index idx_tficha_contas_zuuid on tficha_contas (zuuid);
alter table tficha_end_cobra add zuuid varchar(36);
create unique index idx_tficha_end_cobra_zuuid on tficha_end_cobra (zuuid);
alter table tficha_end_entrega add zuuid varchar(36);
create unique index idx_tficha_end_entrega_zuuid on tficha_end_entrega (zuuid);


update tficha set zuuid = random_uuid();
update tficha_contas set zuuid = random_uuid();
update tficha_end_cobra set zuuid = random_uuid();
update tficha_end_entrega set zuuid = random_uuid();
