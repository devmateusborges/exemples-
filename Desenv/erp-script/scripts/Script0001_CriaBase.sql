--Linux
CREATE DATABASE rfdadosdev
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C.UTF-8' 
    LC_CTYPE = 'C.UTF-8' 
    CONNECTION LIMIT = -1;
		
--Win

SELECT	pg_terminate_backend (pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'rfdadoslocal';
drop database	rfdadoslocal;
CREATE DATABASE rfdadoslocal WITH OWNER = postgres ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C';
		
		
CREATE EXTENSION IF NOT EXISTS "postgis";
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";





grant usage on schema public to postgres;
grant create on schema public to postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO postgres;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO postgres;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO postgres;
