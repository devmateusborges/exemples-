Drop VIEW IF EXISTS public.vwope_centro2_mapa_geometria;
CREATE OR REPLACE VIEW public.vwope_centro2_mapa_geometria
AS SELECT a.unit_id,
    a.ope_centro2_id_area,
    b.ope_centro1_id AS ope_centro1_id_area,
    b.nome as centro2_nome,
    b.sigla_centro2,
    a.geom,
    a.log_user_ins,
    a.log_date_ins,
    a.log_user_upd,
    a.log_date_upd,
    a.id,
    CASE
		WHEN b.sigla_centro2::text = 'T4'::text THEN '#ffff4d'::text
		ELSE '#A9D0F5'::text
	END AS color
   FROM ope_centro2_mapa_geometria a
     JOIN ope_centro2 b ON b.id::text = a.ope_centro2_id_area::text;