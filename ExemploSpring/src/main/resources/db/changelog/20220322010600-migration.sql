CREATE EXTENSION IF NOT EXISTS "postgis";
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";;             

DO
$do$
BEGIN
IF NOT EXISTS (
    SELECT FROM pg_catalog.pg_roles  -- SELECT list can be empty for this
    WHERE  rolname = 'rf') THEN

    CREATE role rf WITH 
                NOSUPERUSER
                NOCREATEDB
                NOCREATEROLE
                INHERIT
                NOLOGIN
                NOREPLICATION
                NOBYPASSRLS;
END IF;
END
$do$;;