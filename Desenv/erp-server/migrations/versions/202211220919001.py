from alembic import op


revision = "202211220919001"
down_revision = "202211100921002"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
INSERT INTO sys_document_category (id, name, log_user_ins, log_date_ins, log_user_upd, log_date_upd, active, code_document_category) VALUES('5babdf36-aba1-4ccf-a8b5-438297b76528', 'Default', 'admin', '2022-11-13 14:57:24.000', NULL, NULL, 'S', '...');

ALTER TABLE sys_document add column mov_id varchar(36);
ALTER TABLE sys_document add column fin_pagrec_id varchar(36);
ALTER TABLE sys_document add column ope_centro1_id varchar(36);
ALTER TABLE sys_document add column ope_centro2_id varchar(36);
ALTER TABLE sys_document add column ope_centro2_ord_id varchar(36);
ALTER TABLE sys_document add column ope_compart_id varchar(36);
ALTER TABLE sys_document add column ope_compart_ocor_id varchar(36);
ALTER TABLE sys_document add column ope_ocor_id varchar(36);
ALTER TABLE sys_document add column ger_pessoa_id varchar(36);
ALTER TABLE sys_document add column crm_mov_id varchar(36);
ALTER TABLE sys_document add column sys_user_id varchar(36);
ALTER TABLE sys_document add column cms_post_id varchar(36);

comment on column sys_document.mov_id is 'ID do Movimento';
comment on column sys_document.fin_pagrec_id is 'ID do Pag/Rec';
comment on column sys_document.ope_centro1_id is 'ID do Centro Nível 1 Entrada/Saída';
comment on column sys_document.ope_centro2_id is 'ID do Centro Nível 2 Entrada/Saída';
comment on column sys_document.ope_centro2_ord_id is 'ID da Operação-Ordem';
comment on column sys_document.ope_compart_id is 'ID do Compartamento';
comment on column sys_document.ope_compart_ocor_id is 'ID do Compartamento da Ocorrência';
comment on column sys_document.ope_ocor_id is 'ID da Ocorrência';
comment on column sys_document.ger_pessoa_id is 'ID da Pessoa';
comment on column sys_document.crm_mov_id is 'ID do Movimento - Atendimento';
comment on column sys_document.sys_user_id is 'ID de Usuário';
comment on column sys_document.cms_post_id is 'ID Sistema de Gerenciamento de Conteúdo-Post';

ALTER TABLE sys_document add constraint fk_sys_document_mov_id foreign key (mov_id) references mov;
ALTER TABLE sys_document add constraint fk_sys_document_fin_pagrec_id foreign key (fin_pagrec_id) references fin_pagrec;
ALTER TABLE sys_document add constraint fk_sys_document_ope_centro1_id foreign key (ope_centro1_id) references ope_centro1;
ALTER TABLE sys_document add constraint fk_sys_document_ope_centro2_id foreign key (ope_centro2_id) references ope_centro2;
ALTER TABLE sys_document add constraint fk_sys_document_ope_centro2_ord_id foreign key (ope_centro2_ord_id) references ope_centro2_ord;
ALTER TABLE sys_document add constraint fk_sys_document_ope_compart_id foreign key (ope_compart_id) references ope_compart;
ALTER TABLE sys_document add constraint fk_sys_document_ope_compart_ocor_id foreign key (ope_compart_ocor_id) references ope_compart_ocor;
ALTER TABLE sys_document add constraint fk_sys_document_ope_ocor_id foreign key (ope_ocor_id) references ope_ocor;
ALTER TABLE sys_document add constraint fk_sys_document_ger_pessoa_id foreign key (ger_pessoa_id) references ger_pessoa;  
ALTER TABLE sys_document add constraint fk_sys_document_crm_mov_id foreign key (crm_mov_id) references crm_mov; 
ALTER TABLE sys_document add constraint fk_sys_document_sys_user_id foreign key (sys_user_id) references sys_user;  
ALTER TABLE sys_document add constraint fk_sys_document_cms_post_id foreign key (cms_post_id) references cms_post; 

