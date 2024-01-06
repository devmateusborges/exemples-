from alembic import op
import sqlalchemy as sa

revision = '202206151339037'
down_revision = '202206151339036'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
------ UPDATE

UPDATE public.sys_type_description
	SET table_name='default_tipo_es'
	WHERE id='6e3738ee-412b-4beb-ac19-e9febd8d3445';


UPDATE public.sys_type_description
	SET table_name='default_tipo_es'
	WHERE id='508f92f5-5600-42b7-8229-b80fad5be2c9';

-- Auto-generated SQL script #202209131505
UPDATE public.sys_type_description
	SET table_name='default_sn'
	WHERE id='92225dc1-4559-474f-9976-fd9bf2f266ce';

UPDATE public.sys_type_description
	SET table_name='default_sn'
	WHERE id='72d16147-0e44-46a1-a9ee-9e5d5fd23660';

-------------------------------------- 
---   SYS
-------------------------------------- 
---Sys Licence

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('39298df1-ee8a-4e92-8c67-826556e8083c','sys_licence','admin','status','AT','Ativo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('aac1dee1-fdb2-411e-a321-1352d92664fc','sys_licence','admin','status','PA','Pend. Ativação');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5abd6870-47c4-4d39-bc2a-56df5b2750e4','sys_licence','admin','status','PF','Pend. Financeira');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f22419d5-4a33-4e5f-932f-980b1755a2c5','sys_licence','admin','status','IN','Inativa');

------Sys Plan --- type_plan

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('52271fac-5056-41f5-ba84-ced4393339d0','sys_plan','admin','type_plan','FR','FREE');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('949ca5b0-de15-4c07-99bd-bb4ae0eac013','sys_plan','admin','type_plan','TR','Trial');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5d98cb05-c290-44f6-9dea-64141e590ed4','sys_plan','admin','type_plan','PG','Pago');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('802316f9-9bff-40d2-8fb0-c8c24542f5a7','sys_plan','admin','type_plan','PU','Pagamento Ãºnico');

------Sys Plan --- Menu

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('cb26c664-4285-498a-b0c3-0a6c5edaf410','sys_program','admin','type_program','T','Tabelas');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('521a17c3-715d-4012-a53c-6ead2d378fe3','sys_program','admin','type_program','L','Lançamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('bda94d03-5009-46fb-a24b-a0160441053a','sys_program','admin','type_program','P','Processamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f3b077d3-c723-4739-b82f-9bdd44139fb5','sys_program','admin','type_program','U','Utilitário');

------Sys User --- origem

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5ab272d9-e064-4b0a-9d9b-e76452c77b70','sys_user','admin','origem','1','Local');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('96812bbb-0cb2-41d7-92f7-fba1f9846728','sys_user','admin','origem','2','Chat');

------Sys Restriction--- type_value

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('76f0c265-cad5-425c-b2e3-860ef4411d92','sys_restriction','admin','type_value','Q','Quantitativo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('aaac2a9b-b0c9-4c88-8434-987dbba2ae6b','sys_restriction','admin','type_value','L','Logico');

------Sys Document -- content_type

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e82af53d-6851-459c-9ede-13928135d522','sys_document','admin','content_type','PDF','application/pdf');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('556aaf06-6419-471d-9bf3-0701f318af82','sys_document','admin','content_type','TXT','application/txt');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5487b5a9-1202-47a5-be03-4cc303a1c910','sys_document','admin','content_type','ZIP','application/zip');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('040b89cf-dfc5-4fda-b9ac-23bfdb000f63','sys_document','admin','content_type','OTS','application/octet-stream');

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('25683663-2422-462e-909e-a641fcbaade0','sys_document','admin','content_type','GIF','application/gif');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('28442ff5-30f5-4729-8c68-41d8f522f143','sys_document','admin','content_type','PNG','application/png');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3283ccbe-8f22-4187-aa32-72cb3765bcb4','sys_document','admin','content_type','JPEG','application/jpeg');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('fe677518-028b-4bc2-8427-f04f869971d4','sys_document','admin','content_type','BMP','application/bmp');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7efc7839-bb7a-4f65-b91f-e4bc3cfd170f','sys_document','admin','content_type','WEBP','application/webp');

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f282c2a1-e178-4cc3-bb45-fe4959a5f086','sys_document','admin','content_type','PLAIN','application/plain');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('31fff099-67ca-41bb-895d-1a94683d05bd','sys_document','admin','content_type','HTML','application/HTML');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b9760b51-8713-4348-9742-be2ac401e667','sys_document','admin','content_type','CSS','application/css');

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2668b24a-670f-4af8-b7f8-4086a2ff2d17','sys_document','admin','content_type','PKCS12','application/pkcs12');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b394ffa5-2474-44ac-80f9-957623b57a8b','sys_document','admin','content_type','VDN_MSPOWERPOINT','application/Vdnmspowerpoint');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9f08e3ed-1dba-4279-a914-fb3a47c5d442','sys_document','admin','content_type','XLSX','application/xlsx');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2c52b9cd-1f8a-4ec0-924e-989fd9d3a551','sys_document','admin','content_type','XML','application/xml');

---------- Sys Param  -- type

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('092b62b3-7abc-4376-9e81-a322c6808ac3','sys_param','admin','type','TX','Texto');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d63ef8bf-cfcb-49a7-865f-74cd74ee5fe1','sys_param','admin','type','DT','Data');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('bd0eb20d-fe24-425b-abb8-d258687f27e4','sys_param','admin','type','VR','Valor');

-------------------------------------- 
---   GER
-------------------------------------- 
 
----------Ger Empresa -- fis_regime 

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f19a9c25-6d63-4274-9e1b-1356c948e9c2','ger_empresa','admin','fis_regime','1','Simples Nacional');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8d2e1d83-db38-4364-8f5e-11cbf2e49979','ger_empresa','admin','fis_regime','2','Simples Nacional-Excesso Rec.Bruta');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('da8c6b9b-50f3-415a-9963-a2bc80421f71','ger_empresa','admin','fis_regime','3','Regime Normal');

