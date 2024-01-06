Drop VIEW IF EXISTS public.vwope_centro2_mapa_coord;
CREATE OR REPLACE VIEW public.vwope_centro2_mapa_coord
AS SELECT a.id,
    a.unit_id,
    b.ope_centro1_id ,
    a.ope_centro2_id_area,
    a.lat_x,
    a.long_y,
    a.ordem,
    a.log_user_ins,
    a.log_date_ins,
    a.log_user_upd,
    a.log_date_upd,
	CASE
		WHEN b.sigla_centro2::text = 'T4'::text THEN '#ffff4d'::text
		ELSE '#A9D0F5'::text
	END AS color
   FROM public.ope_centro2_mapa_coord a
   JOIN public.ope_centro2 b on (b.id = a.ope_centro2_id_area);