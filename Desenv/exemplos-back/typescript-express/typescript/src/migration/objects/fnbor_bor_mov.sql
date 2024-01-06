DROP TRIGGER IF EXISTS trgbor_bor_mov_bui ON public.bor_mov;
Drop FUNCTION IF EXISTS fnbor_bor_mov;

CREATE OR REPLACE FUNCTION public.fnbor_bor_mov()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
declare
  vBorMovAtual record;
begin
  new.geom = ST_GeomFromText('POINT('||new.gps_lat||' '||new.gps_long||')');
  new.geom_circle = ST_SetSRID(ST_Buffer(new.geom::geography , 15)::geometry, 4326);
 
  -- busca data da bor_mov_atual e se a new.dthr_track for maior, atualiza a bor_mov_atual
  select a.dthr_track
    into vBorMovAtual
    from public.bor_mov_atual a
   where a.ope_centro2_equip_id = new.ope_centro2_equip_id_1;
  
 if coalesce(vBorMovAtual.dthr_track, '1900-01-01') = '1900-01-01'
  then
      begin
        insert into public.bor_mov_atual (
  	      id_tipo,					      numero_serie,					    ibutton_rfid,						        dthr_track,				
   	      gps_altitude,				    gps_altitude_status,			gps_lat,							          gps_long,	
	        gps_angulo_norte,		  	gps_posicao_status,				gps_velocidade,						      gps_velocidade_media,
	        equipamento_ignicao,		equipamento_bateria,			equipamento_odometro,				    equipamento_rpm,			
	        equipamento_veloc,		  equipamento_veloc_odom,		equipamento_veloc_odom_media,		log_user_ins,	
	        log_user_upd,				    ope_centro2_equip_id,			ope_centro2_pessoa_id,				  ger_empresa_id,			
	        ope_centro2_area_id,		geom,							        id,                             dthr_ignicao_last_off)
        values (
	      new.id_tipo,				      new.numero_serie,				      new.ibutton_rfid,					          new.dthr_track,				
	      new.gps_altitude,			    new.gps_altitude_status,		  new.gps_lat,						            new.gps_long,	
	      new.gps_angulo_norte,		  new.gps_posicao_status,			  new.gps_velocidade,					        new.gps_velocidade_media,
	      new.equipamento_ignicao,	new.equipamento_bateria,		  new.equipamento_odometro,			      new.equipamento_rpm,			
	      new.equipamento_veloc,	  new.equipamento_veloc_odom,		new.equipamento_veloc_odom_media,	  new.log_user_ins,	
	      new.log_user_upd,			    new.ope_centro2_equip_id_1,		new.ope_centro2_pessoa_id,			    new.ger_empresa_id,			
	      new.ope_centro2_area_id,	new.geom,						          new.id,                             new.dthr_track);
	  exception when others then null;
      end;
  else    
  begin
    update public.bor_mov_atual
       set id_tipo				        = new.id_tipo,				
           numero_serie				 	  = new.numero_serie,				
           ibutton_rfid				 	  = new.ibutton_rfid,						
           dthr_track				      = new.dthr_track,				
           gps_altitude			      = new.gps_altitude,			
           gps_altitude_status	  = new.gps_altitude_status,		
           gps_lat					 	    = new.gps_lat,						
           gps_long	              = new.gps_long,	
           gps_angulo_norte		    = new.gps_angulo_norte,		
           gps_posicao_status  		= new.gps_posicao_status,			
           gps_velocidade			  	= new.gps_velocidade,						
           gps_velocidade_media   = new.gps_velocidade_media,
           equipamento_ignicao  	= new.equipamento_ignicao,	
           equipamento_bateria  	= new.equipamento_bateria,		
           equipamento_odometro   = new.equipamento_odometro,				
           equipamento_rpm			  = new.equipamento_rpm,			
           equipamento_veloc		  = new.equipamento_veloc,		
           equipamento_veloc_odom		    = new.equipamento_veloc_odom,		
           equipamento_veloc_odom_media = new.equipamento_veloc_odom_media,		
           log_user_ins	          = new.log_user_ins,	
           log_user_upd			      = new.log_user_upd,		
					 log_date_upd           = now(),
           ope_centro2_equip_id	  = new.ope_centro2_equip_id_1,		
           ope_centro2_pessoa_id	= new.ope_centro2_pessoa_id,				
           ger_empresa_id			    = new.ger_empresa_id,			
           ope_centro2_area_id	  = new.ope_centro2_area_id,	
           geom						 	      = new.geom,								
           id                     = new.id,
           dthr_ignicao_last_off  = case when new.equipamento_ignicao != 'ON' then new.dthr_track else dthr_ignicao_last_off end
     where ope_centro2_equip_id = new.ope_centro2_equip_id_1;
  exception when others then null;
  end;
  end if;
  return new;
end; $function$
;

CREATE TRIGGER "trgbor_bor_mov_bui" BEFORE INSERT OR UPDATE ON "public"."bor_mov"
FOR EACH ROW
EXECUTE PROCEDURE "public"."fnbor_bor_mov"();