----------Ger Empresa -- fis_regime_trib

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b132ba2b-f43d-4c53-9286-d7eac894c7bc','ger_empresa','admin','fis_regime_trib','1','Microempresa Municipal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('53223e73-0107-40f3-aff6-a38e4f2f5715','ger_empresa','admin','fis_regime_trib','2','Estimativa');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('36a0abed-d8fd-4554-8d17-fd5e1bb750da','ger_empresa','admin','fis_regime_trib','3','Sociedade de Profissionais');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8de29edd-082a-46fe-ba3c-5be5e9291d0c','ger_empresa','admin','fis_regime_trib','4','Cooperativa');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d89889f5-098a-4014-abbe-19f8872133ab','ger_empresa','admin','fis_regime_trib','5','Microempresário Individual (MEI)');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('33238bea-353d-4706-80b1-4642dccf6f47','ger_empresa','admin','fis_regime_trib','6','Microempresário e Empresa de Pequeno Porte (ME EPP)');

----------Ger Empresa -- fis_provedor_nfs

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('64616a7f-b468-4279-ae72-b035b71a97db','ger_empresa','admin','fis_provedor_nfs','1','Fiorilli');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('50cf277c-e30b-4683-9e73-4faffd1e09e8','ger_empresa','admin','fis_provedor_nfs','2','Ginfes');

--------- Ger Empresa Pessoa -- tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c8eb3010-1ee7-472c-8e07-36556668eaff','ger_empresa_pessoa','admin','tipo','1','Contador');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2988010b-c5a2-4706-8b16-d5b92789e5ad','ger_empresa_pessoa','admin','tipo','2','Responsável');

--------- Ger Processo BloqUser-- tipo_bloq

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6da01c7c-3f35-40f9-a4d1-1cc30367127c','ger_processo_bloq_user','admin','tipo_bloq','E','Excluir do Bloqueio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('047b4005-84a9-4759-a7f2-479b381bfd84','ger_processo_bloq_user','admin','tipo_bloq','I','Incluir no Bloqueio');

-------------------------------------- 
---   BOR
-------------------------------------- 

--------- Bor Dispositivo -- tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c5e3a423-dc0c-44e4-bd0e-b7b91cd83467','bor_dispositivo','admin','tipo','1','Bordo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('be090bd3-3289-4378-89e5-464d4af692bd','bor_dispositivo','admin','tipo','2','IButton');

-------------------------------------- 
---   CMS
-------------------------------------- 

--------- Cms Post  -- status

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('cd73d6ca-bec1-4093-8aaf-6421beed3ef5','cms_post','admin','status','C','Criação');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('490823a8-9e7d-44a7-a549-279af8c7b5d6','cms_post','admin','status','P','Publicado');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7fe3f758-b54d-4457-b49e-c36aedc5b7ea','cms_post','admin','status','D','Desativado');

--------- CmsPost  -- TipoRender

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('879f5d96-8a31-42d7-9e3a-f37ac4e1bd0f','cms_post','admin','tipo_render','M','Markdown');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('42a47744-308d-4cdf-bbf9-8ffa4017dd6f','cms_post','admin','tipo_render','H','Html');

--------- CmsPostHist  -- Descricao



INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('01340b74-9156-489d-ba9d-8c0c10cc6e98','cms_post_hist','admin','descricao','F','Fixo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d5b05e9f-5128-4d35-8f07-8f79572cb0d5','cms_post_hist','admin','descricao','V','Variável');

--------- CmsPostHist  -- TipoHist

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d409b308-9a43-4778-ae84-715f332f5b77','cms_post_hist','admin','tipo_hist','V','Visualização');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('30b323dd-6907-45bd-bf2e-d730f86a7da0','cms_post_hist','admin','tipo_hist','A','Alteração');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1debae42-0bad-420e-bc4b-ef412f0faaeb','cms_post_hist','admin','tipo_hist','S','Status');

-------------------------------------- 
---   CRM
-------------------------------------- 

--------- CrmStatus  -- tipo_status


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('13668b32-58b3-4c2b-8f9e-d4f00cff540d','crm_status','admin','tipo_status','AB','Aberto');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4cd68823-7080-451a-8f0b-a87437db3bfc','crm_status','admin','tipo_status','PE','Pendente');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('01e9fa83-a748-4886-a16e-389f191ea627','crm_status','admin','tipo_status','AI','Andamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('50f3268c-3ca3-40d9-aaae-a5b69de7dd2c','crm_status','admin','tipo_status','AT','Andamento Transf');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1e845cc4-39fa-4f4d-b0cc-2d18a0368593','crm_status','admin','tipo_status','FN','Finalizado');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d7aa6560-df11-4a25-8506-6ed588882492','crm_status','admin','tipo_status','CA','Cancelado');

