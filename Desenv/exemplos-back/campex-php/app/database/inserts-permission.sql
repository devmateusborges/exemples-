INSERT INTO system_group (id, name) VALUES( (SELECT max(g.id) + 1 FROM system_group g) , 'Animal');
INSERT INTO system_user_group (id, system_group_id, system_user_id) VALUES((SELECT max(ug.id) + 1 FROM system_user_group ug), 3, 1);
INSERT INTO system_program (id,name,controller) VALUES( (SELECT max(p.id) + 1 FROM system_program p) , 'SISBOV', 'PecSisbovForm');
INSERT INTO system_group_program (id, system_group_id, system_program_id) VALUES( (SELECT max(gp.id) + 1 FROM system_group_program gp), (SELECT max(g.id) FROM system_group g) , (SELECT max(p.id) FROM system_program p));
INSERT INTO system_program (id,name,controller) VALUES( (SELECT max(p.id) + 1 FROM system_program p) , 'SISBOV', 'PecSisbovHeaderList');
INSERT INTO system_group_program (id, system_group_id, system_program_id) VALUES( (SELECT max(gp.id) + 1 FROM system_group_program gp), (SELECT max(g.id) FROM system_group g) , (SELECT max(p.id) FROM system_program p));
INSERT INTO system_group (id, name) VALUES( (SELECT max(g.id) + 1 FROM system_group g) , 'Geral');
INSERT INTO system_user_group (id, system_group_id, system_user_id) VALUES((SELECT max(ug.id) + 1 FROM system_user_group ug), 4, 1);
INSERT INTO system_program (id,name,controller) VALUES( (SELECT max(p.id) + 1 FROM system_program p) , 'Centro de Custo', 'AdmCcustoForm');
INSERT INTO system_group_program (id, system_group_id, system_program_id) VALUES( (SELECT max(gp.id) + 1 FROM system_group_program gp), (SELECT max(g.id) FROM system_group g) , (SELECT max(p.id) FROM system_program p));
INSERT INTO system_program (id,name,controller) VALUES( (SELECT max(p.id) + 1 FROM system_program p) , 'Centro de Custo', 'AdmCcustoHeaderList');
INSERT INTO system_group_program (id, system_group_id, system_program_id) VALUES( (SELECT max(gp.id) + 1 FROM system_group_program gp), (SELECT max(g.id) FROM system_group g) , (SELECT max(p.id) FROM system_program p));