ALTER TABLE sys_document add column test1_id varchar(36);
comment on column sys_document.test1_id is 'ID do Teste 1';
ALTER TABLE sys_document add constraint fk_sys_document_test1_id foreign key (test1_id) references test1; 

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d5f90056-35bd-4a24-a76b-896a50e9b0f0',(select id from sys_program where controller like '%/fisncm'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('5382333e-3fb3-4455-8d78-9750a28733f7',(select id from sys_program where controller like '%/fisncm'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('005f338c-2dce-4f33-aadb-fd5481d23319',(select id from sys_program where controller like '%/fisncm'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('fa1510e4-dbb8-4054-9c3d-ca2cb788d322',(select id from sys_program where controller like '%/fisncm'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/fisncm') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/fisncm') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/fisncm') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/fisncm') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('e96252ed-aa1a-47f2-9660-2b1f62467525',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('838d3924-a969-4264-95b4-baae2a3dd4ce',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('3b46b40c-ea48-49f5-8165-15e76a59acf5',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('a31e787a-3fa5-40cb-95f4-5f12ebf49fc2',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('07198a9e-9771-406a-a875-848183b6d666',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'ADD_DET0'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('a9a8a329-5498-490e-988c-150db7cd01c8',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'EDIT_DET0'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('a8db9f83-dc1b-4fa3-9c54-4e88c0dee8e8',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'DELETE_DET0'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('199c76c4-dbbf-473a-9695-e3891b09e45b',(select id from sys_program where controller like '%/opeatividade'),(select id from sys_action sa  where code = 'SAVE_DET0'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'ADD_DET0')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'EDIT_DET0')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'DELETE_DET0')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividade') and sys_action_id = (select id from sys_action sa  where code = 'SAVE_DET0')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('0d61a6ed-e5ab-44be-bdf4-32e8a4ee1593',(select id from sys_program where controller like '%/opeatividadegrupo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('b685ee07-1fda-48c3-8e38-a131faac58df',(select id from sys_program where controller like '%/opeatividadegrupo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('34708607-f06f-422c-9105-8c4a4bc05dcc',(select id from sys_program where controller like '%/opeatividadegrupo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('ecd77f39-f7fb-4df3-9afb-381d86ab3da5',(select id from sys_program where controller like '%/opeatividadegrupo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadegrupo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadegrupo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadegrupo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadegrupo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('8b947507-63b0-497a-8ff3-1158c3368fab',(select id from sys_program where controller like '%/opeatividadesistema'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('675bd6ab-a81b-4b42-a78c-54df618c86d9',(select id from sys_program where controller like '%/opeatividadesistema'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('87deeaf9-1764-4978-b8cd-6b1d0e0462a5',(select id from sys_program where controller like '%/opeatividadesistema'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('0dc16627-17f2-4031-b0d8-4fcc67fdec81',(select id from sys_program where controller like '%/opeatividadesistema'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadesistema') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadesistema') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadesistema') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeatividadesistema') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('7e5bd6cc-ff00-4215-bef2-b40d2a290caa',(select id from sys_program where controller like '%/opecentro2ordstatus'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('7b0b92c7-7780-4349-9951-b308bd691bc9',(select id from sys_program where controller like '%/opecentro2ordstatus'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('e46cb5fa-ad78-47ff-af9e-e61bb6371152',(select id from sys_program where controller like '%/opecentro2ordstatus'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('7d3fecc0-558a-451b-a732-ba1ccb2d8488',(select id from sys_program where controller like '%/opecentro2ordstatus'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordstatus') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordstatus') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordstatus') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordstatus') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('40129884-ef31-4e10-8ab6-5d30fefdfac5',(select id from sys_program where controller like '%/opecentro2ordtipo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('c168571e-9311-4f0f-a779-8d19dce7daee',(select id from sys_program where controller like '%/opecentro2ordtipo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('3ada289b-846c-4869-9135-c847f0c3f62c',(select id from sys_program where controller like '%/opecentro2ordtipo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('344352a1-9f48-441f-a640-0b6406d62235',(select id from sys_program where controller like '%/opecentro2ordtipo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordtipo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordtipo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordtipo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentro2ordtipo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('3e5a324d-a469-422f-9fa0-64a35e82e024',(select id from sys_program where controller like '%/opecentrotipo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('8741cd83-41c1-4609-b538-fd0fd96b2d18',(select id from sys_program where controller like '%/opecentrotipo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('4ac7bef0-abba-4b19-9b5b-d7702a8204ef',(select id from sys_program where controller like '%/opecentrotipo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('c879a79c-ae8e-4f58-b333-d3efa9c50dbd',(select id from sys_program where controller like '%/opecentrotipo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentrotipo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentrotipo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentrotipo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecentrotipo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('ced2511b-5419-4e31-92e7-e758c89bcfeb',(select id from sys_program where controller like '%/opeciclovar'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('75aec4f7-26f3-42bc-aa8f-f8417eb30cbe',(select id from sys_program where controller like '%/opeciclovar'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('2816f161-0382-46ee-b74f-4137bafc66eb',(select id from sys_program where controller like '%/opeciclovar'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('5ecb7ee7-96f0-4a3d-bd90-a6166c5f508e',(select id from sys_program where controller like '%/opeciclovar'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeciclovar') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeciclovar') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeciclovar') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeciclovar') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('8012af8d-db59-42e0-8671-1df2ebc78e47',(select id from sys_program where controller like '%/opecompart'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('2e0e7795-7b07-4a2a-b145-8930562b5d36',(select id from sys_program where controller like '%/opecompart'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('ee37e72c-33d0-4e86-a687-b4b30e5885c2',(select id from sys_program where controller like '%/opecompart'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('2d38d98b-4778-426a-9d3f-8bd9f0e6e854',(select id from sys_program where controller like '%/opecompart'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompart') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompart') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompart') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompart') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('a354fd22-078c-4dbb-8f24-4cc28820920c',(select id from sys_program where controller like '%/opecompartgrupo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('938a1c8c-8acc-4529-a18e-027dcb09dd87',(select id from sys_program where controller like '%/opecompartgrupo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d1187408-ea7b-40e8-85c1-5a192bbaef3a',(select id from sys_program where controller like '%/opecompartgrupo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('ee40bcb9-a460-4d1d-a956-aa8c0cf90e9f',(select id from sys_program where controller like '%/opecompartgrupo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartgrupo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartgrupo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartgrupo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartgrupo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('726e1d89-50f8-48a7-b639-56de240b160d',(select id from sys_program where controller like '%/opecompartmedida'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('819c9cf4-8e98-48a6-948b-dfb60aa97195',(select id from sys_program where controller like '%/opecompartmedida'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('100e1bd9-649a-472c-8ed6-f46863f0c8a2',(select id from sys_program where controller like '%/opecompartmedida'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('522f7e12-3977-4442-a53d-b5a8ae785601',(select id from sys_program where controller like '%/opecompartmedida'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartmedida') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartmedida') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartmedida') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartmedida') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('ea0bff2c-dd24-4fd0-b867-21520575e903',(select id from sys_program where controller like '%/opecompartposicao'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('81c7719d-2586-4d31-b6c6-06dca1ae786b',(select id from sys_program where controller like '%/opecompartposicao'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('10c5e23e-a939-476c-bfb4-b1c974104742',(select id from sys_program where controller like '%/opecompartposicao'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('9bd46f9a-9b7c-4b36-ab53-65266f5067a7',(select id from sys_program where controller like '%/opecompartposicao'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartposicao') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartposicao') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartposicao') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartposicao') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('534ba295-babc-41ca-a19d-a830d22b6d29',(select id from sys_program where controller like '%/opecompartstatus'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('e9e98874-4ab0-44ee-b91a-5d5a5477dd33',(select id from sys_program where controller like '%/opecompartstatus'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('e07a4f90-2432-4655-b318-96e1dafc2017',(select id from sys_program where controller like '%/opecompartstatus'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d99423f7-e661-4eb7-a78e-e3f6efed0277',(select id from sys_program where controller like '%/opecompartstatus'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartstatus') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartstatus') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartstatus') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecompartstatus') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('b7219013-9534-4b27-81f9-59310c7b033d',(select id from sys_program where controller like '%/opecomparttipo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('ce109bfe-a1e2-45ee-bd61-c7c84334dc32',(select id from sys_program where controller like '%/opecomparttipo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('4b2c9f63-12f0-4813-b939-87aa5c09f9f0',(select id from sys_program where controller like '%/opecomparttipo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d13159dd-e983-40b9-ab64-c228f32e0417',(select id from sys_program where controller like '%/opecomparttipo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecomparttipo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecomparttipo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecomparttipo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opecomparttipo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('e53a0d6e-10f2-4ef0-8a2f-2a710b570765',(select id from sys_program where controller like '%/opeespac'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('549e8ce6-8bda-49d0-adb1-b30c03878af0',(select id from sys_program where controller like '%/opeespac'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('ff78ceda-274f-4607-8d2c-5871df951874',(select id from sys_program where controller like '%/opeespac'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d55981c6-e808-4a61-b950-43aa8b04bdd5',(select id from sys_program where controller like '%/opeespac'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeespac') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeespac') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeespac') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeespac') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('90c540c9-5045-43b4-8c09-29724180d7bf',(select id from sys_program where controller like '%/opeestagio'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('a8f6059c-4835-46ab-955c-57e904762362',(select id from sys_program where controller like '%/opeestagio'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('50131bf0-c072-461b-9df0-af179c535706',(select id from sys_program where controller like '%/opeestagio'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('58034aa4-d17f-42cf-aa58-d37041c98d94',(select id from sys_program where controller like '%/opeestagio'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeestagio') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeestagio') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeestagio') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeestagio') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('22d722e6-a676-4015-b50c-aa59a0a640a4',(select id from sys_program where controller like '%/opefrentetrabalho'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d95ab9a9-9a77-41aa-a5f9-2081976636e6',(select id from sys_program where controller like '%/opefrentetrabalho'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('f0f5b4a1-5b0e-48a8-a296-3ae69ab47c5a',(select id from sys_program where controller like '%/opefrentetrabalho'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('e58c8c11-e80c-4af2-be90-cf95d2db7087',(select id from sys_program where controller like '%/opefrentetrabalho'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opefrentetrabalho') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opefrentetrabalho') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opefrentetrabalho') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opefrentetrabalho') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('a137c1f3-e15a-4c1f-8e54-0910cf2fa295',(select id from sys_program where controller like '%/opeocor'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('f796cf88-1716-431d-aaed-21d1fc10e45f',(select id from sys_program where controller like '%/opeocor'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('9ad8c0a2-2734-4082-acfb-de65baae18b5',(select id from sys_program where controller like '%/opeocor'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('74081987-c93a-4bcf-b3ee-0d9c3acdb880',(select id from sys_program where controller like '%/opeocor'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocor') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocor') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocor') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocor') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d514263e-210c-42de-89ec-d880b06ea084',(select id from sys_program where controller like '%/opeocorgrupo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('edd7a309-87e0-4ddf-81c8-021197ff63d5',(select id from sys_program where controller like '%/opeocorgrupo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('d6e8bf11-72c5-4798-bad3-47658f450076',(select id from sys_program where controller like '%/opeocorgrupo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('c7d96989-2143-4bc9-836c-923bfd386c43',(select id from sys_program where controller like '%/opeocorgrupo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorgrupo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorgrupo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorgrupo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorgrupo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('15d9b2e9-3bf7-4cf2-8c68-ca72f31b75fe',(select id from sys_program where controller like '%/opeocorstatus'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('30f1f444-d07e-4c53-8978-4ef6a025451e',(select id from sys_program where controller like '%/opeocorstatus'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('696d7487-5e0e-4ff5-afaa-356ee17b3ee5',(select id from sys_program where controller like '%/opeocorstatus'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('a38b1ce9-57c9-4e6f-982e-9a1df7e1b292',(select id from sys_program where controller like '%/opeocorstatus'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorstatus') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorstatus') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorstatus') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocorstatus') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('09e75e75-63ec-4542-a68f-b3c3394e99a4',(select id from sys_program where controller like '%/opeocortipo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('784a3a9b-cde4-40a2-9cf5-dd934344483c',(select id from sys_program where controller like '%/opeocortipo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('38b31a63-3a61-466f-807e-2ce7de1d0be6',(select id from sys_program where controller like '%/opeocortipo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('de2cd212-8be1-46fc-abec-5d56f6dab366',(select id from sys_program where controller like '%/opeocortipo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocortipo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocortipo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocortipo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeocortipo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('4eea842d-fed3-41ec-9aad-55afab98c24a',(select id from sys_program where controller like '%/operegiao'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('93b737a8-cb7f-41f3-b9ab-c1cef2e7ce3b',(select id from sys_program where controller like '%/operegiao'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('1a675dda-c296-40b4-9ec1-ed550c10de62',(select id from sys_program where controller like '%/operegiao'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('0a80b9d2-9a05-430d-b612-49cbb1c3ae5e',(select id from sys_program where controller like '%/operegiao'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/operegiao') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/operegiao') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/operegiao') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/operegiao') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('b9275cef-fb7b-4a54-8dcf-b7936e277a1f',(select id from sys_program where controller like '%/opetiposolo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('40b337b0-2f07-473f-b873-25f6fed72fbf',(select id from sys_program where controller like '%/opetiposolo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('21a08ed5-009c-4968-90af-3052630c8b71',(select id from sys_program where controller like '%/opetiposolo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('8b715974-b557-4866-b7a2-5b880e209bfa',(select id from sys_program where controller like '%/opetiposolo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opetiposolo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opetiposolo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opetiposolo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opetiposolo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('5cac8a51-24f9-4981-97df-468a28021a82',(select id from sys_program where controller like '%/opeunitparam'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('55611bce-b98f-4446-b3d8-0f1cb3e3b03d',(select id from sys_program where controller like '%/opeunitparam'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('f2623b4a-71d1-4b4c-9f3a-5ce3d4c2080e',(select id from sys_program where controller like '%/opeunitparam'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('b74a2316-0678-45f6-94ab-a295e204a5fa',(select id from sys_program where controller like '%/opeunitparam'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeunitparam') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeunitparam') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeunitparam') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeunitparam') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('1a83be15-63dc-48d9-b67b-301983888c14',(select id from sys_program where controller like '%/opeperiodo'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('2d6ad152-c846-41df-be60-5eb9b21db84c',(select id from sys_program where controller like '%/opeperiodo'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('3bfe4744-3e24-4b0a-9ce7-55510944f536',(select id from sys_program where controller like '%/opeperiodo'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('0c73b9e4-bcf6-498a-b916-896ad44733de',(select id from sys_program where controller like '%/opeperiodo'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeperiodo') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeperiodo') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeperiodo') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/opeperiodo') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

insert into sys_program_action (id, sys_program_id, sys_action_id) values ('0808661c-f5ba-4f38-bffe-06c901475c4c',(select id from sys_program where controller like '%/geritemservvar'),(select id from sys_action sa  where code = 'ADD'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('b121bef7-09f9-481d-b78f-b3f58e3efb46',(select id from sys_program where controller like '%/geritemservvar'),(select id from sys_action sa  where code = 'EDIT'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('c9d8202a-8f2a-4bc7-8640-36089b83b027',(select id from sys_program where controller like '%/geritemservvar'),(select id from sys_action sa  where code = 'DELETE'));
insert into sys_program_action (id, sys_program_id, sys_action_id) values ('342b4721-a062-43e2-98d5-0937dcf719f9',(select id from sys_program where controller like '%/geritemservvar'),(select id from sys_action sa  where code = 'SAVE'));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/geritemservvar') and sys_action_id = (select id from sys_action sa  where code = 'ADD')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/geritemservvar') and sys_action_id = (select id from sys_action sa  where code = 'EDIT')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/geritemservvar') and sys_action_id = (select id from sys_action sa  where code = 'DELETE')));
insert into sys_group_program_action (sys_group_id, sys_program_action_id) values ('4218d8f1-8595-4052-aace-ba36f772623e', (select id from sys_program_action where sys_program_id = (select id from sys_program where controller like '%/geritemservvar') and sys_action_id = (select id from sys_action sa  where code = 'SAVE')));

create table test1a_child (
	unit_id varchar(36) NOT NULL,
	id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
	observacao varchar(250) NOT NULL,
	log_user_ins varchar(100),
	log_date_ins timestamp(0) DEFAULT now(),
	log_user_upd varchar(100),
	log_date_upd timestamp(0),
	CONSTRAINT pk_tst_test1a_child PRIMARY KEY (id)
)
WITHOUT OIDS;
COMMENT ON TABLE test1a_child IS 'Test-Documentos';
COMMENT ON COLUMN test1a_child.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN test1a_child.observacao IS 'ID da Unidade';
COMMENT ON COLUMN test1a_child.id IS 'ID do Documentos';
COMMENT ON COLUMN test1a_child.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN test1a_child.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN test1a_child.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN test1a_child.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE test1a_child OWNER TO postgres;

update sys_type_description set value_type = description_type, description_type  = value_type where table_name = 'sys_document' and field_name = 'content_type';
ALTER TABLE sys_type_description ALTER COLUMN value_type TYPE varchar(100) USING value_type::varchar;
ALTER TABLE sys_document ALTER COLUMN content_type TYPE varchar(100) USING content_type::varchar;
update sys_type_description set value_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' where table_name = 'sys_document' and field_name = 'content_type' and value_type = 'application/xlsx';
update sys_type_description set value_type = description_type, description_type  = value_type where table_name = 'sys_document' and field_name = 'content_type';
update sys_type_description set value_type = 'application/html' where table_name = 'sys_document' and field_name = 'content_type' and value_type = 'application/HTML';

alter table sys_document add column test1_child_id varchar(36);
alter table sys_document add column test1a_child_id varchar(36);

ALTER TABLE sys_document add constraint fk_test1_child_id foreign key (test1_child_id) references test1_child;
ALTER TABLE sys_document add constraint fk_test1a_child_id foreign key (test1a_child_id) references test1a_child;

comment on column sys_document.test1_child_id is 'ID do Teste 1 Child 1';
comment on column sys_document.test1a_child_id is 'ID do Teste 1 Child 1a';

alter table test1a_child add column test1_id varchar(36);
ALTER TABLE test1a_child add constraint fk_test1_id foreign key (test1_id) references test1;

INSERT INTO public.ger_per_tipo (unit_id, id, nome, ativo, sigla_per_tipo, log_user_ins, log_date_ins, log_user_upd, log_date_upd, ini_semana) VALUES('f3996813-838e-49af-9649-8dc44e24bc75', 'c39ac4a7-a460-450d-86cf-6790b61d382c', 'Default', 'S', 'DEFAULT', NULL, '2022-11-29 08:56:22.000', NULL, NULL, '1');

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
--actions
delete from sys_group_program_action a where sys_group_id in('4218d8f1-8595-4052-aace-ba36f772623e','0256e515-51a4-49a2-a8b8-adc36470cd51');
--actions - interno
insert into sys_group_program_action(id,sys_group_id,sys_program_action_id)
select uuid_generate_v4(),'4218d8f1-8595-4052-aace-ba36f772623e', c.id
from sys_program b 
join sys_program_action c on(b.id = c.sys_program_id);
commit;
--actions - unit
insert into sys_group_program_action(id,sys_group_id,sys_program_action_id)
select uuid_generate_v4(),'0256e515-51a4-49a2-a8b8-adc36470cd51', c.id
from sys_program b 
join sys_program_action c on(b.id = c.sys_program_id) where b.admin='N';
commit;
"""
    )


def downgrade():
    pass