--------- CrmChatGrupo --tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('380a7ddb-bf23-476b-9405-61a8c6422c1c','crm_chat_grupo','admin','tipo','G','Grupo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('0360eb92-31ef-4481-b78a-3f75760df2b1','crm_chat_grupo','admin','tipo','U','Usuário');

-------------------------------------- 
---   CTB
-------------------------------------- 
--------- CtbVersao -- tipo_rp

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('905da29e-ed03-4830-abb8-b3cc211d1c10','ctb_versao','admin','tipo_rp','R','Previsto');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6ddb5c52-6c66-47f9-b28f-311901bec6be','ctb_versao','admin','tipo_rp','P','Real');

--------- CtbConta -- tipo_variacao



INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('31103c64-6034-4cb1-9598-580f0041524d','ctb_conta','admin','tipo_variacao','F','Fixo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('83dd8f55-d4de-4e6a-b44e-193a1ecd54b5','ctb_conta','admin','tipo_variacao','V','Variável');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('0c1818a7-4adc-463a-8f6f-ff63e46c9fb1','ctb_conta','admin','tipo_variacao','I','Investimento');

--------- CtbConta -- tipo_dc

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f7ad7adc-4f28-404a-ad7b-08347e482e9c','ctb_conta','admin','tipo_dc','D','Débito');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('040e324d-9439-4a57-9406-c18f0c5a009e','ctb_conta','admin','tipo_dc','C','Crédito"');

--------- CtbConta -- tipo_conta


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('dc9e4c95-00ed-44bf-ab9b-75f44ad7e281','ctb_conta','admin','tipo_conta','1','Ativo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1d901603-6beb-4cf5-9963-d6e417c22aac','ctb_conta','admin','tipo_conta','2','Passivo"');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('54a77e2d-2189-4862-95e7-4941427a1ba8','ctb_conta','admin','tipo_conta','3','P.Liquido');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1648bc09-5f52-420b-891b-531c65da0d70','ctb_conta','admin','tipo_conta','4','Resultado"');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b54f9ac4-604a-466b-9b4b-762fb0c50e16','ctb_conta','admin','tipo_conta','5','Compensação"');

--------- CtbLanc -- status



INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('83d7180b-5013-416a-9fde-48349d8b73bd','ctb_lanc','admin','status','PD','Pendente');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6bfcebe4-a120-45a2-9349-fa60ed3e4fa6','ctb_lanc','admin','status','EA','Em analise');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4534b09c-f4cb-422b-b222-c3c7dfa5ff08','ctb_lanc','admin','status','CD','Consciliado');

--------- CtbLancDet -- tipo_dc


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('131f82c5-3555-43f6-ae41-16bce27e4167','ctb_lanc_det','admin','tipo_dc','D','Débito');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('84c8ba16-f43f-4438-a197-840b1263b498','ctb_lanc_det','admin','tipo_dc','C','Crédito');

-------------------------------------- 
---   FIN
-------------------------------------- 

--------- FinPagrecBaixa-- tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9e545988-9bcc-4455-9471-7f416c1c6801','fin_pagrec_baixa','admin','tipo','N','Normal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('62dc6462-b8a0-44df-8fc3-7d26c190de57','fin_pagrec_baixa','admin','tipo','A','Agrupamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7493d99f-9a95-481f-a546-55b323ec00b5','fin_pagrec_baixa','admin','tipo','E','Encontro');


--------- FinClass -- tipo_fluxo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4e1b14f3-85a1-4249-96db-e752d7603fdb','fin_class','admin','tipo_fluxo','PR','Pagamento / Recebimento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7beb4313-15ac-4e86-b5bc-50145ebd98fd','fin_class','admin','tipo_fluxo','TR','Transfência');

--------- FinClass -- fixo_variavel

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5f74f8a2-0fc1-4238-8906-97889cd40639','fin_class','admin','fixo_variavel','F','Fixo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3e5ea87e-24b3-415a-a546-064f0ee91cc8','fin_class','admin','fixo_variavel','V','Variável');

--------- FinPagrecVersao -- tipo_per

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f8f21ce9-2c0f-42c9-9bf7-13b36560f816','fin_pagrec_versao','admin','tipo_per','D','Diário');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('eb6847ff-3c96-4d0b-b119-5c2cac94d432','fin_pagrec_versao','admin','tipo_per','M','Mensal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('94a58236-e73d-425a-8f49-7a2af68f39d0','fin_pagrec_versao','admin','tipo_per','A','Anual');

--------- FinPagrec -- tipo_es

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('62fc78d5-243e-4d52-92bf-b80244f35db0','fin_pagrec','admin','tipo_es','E','Entrada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('16d314c3-8061-4f14-ab35-3909244dc673','fin_pagrec','admin','tipo_es','S','Saída');

--------- FinPagrecPrev -- tipo_es

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6ce3d8f5-fda0-4e56-90a3-8930bd46d8ae','fin_pagrec_prev','admin','tipo_es','E','Entrada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a6ff2733-41ee-43b6-bb11-467b4a108483','fin_pagrec_prev','admin','tipo_es','S','Saída');

--------- FinPagrecBancoExtrato -- tipo_es

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1feb240f-82a5-42d8-b07f-2eadc9665f31','fin_pagrec_banco_extrato','admin','status','PD','Pendente');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b32188ff-3de0-47e8-94b7-2074a689dbd5','fin_pagrec_banco_extrato','admin','status','EA','Em analise');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('90e6ebab-3627-4f19-8e1a-3cd993bde4c8','fin_pagrec_banco_extrato','admin','status','CD ','Consciliado');

--------- FinPagrecPrevVar -- tipo_es

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7fc44245-e07e-4a55-b803-97899374ba5e','fin_pagrec_prev_var','admin','tipo','N','Normal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('49417817-293c-492a-b69d-ac9c1f2433cc','fin_pagrec_prev_var','admin','tipo','A','Agrupamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6394c7c9-a220-4ac3-b4c6-964e308ae59f','fin_pagrec_prev_var','admin','tipo','E','Encontro');

-------------------------------------- 
---   FIS
-------------------------------------- 

--------- FisDoc -- Ambiente

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8e1fa840-14cc-468e-95e2-f1e8a2e50111','fis_doc','admin','ambiente','1','Producao');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e9290033-1908-4341-88db-27a5dbed2fa4','fis_doc','admin','ambiente','2','Homologacao');

--------- FisDoc -- TipoEmissao

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8d8c3425-c512-41a8-8d9e-18115ceed04d','fis_doc','admin','tipo_emissao','1','Normal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('59b2970b-df48-4dd1-8e47-e46ae4b45eb1','fis_doc','admin','tipo_emissao','2','SCAN');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('0cf1f565-012c-4621-bfeb-975f5c8e2457','fis_doc','admin','tipo_emissao','3','Off-Line');


--------- FisDocEvento -- tipo_evento

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e062a22f-646e-4062-965d-51823c8806f7','fis_doce_vento','admin','tipo_evento','1','Autorizacao');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4dd99e7f-a3bd-4e54-8735-1fe6d88974e3','fis_doce_vento','admin','tipo_evento','2','Cancelamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7c14f3b6-8415-4048-99d2-727e25dacfef','fis_doce_vento','admin','tipo_evento','3','Inutilizacao');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('df632094-7adb-4e99-b850-2d6567dfcaa1','fis_doce_vento','admin','tipo_evento','4','Carta de Correcao');

-------------------------------------- 
---   IND
-------------------------------------- 

--------- IndCnd -- tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e5515b52-dc69-43e1-9398-6c2bb5d9839f','ind_cnd','admin','tipo','S1','SQL postgres - Externo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6ac2bad4-c119-4095-8416-7909040fcdab','ind_cnd','admin','tipo','S2','SQL postrgres - Interno');

--------- IndPnl -- tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3fb6fe8f-b205-45b0-8090-204d09ec5a90','ind_pnl','admin','tipo','1','Painel de Relatórios');

--------- IndPrm -- TipoDado

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b44fd15b-0575-4385-a3eb-506d734c31a6','ind_prm','admin','tipo_dado','TX','Texto');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a4dda6c3-25f6-41c5-957f-e6c096e4fd37','ind_prm','admin','tipo_dado','DT','Data');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9b25488e-d144-4d7d-ab1a-80b6ce0dcbee','ind_prm','admin','tipo_dado','NM','Numero');

