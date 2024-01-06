CREATE OR REPLACE FUNCTION fnutil_last_day(date)
        RETURNS date AS
        $$
        SELECT (date_trunc('MONTH', $1) + INTERVAL '1 MONTH - 1 day')::date;
        $$ LANGUAGE 'sql'
        IMMUTABLE STRICT;