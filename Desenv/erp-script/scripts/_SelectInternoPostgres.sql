SELECT oid,* FROM pg_database WHERE datname = 'abdados';

SELECT * FROM pg_stat_database WHERE datname = 'abdados';

SELECT * FROM pg_stat_bgwriter;

SELECT * FROM pg_stat_activity;
 
SELECT * FROM pg_locks;
 
SELECT * FROM pg_stat_user_tables WHERE schemaname = 'public' AND relname = 'fin_banco';
 
SELECT * FROM pg_statio_user_tables WHERE schemaname = 'public' AND relname = 'fin_banco';
 
SELECT * FROM pg_stat_user_indexes WHERE indexrelname = 'pk_fis_cfop';
 
SELECT * FROM pg_statio_user_indexes WHERE indexrelname = 'pk_fin_class_agrup_grupo';
 
 
--Restaurar 
pg_restore.exe --host "54.233.252.199" --port "5432" --username "postgres" --no-password --dbname "rfdadosdev1" --verbose "C:\\temp\\RFDADO~1.BAC" 
 
 --Para drop database
 SELECT
	pg_terminate_backend (pg_stat_activity.pid)
FROM
	pg_stat_activity
WHERE
	pg_stat_activity.datname = 'rfdadoslocal';

--drop database rfdadoslocal;
 
CREATE DATABASE "rfdadoslocal"
WITH
  OWNER = "postgres"
  ENCODING = 'utF8'
;


SELECT C.table_schema as Dono,
	C.TABLE_NAME as Tabela,
	C.COLUMN_NAME as coluna,
	pgd.description as coluna_comentario,
	'alter table '||C.TABLE_NAME ||' RENAME column '||C.COLUMN_NAME||' to '||replace(C.COLUMN_NAME,'system','sys')||';' 
FROM
	pg_catalog.pg_statio_all_tables AS st
	INNER JOIN pg_catalog.pg_description pgd ON ( pgd.objoid = st.relid )
	INNER JOIN information_schema.COLUMNS C ON ( pgd.objsubid = C.ordinal_position AND C.table_schema = st.schemaname AND C.TABLE_NAME = st.relname )
	where C.COLUMN_NAME  like '%system%'

	


SELECT * FROM information_schema.tables WHERE table_schema = 'public';
SELECT * FROM information_schema.columns WHERE table_name ='fin_banco';


--====================================================================================
--Listagem de Tiggers
--====================================================================================
select event_object_schema as table_schema,
       event_object_table as table_name,
       trigger_schema,
       trigger_name,
       string_agg(event_manipulation, ',') as event,
       action_timing as activation,
       action_condition as condition,
       action_statement as definition
from information_schema.triggers
group by 1,2,3,4,6,7,8
order by table_schema,
         table_name;
				 
				 
--====================================================================================
--Sem comentario de coluna
--====================================================================================
SELECT isc.table_schema,
    isc."table_name",
    obj_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid, 'pg_class') as table_description,
    isc."column_name",
		isc.ordinal_position,
		pg_catalog.col_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid,isc.ordinal_position) as column_description,
		isc.data_type
FROM
    information_schema.columns isc
where isc."table_name" not like 'pg_%' 
   and isc."table_name"  not like 'sql_%' 
	 and isc."table_name"  not like 'vw%' 
	 and isc."table_name"  not like 'fr_%' 	 
   and isc.table_schema= 'public'
	 and isc."table_name"  not in('geography_columns','geometry_columns','raster_columns','raster_overviews','spatial_ref_sys')
	 and isc."table_name" like 'mov%'
	 and isc."column_name" not in('log_date_ins','log_user_upd','log_user_ins','log_date_upd','unit_id')
	 --and pg_catalog.col_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid,isc.ordinal_position)  is null
order by 2,5	
	
--====================================================================================	
--Primary Key
--====================================================================================
SELECT c.relname as tabela, a.attname as coluna, format_type(a.atttypid, a.atttypmod) AS data_type, a.attnum
FROM   pg_index i
JOIN   pg_attribute a ON a.attrelid = i.indrelid
                     AND a.attnum = ANY(i.indkey)
join pg_class  c on c.oid = i.indrelid										 
WHERE  --c.relname  = 'mov'
     c.relname  not like 'pg%'
		and c.relname not in('spatial_ref_sys')
    and i.indisprimary
order by c.relname 		
	
	
--====================================================================================	
--Primary Key
--====================================================================================	

ALTER TABLE system_user RENAME CONSTRAINT pk_system_user TO pk_sys_user;