--------- IndPrm -- tipo_entrada

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('51b5382d-0e15-41b0-b523-3d111f5bc1fa','ind_prm','admin','tipo_dado','IS','Input Simples');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e78e568e-2862-41eb-8452-415ce21254da','ind_prm','admin','tipo_dado','CS','Combo Simples');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('32d4980d-3fa4-4060-ad4b-ecf5e2bead14','ind_prm','admin','tipo_dado','CF','Combo Fonte de Dadoso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ed98929c-9050-478a-89cc-769a6d21f03b','ind_prm','admin','tipo_dado','SP','Separador');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('78f71c13-35a5-44f3-b6b5-1c8bf511962d','ind_prm','admin','tipo_dado','VL','Variável');


--------- Ind-- MetodoOrdenacao

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('fe0753af-5ade-40d2-8bda-c702e5c30187','ind','admin','metodo_ordenacao','1','Crescente');

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6676bd15-ef83-4aa4-b84b-156798ef3170','ind','admin','metodo_ordenacao','2','Descrescente');

--------- Ind--  totalizador_atributo 

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2170ffa3-a808-466a-9b64-59e64fde8658','ind','admin','totalizador_atributo','1','Nenhum');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('906dd946-a95e-4d09-9de0-3b4fea835826','ind','admin','totalizador_atributo','2','Soma');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6deb0c7a-1ad3-4aa3-9dd1-6170e7f8c125','ind','admin','totalizador_atributo','3','Média');

--------- Ind --  tipo_acumulo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ce6a7a65-5d8e-49cd-aec2-bc8661d35847','ind','admin','tipo_acumulo','1','Manual');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5b00116a-42c0-40c9-b45b-b5ee321793f7','ind','admin','tipo_acumulo','2','Soma');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('78d9c467-06c4-4212-9612-8a89611576c2','ind','admin','tipo_acumulo','3','Média');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a4df50c2-ef32-4ba4-a519-eb61050bc83e','ind','admin','tipo_acumulo','4','Media Ponderada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9be0d5b4-5003-4c6f-8b6a-56b5d5ee1db0','ind','admin','tipo_acumulo','5','Ultimo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5f77fc93-8797-4618-b35b-933d92cf5133','ind','admin','tipo_acumulo','6','Maior');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6028c113-86e1-4209-b884-10c2e85d6312','ind','admin','tipo_acumulo','7','Menor');


--------- Ind --  grafico_tipo_atributo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('04d52aad-2b2f-4403-9f71-f2b23a700dc0','ind','admin','grafico_tipo_atributo','1','Coluna');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d63a3130-5360-4300-8e4a-aef1dd28f514','ind','admin','grafico_tipo_atributo','2','Linha');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('52714103-81f2-4b04-b3e0-45582def2d2f','ind','admin','grafico_tipo_atributo','3','Area');

--------- Ind --  grafico_tipo_ind

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('63dedd17-406a-4582-8ea9-4f146ca7a1fd','ind','admin','grafico_tipo_ind','1','Coluna');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6f7248aa-a38b-4563-ba81-8524b2bd285e','ind','admin','grafico_tipo_ind','2','Pizza');

--------- IndRel --  tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1be4dc46-ac3a-487c-8d2c-680c5f090496','ind_rel','admin','tipo','R','Report');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9be0cf46-3aa0-4f48-8c32-528e01c04367','ind_rel','admin','tipo','D','Dashboard');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('43fe5967-6dae-4749-a548-18e4dce01f7a','ind_rel','admin','tipo','C','Report Config');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('25bf6434-b925-42f7-a5c3-0162c1b271d7','ind_rel','admin','tipo','L','Lista Simples');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4c81e41f-a134-49a6-a35c-a71f0acb68aa','ind_rel','admin','tipo','F','Fonte de Dados');



-------------------------------------- 
---   MOV
-------------------------------------- 

--------- MovOperacao -- finalidade_doc


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d0bf707c-657f-4fd5-8221-431739ca698d','mov_operacao','admin','finalidade_doc','1','NF-e normal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3c0d321d-049e-43ff-92b0-67c95823ddb3','mov_operacao','admin','finalidade_doc','2','NF-e complementar');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b7bac9c7-69cf-4aeb-b765-4550a5d12d65','mov_operacao','admin','finalidade_doc','3','NF-e de ajuste');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('59b90e0d-640f-4fbf-9c3e-673df7b038a2','mov_operacao','admin','finalidade_doc','4','Devolução de mercadoria');

--------- MovOperacao -- finalidade_doc

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f7216c76-30de-47a9-8498-7e38708efd0e','mov_operacao','admin','tipo_es','E','Entrada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('21f35e75-5bd8-457b-b98f-b700b61d4a65','mov_operacao','admin','tipo_es','S','Saída"');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4ce224f7-cb4c-4261-adb9-a408e528513c','mov_operacao','admin','tipo_es','T','Transferência');


-------------------------------------- 
---   OPE
-------------------------------------- 

--------- OpeAtividade -- valida_seq_medicao_trab_centro


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9dc372cf-949b-4c6f-8279-2c2c55352b12','ope_atividade','admin','valida_seq_medicao_trab_centro','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a46d1cac-c2ef-4212-8648-2d720ff7ed58','ope_atividade','admin','valida_seq_medicao_trab_centro','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('98ff221e-12cd-48de-b363-d6fe306d699a','ope_atividade','admin','valida_seq_medicao_trab_centro','A','Aviso');


