

for i in 1..20 loop
	
	
	INSERT INTO users("id", "name", "login", "password", "long_x", "created_at", "ponto") VALUES ('f3996813-838e-49af-9649-8dc44e24bc75', pParIdGenerate, pParOpeOcorMovId, pParOpeOcorId, 'obs', pParQntOcor, pParQntOcorCal, 'admin', now(), NULL, NULL, pParOpeOcorStatus, pParDataStatus, pParLat, pParLong, pParPonto);


end loop;

end $$;

-- select * from ope_ocor_mov_det