SELECT   'alter table '||t.relname||' RENAME CONSTRAINT '||pg_class.relname||' to '||replace(pg_class.relname,'pk_system','pk_sys')||';' 
 FROM pg_class, pg_index, pg_class t
 WHERE pg_class.oid = pg_index.indexrelid
 and pg_index.indrelid = t.oid
 AND pg_class.oid IN (
     SELECT indexrelid
     FROM pg_index, pg_class
     WHERE pg_class.oid=pg_index.indrelid
     --AND indisunique != 't'
     --AND indisprimary != 't'
     AND relname !~ '^pg_'
		 ) 
		 and pg_class.relname ilike 'pk_syst%';
		 
		 
		 
		 
		 
	select * FROM pg_class
	where pg_class.oid	 in (358429,358431)
		
--====================================================================================	
--Retorna Tabela,Coluna e seus comentários	
--====================================================================================	
SELECT  isc.table_schema,
    isc."table_name",
    obj_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid, 'pg_class') as table_description,
    isc."column_name",
		isc.ordinal_position,
		pg_catalog.col_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid,isc.ordinal_position) as column_description,
		isc.data_type
FROM
    information_schema.columns isc
where isc."table_name" not like 'pg_%' 
   and isc."table_name"  not like 'sql_%' 
	 and isc."table_name"  not like 'vw%' 
   and isc.table_schema= 'public'
	 --and (isc."column_name" like '%\_id%' or isc."column_name" like '%id\_%')
	 --and isc.data_type = 'uuid'
	 --and isc.column_name like '%config%' 
	 --and isc.table_name in ('bor_mov','bor_tel')
	 --and pg_catalog.col_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid,isc.ordinal_position)  is null
order by 2,5	


SELECT   isc.table_schema,
    isc.table_name,
    isc.column_name,
		isc.ordinal_position,
		isc.data_type,
		isc.column_default
FROM
    information_schema.columns isc
where isc."table_name" not like 'pg_%' 
   and isc."table_name"  not like 'sql_%' 
	 and isc."table_name"  not like 'vw%' 
   and isc.table_schema= 'public'		


--====================================================================================	
--Retorna Tabela e seu comentário
--====================================================================================	
SELECT distinct,
    isc."table_name",
    obj_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid, 'pg_class') as table_description
FROM
    information_schema.columns isc
where isc."table_name" not like 'pg_%' and isc."table_name"  not like 'sql_%' 
   and isc.table_schema= 'public'
order by 1,2


select * from vsystemversion

--====================================================================================	
--Terminar sessao banco de dados	
--====================================================================================	
SELECT
 pg_terminate_backend (pg_stat_activity.pid)
FROM
 pg_stat_activity
WHERE
 pg_stat_activity.datname = 'abdadosdev';
 
 
 
--====================================================================================	
--Retorna apenas Index e seus tamanhos
--====================================================================================	
SELECT c.relname AS name, 
c.reltuples as count, (c.relpages *  (8192 /1024) / 1024 ) as size_mb,
c.relfilenode::regclass, cast(c.oid::regclass as TEXT), c.relnatts, c.relkind,
c.*
FROM pg_class  c, pg_namespace n 
WHERE n.oid = c.relnamespace
and c.relkind = 'i'
and c.relname not like 'pg_%' 
and c.relname not like 'sql_%' 
and c.relname not like 'pk_%' 
--and c.relname not like 'idx_%' 
--and n.nspname ='MyNamespace' 
ORDER BY c.relpages DESC;

--====================================================================================	
--Retorna apenas Index e suas tabelas
--====================================================================================	
SELECT tab.relname, cls.relname, am.amname
FROM pg_index idx 
JOIN pg_class cls ON cls.oid=idx.indexrelid
JOIN pg_class tab ON tab.oid=idx.indrelid
JOIN pg_am am ON am.oid=cls.relam
where cls.relname not like 'pg_%' 
and cls.relname not like 'sql_%' 
and cls.relname not like 'pk_%' 
--and cls.relname not like 'idx_%' 

--====================================================================================	
--Foreing Key fora do padrao "fk_"
--====================================================================================	
select *
from information_schema.table_constraints tc
join information_schema.referential_constraints rc using (constraint_name)
where constraint_name not like 'fk_%' 


--====================================================================================	
--Retorna todas Foreing Key
--====================================================================================	
select 'alter table '||tc.table_name||' RENAME CONSTRAINT '||tc.CONSTRAINT_NAME||' to '||replace(tc.CONSTRAINT_NAME,'fk_system','fk_sys')||';'
--'alter table '||tc.table_name||' drop CONSTRAINT '||tc.CONSTRAINT_NAME||';'
from information_schema.table_constraints tc
join information_schema.referential_constraints rc using (constraint_name)
where (constraint_name like 'fk_%' 
or constraint_name like '%fkey')
and tc.CONSTRAINT_NAME like 'fk_syst%'

