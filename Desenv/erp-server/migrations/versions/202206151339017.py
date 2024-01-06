from alembic import op
import sqlalchemy as sa

revision = '202206151339017'
down_revision = '202206151339016'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""


INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value) 
VALUES ('a95523e8-eaf6-49c4-b6e6-dbf871571e2f', 'Limite de fazendas', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('99d94b26-e2e9-4734-bb33-dd2819bd6f7b', 'Limite de lotes animais', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('fd554963-84a1-4ff5-be38-1ca59d191170', 'Limite de equipamentos', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('9f42d6b8-dfab-4f6a-a5b5-345b5c34f490', 'Limite de funcionarios', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('c4cf4f41-c997-4978-8429-a4814c2c120f', 'Limite de materiais/serviÃ§os', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('63f44e43-8012-4ab6-bec7-f8053b46e3f2', 'Utiliza emissÃ£o NFE', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('63b952a4-970e-4df9-892e-2a771613d36d', 'Utiliza emissÃ£o CTE', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('77184dfc-4ca5-4a3d-b44e-342cee684e34', 'Utiliza apuracao LCDPR', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('c0b8eb6a-ea68-4de1-b779-97af7ffd9245', 'Utiliza conciliacao bancÃ¡ria integrada', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('699c1cc5-a71d-403a-a7fc-1b0e52252762', 'Utiliza emissÃ£o de boleto integrado', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('5549653e-5d11-4a83-b644-3309f2c3fcd6', 'Utiliza ordem de serviÃ§o programada', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('c1764231-869d-428b-a67b-4319271281e3', 'Utiliza pagamento via CNAB', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('8e44b028-d418-4712-8738-0461e48d76af', 'Utiliza modulo CRM', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('3e76241d-1a7f-459e-96cd-b15ea9db8fa2', 'Utiliza modulo BOV', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('423a9d75-f2bb-48b1-9cd3-6273fc632f53', 'Utiliza modulo BOR', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('cfc30725-0b30-4f68-a482-cf10a48681ef', 'Utiliza modulo PTO', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('c6365950-680d-42ca-b5e0-c86ca9f7183c', 'Utiliza modulo RHM', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');
INSERT INTO sys_restriction(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active,type_value)
VALUES ('6f411fd2-8499-4400-b1d1-7677b4ebbaf8', 'Utiliza Monitoramento/Qualidade', 'admin', '2020-05-26 11:35:31', NULL, NULL, NULL,'L');

DELETE FROM sys_plan_restriction WHERE sys_restriction_id='0cb07802-7cfa-425b-890e-44075d6e75b1';
DELETE FROM sys_restriction WHERE id='0cb07802-7cfa-425b-890e-44075d6e75b1';


--Plano Trial
delete from sys_plan_restriction where sys_plan_id='09cfa735-9357-495e-bfac-4d35cbb8c172';
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('b86c10e3-0efe-4211-83a6-84b0b21e0007', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'c7924fb8-b0f5-49ae-9d17-311cf96f545e', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('391df2c7-f85d-4ddb-8291-b4fab0a1a2df', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '31da7d22-1925-4f32-85cc-d578834aad3a', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('ee313e7f-2cea-427b-a536-69e2ad9e5956', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'a95523e8-eaf6-49c4-b6e6-dbf871571e2f', 999999, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('859e00c0-9592-4be1-940c-b1dec70a63f0', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '99d94b26-e2e9-4734-bb33-dd2819bd6f7b', 999999, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('bd2b6ae7-58e4-4328-a1ab-9039c1b17ba1', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'fd554963-84a1-4ff5-be38-1ca59d191170', 999999, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('31083f21-5697-443a-bc8f-7568923153cb', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '9f42d6b8-dfab-4f6a-a5b5-345b5c34f490', 999999, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('9544ae2a-e31b-4fe0-8482-d14cd6b6581c', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'c4cf4f41-c997-4978-8429-a4814c2c120f', 999999, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('98967570-9265-4914-8c85-be41efc5fc32', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '63f44e43-8012-4ab6-bec7-f8053b46e3f2', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('a0044f82-7016-4d8a-8766-275fcc13c9e8', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '63b952a4-970e-4df9-892e-2a771613d36d', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('9a7920f5-ae8d-4f03-a79b-addee8d172cc', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '77184dfc-4ca5-4a3d-b44e-342cee684e34', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('364fa4de-481a-4544-b196-af8cd7d2c26a', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'c0b8eb6a-ea68-4de1-b779-97af7ffd9245', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('ea8a78c6-d48d-41ce-ae1e-d00b81d1f218', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '699c1cc5-a71d-403a-a7fc-1b0e52252762', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('f8443ee6-035e-456d-9183-8208e2b050fb', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '5549653e-5d11-4a83-b644-3309f2c3fcd6', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('3cf35367-2965-442c-8aac-832cca77f0c2', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'c1764231-869d-428b-a67b-4319271281e3', 1, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('90807a67-82c8-49d2-9562-9cdd72036db2', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '8e44b028-d418-4712-8738-0461e48d76af', 0, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('39c12146-dd48-4ee1-a140-e31ff397dd60', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '3e76241d-1a7f-459e-96cd-b15ea9db8fa2', 0, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('0750b3fd-7d26-4723-91b5-daf6179a542d', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '423a9d75-f2bb-48b1-9cd3-6273fc632f53', 0, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('4368b5a3-2db6-4a30-bb8c-69a0938586ce', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'cfc30725-0b30-4f68-a482-cf10a48681ef', 0, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('57c40416-fdf0-41dd-ab5d-6b49fb6889a1', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', 'c6365950-680d-42ca-b5e0-c86ca9f7183c', 0, 0, 30, 15);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('6ff1dfa9-187b-4791-9bef-4aceb82d3317', 'admin', '2020-05-26 11:49:04', NULL, NULL, '09cfa735-9357-495e-bfac-4d35cbb8c172', '6f411fd2-8499-4400-b1d1-7677b4ebbaf8', 1, 0, 30, 15);

INSERT INTO sys_plan(id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, type_plan, sys_id, description, active, indicated) VALUES ('47bf23c2-61e5-482a-af8e-8b08fba598e7', 'Basic', 'admin', '2020-05-26 11:33:18', NULL, NULL, 'PG', 'e8329d00-443f-4c03-8e73-c161f0d4f37d', 'Plano Basic (Pago)', 'S', 'S');


--Plano Basic (Pago)
delete from sys_plan_restriction where sys_plan_id='47bf23c2-61e5-482a-af8e-8b08fba598e7';
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('4d14d6c7-65bd-45b3-83ce-65ee6cc7f228', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'c7924fb8-b0f5-49ae-9d17-311cf96f545e', 5, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('748c751c-2430-4e04-88b6-52bd4eb6a457', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '31da7d22-1925-4f32-85cc-d578834aad3a', 5, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('b02e7f98-9b98-4793-a847-bfcacc27392d', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'a95523e8-eaf6-49c4-b6e6-dbf871571e2f', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('52e876eb-287e-4892-866b-3908f34d63be', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '99d94b26-e2e9-4734-bb33-dd2819bd6f7b', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('2a8259e4-5e8f-4c4e-9178-b14f96249224', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'fd554963-84a1-4ff5-be38-1ca59d191170', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('f60418e0-8472-4ba6-b439-b893d6300050', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '9f42d6b8-dfab-4f6a-a5b5-345b5c34f490', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('ca197d19-6a15-4742-ae9a-0e1748f6df99', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'c4cf4f41-c997-4978-8429-a4814c2c120f', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('d09b6772-4aa2-42f3-abcf-26e11ec2624f', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '63f44e43-8012-4ab6-bec7-f8053b46e3f2', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('ab94a672-a7e6-4f80-938d-fbc7ae38b51b', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '63b952a4-970e-4df9-892e-2a771613d36d', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('44d55422-9458-4301-97e8-f53c9c6ec669', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '77184dfc-4ca5-4a3d-b44e-342cee684e34', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('b63cb47c-4070-4af8-af66-56f6948dcb3c', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'c0b8eb6a-ea68-4de1-b779-97af7ffd9245', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('e8952bdd-fe43-430e-a67e-bfbfc0f24fee', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '699c1cc5-a71d-403a-a7fc-1b0e52252762', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('224b5dc4-7dd2-44b4-9b5a-4e2f60a050df', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '5549653e-5d11-4a83-b644-3309f2c3fcd6', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('ffdc1f60-62f0-494e-b3cc-85cebc79b485', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'c1764231-869d-428b-a67b-4319271281e3', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('348c71d6-3914-4f44-8913-820c981ed4af', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '8e44b028-d418-4712-8738-0461e48d76af', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('d2d8218a-db9b-42f9-839f-e320162fa8b0', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '3e76241d-1a7f-459e-96cd-b15ea9db8fa2', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('509cb6a5-8c02-4760-a0d2-8375b6108737', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '423a9d75-f2bb-48b1-9cd3-6273fc632f53', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('59c96311-d0b1-4117-981b-e1645d34ca81', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'cfc30725-0b30-4f68-a482-cf10a48681ef', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('7f77a26c-360d-4adf-b0f6-d859666d73c4', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', 'c6365950-680d-42ca-b5e0-c86ca9f7183c', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('00e5fe37-69a2-4a88-a512-bf2dc400ef03', 'admin', '2020-05-26 11:49:04', NULL, NULL, '47bf23c2-61e5-482a-af8e-8b08fba598e7', '6f411fd2-8499-4400-b1d1-7677b4ebbaf8', 0, 0, 999999,999999);


--Plano Free
delete from sys_plan_restriction where sys_plan_id='d5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103';
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('07d57007-1f0c-42d4-a2ed-031a7458d4b3', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'c7924fb8-b0f5-49ae-9d17-311cf96f545e', 5, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('735ba869-91d8-4dc0-93c2-d159a9202f97', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '31da7d22-1925-4f32-85cc-d578834aad3a', 5, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('4a07a470-6f12-485e-a52c-6b0f165148bb', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'a95523e8-eaf6-49c4-b6e6-dbf871571e2f', 3, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('26c208dd-3de6-44b1-ba27-a6572df0232a', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '99d94b26-e2e9-4734-bb33-dd2819bd6f7b', 3, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('fef7f507-70b0-4db3-89d5-f51990062a51', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'fd554963-84a1-4ff5-be38-1ca59d191170', 10, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('4f4b7b37-a4b3-4fab-a3d0-a8a05cb6b5c6', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '9f42d6b8-dfab-4f6a-a5b5-345b5c34f490', 10, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('f643eb00-5c2a-42ab-9c91-a92338649b24', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'c4cf4f41-c997-4978-8429-a4814c2c120f', 30, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('d721ec38-8794-4ced-8e15-8ad7fb312bfa', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '63f44e43-8012-4ab6-bec7-f8053b46e3f2', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('2cf7c044-9e6d-4d06-be58-fd8e033bbc37', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '63b952a4-970e-4df9-892e-2a771613d36d', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('c6644fd8-166c-46b9-a7d3-3ed65fb10f19', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '77184dfc-4ca5-4a3d-b44e-342cee684e34', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('bf7f1f03-3ba5-4525-aa55-43d285fcb530', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'c0b8eb6a-ea68-4de1-b779-97af7ffd9245', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('c3d908d8-812d-41e7-b20a-e1d1cf88476c', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '699c1cc5-a71d-403a-a7fc-1b0e52252762', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('d8cd95ec-f6c7-4d1b-91c7-12c985ab607d', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '5549653e-5d11-4a83-b644-3309f2c3fcd6', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('fc0478a2-c973-4b4c-a3f2-680210164495', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'c1764231-869d-428b-a67b-4319271281e3', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('edd3f006-c4c2-46ce-8304-2e24403b4eb9', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '8e44b028-d418-4712-8738-0461e48d76af', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('701eee5b-52b7-4354-a8ad-2da68c7c06cf', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '3e76241d-1a7f-459e-96cd-b15ea9db8fa2', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('56fa0333-29e2-4132-be1a-2b892c7e2984', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '423a9d75-f2bb-48b1-9cd3-6273fc632f53', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('bf754ad5-9252-4883-8cf9-2a9131ef8c72', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'cfc30725-0b30-4f68-a482-cf10a48681ef', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('5df0f7fb-6aba-4ddd-be90-3575e542ab98', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', 'c6365950-680d-42ca-b5e0-c86ca9f7183c', 0, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('d64873c7-8063-4978-a91f-a4e0382dec44', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'd5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103', '6f411fd2-8499-4400-b1d1-7677b4ebbaf8', 0, 0, 999999,999999);
--Plano Full (Pago)
delete from sys_plan_restriction where sys_plan_id='b934c023-f458-4b24-b626-556a6c25afdf';
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('e3de7d02-e9ab-4508-8761-16933f74a687', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'c7924fb8-b0f5-49ae-9d17-311cf96f545e', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('13d04dd5-e2d6-4e5d-9f0a-65ee2b310e89', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '31da7d22-1925-4f32-85cc-d578834aad3a', 50, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('ffc3cfbc-0ab1-4f09-b46e-569bf7c024fd', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'a95523e8-eaf6-49c4-b6e6-dbf871571e2f', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('19eb6ee4-fb59-46df-ab46-362bac12798d', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '99d94b26-e2e9-4734-bb33-dd2819bd6f7b', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('5058361b-7763-4c0e-a269-ba976f778194', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'fd554963-84a1-4ff5-be38-1ca59d191170', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('f7168e09-72a3-468e-b88f-34f2e2c9e7de', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '9f42d6b8-dfab-4f6a-a5b5-345b5c34f490', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('9c85113d-4fb9-47f5-b392-57313c357857', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'c4cf4f41-c997-4978-8429-a4814c2c120f', 999999, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('6735f572-cc50-40c4-affd-4f32e0434272', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '63f44e43-8012-4ab6-bec7-f8053b46e3f2', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('44f94f2f-6eaf-4b96-91de-392287513185', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '63b952a4-970e-4df9-892e-2a771613d36d', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('09f0df7a-9f72-4a59-b776-0df537c26375', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '77184dfc-4ca5-4a3d-b44e-342cee684e34', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('647d3e4d-2a56-4cb2-922c-12ded42e7319', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'c0b8eb6a-ea68-4de1-b779-97af7ffd9245', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('a6f40696-f3f1-4497-847c-deb137098dca', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '699c1cc5-a71d-403a-a7fc-1b0e52252762', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('f08c0fb0-65e6-469e-92b0-3fcaa0e5ed50', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '5549653e-5d11-4a83-b644-3309f2c3fcd6', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('bc5db446-7d0a-4bdb-90fe-9a826e59e798', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'c1764231-869d-428b-a67b-4319271281e3', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('dd1440c5-ccd6-477d-822b-753cd0aad49f', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '8e44b028-d418-4712-8738-0461e48d76af', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('08bd5d75-9286-45f0-a18a-83bf6986d553', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '3e76241d-1a7f-459e-96cd-b15ea9db8fa2', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('b7e1b74f-463d-40c8-b6e3-d8068a2300cd', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '423a9d75-f2bb-48b1-9cd3-6273fc632f53', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('a7626eb5-47d0-458d-ada1-41f6f2c15db8', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'cfc30725-0b30-4f68-a482-cf10a48681ef', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('d2bceefb-4817-4675-bff3-364301c35989', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', 'c6365950-680d-42ca-b5e0-c86ca9f7183c', 1, 0, 999999,999999);
INSERT INTO sys_plan_restriction(id, log_user_ins, log_date_ins, log_user_upd, log_date_upd, sys_plan_id, sys_restriction_id, value_restriction, value_restriction_blocked, days_blocked_extra, days_blocked) VALUES ('150d6bb7-63b7-4f72-a40e-332c2851f0eb', 'admin', '2020-05-26 11:49:04', NULL, NULL, 'b934c023-f458-4b24-b626-556a6c25afdf', '6f411fd2-8499-4400-b1d1-7677b4ebbaf8', 1, 0, 999999,999999);




--================================================================
--Liberar acesso para todos usuários
--================================================================
--admin interno
delete from sys_group_program a where sys_group_id='4218d8f1-8595-4052-aace-ba36f772623e';
insert into sys_group_program(id,sys_group_id,sys_program_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', b.id
from sys_program b;
--admin unit
delete from sys_group_program a where sys_group_id='0256e515-51a4-49a2-a8b8-adc36470cd51';
insert into sys_group_program(id,sys_group_id,sys_program_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', b.id
from sys_program b where b.admin='N';
commit;
               """)


def downgrade():
    pass