--------- OpeAtividade -- valida_saldo_area_aberta

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('dee076b8-d293-480a-b0ae-9a9e69585779','ope_atividade','admin','valida_saldo_area_aberta','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9c4b59e0-61fd-447e-9e9c-968e56a693d9','ope_atividade','admin','valida_saldo_area_aberta','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('cf688d52-2d60-47a1-8cec-e7b2535a2bb2','ope_atividade','admin','valida_saldo_area_aberta','A','Aviso');

--------- OpeAtividade -- valida_prev_itemserv

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1102b8c7-8c36-4237-8f50-760262a68c73','ope_atividade','admin','valida_prev_itemserv','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('92cf8b5d-c7f6-4ad5-9597-e07c6429c58b','ope_atividade','admin','valida_prev_itemserv','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('265b9362-1410-455b-84cc-c0d14fe84399','ope_atividade','admin','valida_prev_itemserv','A','Aviso');

--------- OpeAtividade -- valida_prev_rec

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ddc85c30-32cc-45c9-b0fa-f40c5216bfcd','ope_atividade','admin','valida_prev_rec','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ad87e324-b969-437e-a484-3addc77d2be9','ope_atividade','admin','valida_prev_rec','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('576180ae-5725-411c-b7cf-6a2b46fd76e2','ope_atividade','admin','valida_prev_rec','A','Aviso');

--------- OpeAtividade -- valida_regra_config 

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d182bf44-f3a7-4d4c-829c-8b71fd03a033','ope_atividade','admin','valida_regra_config','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('040d51e3-6012-41cf-b466-fa7c6a854e7a','ope_atividade','admin','valida_regra_config','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9f018ec3-29b6-4fff-8d08-c844c66f14b6','ope_atividade','admin','valida_regra_config','A','Aviso');

--------- OpeAtividade -- valida_tipo_executor

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('392e88bd-b7b3-4e4e-a62b-fdff2da6e624','ope_atividade','admin','valida_tipo_executor','SP','Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('99c0a6d8-e949-43ae-9f57-39f14a77d4fb','ope_atividade','admin','valida_tipo_executor','ST','Terceiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('fc29ba5f-f188-4b61-b6d9-06eb58fb907b','ope_atividade','admin','valida_tipo_executor','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('bb21c771-8fd4-4359-9193-4b5486aa424b','ope_atividade','admin','valida_tipo_executor','AP','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6d9183ef-9b37-4f6b-99a6-c89571c6a9d9','ope_atividade','admin','valida_tipo_executor','AT','Aviso-Terceiro');

--------- OpeAtividade -- valida_rec_equip 

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('28e7bf8c-10d9-48d2-b781-e111f1e3a174','ope_atividade','admin','valida_rec_equip','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('122f6ae7-737f-4965-a750-1ecb66d8980b','ope_atividade','admin','valida_rec_equip','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f44dab7c-0908-475a-924d-2e14ba501e38','ope_atividade','admin','valida_rec_equip','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('213e7b81-02a7-4267-94e2-f90f3b71e94f','ope_atividade','admin','valida_rec_equip','B','Bloqueia');

--------- OpeAtividade -- valida_rec_pessoa

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('0cdf6992-3796-48a8-a4fd-9a96a333aed9','ope_atividade','admin','valida_rec_pessoa','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1642f62e-8a99-47cc-aeab-9ce384d47ec6','ope_atividade','admin','valida_rec_pessoa','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3e6c2280-1802-45c0-863c-fbbc1f869c6d','ope_atividade','admin','valida_rec_pessoa','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7dbe513c-6cf7-4690-9639-d6c5c53c6e5b','ope_atividade','admin','valida_rec_pessoa','B','Bloqueia');

--------- OpeAtividade -- valida_itemserv_i

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3dea9154-4a1c-4497-aaf3-872163c8dfa8','ope_atividade','admin','valida_itemserv_i','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8ef1021c-02c9-4519-90cb-2aef47abc6e5','ope_atividade','admin','valida_itemserv_i','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ee94de33-5332-4cf9-8526-767ec5c7c3d3','ope_atividade','admin','valida_itemserv_i','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c91e4b03-fce8-40a4-b121-7e41fe9264af','ope_atividade','admin','valida_itemserv_i','B','Bloqueia');

--------- OpeAtividade -- valida_itemserv_s

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e1eb11ee-a133-4544-8d9c-ee8aab27b515','ope_atividade','admin','valida_itemserv_s','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4d037134-a898-477a-8481-24511c382213','ope_atividade','admin','valida_itemserv_s','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('dc9a60ea-dc64-4a05-96a7-ca3e5b7887ea','ope_atividade','admin','valida_itemserv_s','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('82a878f3-784d-488e-bbeb-8ecb2d8340ed','ope_atividade','admin','valida_itemserv_s','B','Bloqueia');

--------- OpeAtividade -- valida_tipo_prop_rec_equip

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('0b395762-e667-4f63-bca6-fca24e7e8735','ope_atividade','admin','valida_tipo_prop_rec_equip','SP','Sim-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f1e04ed9-7708-42b0-9bd1-8915718431f7','ope_atividade','admin','valida_tipo_prop_rec_equip','ST','Sim-Terceiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8d3a14d3-fb59-41a0-b034-811314bc6e04','ope_atividade','admin','valida_tipo_prop_rec_equip','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a08a49ce-5f0d-4cf8-b427-eac837b7be47','ope_atividade','admin','valida_tipo_prop_rec_equip','AP','Aviso-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('22f49226-8eed-47a3-8d6d-39ffc67ceef3','ope_atividade','admin','valida_tipo_prop_rec_equip','AT','Aviso-Terceiro');

--------- OpeAtividade -- valida_tipo_prop_rec_pessoa 

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('41a68a2a-8340-449c-8a90-e4bff0e43305','ope_atividade','admin','valida_tipo_prop_rec_pessoa','SP','Sim-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3fd0fc35-70fc-4029-a65f-169a260a333a','ope_atividade','admin','valida_tipo_prop_rec_pessoa','ST','Sim-Terceiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('007adbea-afa5-4964-865d-3c6d34f2c5d0','ope_atividade','admin','valida_tipo_prop_rec_pessoa','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('fb79da80-dc0e-4476-9d2f-df2ed7f25ae9','ope_atividade','admin','valida_tipo_prop_rec_pessoa','AP','Aviso-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9125c96f-a381-494c-8c62-d5c1581c8c23','ope_atividade','admin','valida_tipo_prop_rec_pessoa','AT','Aviso-Terceiro');


--------- OpeAtividade -- valida_tot_area_acum_per_centro_plan

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('411d398e-ad3f-4f7e-8da6-0838e6ce7d1a','ope_atividade','admin','valida_tot_area_acum_per_centro_plan','SP','Sim-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d7565a54-1384-4426-87f6-b2caed9904b3','ope_atividade','admin','valida_tot_area_acum_per_centro_plan','ST','Sim-Terceiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e6c735f4-a2e7-49af-9d83-9d16b52d064a','ope_atividade','admin','valida_tot_area_acum_per_centro_plan','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('171ae538-ecf6-4701-b5af-bb94be7416cd','ope_atividade','admin','valida_tot_area_acum_per_centro_plan','AP','Aviso-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4782206c-279a-4155-8d29-1c3238c6ea26','ope_atividade','admin','valida_tot_area_acum_per_centro_plan','AT','Aviso-Terceiro');

--------- OpeAtividade -- valida_tot_area_acum_per_centro_exec


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('49e95954-86b7-46b7-b9d3-d984da1bc61c','ope_atividade','admin','valida_tot_area_acum_per_centro_exec','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('429f8180-ef41-418d-9789-5244ffdd5336','ope_atividade','admin','valida_tot_area_acum_per_centro_exec','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f8d551de-5564-4bba-9150-68f425995906','ope_atividade','admin','valida_tot_area_acum_per_centro_exec','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ab5680e6-cf9d-4bd5-a9f6-69060d926cc2','ope_atividade','admin','valida_tot_area_acum_per_centro_exec','B','Bloqueia');

--------- ope_centro_rat_periodo -- tipo_rp  

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('0c015a28-3b2a-4375-8219-6af32c3d12b7','ope_centro_rat_periodo','admin','tipo_rp','R','Real');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e5ae1e81-27d1-4ca2-b6ba-b6c7fd2ece1a','ope_centro_rat_periodo','admin','tipo_rp','P','Previsto');


--------- ope_compart-- medicao_trab_centro 

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a650edee-fbd4-430a-a184-43e4c84a26da','ope_compart','admin','medicao_trab_centro','P','Principal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c5a56553-61db-446c-82ec-cea0992ac1aa','ope_compart','admin','medicao_trab_centro','S','Secundário');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('63bf638c-2b4d-445e-88b8-e6a23cae0b55','ope_compart','admin','medicao_trab_centro','N','Nenhum');


--------- ope_ocor_tipo  -- obrig_ope_compart

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8ec3347c-3cb8-4e12-b2fd-837b11160aa4','ope_ocor_tipo','admin','obrig_ope_compart','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5c4b4ae4-f63d-4fb3-b8bc-7926d9c06762','ope_ocor_tipo','admin','obrig_ope_compart','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('27990e59-2dce-411c-b706-ba066566d61e','ope_ocor_tipo','admin','obrig_ope_compart','O','Opcional');

--------- ope_compart_ocor -- tipo_ocor

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ed3cd4c6-57d3-4e84-81f9-20b0585a531a','ope_compart_ocor','admin','tipo_ocor','M','Movimentação');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('cb7daca0-d06e-497e-8930-8f03fd739301','ope_compart_ocor','admin','tipo_ocor','D','Medidação');

--------- ope_ocor -- tipo_lanc

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('93f71dc7-919c-44fa-a78b-99d48dce83a4','ope_ocor','admin','tipo_lanc','1','Movimentação');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7da81608-c2df-4564-b439-9ba5a42c93f9','ope_ocor','admin','tipo_lanc','2','Percentual');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2d298261-1b4a-4765-a8ca-00963b960bd0','ope_ocor','admin','tipo_lanc','3','Sim/Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('15502a52-b10f-422e-ac92-38d68519321e','ope_ocor','admin','tipo_lanc','4','Nota');

--------- ope_centro2_pessoa -- pto_idenf_tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f7a9bbea-9fe7-4cce-8830-c51f7a229cd3','ope_centro2_pessoa','admin','pto_idenf_tipo','1','CPF');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e83c8434-26d2-4062-a8a4-1fd39f2ad392','ope_centro2_pessoa','admin','pto_idenf_tipo','2','Senha');


--------- ope_centro_config -- tipo_regra

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ec77b057-0e3f-4ccb-abda-17bb5dc847ea','ope_centro_config','admin','tipo_regra','E','Exclusão');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2b2407d0-9c3e-4184-b909-4f2bf801dd21','ope_centro_config','admin','tipo_regra','I','Inclusão');

--------- ope_centro_prev -- tipo_executor

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('dd291349-e42c-44ef-9d8f-3856f79a2726','ope_centro_prev','admin','tipo_executor','P','Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7af4b762-e900-4dbb-af4e-bd26700a2a77','ope_centro_prev','admin','tipo_executor','T','Terceiro');


--------- ope_centro_dest -- tipo_es 

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('cf939c41-1676-47b9-ba06-4695024ff1d0','ope_centro_dest','admin','tipo_es','E','Entrada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('541ef204-f18f-4f49-bdd8-83fe58e6b122','ope_centro_dest','admin','tipo_es','S','Saída');

--------- ope_centro_prev_dest -- tipo_prev

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('43c9489c-90a4-4c83-aba2-ecbb244ef3dc','ope_centro_prev_dest','admin','tipo_prev','1','Produção');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6544ab21-635e-4c54-87f2-af13ac7e0cf3','ope_centro_prev_dest','admin','tipo_prev','2','Equipamentos');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e963fb77-4c95-44ec-8458-753c7ff51eae','ope_centro_prev_dest','admin','tipo_prev','3','Pessoa');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f6bfb6cb-00a7-402a-bbef-0d7c62b6355b','ope_centro_prev_dest','admin','tipo_prev','4','Item/Serviço');

--------- ope_centro2_ord_tipo -- valida_saldo_area_aberta

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2a787192-7290-45b6-811c-397b187b69d2','ope_centro2_ord_tipo','admin','valida_saldo_area_aberta','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b514edcf-cdd5-4348-96f7-4d16542210d7','ope_centro2_ord_tipo','admin','valida_saldo_area_aberta','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('640026cd-d3df-47f9-8915-6fa630ac8700','ope_centro2_ord_tipo','admin','valida_saldo_area_aberta','A','Aviso');


--------- ope_centro2_ord_tipo -- valida_prev_itemserv

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('79aa6e32-5b8d-4e98-8ca4-18ce25c87693','ope_centro2_ord_tipo','admin','valida_prev_itemserv','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('763ba6d2-80e5-442a-afe8-6971a0027ebe','ope_centro2_ord_tipo','admin','valida_prev_itemserv','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('87e02925-20e1-4018-b992-6674acde6d89','ope_centro2_ord_tipo','admin','valida_prev_itemserv','A','Aviso');

--------- ope_centro2_ord_tipo -- valida_prev_rec

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('64e85cd0-7711-4581-9e31-aa8eeb667bbf','ope_centro2_ord_tipo','admin','valida_prev_rec','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('6e718bb6-45a3-4e0a-b02d-d0e0761ed480','ope_centro2_ord_tipo','admin','valida_prev_rec','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a3df6501-d1ec-4a03-a982-23745db0764a','ope_centro2_ord_tipo','admin','valida_prev_rec','A','Aviso');

--------- ope_centro2_ord_tipo -- valida_regra_config

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('78bf4df4-c663-4e68-8731-ebc6fb4b769c','ope_centro2_ord_tipo','admin','valida_regra_config','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7a5e0003-90a7-4376-b002-371166176863','ope_centro2_ord_tipo','admin','valida_regra_config','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1466a99f-7bb6-4bdc-b765-874a86aec38d','ope_centro2_ord_tipo','admin','valida_regra_config','A','Aviso');

--------- ope_centro2_ord_tipo -- valida_tipo_executor

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('46d525da-c5bc-4f5c-a318-cdff65823fb8','ope_centro2_ord_tipo','admin','valida_tipo_executor','SP','Sim-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('440c5478-70d9-48ce-9c46-a5e5f0199e12','ope_centro2_ord_tipo','admin','valida_tipo_executor','ST','Sim-Terceiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('779ae81d-fb2c-4be9-806d-a2c67128d5aa','ope_centro2_ord_tipo','admin','valida_tipo_executor','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('03451a06-163f-4c21-bddd-f19ac42fc1fe','ope_centro2_ord_tipo','admin','valida_tipo_executor','AP','Aviso-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e39b5285-33cc-490b-bd65-5e80e8d548a5','ope_centro2_ord_tipo','admin','valida_tipo_executor','AT','Aviso-Terceiro');

--------- ope_centro2_ord_tipo -- valida_rec_equip

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f1e0941e-0c9b-481a-bf1b-c4c6535496c1','ope_centro2_ord_tipo','admin','valida_rec_equip','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b6785ac2-fc10-4464-9063-af67cae3a6fc','ope_centro2_ord_tipo','admin','valida_rec_equip','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d2cc5e11-3e07-4375-898b-6dd5e9d09028','ope_centro2_ord_tipo','admin','valida_rec_equip','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9179736c-a3e4-4225-8529-f498c8f5bf2f','ope_centro2_ord_tipo','admin','valida_rec_equip','B','Bloqueia');


--------- ope_centro2_ord_tipo -- valida_rec_pessoa

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a49face3-7e31-488c-9c44-7826d6130f7d','ope_centro2_ord_tipo','admin','valida_rec_pessoa','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('7219c13a-bcae-4b6b-a5a6-11e4182b106c','ope_centro2_ord_tipo','admin','valida_rec_pessoa','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a7f7e7cc-5a06-4af4-9ffe-5a10686e28fe','ope_centro2_ord_tipo','admin','valida_rec_pessoa','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('623fcd2c-6ca7-4d42-9d70-6e2f51e53b2e','ope_centro2_ord_tipo','admin','valida_rec_pessoa','B','Bloqueia');


--------- ope_centro2_ord_tipo -- valida_itemserv_i

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a3716753-7ec4-43b5-8592-e0b1e3facc0f','ope_centro2_ord_tipo','admin','valida_itemserv_i','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('d0943d55-dadd-4934-a2ff-3a41c7c28270','ope_centro2_ord_tipo','admin','valida_itemserv_i','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a514eddf-06de-4ecc-8064-6d1ff81e7a47','ope_centro2_ord_tipo','admin','valida_itemserv_i','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('fec697f9-06e9-46bd-960e-bc1273643ef2','ope_centro2_ord_tipo','admin','valida_itemserv_i','B','Bloqueia');


--------- ope_centro2_ord_tipo -- valida_itemserv_s

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('eac696f9-bfd7-45e0-b2e5-75017d90a1fd','ope_centro2_ord_tipo','admin','valida_itemserv_s','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('fc0659e4-f04e-4879-82b6-178d95adf27b','ope_centro2_ord_tipo','admin','valida_itemserv_s','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4173dcf8-362d-4505-9c05-3475182491c3','ope_centro2_ord_tipo','admin','valida_itemserv_s','A','Aviso');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f63af171-e2bd-402b-8be1-dbdaa5327547','ope_centro2_ord_tipo','admin','valida_itemserv_s','B','Bloqueia');

--------- ope_centro2_ord_tipo -- valida_tipo_prop_rec_equip

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('5411d7e0-5805-47c3-8b68-dfdc35eb62f5','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_equip','SP','Sim-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('9ada01bc-b464-49df-9ddf-2c9e9f49a097','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_equip','ST','Sim-Terceiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('849a59a6-5097-4396-8793-231abfb9980f','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_equip','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('840108cc-5a89-4824-b688-0e3aac468359','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_equip','AP','Aviso-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e84a27a8-b198-435b-a6ad-a2695170b77d','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_equip','AT','Aviso-Terceiro');

--------- ope_centro2_ord_tipo -- valida_tipo_prop_rec_pessoa

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('01830c78-7d7e-4dd9-a388-c682b61655e0','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_pessoa','SP','Sim-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1efdf514-d2ab-41e8-af4f-47750dc849ca','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_pessoa','ST','Sim-Terceiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('199e2fca-783f-4a4d-8060-e7154a4241aa','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_pessoa','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4a922e94-eedd-48ca-a03e-6fa752890daa','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_pessoa','AP','Aviso-Próprio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('8b588e57-130e-4b93-966d-93726215a260','ope_centro2_ord_tipo','admin','valida_tipo_prop_rec_pessoa','AT','Aviso-Terceiro');


--------- ope_atividade -- valida_tot_area_ord_exec

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('799b0b03-ec72-4a46-92fe-45bfa7759144','ope_atividade','admin','valida_tot_area_ord_exec','S','Sim');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('0c922cc1-82bd-420d-8627-02bd2dff5b44','ope_atividade','admin','valida_tot_area_ord_exec','N','Não');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('93278e84-c69b-4855-98bb-80e6ab753257','ope_atividade','admin','valida_tot_area_ord_exec','A','Aviso');

--------- ope_atividade -- tipo_destinacao

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('32b688e5-abcf-4286-8647-b8332d3312e6','ope_centro_subtipo','admin','tipo_destinacao','P','Pessoa');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b9e8dcef-40da-4fd2-96e2-bfafeed2302d','ope_centro_subtipo','admin','tipo_destinacao','E','Equipamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('65cf432c-8632-4128-8f1d-8a3ebca836f9','ope_centro_subtipo','admin','tipo_destinacao','T','Estoque');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('920458e0-cb47-4c9d-b581-aa7fb581fb00','ope_centro_subtipo','admin','tipo_destinacao','A','Area');

--------- ope_centro_rat_tipo -- tipo_apur


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ce3eef1a-e25f-4619-b625-52a94619a26d','ope_centro_rat_tipo','admin','tipo_apur','R','Rateio');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('e92f600f-e0a1-4029-a5bc-325fb148fe15','ope_centro_rat_tipo','admin','tipo_apur','A','Apontado');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('91cf721e-af4f-4610-aac2-89bbbb6c4351','ope_centro_rat_tipo','admin','tipo_apur','V','Valor Direto');

--------- ope_centro_rat_tipo --  tipo_ps

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a70e1c49-9f0e-4a69-bcca-fc717c0a936f','ope_centro_rat_tipo','admin','tipo_ps','P','Primario');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2fce0447-fe99-41b7-b317-3e90516b58a6','ope_centro_rat_tipo','admin','tipo_ps','S','Secundario');

--------- ope_compart_status --  tipo_status

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('da010b9e-023c-41f2-8844-ef5e0d79b210','ope_compart_status','admin','tipo_status','M','M-Montado/Utilizando');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c109406c-6d08-4160-a6e9-19a4138b3fe0','ope_compart_status','admin','tipo_status','D','D-Desmontado/Parado');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('ea13df01-c684-443d-b684-9b4de726e2c4','ope_compart_status','admin','tipo_status','C','C-Cancelado/Eliminado');

--------- ope_compart_posicao --  posicao

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('141e1e3b-ef97-4893-be49-b1462aea1246','ope_compart_posicao','admin','posicao','D','D-Dianteiro');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('88db0dc0-2a57-4ce0-9c0c-4c33767b4975','ope_compart_posicao','admin','posicao','T','T-Traseiro');

--------- ope_compart_posicao --  banda_montagem

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3001e4ca-302e-440e-899d-4ea674320eab','ope_compart_posicao','admin','banda_montagem','I','I-Interna');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f54b6b34-7402-4476-a685-c40d719272dd','ope_compart_posicao','admin','banda_montagem','E','E-Externa');

--------- ope_compart_posicao --  lado_montagem


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('46a8ac60-ab48-4207-a0da-c519a4288146','ope_compart_posicao','admin','lado_montagem','D','D-Direito');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('78d897d6-c2c5-48b4-abb7-01cd59c735b6','ope_compart_posicao','admin','lado_montagem','E','E-Esquerdo');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('be53173a-4249-496d-a62c-0ca1636a2e2a','ope_compart_posicao','admin','lado_montagem','C','C-Central');

--------- ope_compart_tipo --  tipo_compart

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('dbd6cb8a-93eb-4d1f-a0bf-0fb25fc40c33','ope_compart_tipo','admin','tipo_compart','P','P-Pneu');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('2998626e-3100-4920-ba17-55966393192f','ope_compart_tipo','admin','tipo_compart','O','O-Outro');


--------- ope_ocor --  tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('a45c549b-e7de-4937-a3ae-74bfac59f43c','ope_ocor','admin','tipo','A','A-Área');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('896e3985-1869-4a6d-a2cd-053d3add9a47','ope_ocor','admin','tipo','E','E-Equipamento');

--------- ope_ocor_tipo --  tipo

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b07d30dc-2d2d-4a5e-8ede-18eac7c9fbe1','ope_ocor_tipo','admin','tipo','A','A-Área');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('c6e3f074-a6fa-4c7c-9734-6077af91115f','ope_ocor_tipo','admin','tipo','E','E-Equipamento');

--------- ope_ocor_status -- ope_ocor_status


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('44fd8cdb-2cbd-4abc-b009-ba7de8363f66','ope_ocor_status','admin','tipo_status','A','A-Aberta');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('69cc34e0-4621-4269-a843-4b6c2b7c1600','ope_ocor_status','admin','tipo_status','N','N-Andamento');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('abe49424-1d25-424c-9f66-2ba1224898a4','ope_ocor_status','admin','tipo_status','F','F-Solucionada');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('4d6691e9-1129-4873-ac24-c11b1d99d95e','ope_ocor_status','admin','tipo_status','C','C-Cancelada');

------- ajustes 

-------------- ind_prm -- tipo_entrada


INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('1c0d3b13-3356-4963-ab4f-1fc828a84af2','ind_prm','admin','tipo_entrada','IS','IS-Input Simples');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('230db8af-9bde-4d3b-8d25-248e3357ae3b','ind_prm','admin','tipo_entrada','CS','CS-Combo Simples');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('26edf967-f75b-40b2-b51a-4eb1d1550f79','ind_prm','admin','tipo_entrada','CF','CF-Combo Fonte de Dados');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('f84a7589-7d9a-42f7-8432-83c9f7df71fa','ind_prm','admin','tipo_entrada','SP','SP-Separador');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('dd234b83-67df-4dff-a102-2eaa8a0ca7ec','ind_prm','admin','tipo_entrada','VL','VL-Var');

-------------- ger_empresa -- fis_regime_trib_nfs

INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('3ac48e2e-3e49-49d2-9037-0fbd08a2f631','ger_empresa','admin','fis_regime_trib_nfs','1','Microempresa Municipal');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('683d5cbe-24d1-4b19-8a0a-b0887e7e19a8','ger_empresa','admin','fis_regime_trib_nfs','2','Estimativa');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('562a2886-b4b8-4e51-91e2-9b8ddd90e031','ger_empresa','admin','fis_regime_trib_nfs','3','Sociedade de Profissionais');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('b1643ecc-c09a-4aa4-a5ff-943043bbff88','ger_empresa','admin','fis_regime_trib_nfs','4','Cooperativa');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('16baa58e-dc89-4b76-a668-8392d148205b','ger_empresa','admin','fis_regime_trib_nfs','5','Microempresário Individual (MEI)');
INSERT INTO sys_type_description (id,table_name,log_user_ins,field_name,value_type,description_type)
	VALUES ('17a74fb1-bf5a-41b3-81ac-47a9a28a83ce','ger_empresa','admin','fis_regime_trib_nfs','6','Microempresário e Empresa de Pequeno Porte (ME EPP)');

ALTER TABLE public.ope_atividade ALTER COLUMN valida_tot_area_acum_per_centro_exec TYPE varchar(2) USING valida_tot_area_acum_per_centro_exec::varchar;
ALTER TABLE public.ope_atividade ALTER COLUMN valida_tot_area_acum_per_centro_plan TYPE varchar(2) USING valida_tot_area_acum_per_centro_plan::varchar;




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