ALTER TABLE name RENAME CONSTRAINT "error_test_id_fkey" TO "the_new_name_fkey";


--====================================================================================	
--Retorna uma Foreing Key
--====================================================================================	
select *
from information_schema.table_constraints tc
join information_schema.referential_constraints rc using (constraint_name)
where constraint_name like 'fk_system_document_system_document_category_id' 




--====================================================================================	
--Foreing Key relacionadas a uma Primary Key	
--====================================================================================	
select 'alter table '||tc.table_name||' drop CONSTRAINT '||tc.CONSTRAINT_NAME||';'
from information_schema.table_constraints tc
join information_schema.referential_constraints rc using (constraint_name)
where constraint_name like 'fk_%' 
--and tc.table_name = 'mov'
and rc.unique_constraint_name = 'pk_ger_per'


--====================================================================================	
--Dropa todas as FK das tabelas
--====================================================================================	
select 'alter table '||table_name||' drop CONSTRAINT '||constraint_name||';' 
from information_schema.table_constraints tc
join information_schema.referential_constraints rc using (constraint_name)
where constraint_name like 'fk_%' 


--====================================================================================	
--Dropa todas as PK das tabelas
--====================================================================================	
select 'alter table '||table_name||' drop CONSTRAINT '||constraint_name||';' 
from information_schema.table_constraints tc
where constraint_type='PRIMARY KEY'





--====================================================================================	
--gera script para alter em tabelas
--====================================================================================	
SELECT 'alter table '||isc."table_name"||' alter column '||isc."column_name"||' type varchar(38);'
   
FROM
    information_schema.columns isc
where isc."table_name" not like 'pg_%' and isc."table_name"  not like 'sql_%' 
   and isc.table_schema= 'public'
	 and isc."column_name" like '%\_id%'
	 and isc."column_name"  not in('ger_per_id','chamado_id','name_identify')
	 and isc.data_type  not in('uuid','date')
	 --AND isc."table_name" NOT LIKE 'system%'
	 --and pg_catalog.col_description(format('%s.%s',isc.table_schema,isc.table_name)::regclass::oid,isc.ordinal_position)  is null
order by 1



--====================================================================================	
--Desabilita - Fk e  PK e Triggers da tabela
--====================================================================================	
DO $$DECLARE r record;
BEGIN
FOR r IN (
		SELECT distinct 'alter table '||isc."table_name"||' disable trigger all;' as script
			 FROM
				information_schema.columns isc
		where isc."table_name" not like 'pg_%' 
			and isc."table_name"  not like 'sql_%' 
			and isc."table_name"  not like 'fr_%' 
			and isc."table_name"  not like 'spatial_%'
			and isc."table_name"  not like 'geography_%'
			and isc."table_name"  not like 'geometry_%'
			and isc."table_name"  not like 'raster_%'
			
			and isc."table_name"  not like 'vw%'
			and isc.table_schema= 'public'
		order by 1)
LOOP
	
	execute r.script;
	raise notice 'Script :%', r.script;
	   
end loop;

END$$;



--====================================================================================	
--Habilita - Fk e  PK e Triggers da tabela
--====================================================================================	
DO $$DECLARE r record;
BEGIN
FOR r IN (
		SELECT distinct 'alter table '||isc."table_name"||' enable trigger all;' as script
			 FROM
				information_schema.columns isc
		where isc."table_name" not like 'pg_%' 
			and isc."table_name"  not like 'sql_%' 
			and isc."table_name"  not like 'fr_%' 
			and isc."table_name"  not like 'spatial_%'
			and isc."table_name"  not like 'geography_%'
			and isc."table_name"  not like 'geometry_%'
			and isc."table_name"  not like 'raster_%'
			
			and isc."table_name"  not like 'vw%'
			and isc.table_schema= 'public'
		order by 1)
LOOP
	
	execute r.script;
	raise notice 'Script :%', r.script;
	   
end loop;

END$$;




--====================================================================================	
--Limpa todas as tabelas tabela
--====================================================================================	
DO $$DECLARE r record;
BEGIN
FOR r IN (
		SELECT distinct 'truncate '||isc."table_name"||' cascade;' as script
   FROM
    information_schema.columns isc
where isc."table_name" not like 'pg_%' 
  and isc."table_name"  not like 'sql_%' 
	and isc."table_name"  not like 'fr_%' 
  and isc."table_name"  not like 'spatial_%'
	and isc."table_name"  not like 'geography_%'
	and isc."table_name"  not like 'geometry_%'
	and isc."table_name"  not like 'vw%'
	and isc."table_name"  not like 'raster_%'
	and isc.table_schema= 'public'
order by 1)
LOOP
	
	execute r.script;
	raise notice 'Script :%', r.script;
	   
end loop;

END$$;



