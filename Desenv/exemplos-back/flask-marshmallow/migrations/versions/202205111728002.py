from alembic import op
import sqlalchemy as sa

revision = '202205111728002'
down_revision = '202205111728001'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
      
CREATE TABLE fin_banco (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
nr_banco varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_banco PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_banco IS 'Financeiro-Banco';
COMMENT ON COLUMN fin_banco.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN fin_banco.id IS 'ID de Banco';
COMMENT ON COLUMN fin_banco.nome IS 'Nome';
COMMENT ON COLUMN fin_banco.ativo IS 'Ativo';
COMMENT ON COLUMN fin_banco.nr_banco IS 'Numero do Banco';
COMMENT ON COLUMN fin_banco.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_banco.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_banco.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_banco.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_banco OWNER TO postgres;

CREATE TABLE fin_conta (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
fin_banco_id varchar(36) NOT NULL,
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
nr_agencia varchar(50) NOT NULL,
nr_conta varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_conta PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_conta IS 'Financeiro-Conta Bancária';
COMMENT ON COLUMN fin_conta.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_conta.id IS 'ID da Conta Bancária';
COMMENT ON COLUMN fin_conta.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN fin_conta.fin_banco_id IS 'ID do Banco';
COMMENT ON COLUMN fin_conta.nome IS 'Nome';
COMMENT ON COLUMN fin_conta.ativo IS 'Ativo';
COMMENT ON COLUMN fin_conta.nr_agencia IS 'Numero Agência';
COMMENT ON COLUMN fin_conta.nr_conta IS 'Numero Conta';
COMMENT ON COLUMN fin_conta.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_conta.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_conta.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_conta.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_conta OWNER TO postgres;

CREATE TABLE system_unit (
id varchar(36) NOT NULL,
name varchar(100)  NOT NULL,
sigla_unit varchar(100) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
img_logo bytea,
connection_name varchar(50),
CONSTRAINT pk_system_unit PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_unit IS 'System-Unidade (Base de Clientes)';
COMMENT ON COLUMN system_unit.id IS 'ID da Unidade';
COMMENT ON COLUMN system_unit.name IS 'Nome';
COMMENT ON COLUMN system_unit.sigla_unit IS 'Sigla da (Dono Unidade/Tenancy)';
COMMENT ON COLUMN system_unit.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_unit.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_unit.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_unit.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_unit.img_logo IS 'Imagem do Logo';
COMMENT ON COLUMN system_unit.connection_name IS 'Nome da Conexão';
ALTER TABLE system_unit OWNER TO postgres;

CREATE TABLE system_user (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
name varchar(100)  NOT NULL,
login varchar(100)  NOT NULL,
password varchar(100)  NOT NULL,
email varchar(100)  NOT NULL,
active varchar(1)  NOT NULL DEFAULT 'N',
active_message text,
phone varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
document varchar(50),
admin varchar(1) DEFAULT 'N',
login_ext varchar(100),
frontpage_id varchar(36),
origem varchar(1) DEFAULT '1',
chat varchar(1) DEFAULT 'S',
CONSTRAINT pk_system_user PRIMARY KEY (id) ,
CONSTRAINT idx_unq_system_user_login UNIQUE (login) WITH (fillfactor = 90),
CONSTRAINT idx_unq_system_user_email UNIQUE (email) WITH (fillfactor = 90)
)
WITHOUT OIDS;
COMMENT ON TABLE system_user IS 'System-Usuário';
COMMENT ON COLUMN system_user.id IS 'ID do Usuário';
COMMENT ON COLUMN system_user.name IS 'Nome';
COMMENT ON COLUMN system_user.login IS 'Login';
COMMENT ON COLUMN system_user.password IS 'Password';
COMMENT ON COLUMN system_user.email IS 'Email';
COMMENT ON COLUMN system_user.active IS 'Ativo';
COMMENT ON COLUMN system_user.active_message IS 'Mensagem de Ativação';
COMMENT ON COLUMN system_user.phone IS 'Telefone';
COMMENT ON COLUMN system_user.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_user.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_user.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_user.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_user.document IS 'Documento CPF / RG';
COMMENT ON COLUMN system_user.admin IS 'Administrador';
COMMENT ON COLUMN system_user.login_ext IS 'Login externo';
COMMENT ON COLUMN system_user.frontpage_id IS 'ID do Programa - Inicial';
COMMENT ON COLUMN system_user.origem IS 'Origem: 1-Local, 2-Chat';
COMMENT ON COLUMN system_user.chat IS 'Utiliza Chat';
ALTER TABLE system_user OWNER TO postgres;

CREATE TABLE system_user_unit (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
system_user_id varchar(36),
system_unit_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
owner varchar(1) DEFAULT 'N',
CONSTRAINT pk_system_user_unit PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_user_unit IS 'System-Usuário x Unidade (Base de Clientes)';
COMMENT ON COLUMN system_user_unit.id IS 'ID do Usuário x Unidade';
COMMENT ON COLUMN system_user_unit.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_user_unit.system_unit_id IS 'ID da Unidade';
COMMENT ON COLUMN system_user_unit.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_user_unit.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_user_unit.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_user_unit.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_user_unit.owner IS 'Dono';
ALTER TABLE system_user_unit OWNER TO postgres;

CREATE TABLE fin_class (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
tipo_es varchar(1) NOT NULL,
tipo_fluxo varchar(2) NOT NULL,
fixo_variavel varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
sigla_class varchar(15),
tipo_prev varchar(1),
CONSTRAINT pk_fin_class PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_class IS 'Financeiro-Classificação Financeira';
COMMENT ON COLUMN fin_class.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_class.id IS 'ID do Classificação';
COMMENT ON COLUMN fin_class.nome IS 'Nome';
COMMENT ON COLUMN fin_class.ativo IS 'Ativo';
COMMENT ON COLUMN fin_class.tipo_es IS 'Tipo Entrada/Saída';
COMMENT ON COLUMN fin_class.tipo_fluxo IS 'Considerado como Pag ou Rec: PR-Pagamento / Recebimento, TR-Transfência';
COMMENT ON COLUMN fin_class.fixo_variavel IS 'F-Fixo, V-Variável';
COMMENT ON COLUMN fin_class.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_class.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_class.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_class.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_class.sigla_class IS 'Sigla da Classificação';
COMMENT ON COLUMN fin_class.tipo_prev IS 'Tipo Previsão: S-Sim, N-Não';
ALTER TABLE fin_class OWNER TO postgres;

CREATE TABLE fin_class_agrup (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
padrao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_class_agrup PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_class_agrup IS 'Financeiro-Grupo de Classificação Financeira';
COMMENT ON COLUMN fin_class_agrup.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_class_agrup.id IS 'ID do Grupo de Classificação Financeira';
COMMENT ON COLUMN fin_class_agrup.nome IS 'Nome';
COMMENT ON COLUMN fin_class_agrup.ativo IS 'Ativo';
COMMENT ON COLUMN fin_class_agrup.padrao IS 'Padrão';
COMMENT ON COLUMN fin_class_agrup.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_class_agrup.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_class_agrup.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_class_agrup.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_class_agrup OWNER TO postgres;

CREATE TABLE fin_class_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
estrutura varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
sigla_class_grupo varchar(255),
CONSTRAINT pk_fin_class_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_class_grupo IS 'Financeiro-Grupo de Classificação Financeira';
COMMENT ON COLUMN fin_class_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_class_grupo.id IS 'ID do Classificação de Grupo';
COMMENT ON COLUMN fin_class_grupo.nome IS 'Nome';
COMMENT ON COLUMN fin_class_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN fin_class_grupo.estrutura IS 'Estrutura';
COMMENT ON COLUMN fin_class_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_class_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_class_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_class_grupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_class_grupo.sigla_class_grupo IS 'Sigla da Classificação do Grupo';
ALTER TABLE fin_class_grupo OWNER TO postgres;

CREATE TABLE fin_class_agrup_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fin_class_grupo_id varchar(36) NOT NULL,
fin_class_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
fin_class_agrup_id varchar(36) NOT NULL,
CONSTRAINT pk_fin_class_agrup_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_class_agrup_grupo IS 'Financeiro-Agrupamento x Grupo Classif. Financeira';
COMMENT ON COLUMN fin_class_agrup_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_class_agrup_grupo.id IS 'ID do Agrupamento x Grupo Classif. Financeira';
COMMENT ON COLUMN fin_class_agrup_grupo.fin_class_grupo_id IS 'ID de Grupo Classificação Financeira';
COMMENT ON COLUMN fin_class_agrup_grupo.fin_class_id IS 'ID de Classificação Financeira';
COMMENT ON COLUMN fin_class_agrup_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_class_agrup_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_class_agrup_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_class_agrup_grupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_class_agrup_grupo.fin_class_agrup_id IS 'ID do Grupo de Classificação Financeira';
ALTER TABLE fin_class_agrup_grupo OWNER TO postgres;

CREATE TABLE ger_pais (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
nr_pais varchar(50) NOT NULL,
sigla_pais varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_pais PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_pais IS 'Geral-País';
COMMENT ON COLUMN ger_pais.id IS 'ID do País';
COMMENT ON COLUMN ger_pais.nome IS 'Nome';
COMMENT ON COLUMN ger_pais.ativo IS 'Ativo';
COMMENT ON COLUMN ger_pais.nr_pais IS 'Numero País';
COMMENT ON COLUMN ger_pais.sigla_pais IS 'Sigla Pais';
COMMENT ON COLUMN ger_pais.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_pais.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_pais.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_pais.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_pais OWNER TO postgres;

CREATE TABLE ger_uf (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
nr_uf varchar(50) NOT NULL,
ger_pais_id varchar(36) NOT NULL,
sigla_uf varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_uf PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_uf IS 'Geral-Unidade Federação';
COMMENT ON COLUMN ger_uf.id IS 'ID da Uf';
COMMENT ON COLUMN ger_uf.nome IS 'Nome';
COMMENT ON COLUMN ger_uf.ativo IS 'Ativo';
COMMENT ON COLUMN ger_uf.nr_uf IS 'Numero Uf';
COMMENT ON COLUMN ger_uf.ger_pais_id IS 'ID do Pais';
COMMENT ON COLUMN ger_uf.sigla_uf IS 'Sigla da Uf';
COMMENT ON COLUMN ger_uf.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_uf.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_uf.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_uf.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_uf OWNER TO postgres;

CREATE TABLE ger_cidade (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
nr_cidade varchar(50) NOT NULL,
ger_uf_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_cidade PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_cidade IS 'Geral-Cidade';
COMMENT ON COLUMN ger_cidade.id IS 'ID da Cidade';
COMMENT ON COLUMN ger_cidade.nome IS 'Nome';
COMMENT ON COLUMN ger_cidade.ativo IS 'Ativo';
COMMENT ON COLUMN ger_cidade.nr_cidade IS 'Numero Cidade';
COMMENT ON COLUMN ger_cidade.ger_uf_id IS 'ID da Uf';
COMMENT ON COLUMN ger_cidade.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_cidade.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_cidade.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_cidade.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_cidade OWNER TO postgres;

CREATE TABLE ger_index (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_index varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_index PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_index IS 'Geral-Index';
COMMENT ON COLUMN ger_index.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_index.id IS 'ID do Index';
COMMENT ON COLUMN ger_index.nome IS 'Nome';
COMMENT ON COLUMN ger_index.ativo IS 'Ativo';
COMMENT ON COLUMN ger_index.sigla_index IS 'Sigla Index';
COMMENT ON COLUMN ger_index.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_index.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_index.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_index.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_index OWNER TO postgres;

CREATE TABLE ger_index_mov (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
data_mov date NOT NULL,
ger_index_id varchar(36) NOT NULL,
valor1 decimal(18,6) NOT NULL DEFAULT 0,
valor2 decimal(18,6) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_index_mov PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_index_mov IS 'Geral-Movimento de Index';
COMMENT ON COLUMN ger_index_mov.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_index_mov.id IS 'ID do Movimento do Index';
COMMENT ON COLUMN ger_index_mov.data_mov IS 'Data Movimento';
COMMENT ON COLUMN ger_index_mov.ger_index_id IS 'ID do Index';
COMMENT ON COLUMN ger_index_mov.valor1 IS 'Valor 1';
COMMENT ON COLUMN ger_index_mov.valor2 IS 'Valor 2';
COMMENT ON COLUMN ger_index_mov.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_index_mov.log_date_ins IS ' Log - Data de Inserção';
COMMENT ON COLUMN ger_index_mov.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_index_mov.log_date_upd IS ' Log - Data de Alteração';
ALTER TABLE ger_index_mov OWNER TO postgres;

CREATE TABLE ger_empresa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
razao_social varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_empresa varchar(50) NOT NULL,
doc_cnpj varchar(50),
doc_cpf varchar(50),
doc_ie varchar(50),
doc_im varchar(50),
doc_cnae varchar(50),
data_abertura date,
doc_junta varchar(50),
fis_regime varchar(50),
data_validade_a3 date,
data_validade_a1 date,
end_logradouro varchar(100),
end_logradouro_nr varchar(10),
end_bairro varchar(100),
end_complemento varchar(100),
end_cep varchar(100),
end_ger_cidade_id varchar(36) NOT NULL,
fone_1 varchar(100),
fone_2 varchar(100),
fone_3 varchar(100),
contato_1 varchar(100),
contato_2 varchar(100),
contato_3 varchar(100),
email_1 varchar(255),
doc_rntrc varchar(100),
fis_certificado_id varchar(36),
ger_empresa_grupo_id varchar(36),
log_user_ins varchar(255),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(255),
log_date_upd timestamp(0),
fis_dfe_ambiente varchar(1),
fis_dfe_api_token text,
fis_regime_trib_nfs varchar(1),
fis_provedor_nfs varchar(1),
fis_incent_cultura varchar(1),
fis_incent_fiscal_nfs varchar(1),
CONSTRAINT pk_ger_empresa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_empresa IS 'Geral-Empresa';
COMMENT ON COLUMN ger_empresa.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_empresa.id IS 'ID da Empresa';
COMMENT ON COLUMN ger_empresa.nome IS 'Nome';
COMMENT ON COLUMN ger_empresa.razao_social IS 'Razao Social';
COMMENT ON COLUMN ger_empresa.ativo IS 'Ativo';
COMMENT ON COLUMN ger_empresa.sigla_empresa IS 'Sigla da Empresa';
COMMENT ON COLUMN ger_empresa.doc_cnpj IS 'Doc. CNPJ';
COMMENT ON COLUMN ger_empresa.doc_cpf IS 'Doc. CPF';
COMMENT ON COLUMN ger_empresa.doc_ie IS 'Doc. Ins.Estadual';
COMMENT ON COLUMN ger_empresa.doc_im IS 'Doc. Ins.Municipal';
COMMENT ON COLUMN ger_empresa.doc_cnae IS 'Doc. CNAE';
COMMENT ON COLUMN ger_empresa.data_abertura IS 'Data de Abertura';
COMMENT ON COLUMN ger_empresa.doc_junta IS 'Doc. Junta Comercial';
COMMENT ON COLUMN ger_empresa.fis_regime IS 'Tipo Regime: 1-Simples Nacional, 2-Simples Nacional-Excesso Rec.Bruta,3-Regime Normal ';
COMMENT ON COLUMN ger_empresa.data_validade_a3 IS 'Data Validade Certificado A3';
COMMENT ON COLUMN ger_empresa.data_validade_a1 IS 'Data Validade Certificado A1';
COMMENT ON COLUMN ger_empresa.end_logradouro IS 'Endereço - Logradouro';
COMMENT ON COLUMN ger_empresa.end_logradouro_nr IS 'Endereço - Numero';
COMMENT ON COLUMN ger_empresa.end_bairro IS 'Endereço - Bairro';
COMMENT ON COLUMN ger_empresa.end_complemento IS 'Endereço - Complemento';
COMMENT ON COLUMN ger_empresa.end_cep IS 'Endereço - Cep';
COMMENT ON COLUMN ger_empresa.end_ger_cidade_id IS 'Endereço - ID da Cidade';
COMMENT ON COLUMN ger_empresa.fone_1 IS 'Telefone 1';
COMMENT ON COLUMN ger_empresa.fone_2 IS 'Telefone 2';
COMMENT ON COLUMN ger_empresa.fone_3 IS 'Telefone 3';
COMMENT ON COLUMN ger_empresa.contato_1 IS 'Contato 1';
COMMENT ON COLUMN ger_empresa.contato_2 IS 'Contato 2';
COMMENT ON COLUMN ger_empresa.contato_3 IS 'Contato 3';
COMMENT ON COLUMN ger_empresa.email_1 IS 'Email 1';
COMMENT ON COLUMN ger_empresa.doc_rntrc IS 'Doc. RNTRC';
COMMENT ON COLUMN ger_empresa.fis_certificado_id IS 'ID do Certificado';
COMMENT ON COLUMN ger_empresa.ger_empresa_grupo_id IS 'ID do Grupo de Empresa';
COMMENT ON COLUMN ger_empresa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_empresa.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_empresa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_empresa.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ger_empresa.fis_dfe_ambiente IS 'Ambiente Transmissão DFE';
COMMENT ON COLUMN ger_empresa.fis_dfe_api_token IS 'Token da API de DFE ';
COMMENT ON COLUMN ger_empresa.fis_regime_trib_nfs IS 'Regime Tributação da NFS: 1 – Microempresa Municipal, 2 – Estimativa, 3 – Sociedade de Profissionais, 4 – Cooperativa, 5 – Microempresário Individual (MEI), 6 – Microempresário e Empresa de Pequeno Porte (ME EPP)';
COMMENT ON COLUMN ger_empresa.fis_provedor_nfs IS 'Provedor emissão NFS: 1-Fiorilli, 2-Ginfes';
COMMENT ON COLUMN ger_empresa.fis_incent_cultura IS 'Incentiva Cultura: S-Sim, N-Não';
COMMENT ON COLUMN ger_empresa.fis_incent_fiscal_nfs IS 'Possue incentivo fiscal da NFS';
ALTER TABLE ger_empresa OWNER TO postgres;

CREATE TABLE ger_empresa_param (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
sigla_param varchar(50) NOT NULL,
ger_empresa_id varchar(36) NOT NULL,
valor_tx varchar(250) NOT NULL,
valor_dt date NOT NULL,
valor_nm decimal(18,6) NOT NULL,
observacao varchar(250) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_empresa_param PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_empresa_param IS 'Geral-Parâmetros da Empresa';
COMMENT ON COLUMN ger_empresa_param.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_empresa_param.id IS 'ID do Parâmetro da Empresa';
COMMENT ON COLUMN ger_empresa_param.sigla_param IS 'Sigla do Parametro';
COMMENT ON COLUMN ger_empresa_param.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ger_empresa_param.valor_tx IS 'Valor Texto';
COMMENT ON COLUMN ger_empresa_param.valor_dt IS 'Valor Data';
COMMENT ON COLUMN ger_empresa_param.valor_nm IS 'Valor Numero';
COMMENT ON COLUMN ger_empresa_param.observacao IS 'Observação';
COMMENT ON COLUMN ger_empresa_param.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_empresa_param.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_empresa_param.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_empresa_param.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_empresa_param OWNER TO postgres;

CREATE TABLE ger_pessoa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
razao_social varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
doc_cnpj varchar(50),
doc_cpf varchar(50),
doc_ie varchar(50),
doc_im varchar(50),
doc_cnae varchar(50),
data_abertura varchar(50),
doc_junta varchar(50),
fis_regime varchar(50),
fone_1 varchar(100),
fone_2 varchar(100),
fone_3 varchar(100),
contato_1 varchar(100),
contato_2 varchar(100),
contato_3 varchar(100),
contrib_icms int4 NOT NULL,
nr_rntrc varchar(8),
doc_rg varchar(50),
doc_rg_org_exp varchar(50),
doc_crc varchar(50),
doc_crc_seq varchar(50),
doc_crc_org_exp varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
sigla_pes varchar(50),
nr_registro_est_cte varchar(50),
doc_taf varchar(50),
data_valid date,
CONSTRAINT pk_ger_pessoa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_pessoa IS 'Geral-Pessoa';
COMMENT ON COLUMN ger_pessoa.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ger_pessoa.id IS 'ID da Pessoa';
COMMENT ON COLUMN ger_pessoa.nome IS 'Nome';
COMMENT ON COLUMN ger_pessoa.razao_social IS 'Razão Social';
COMMENT ON COLUMN ger_pessoa.ativo IS 'Ativo';
COMMENT ON COLUMN ger_pessoa.doc_cnpj IS 'Doc. CNPJ';
COMMENT ON COLUMN ger_pessoa.doc_cpf IS 'Doc. CPF';
COMMENT ON COLUMN ger_pessoa.doc_ie IS 'Doc. Ins.Estadual';
COMMENT ON COLUMN ger_pessoa.doc_im IS 'Doc. Ins.Municipal';
COMMENT ON COLUMN ger_pessoa.doc_cnae IS 'Doc. CNAE';
COMMENT ON COLUMN ger_pessoa.data_abertura IS 'Data Abertura';
COMMENT ON COLUMN ger_pessoa.doc_junta IS 'Doc. Junta';
COMMENT ON COLUMN ger_pessoa.fis_regime IS 'Regime';
COMMENT ON COLUMN ger_pessoa.fone_1 IS 'Tefone 1';
COMMENT ON COLUMN ger_pessoa.fone_2 IS 'Tefone 2';
COMMENT ON COLUMN ger_pessoa.fone_3 IS 'Tefone 3';
COMMENT ON COLUMN ger_pessoa.contato_1 IS 'Contato 1';
COMMENT ON COLUMN ger_pessoa.contato_2 IS 'Contato 2';
COMMENT ON COLUMN ger_pessoa.contato_3 IS 'Contato 3';
COMMENT ON COLUMN ger_pessoa.contrib_icms IS 'Tipo de Contribuinte ICMS';
COMMENT ON COLUMN ger_pessoa.nr_rntrc IS 'Numero RNTRC ';
COMMENT ON COLUMN ger_pessoa.doc_rg IS 'Doc. R.G';
COMMENT ON COLUMN ger_pessoa.doc_rg_org_exp IS 'Doc. R.G Orgão Exp.';
COMMENT ON COLUMN ger_pessoa.doc_crc IS 'Doc. C.R.C';
COMMENT ON COLUMN ger_pessoa.doc_crc_seq IS 'Doc. C.R.C Seq.';
COMMENT ON COLUMN ger_pessoa.doc_crc_org_exp IS 'Doc. C.R.C Orgão Exp.';
COMMENT ON COLUMN ger_pessoa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_pessoa.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_pessoa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_pessoa.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ger_pessoa.sigla_pes IS 'Sigla';
COMMENT ON COLUMN ger_pessoa.nr_registro_est_cte IS 'Número do registro estadual de CTE';
COMMENT ON COLUMN ger_pessoa.doc_taf IS 'Termo de autorização de fretamento';
COMMENT ON COLUMN ger_pessoa.data_valid IS 'Data de Validação';
ALTER TABLE ger_pessoa OWNER TO postgres;

CREATE TABLE ger_pessoa_conta_banco (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fin_banco_id varchar(36) NOT NULL,
agencia varchar(100) NOT NULL,
conta varchar(100) NOT NULL,
observacao varchar(250) NOT NULL,
ger_pessoa_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_pessoa_conta_banco PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_pessoa_conta_banco IS 'Geral-Conta Bancária da Pessoa';
COMMENT ON COLUMN ger_pessoa_conta_banco.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_pessoa_conta_banco.id IS 'ID da Conta Bancária da Pessoa';
COMMENT ON COLUMN ger_pessoa_conta_banco.fin_banco_id IS 'ID do Banco';
COMMENT ON COLUMN ger_pessoa_conta_banco.agencia IS 'Agência';
COMMENT ON COLUMN ger_pessoa_conta_banco.conta IS 'Conta';
COMMENT ON COLUMN ger_pessoa_conta_banco.observacao IS 'Observacao';
COMMENT ON COLUMN ger_pessoa_conta_banco.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN ger_pessoa_conta_banco.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_pessoa_conta_banco.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_pessoa_conta_banco.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_pessoa_conta_banco.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_pessoa_conta_banco OWNER TO postgres;

CREATE TABLE ger_pessoa_endereco (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_pessoa_id varchar(36) NOT NULL,
ativo varchar(1) NOT NULL,
tipo varchar(1) NOT NULL,
padrao varchar(1) NOT NULL,
end_logradouro varchar(100),
end_logradouro_nr varchar(10),
end_bairro varchar(100),
end_complemento varchar(100),
end_cep varchar(100),
end_ger_cidade_id varchar(36) NOT NULL,
fone varchar(100),
email varchar(100),
contato varchar(100),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_pessoa_endereco PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_pessoa_endereco IS 'Geral-Endereço da Pessoa';
COMMENT ON COLUMN ger_pessoa_endereco.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_pessoa_endereco.id IS 'ID do Endereço da Pessoa';
COMMENT ON COLUMN ger_pessoa_endereco.ger_pessoa_id IS 'ID de Pessoa';
COMMENT ON COLUMN ger_pessoa_endereco.ativo IS 'Ativo';
COMMENT ON COLUMN ger_pessoa_endereco.tipo IS 'Tipo (F-Fiscal; C-Cobrança; E-Entrega)';
COMMENT ON COLUMN ger_pessoa_endereco.padrao IS 'Padrão (S-Sim; N-Não)';
COMMENT ON COLUMN ger_pessoa_endereco.end_logradouro IS 'Endereço - Logradouro';
COMMENT ON COLUMN ger_pessoa_endereco.end_logradouro_nr IS 'Endereço - Logradouro Numero';
COMMENT ON COLUMN ger_pessoa_endereco.end_bairro IS 'Endereço - Logradouro Bairro';
COMMENT ON COLUMN ger_pessoa_endereco.end_complemento IS 'Endereço - Logradouro Complemento';
COMMENT ON COLUMN ger_pessoa_endereco.end_cep IS 'Endereço - Logradouro Cep';
COMMENT ON COLUMN ger_pessoa_endereco.end_ger_cidade_id IS 'Endereço - ID da Cidade';
COMMENT ON COLUMN ger_pessoa_endereco.fone IS 'Telefone';
COMMENT ON COLUMN ger_pessoa_endereco.email IS 'Email';
COMMENT ON COLUMN ger_pessoa_endereco.contato IS 'Contato';
COMMENT ON COLUMN ger_pessoa_endereco.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_pessoa_endereco.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_pessoa_endereco.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_pessoa_endereco.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_pessoa_endereco OWNER TO postgres;

CREATE TABLE ger_itemserv (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
referencia1 varchar(50),
referencia2 varchar(50),
referencia3 varchar(50),
ger_itemserv_subgrupo_id varchar(36) NOT NULL,
fis_ncm_id varchar(36),
ger_umedida_id varchar(36) NOT NULL,
tipo varchar(1) NOT NULL,
tipo_ctb_comp varchar(1) NOT NULL,
origem_fiscal int4 NOT NULL,
fis_cest_id varchar(36) NOT NULL,
fis_nbs_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
nome_alternativo varchar(100),
tipo_composicao varchar(1) DEFAULT 'N',
fis_sigla_servico varchar(50),
ctb_comp_id varchar(36),
fis_doc_cnae_nfs varchar(50),
fis_sigla_servico_municipio varchar(50),
sigla_itemserv varchar(15),
CONSTRAINT pk_ger_itemserv PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv IS 'Geral-Item/Serviço';
COMMENT ON COLUMN ger_itemserv.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv.id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ger_itemserv.nome IS 'Nome';
COMMENT ON COLUMN ger_itemserv.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv.referencia1 IS 'Referência 1';
COMMENT ON COLUMN ger_itemserv.referencia2 IS 'Referência 2';
COMMENT ON COLUMN ger_itemserv.referencia3 IS 'Referência 3';
COMMENT ON COLUMN ger_itemserv.ger_itemserv_subgrupo_id IS 'ID do Item/Serviço do Sub-grupo';
COMMENT ON COLUMN ger_itemserv.fis_ncm_id IS 'ID da NCM';
COMMENT ON COLUMN ger_itemserv.ger_umedida_id IS 'ID da U.Medida';
COMMENT ON COLUMN ger_itemserv.tipo IS 'Tipo (I-Item; S-Serviço)';
COMMENT ON COLUMN ger_itemserv.tipo_ctb_comp IS 'Tipo Componente Contábil: C-Código, S-Sub-Grupo';
COMMENT ON COLUMN ger_itemserv.origem_fiscal IS 'Origem Fiscal';
COMMENT ON COLUMN ger_itemserv.fis_cest_id IS 'ID do CEST';
COMMENT ON COLUMN ger_itemserv.fis_nbs_id IS 'ID do NBS';
COMMENT ON COLUMN ger_itemserv.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ger_itemserv.nome_alternativo IS 'Nome alternativo Ex: Insumos em relatórios';
COMMENT ON COLUMN ger_itemserv.tipo_composicao IS 'Tipo de Composição: N-Nehum, K-Kit';
COMMENT ON COLUMN ger_itemserv.fis_sigla_servico IS 'Sigla do Item/Serv - Fiscal';
COMMENT ON COLUMN ger_itemserv.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ger_itemserv.fis_doc_cnae_nfs IS 'Documento Cnae da NFS';
COMMENT ON COLUMN ger_itemserv.fis_sigla_servico_municipio IS 'Sigla do Item/Serv - Fiscal do Municipio';
COMMENT ON COLUMN ger_itemserv.sigla_itemserv IS 'Sigla do Item/Serviço';
ALTER TABLE ger_itemserv OWNER TO postgres;

CREATE TABLE fis_ncm (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nr_ncm varchar(50) NOT NULL,
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
data_validade date NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_ncm PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_ncm IS 'Fiscal-Ncm';
COMMENT ON COLUMN fis_ncm.id IS 'ID do NCM';
COMMENT ON COLUMN fis_ncm.nr_ncm IS 'Numero NCM';
COMMENT ON COLUMN fis_ncm.nome IS 'Nome';
COMMENT ON COLUMN fis_ncm.ativo IS 'Ativo';
COMMENT ON COLUMN fis_ncm.data_validade IS 'Data Validade';
COMMENT ON COLUMN fis_ncm.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_ncm.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_ncm.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_ncm.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_ncm OWNER TO postgres;

CREATE TABLE ger_itemserv_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_itemserv_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_grupo IS 'Geral-Grupo de Item/Serviço';
COMMENT ON COLUMN ger_itemserv_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_grupo.id IS 'ID do Grupo do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_grupo.nome IS 'Nome';
COMMENT ON COLUMN ger_itemserv_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_grupo.log_user_upd IS ' Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_itemserv_grupo OWNER TO postgres;

CREATE TABLE ger_itemserv_subgrupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
ger_grupo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ctb_comp_id varchar(36),
CONSTRAINT pk_ger_itemserv_subgrupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_subgrupo IS 'Geral-Grupo de Item/Serviço';
COMMENT ON COLUMN ger_itemserv_subgrupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_subgrupo.id IS 'ID do Sub-Grupo de Item/Serviço';
COMMENT ON COLUMN ger_itemserv_subgrupo.nome IS 'Nome';
COMMENT ON COLUMN ger_itemserv_subgrupo.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv_subgrupo.ger_grupo_id IS 'ID do Grupo de Item/Serviço';
COMMENT ON COLUMN ger_itemserv_subgrupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_subgrupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_subgrupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_subgrupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ger_itemserv_subgrupo.ctb_comp_id IS 'ID do Componente Contábil';
ALTER TABLE ger_itemserv_subgrupo OWNER TO postgres;

CREATE TABLE fis_cfop (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nr_cfop varchar(50) NOT NULL,
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
data_validade date NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_cfop PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_cfop IS 'Fiscal-Cfop';
COMMENT ON COLUMN fis_cfop.id IS 'ID do Cfop';
COMMENT ON COLUMN fis_cfop.nr_cfop IS 'Numero Cfop';
COMMENT ON COLUMN fis_cfop.nome IS 'Nome Cfop';
COMMENT ON COLUMN fis_cfop.ativo IS 'Ativo';
COMMENT ON COLUMN fis_cfop.data_validade IS 'Data Validade';
COMMENT ON COLUMN fis_cfop.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_cfop.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_cfop.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_cfop.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_cfop OWNER TO postgres;

CREATE TABLE ger_umedida (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_umedida varchar(50) NOT NULL,
nr_umedida varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_umedida PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_umedida IS 'Geral-U.Medida';
COMMENT ON COLUMN ger_umedida.id IS 'ID da U.Medida';
COMMENT ON COLUMN ger_umedida.nome IS 'Nome';
COMMENT ON COLUMN ger_umedida.ativo IS 'Ativo';
COMMENT ON COLUMN ger_umedida.sigla_umedida IS 'Sigla da U.Medida';
COMMENT ON COLUMN ger_umedida.nr_umedida IS 'Numero da U.Medida';
COMMENT ON COLUMN ger_umedida.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_umedida.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_umedida.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_umedida.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_umedida OWNER TO postgres;

CREATE TABLE ger_umedida_conv (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ativo varchar(1) NOT NULL,
ger_umedida_id_de varchar(36) NOT NULL,
ger_umedida_id_para varchar(36) NOT NULL,
fator_mult decimal(18,6) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_umedida_conv PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_umedida_conv IS 'Geral-U.Medida - Conversão';
COMMENT ON COLUMN ger_umedida_conv.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ger_umedida_conv.id IS 'ID do Item/Serviço x U.Medida';
COMMENT ON COLUMN ger_umedida_conv.ativo IS 'Ativo';
COMMENT ON COLUMN ger_umedida_conv.ger_umedida_id_de IS 'ID de U.Medida - De';
COMMENT ON COLUMN ger_umedida_conv.ger_umedida_id_para IS 'ID de U.Medida - Para';
COMMENT ON COLUMN ger_umedida_conv.fator_mult IS 'Fator Multiplacao';
COMMENT ON COLUMN ger_umedida_conv.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_umedida_conv.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_umedida_conv.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_umedida_conv.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_umedida_conv OWNER TO postgres;

CREATE TABLE ger_itemserv_lote (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
data_ini date NOT NULL,
data_fin date,
observacao varchar(250),
data_validade date,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_itemserv_lote PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_lote IS 'Geral-Lote do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_lote.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_lote.id IS 'ID do Lote do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_lote.nome IS 'Nome';
COMMENT ON COLUMN ger_itemserv_lote.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv_lote.data_ini IS 'Data Inicial';
COMMENT ON COLUMN ger_itemserv_lote.data_fin IS 'Data Final';
COMMENT ON COLUMN ger_itemserv_lote.observacao IS 'Observação';
COMMENT ON COLUMN ger_itemserv_lote.data_validade IS 'Data Validade';
COMMENT ON COLUMN ger_itemserv_lote.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_lote.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_lote.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_lote.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_itemserv_lote OWNER TO postgres;

CREATE TABLE ger_marca (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_marca PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_marca IS 'Geral-Marca';
COMMENT ON COLUMN ger_marca.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_marca.id IS 'ID da Marca';
COMMENT ON COLUMN ger_marca.nome IS 'Nome';
COMMENT ON COLUMN ger_marca.ativo IS 'Ativo';
COMMENT ON COLUMN ger_marca.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_marca.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_marca.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_marca.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_marca OWNER TO postgres;

CREATE TABLE ger_itemserv_var (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
sigla_itemserv_var varchar(50),
ope_ciclo_var_id varchar(36),
CONSTRAINT pk_ger_itemserv_var PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_var IS 'Geral-Variação do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_var.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_var.id IS 'ID da Variação do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_var.nome IS 'Nome';
COMMENT ON COLUMN ger_itemserv_var.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv_var.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_var.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_var.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_var.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ger_itemserv_var.sigla_itemserv_var IS 'Sigla da Variação do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_var.ope_ciclo_var_id IS 'ID do Cliclo da Variedade';
ALTER TABLE ger_itemserv_var OWNER TO postgres;

CREATE TABLE ope_atividade_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_atividade_grupo varchar(50) NOT NULL,
ordem varchar(3) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_atividade_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_atividade_grupo IS 'Operação-Grupo de Atividade';
COMMENT ON COLUMN ope_atividade_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_atividade_grupo.id IS 'ID do Grupo de Atividade';
COMMENT ON COLUMN ope_atividade_grupo.nome IS 'Nome';
COMMENT ON COLUMN ope_atividade_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_atividade_grupo.sigla_atividade_grupo IS 'Sigla de Grupo de Atividade';
COMMENT ON COLUMN ope_atividade_grupo.ordem IS 'Ordem';
COMMENT ON COLUMN ope_atividade_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_atividade_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_atividade_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_atividade_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_atividade_grupo OWNER TO postgres;

CREATE TABLE ope_atividade (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_atividade varchar(50) NOT NULL,
ope_atividade_grupo_id varchar(36) NOT NULL,
ger_umedida_id varchar(36) NOT NULL,
parada varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
index_bor varchar(50),
largura numeric(18,6) DEFAULT 0,
valida_seq_medicao_trab_centro varchar(1) DEFAULT 'S',
valida_saldo_area_aberta varchar(1) DEFAULT 'S',
valida_prev_itemserv varchar(1) DEFAULT 'S',
valida_prev_rec varchar(1) DEFAULT 'S',
valida_regra_config varchar(1) DEFAULT 'S',
valida_tipo_executor varchar(2) DEFAULT 'SP',
valida_rec_equip varchar(1) DEFAULT 'S',
valida_rec_pessoa varchar(1) DEFAULT 'S',
valida_itemserv_i varchar(1) DEFAULT 'S',
valida_itemserv_s varchar(1) DEFAULT 'S',
valida_tipo_prop_rec_equip varchar(2) DEFAULT 'SP',
valida_tipo_prop_rec_pessoa varchar(2) DEFAULT 'SP',
valida_tot_area_acum_per_centro_plan varchar(1) DEFAULT 'S',
valida_tot_area_acum_per_centro_exec varchar(1) DEFAULT 'S',
valida_tot_area_ord_exec varchar(1) DEFAULT 'S',
CONSTRAINT pk_ope_atividade PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_atividade IS 'Operação-Atividade';
COMMENT ON COLUMN ope_atividade.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_atividade.id IS 'ID da Atividade';
COMMENT ON COLUMN ope_atividade.nome IS 'Nome';
COMMENT ON COLUMN ope_atividade.ativo IS 'Ativo';
COMMENT ON COLUMN ope_atividade.sigla_atividade IS 'Sigla da Atividade';
COMMENT ON COLUMN ope_atividade.ope_atividade_grupo_id IS 'ID da Grupo da Atividade';
COMMENT ON COLUMN ope_atividade.ger_umedida_id IS 'ID da U.Medida';
COMMENT ON COLUMN ope_atividade.parada IS 'Parada: S-Sim, N-Não';
COMMENT ON COLUMN ope_atividade.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_atividade.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_atividade.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_atividade.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_atividade.index_bor IS 'Index Atividade Bordo';
COMMENT ON COLUMN ope_atividade.largura IS 'Largura (Mt) da Operação';
COMMENT ON COLUMN ope_atividade.valida_seq_medicao_trab_centro IS 'Valida sequencia medição do centro trabalho: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_atividade.valida_saldo_area_aberta IS 'Valida saldo Área em aberto: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_atividade.valida_prev_itemserv IS 'Valida previsão Item/Serviço: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_atividade.valida_prev_rec IS 'Valida previsão Recurso: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_atividade.valida_regra_config IS 'Valida regra configurável: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_atividade.valida_tipo_executor IS 'Valida tipo executor: SP-Sim-Próprio, ST-Sim-Terceiro, N-Não, AP-Aviso-Próprio, AT-Aviso-Terceiro';
COMMENT ON COLUMN ope_atividade.valida_rec_equip IS 'Obriga Recurso - Equipamento: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_atividade.valida_rec_pessoa IS 'Obriga Recurso - Pessoa: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_atividade.valida_itemserv_i IS ' Obriga Item: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_atividade.valida_itemserv_s IS 'Obriga Serviço: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_atividade.valida_tipo_prop_rec_equip IS 'Valida tipo prop. Recurso - Equipamento: SP-Sim-Próprio, ST-Sim-Terceiro, N-Não, AP-Aviso-Próprio, AT-Aviso-Terceiro';
COMMENT ON COLUMN ope_atividade.valida_tipo_prop_rec_pessoa IS 'Valida tipo prop. Recurso - Pessoa: SP-Sim-Próprio, ST-Sim-Terceiro, N-Não, AP-Aviso-Próprio, AT-Aviso-Terceiro';
COMMENT ON COLUMN ope_atividade.valida_tot_area_acum_per_centro_plan IS 'Valida total de area/prod acumulada periodo por centro - Planejamento: S-Sim, N-Não, A-Aviso ';
COMMENT ON COLUMN ope_atividade.valida_tot_area_acum_per_centro_exec IS 'Valida total de area/prod acumulada periodo por centro - Execução: S-Sim, N-Não, A-Aviso ';
COMMENT ON COLUMN ope_atividade.valida_tot_area_ord_exec IS 'Valida total de area/prod por ordem - Execução: S-Sim, N-Não, A-Aviso ';
ALTER TABLE ope_atividade OWNER TO postgres;

CREATE TABLE ger_marca_modelo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
ger_marca_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_marca_modelo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_marca_modelo IS 'Geral-Marca x Modelo';
COMMENT ON COLUMN ger_marca_modelo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_marca_modelo.id IS 'ID do Modelo';
COMMENT ON COLUMN ger_marca_modelo.nome IS 'Nome';
COMMENT ON COLUMN ger_marca_modelo.ativo IS 'Ativo';
COMMENT ON COLUMN ger_marca_modelo.ger_marca_id IS 'ID da Marca';
COMMENT ON COLUMN ger_marca_modelo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_marca_modelo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_marca_modelo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_marca_modelo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_marca_modelo OWNER TO postgres;

CREATE TABLE ctb_centro (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_centro varchar(50) NOT NULL,
ctb_centro_grupo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ctb_centro PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_centro IS 'Contábil-Centro';
COMMENT ON COLUMN ctb_centro.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_centro.id IS 'ID do Centro Contábil';
COMMENT ON COLUMN ctb_centro.nome IS 'Nome';
COMMENT ON COLUMN ctb_centro.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_centro.sigla_centro IS 'Sigla Centro Contábil';
COMMENT ON COLUMN ctb_centro.ctb_centro_grupo_id IS 'ID do Grupo do Centro Contábil';
COMMENT ON COLUMN ctb_centro.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_centro.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_centro.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_centro.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ctb_centro OWNER TO postgres;

CREATE TABLE ctb_centro_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_centro_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ctb_centro_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_centro_grupo IS 'Contábil-Grupo de Centro';
COMMENT ON COLUMN ctb_centro_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_centro_grupo.id IS 'ID do Grupo do Centro';
COMMENT ON COLUMN ctb_centro_grupo.nome IS 'Nome';
COMMENT ON COLUMN ctb_centro_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_centro_grupo.sigla_centro_grupo IS 'Sigla do Centro do Grupo';
COMMENT ON COLUMN ctb_centro_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_centro_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_centro_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_centro_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ctb_centro_grupo OWNER TO postgres;

CREATE TABLE ctb_comp_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_comp_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ctb_comp_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_comp_grupo IS 'Contábil-Grupo de Componente';
COMMENT ON COLUMN ctb_comp_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_comp_grupo.id IS 'ID do Grupo de Componente';
COMMENT ON COLUMN ctb_comp_grupo.nome IS 'Nome';
COMMENT ON COLUMN ctb_comp_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_comp_grupo.sigla_comp_grupo IS 'Sigla do Grupo de Componente';
COMMENT ON COLUMN ctb_comp_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_comp_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_comp_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_comp_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ctb_comp_grupo OWNER TO postgres;

CREATE TABLE ctb_comp (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_comp varchar(50) NOT NULL,
ctb_comp_grupo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ger_umedida_id varchar(36) NOT NULL,
ctb_comp_id_calc_orig varchar(36),
fator_calc_origem numeric(18,6) DEFAULT 0,
CONSTRAINT pk_ctb_comp PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_comp IS 'Contábil-Componente';
COMMENT ON COLUMN ctb_comp.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_comp.id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ctb_comp.nome IS 'Nome';
COMMENT ON COLUMN ctb_comp.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_comp.sigla_comp IS 'Sigla do Componente Contábil';
COMMENT ON COLUMN ctb_comp.ctb_comp_grupo_id IS 'ID do Grupo do Componente';
COMMENT ON COLUMN ctb_comp.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_comp.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_comp.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_comp.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_comp.ger_umedida_id IS 'ID da U.Medida';
COMMENT ON COLUMN ctb_comp.ctb_comp_id_calc_orig IS 'ID do Componente Contábil - Cálculo Origem';
COMMENT ON COLUMN ctb_comp.fator_calc_origem IS 'Fator Cálculo Origem';
ALTER TABLE ctb_comp OWNER TO postgres;

CREATE TABLE ope_centro_tipo (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
tipo_es varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_centro_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_tipo IS 'Operação-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_tipo.id IS 'ID do Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_tipo.nome IS 'Nome';
COMMENT ON COLUMN ope_centro_tipo.tipo_es IS 'Tipo de Entrada/Saída';
COMMENT ON COLUMN ope_centro_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_tipo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_centro_tipo OWNER TO postgres;

CREATE TABLE ope_centro_subtipo (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ope_centro_tipo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_destinacao varchar(1),
CONSTRAINT pk_ope_centro_subtipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_subtipo IS 'Operação-Sub-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_subtipo.id IS 'ID do Sub-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_subtipo.nome IS 'Nome';
COMMENT ON COLUMN ope_centro_subtipo.ope_centro_tipo_id IS 'ID do Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_subtipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_subtipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_subtipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_subtipo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_subtipo.tipo_destinacao IS 'Tipo destinação: P-Pessoa, E-Equipamento, T-Estoque, A-Area';
ALTER TABLE ope_centro_subtipo OWNER TO postgres;

CREATE TABLE ope_centro1 (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_centro1 varchar(50) NOT NULL,
ger_pessoa_id varchar(36) NOT NULL,
ope_centro_subtipo_id varchar(36) NOT NULL,
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ctb_comp_id varchar(36),
data_valid date,
CONSTRAINT pk_ope_centro1 PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro1 IS 'Operação-Centro Nível 1 de Entrada/Saída';
COMMENT ON COLUMN ope_centro1.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro1.id IS 'ID do Centro Nível 1 Entrada/Saída';
COMMENT ON COLUMN ope_centro1.nome IS 'Nome';
COMMENT ON COLUMN ope_centro1.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro1.sigla_centro1 IS 'Sigla do Centro 1 Entrada/Saída';
COMMENT ON COLUMN ope_centro1.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN ope_centro1.ope_centro_subtipo_id IS 'ID do Sub-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro1.observacao IS 'Observação';
COMMENT ON COLUMN ope_centro1.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro1.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro1.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro1.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro1.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ope_centro1.data_valid IS 'Data de Validação';
ALTER TABLE ope_centro1 OWNER TO postgres;

CREATE TABLE ope_periodo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_periodo varchar(50) NOT NULL,
data_ini date NOT NULL,
data_fin date NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_periodo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_periodo IS 'Operação-Período';
COMMENT ON COLUMN ope_periodo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_periodo.id IS 'ID do Período da Operação';
COMMENT ON COLUMN ope_periodo.nome IS 'Nome';
COMMENT ON COLUMN ope_periodo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_periodo.sigla_periodo IS 'Sigla da Período da Operação';
COMMENT ON COLUMN ope_periodo.data_ini IS 'Data Inicial';
COMMENT ON COLUMN ope_periodo.data_fin IS 'Data Final';
COMMENT ON COLUMN ope_periodo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_periodo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_periodo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_periodo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_periodo OWNER TO postgres;

CREATE TABLE ope_centro2 (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_centro2 varchar(50) NOT NULL,
ope_centro1_id varchar(36) NOT NULL,
ope_centro_subgrupo_id varchar(36) NOT NULL,
utiliza_compart varchar(1) NOT NULL,
observacao varchar(250),
ope_centro_rat_tipo_id varchar(36),
ger_marca_modelo_id varchar(36) NOT NULL,
tipo_prop varchar(1),
ger_pessoa_endereco_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_destinacao varchar(1),
tipo_ctb_comp varchar(1),
ctb_comp_id varchar(36),
ger_umedida_id varchar(36),
ope_regiao_id varchar(36),
medicao_trab_centro varchar(1) DEFAULT 'S',
valida_seq_medicao_trab_centro varchar(1) DEFAULT 'S',
data_valid date,
CONSTRAINT pk_ope_centro2 PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2 IS 'Operação-Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2.id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2.nome IS 'Nome';
COMMENT ON COLUMN ope_centro2.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro2.sigla_centro2 IS 'Sigla Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2.ope_centro1_id IS 'ID do Centro Nível 1 Entrada/Saída';
COMMENT ON COLUMN ope_centro2.ope_centro_subgrupo_id IS 'ID do Sub-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro2.utiliza_compart IS 'Utiliza Compartimento (S-Sim,N-Não)';
COMMENT ON COLUMN ope_centro2.observacao IS 'Observação';
COMMENT ON COLUMN ope_centro2.ope_centro_rat_tipo_id IS 'ID do Tipo de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro2.ger_marca_modelo_id IS 'ID do Modelo';
COMMENT ON COLUMN ope_centro2.tipo_prop IS 'Tipo P-Proprio, T-Terceiro';
COMMENT ON COLUMN ope_centro2.ger_pessoa_endereco_id IS 'ID do Endereço da Pessoal';
COMMENT ON COLUMN ope_centro2.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2.tipo_destinacao IS 'Tipo destinação: P-Pessoa, E-Equipamento, T-Estoque, A-Area';
COMMENT ON COLUMN ope_centro2.tipo_ctb_comp IS 'Tipo Componente Contábil: 1-Centro1, 2-Centro2, 3-SubGrupo Centro';
COMMENT ON COLUMN ope_centro2.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ope_centro2.ger_umedida_id IS 'ID da U.Medida';
COMMENT ON COLUMN ope_centro2.ope_regiao_id IS 'ID da Região';
COMMENT ON COLUMN ope_centro2.medicao_trab_centro IS 'Medição Trabalho: A-Ativa, I-Inativa, T-Automática';
COMMENT ON COLUMN ope_centro2.valida_seq_medicao_trab_centro IS 'Valida sequencia medição do centro trabalho: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_centro2.data_valid IS 'Data de Validação';
ALTER TABLE ope_centro2 OWNER TO postgres;

CREATE TABLE ope_centro_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_centro_grupo varchar(50) NOT NULL,
ope_centro_subtipo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_centro_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_grupo IS 'Operação-Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_grupo.id IS 'ID do Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_grupo.nome IS 'Nome';
COMMENT ON COLUMN ope_centro_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro_grupo.sigla_centro_grupo IS 'Sigla do Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_grupo.ope_centro_subtipo_id IS 'ID do Sub-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_centro_grupo OWNER TO postgres;

CREATE TABLE ope_centro_subgrupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_centro_subgrupo varchar(50) NOT NULL,
ope_centro_grupo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ctb_comp_id varchar(36),
icon varchar(50),
CONSTRAINT pk_ope_centro_subgrupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_subgrupo IS 'Operação-Sub-Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_subgrupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_subgrupo.id IS 'ID do Sub-Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_subgrupo.nome IS 'Nome';
COMMENT ON COLUMN ope_centro_subgrupo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro_subgrupo.sigla_centro_subgrupo IS 'Sigla do Sub-Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_subgrupo.ope_centro_grupo_id IS 'ID do Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_subgrupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_subgrupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_subgrupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_subgrupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_subgrupo.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ope_centro_subgrupo.icon IS 'Icone para Relatórios';
ALTER TABLE ope_centro_subgrupo OWNER TO postgres;

CREATE TABLE ope_centro_rat_fator (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ope_centro1_id varchar(36),
ope_centro2_id varchar(36),
ope_periodo_id varchar(36),
ctb_centro_id varchar(36),
ope_centro_subtipo_id varchar(36) NOT NULL,
fator_rat decimal(18,6) NOT NULL DEFAULT 0,
perc_rat numeric(18,6) DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro_rat_periodo_id varchar(36) NOT NULL,
CONSTRAINT pk_ope_centro2_rat_fator PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_rat_fator IS 'Operação-Fator de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_fator.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_rat_fator.id IS 'ID do Fator de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_fator.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_centro_rat_fator.ope_centro1_id IS 'ID do Centro Nível 1 de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_fator.ope_centro2_id IS 'ID do Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_fator.ope_periodo_id IS 'ID do Operação do Período';
COMMENT ON COLUMN ope_centro_rat_fator.ctb_centro_id IS 'ID do Centro Contábil';
COMMENT ON COLUMN ope_centro_rat_fator.ope_centro_subtipo_id IS 'ID do Sub-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_fator.fator_rat IS 'Fator de Rateio';
COMMENT ON COLUMN ope_centro_rat_fator.perc_rat IS 'Percentual de Rateio';
COMMENT ON COLUMN ope_centro_rat_fator.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_rat_fator.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_rat_fator.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_rat_fator.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_rat_fator.ope_centro_rat_periodo_id IS 'ID do Período de Rateio do Centro do Entrada/Saída';
ALTER TABLE ope_centro_rat_fator OWNER TO postgres;

CREATE TABLE ope_centro_rat_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
tipo_ps varchar(1) NOT NULL DEFAULT 'P',
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_apur varchar(1) NOT NULL DEFAULT 'P',
sigla_centro_rat_tipo varchar(50),
ope_centro_versao_id varchar(36),
CONSTRAINT pk_ope_centro_rat_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_rat_tipo IS 'Operação-Tipo de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_rat_tipo.id IS 'ID do Tipo de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_tipo.nome IS 'Nome';
COMMENT ON COLUMN ope_centro_rat_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro_rat_tipo.tipo_ps IS 'Tipo (P-Primario,S-Secundario)';
COMMENT ON COLUMN ope_centro_rat_tipo.observacao IS 'Observação';
COMMENT ON COLUMN ope_centro_rat_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_rat_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_rat_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_rat_tipo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_rat_tipo.tipo_apur IS 'Tipo Apuração: R-Rateio, A-Apontado, V-Valor Direto';
COMMENT ON COLUMN ope_centro_rat_tipo.sigla_centro_rat_tipo IS 'Sigla do Tipo de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_tipo.ope_centro_versao_id IS 'ID da Versão da Operação';
ALTER TABLE ope_centro_rat_tipo OWNER TO postgres;

CREATE TABLE ope_centro_rat_periodo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
data_ini date NOT NULL,
ope_centro_rat_tipo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_rp varchar(1),
CONSTRAINT pk_ope_centro_rat_periodo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_rat_periodo IS 'Operação-Período de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_periodo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_rat_periodo.id IS 'ID do Período de Rateio do Centro do Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_periodo.data_ini IS 'Data Inicial';
COMMENT ON COLUMN ope_centro_rat_periodo.ope_centro_rat_tipo_id IS 'ID do Tipo de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN ope_centro_rat_periodo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_rat_periodo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_rat_periodo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_rat_periodo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_rat_periodo.tipo_rp IS 'Tipo: R-Real, P-Previsto';
ALTER TABLE ope_centro_rat_periodo OWNER TO postgres;

CREATE TABLE ope_ocor_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_ocor_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_ocor_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_grupo IS 'Operação-Grupo de Ocorrência';
COMMENT ON COLUMN ope_ocor_grupo.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ope_ocor_grupo.id IS 'ID de Grupo de Ocorrência';
COMMENT ON COLUMN ope_ocor_grupo.nome IS 'Nome';
COMMENT ON COLUMN ope_ocor_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_ocor_grupo.sigla_ocor_grupo IS 'Sigla de Grupo de Ocorrência';
COMMENT ON COLUMN ope_ocor_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_ocor_grupo OWNER TO postgres;

CREATE TABLE ope_ocor (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_ocor varchar(50) NOT NULL,
ope_ocor_grupo_id varchar(36) NOT NULL,
ger_umedida_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
icon varchar(50) NOT NULL,
tipo varchar(1) NOT NULL,
tipo_lanc varchar(1) NOT NULL,
CONSTRAINT pk_ope_ocor PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor IS 'Operação-Ocorrência';
COMMENT ON COLUMN ope_ocor.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor.id IS 'ID do Ocorrência';
COMMENT ON COLUMN ope_ocor.nome IS 'Nome';
COMMENT ON COLUMN ope_ocor.ativo IS 'Ativo';
COMMENT ON COLUMN ope_ocor.sigla_ocor IS 'Sigla de Ocorrência';
COMMENT ON COLUMN ope_ocor.ope_ocor_grupo_id IS 'ID do Grupo de Ocorrência';
COMMENT ON COLUMN ope_ocor.ger_umedida_id IS 'ID da U.Medida';
COMMENT ON COLUMN ope_ocor.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_ocor.icon IS 'Icone da Ocorrência';
COMMENT ON COLUMN ope_ocor.tipo IS 'Tipo: A-Área, E-Equipamento';
COMMENT ON COLUMN ope_ocor.tipo_lanc IS 'Tipo Lancamento:1-Quantidade, 2-Percentual,3-Sim/Não,4-Nota';
ALTER TABLE ope_ocor OWNER TO postgres;

CREATE TABLE mov_tipo (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_mov_tipo varchar(50) NOT NULL,
tipo_mov varchar(10) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
configuracao text,
CONSTRAINT pk_mov_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_tipo IS 'Movimentação-Tipo de Movimento';
COMMENT ON COLUMN mov_tipo.id IS 'ID do Tipo de Movimento';
COMMENT ON COLUMN mov_tipo.nome IS 'Nome';
COMMENT ON COLUMN mov_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN mov_tipo.sigla_mov_tipo IS 'Sigla do Tipo do Movimento';
COMMENT ON COLUMN mov_tipo.tipo_mov IS 'Tipo do Movimento';
COMMENT ON COLUMN mov_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_tipo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN mov_tipo.configuracao IS 'Configuração da Tipo de Operação';
ALTER TABLE mov_tipo OWNER TO postgres;

CREATE TABLE fis_doc_tipo (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
modelo varchar(50) NOT NULL,
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_doc_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_doc_tipo IS 'Fiscal-Tipo de Documento';
COMMENT ON COLUMN fis_doc_tipo.id IS 'ID do Tipo de Documento';
COMMENT ON COLUMN fis_doc_tipo.modelo IS 'Modelo';
COMMENT ON COLUMN fis_doc_tipo.nome IS 'Nome';
COMMENT ON COLUMN fis_doc_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN fis_doc_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_doc_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_doc_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_doc_tipo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_doc_tipo OWNER TO postgres;

CREATE TABLE fis_obs (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
observacao text NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_obs PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_obs IS 'Fiscal-Observação';
COMMENT ON COLUMN fis_obs.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fis_obs.id IS 'ID da Observação';
COMMENT ON COLUMN fis_obs.nome IS 'Nome';
COMMENT ON COLUMN fis_obs.ativo IS 'Ativo';
COMMENT ON COLUMN fis_obs.observacao IS 'Observação';
COMMENT ON COLUMN fis_obs.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_obs.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_obs.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_obs.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_obs OWNER TO postgres;

CREATE TABLE ope_centro2_equip (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL,
tipo_rodado varchar(100) NOT NULL,
tipo_carroceria varchar(100) NOT NULL,
ger_cidade_id varchar(36) NOT NULL,
placa varchar(100),
renavam varchar(100),
tara decimal(18,6),
capacidade_kg decimal(18,6),
capacidade_m3 decimal(18,6),
potencia varchar(100),
nr_chassi varchar(100),
nr_serie varchar(100),
liberado_abastec varchar(1) NOT NULL,
largura decimal(18,6),
altura decimal(18,6),
nr_registro_estadual varchar(50),
tipo_tracao int4,
tipo_transp_auto_carga int4,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro2_id varchar(36) NOT NULL,
ope_frente_trabalho_id varchar(36),
data_venc_licenciamento date,
data_venc_imposto date,
CONSTRAINT pk_ope_centro_equip PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_equip IS 'Operação-Dados de Equipamento do Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2_equip.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_equip.id IS 'ID do Centro Nível 2 - Equipamento';
COMMENT ON COLUMN ope_centro2_equip.tipo_rodado IS 'Tipo do Rodado (00 - Não Aplicável; 01 - Truck; 02 - Toco; 03 - Cavalo Mecânico; 04 - Van; 05 - Utilitário; 06 - Outros)';
COMMENT ON COLUMN ope_centro2_equip.tipo_carroceria IS 'Tipo do Carroceria (00 - Não Aplicável; 01 - Aberta; 02 - Fechada/Baú; 03 - Graneleira; 04 - Porta Container; 05 - Siber)';
COMMENT ON COLUMN ope_centro2_equip.ger_cidade_id IS 'ID Cidade';
COMMENT ON COLUMN ope_centro2_equip.placa IS 'Placa';
COMMENT ON COLUMN ope_centro2_equip.renavam IS 'Renavam';
COMMENT ON COLUMN ope_centro2_equip.tara IS 'Tara';
COMMENT ON COLUMN ope_centro2_equip.capacidade_kg IS 'Capacidade em Kg';
COMMENT ON COLUMN ope_centro2_equip.capacidade_m3 IS 'Capacidade em M3';
COMMENT ON COLUMN ope_centro2_equip.potencia IS 'Potência';
COMMENT ON COLUMN ope_centro2_equip.nr_chassi IS 'Numero Chassi';
COMMENT ON COLUMN ope_centro2_equip.nr_serie IS 'Numero Série';
COMMENT ON COLUMN ope_centro2_equip.liberado_abastec IS 'Liberado para abastecimento';
COMMENT ON COLUMN ope_centro2_equip.largura IS 'Largura';
COMMENT ON COLUMN ope_centro2_equip.altura IS 'Altura';
COMMENT ON COLUMN ope_centro2_equip.nr_registro_estadual IS 'Numero Registro Estadual';
COMMENT ON COLUMN ope_centro2_equip.tipo_tracao IS 'Tipo 0-Tração, 1-Reboque/Implemento';
COMMENT ON COLUMN ope_centro2_equip.tipo_transp_auto_carga IS 'Tipo Transp. Automo Carga 1-Agreg; 2-Indenp; 3-Outros';
COMMENT ON COLUMN ope_centro2_equip.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_equip.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_equip.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_equip.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_equip.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_equip.ope_frente_trabalho_id IS 'ID da Frente de Trabalho';
COMMENT ON COLUMN ope_centro2_equip.data_venc_licenciamento IS 'Data de vencimento de Licenciamento';
COMMENT ON COLUMN ope_centro2_equip.data_venc_imposto IS 'Data de vencimento do Imposto';
ALTER TABLE ope_centro2_equip OWNER TO postgres;

CREATE TABLE ope_compart (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_compart varchar(50) NOT NULL,
capacidade decimal(18,6) NOT NULL DEFAULT 0,
valida_itemserv varchar(1) NOT NULL,
medicao_trab_centro varchar(1) NOT NULL DEFAULT 'N',
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_compart_subgrupo_id varchar(36),
data_aquisicao varchar(255),
data_baixa varchar(255),
ope_compart_status_id varchar(36),
data_status date,
observacao varchar(250),
valor_aquisicao numeric(18,2) NOT NULL DEFAULT 0,
numero_serie varchar(100),
CONSTRAINT pk_ope_compart PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart IS 'Operação-Compartimento';
COMMENT ON COLUMN ope_compart.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_compart.id IS 'ID do Compartimento';
COMMENT ON COLUMN ope_compart.nome IS 'Nome';
COMMENT ON COLUMN ope_compart.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart.sigla_compart IS 'Sigla do Compartimento';
COMMENT ON COLUMN ope_compart.capacidade IS 'Capacidade - Padrão';
COMMENT ON COLUMN ope_compart.valida_itemserv IS 'Valida Item/Serviço';
COMMENT ON COLUMN ope_compart.medicao_trab_centro IS 'Medicao de Trabalho: P-Principal, S-Secundário, N-Nenhum';
COMMENT ON COLUMN ope_compart.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_compart.ope_compart_subgrupo_id IS 'ID do Sub-Grupo do Compartimento';
COMMENT ON COLUMN ope_compart.data_aquisicao IS 'Data de Aquisição';
COMMENT ON COLUMN ope_compart.data_baixa IS 'Data da Baixa';
COMMENT ON COLUMN ope_compart.ope_compart_status_id IS 'ID do Status do Compartimento';
COMMENT ON COLUMN ope_compart.data_status IS 'Data do Status';
COMMENT ON COLUMN ope_compart.observacao IS 'Observação';
COMMENT ON COLUMN ope_compart.valor_aquisicao IS 'Valor Aquisição';
COMMENT ON COLUMN ope_compart.numero_serie IS 'Número Série';
ALTER TABLE ope_compart OWNER TO postgres;

CREATE TABLE ope_compart_itemserv (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
observacao varchar(250),
ativo varchar(1) NOT NULL,
ger_itemserv_id varchar(36) NOT NULL,
ope_compart_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_compart_itemserv PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_itemserv IS 'Operação-Item/Serviço do Compartimento';
COMMENT ON COLUMN ope_compart_itemserv.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_compart_itemserv.id IS 'ID do Item/Serviço do Compartimento';
COMMENT ON COLUMN ope_compart_itemserv.observacao IS 'Observação';
COMMENT ON COLUMN ope_compart_itemserv.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_itemserv.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ope_compart_itemserv.ope_compart_id IS 'ID do Compartamento';
COMMENT ON COLUMN ope_compart_itemserv.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_itemserv.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_itemserv.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_itemserv.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_compart_itemserv OWNER TO postgres;

CREATE TABLE ope_centro2_mov_media (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ope_centro2_id varchar(36),
ope_compart_id varchar(36) NOT NULL,
observacao varchar(250),
qnt_media_min numeric(18,6) NOT NULL DEFAULT 0,
qnt_media_max numeric(18,6) NOT NULL DEFAULT 0,
ger_itemserv_id varchar(36) NOT NULL,
ger_marca_modelo_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
capacidade numeric(18,6) DEFAULT 0,
dt_valid_ini date NOT NULL,
CONSTRAINT pk_ope_centro2_compart PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_mov_media IS 'Operação-Mov. Médio do Compart. x Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2_mov_media.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_mov_media.id IS 'Mov. Médio do Compart. x Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2_mov_media.ope_centro2_id IS 'ID do Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2_mov_media.ope_compart_id IS 'ID do Compartimento';
COMMENT ON COLUMN ope_centro2_mov_media.observacao IS 'Observação';
COMMENT ON COLUMN ope_centro2_mov_media.qnt_media_min IS 'Quantidade Média Mínima';
COMMENT ON COLUMN ope_centro2_mov_media.qnt_media_max IS 'Quantidade Média Máxima';
COMMENT ON COLUMN ope_centro2_mov_media.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ope_centro2_mov_media.ger_marca_modelo_id IS 'ID do Modelo';
COMMENT ON COLUMN ope_centro2_mov_media.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_mov_media.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_mov_media.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_mov_media.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_mov_media.capacidade IS 'Capacidade';
COMMENT ON COLUMN ope_centro2_mov_media.dt_valid_ini IS 'Data validade inicial';
ALTER TABLE ope_centro2_mov_media OWNER TO postgres;

CREATE TABLE fis_tributo (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nr_tributo varchar(50) NOT NULL,
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_tributo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_tributo IS 'Fiscal-Tributo';
COMMENT ON COLUMN fis_tributo.id IS 'ID da Unidade';
COMMENT ON COLUMN fis_tributo.nr_tributo IS 'Numero do Tributo';
COMMENT ON COLUMN fis_tributo.nome IS 'Nome';
COMMENT ON COLUMN fis_tributo.ativo IS 'Ativo';
COMMENT ON COLUMN fis_tributo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_tributo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_tributo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_tributo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_tributo OWNER TO postgres;

CREATE TABLE fin_cond_pagrec (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_cond_pagamento varchar(50)  NOT NULL,
considera_feriado varchar(1)  NOT NULL,
considera_final_sem varchar(1)  NOT NULL,
qnt_dia_ini int4 NOT NULL,
observacao varchar(250) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_prazo varchar(1),
CONSTRAINT pk_fin_cond_pagrec PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_cond_pagrec IS 'Financeiro-Condiçao de Pagamento/Recebimento';
COMMENT ON COLUMN fin_cond_pagrec.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_cond_pagrec.id IS 'ID da Condiçao de Pag/Rec';
COMMENT ON COLUMN fin_cond_pagrec.nome IS 'Nome';
COMMENT ON COLUMN fin_cond_pagrec.ativo IS 'Ativo';
COMMENT ON COLUMN fin_cond_pagrec.sigla_cond_pagamento IS 'Sigla da Condiçao de Pag/Rec';
COMMENT ON COLUMN fin_cond_pagrec.considera_feriado IS 'Considera Feriado: S-Sim, N-Não';
COMMENT ON COLUMN fin_cond_pagrec.considera_final_sem IS 'Considera Final de Semana: S-Sim, N-Não';
COMMENT ON COLUMN fin_cond_pagrec.qnt_dia_ini IS 'Quantidade Dias Inicial';
COMMENT ON COLUMN fin_cond_pagrec.observacao IS 'Observação';
COMMENT ON COLUMN fin_cond_pagrec.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_cond_pagrec.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_cond_pagrec.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_cond_pagrec.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_cond_pagrec.tipo_prazo IS 'À prazo: S-Sim, N-Não';
ALTER TABLE fin_cond_pagrec OWNER TO postgres;

CREATE TABLE fin_cond_pagrec_config (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
qnt_dia int4 NOT NULL,
fin_cond_pag_rec_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_cond_pagrec_config PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_cond_pagrec_config IS 'Financeiro-Configuração de Condiçao de Pagamento/Recebimento';
COMMENT ON COLUMN fin_cond_pagrec_config.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_cond_pagrec_config.id IS 'ID da Configuração de Condiçao de Pag/Rec';
COMMENT ON COLUMN fin_cond_pagrec_config.qnt_dia IS 'Quantidade Dias';
COMMENT ON COLUMN fin_cond_pagrec_config.fin_cond_pag_rec_id IS 'ID da Condiçao de Pag/Rec';
COMMENT ON COLUMN fin_cond_pagrec_config.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_cond_pagrec_config.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_cond_pagrec_config.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_cond_pagrec_config.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_cond_pagrec_config OWNER TO postgres;

CREATE TABLE fis_doc (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
mov_id varchar(36),
data_emissao timestamp(6) NOT NULL,
chave varchar(50) ,
numero int4 NOT NULL,
serie varchar(3)  NOT NULL,
fis_doc_tipo_id varchar(36) NOT NULL,
numero_ini int4,
numero_fin int4,
data_autorizado timestamp(6),
data_cancelado timestamp(6),
data_encerrado timestamp(6),
xml_assinado text ,
ambiente int4 NOT NULL,
tipo_emissao int4 NOT NULL,
status_sefaz int4,
xml_protocolado text,
log_user_ins text,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
pdf_emitido text,
numero_pre int4,
serie_pre varchar(3),
CONSTRAINT pk_fis_doc PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_doc IS 'Fiscal-Documentos';
COMMENT ON COLUMN fis_doc.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fis_doc.id IS 'ID do Documento';
COMMENT ON COLUMN fis_doc.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN fis_doc.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN fis_doc.data_emissao IS 'Data Emissão';
COMMENT ON COLUMN fis_doc.chave IS 'Chave Emissão';
COMMENT ON COLUMN fis_doc.numero IS 'Numero do Documento';
COMMENT ON COLUMN fis_doc.serie IS 'Série';
COMMENT ON COLUMN fis_doc.fis_doc_tipo_id IS 'ID do Tipo de Documento';
COMMENT ON COLUMN fis_doc.numero_ini IS 'Numero Inicial';
COMMENT ON COLUMN fis_doc.numero_fin IS 'Numero Final';
COMMENT ON COLUMN fis_doc.data_autorizado IS 'Data Autorizado';
COMMENT ON COLUMN fis_doc.data_cancelado IS 'Data Cancelado';
COMMENT ON COLUMN fis_doc.data_encerrado IS 'Data Encerrado';
COMMENT ON COLUMN fis_doc.xml_assinado IS 'XML Assinado';
COMMENT ON COLUMN fis_doc.ambiente IS 'Ambiente (1 - Producao 2 - Homologacao)';
COMMENT ON COLUMN fis_doc.tipo_emissao IS 'Tipo de Emissao (1 - Normal; 2 - SCAN; 9 - Off-Line)';
COMMENT ON COLUMN fis_doc.status_sefaz IS 'Código SEFAZ';
COMMENT ON COLUMN fis_doc.xml_protocolado IS 'XML Protocolado';
COMMENT ON COLUMN fis_doc.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_doc.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_doc.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_doc.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fis_doc.pdf_emitido IS 'PDF do Documento Emitido';
COMMENT ON COLUMN fis_doc.numero_pre IS 'Número Pré';
COMMENT ON COLUMN fis_doc.serie_pre IS 'Série Pré';
ALTER TABLE fis_doc OWNER TO postgres;

CREATE TABLE fis_doc_evento (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fis_doc_id varchar(36) NOT NULL,
xml_retorno text  NOT NULL,
tipo_evento int4 NOT NULL,
nr_protocolo varchar(50)  NOT NULL,
qnt_evento int4,
descricao_evento text ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
pdf_retorno text,
CONSTRAINT pk_fis_doc_evento PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_doc_evento IS 'Fiscal-Evento do Documento';
COMMENT ON COLUMN fis_doc_evento.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fis_doc_evento.id IS 'ID do Evento do Documento';
COMMENT ON COLUMN fis_doc_evento.fis_doc_id IS 'ID do Documento';
COMMENT ON COLUMN fis_doc_evento.xml_retorno IS 'XML Retorno';
COMMENT ON COLUMN fis_doc_evento.tipo_evento IS '1 - Autorizacao; 2 - Cancelamento; 3 - Inutilizacao; 4 - Carta de Correcao';
COMMENT ON COLUMN fis_doc_evento.nr_protocolo IS 'Numero Protocolo';
COMMENT ON COLUMN fis_doc_evento.qnt_evento IS 'Quantidade do Evento';
COMMENT ON COLUMN fis_doc_evento.descricao_evento IS 'Descricao do Evento';
COMMENT ON COLUMN fis_doc_evento.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_doc_evento.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_doc_evento.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_doc_evento.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fis_doc_evento.pdf_retorno IS 'PDF Retorno';
ALTER TABLE fis_doc_evento OWNER TO postgres;

CREATE TABLE fis_tributacao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fis_tributo_id varchar(36) NOT NULL,
mov_id varchar(36),
mov_itemserv_id varchar(36),
cst varchar(4)  NOT NULL,
modalidade_base_calc int4 NOT NULL,
valor_base_calc numeric(18,6) NOT NULL DEFAULT 0,
perc_aliquota numeric(18,6) NOT NULL DEFAULT 0,
valor_imposto numeric(18,6) NOT NULL DEFAULT 0,
valor_base_calc_isento numeric(18,6) NOT NULL DEFAULT 0,
perc_aliquota_isento numeric(18,6) NOT NULL DEFAULT 0,
valor_imposto_isento numeric(18,6) NOT NULL DEFAULT 0,
valor_base_calc_st numeric(18,6) NOT NULL DEFAULT 0,
margem_agregada_st numeric(18,6) NOT NULL DEFAULT 0,
perc_aliquota_st numeric(18,6) NOT NULL DEFAULT 0,
valor_imposto_st numeric(18,6) NOT NULL DEFAULT 0,
perc_reducao_base_calc numeric(18,6) NOT NULL DEFAULT 0,
observacao varchar(250) ,
valor_imposto_operacao numeric(18,6) NOT NULL DEFAULT 0,
valor_imposto_diferido numeric(18,6) NOT NULL DEFAULT 0,
perc_credito_sn numeric(18,6) NOT NULL DEFAULT 0,
valor_credito_sn numeric(18,6) NOT NULL DEFAULT 0,
valor_base_calc_fcp numeric(18,6) NOT NULL DEFAULT 0,
perc_aliquota_fcp numeric(18,6) NOT NULL DEFAULT 0,
valor_imposto_fcp numeric(18,6) NOT NULL DEFAULT 0,
valor_base_calc_fcp_st numeric(18,6) NOT NULL DEFAULT 0,
perc_aliquota_fcp_st numeric(18,6) NOT NULL DEFAULT 0,
valor_imposto_fcp_st numeric(18,6) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
fin_pagrec_id varchar(36),
ger_pessoa_endereco_id varchar(36),
perc_uf_fim_fcp numeric(18,6) DEFAULT 0,
valor_total_uf_fim_fcp numeric(18,6) DEFAULT 0,
valor_imposto_fcp_st_ret numeric(18,6) DEFAULT 0,
valor_base_calc_fcp_st_ret numeric(18,6) DEFAULT 0,
perc_aliquota_fcp_st_ret numeric(18,6) DEFAULT 0,
valor_imposto_desonerado numeric(18,6) DEFAULT 0,
motivo_imposto_desonerado int4,
modalidade_base_calc_st int4,
valor_base_calc_st_ret numeric(18,6) DEFAULT 0,
valor_imposto_st_ret numeric(18,6) DEFAULT 0,
perc_aliquota_red_base_calc_efetiva numeric(18,6) DEFAULT 0,
valor_base_calc_efetiva numeric(18,6) DEFAULT 0,
perc_aliquota_efetiva numeric(18,6) DEFAULT 0,
valor_imposto_efetiva numeric(18,6) DEFAULT 0,
perc_aliquota_credito numeric(18,6) DEFAULT 0,
valor_imposto_credito numeric(18,6) DEFAULT 0,
valor_base_calc_uf_fim numeric(18,6) DEFAULT 0,
perc_interna_uf_fim numeric(18,6) DEFAULT 0,
perc_interestadual_uf_fim numeric(18,6) DEFAULT 0,
perc_partilha_uf_fim numeric(18,6) DEFAULT 0,
valor_partilha_uf_fim numeric(18,6) DEFAULT 0,
valor_partilha_uf_inicio numeric(18,6) DEFAULT 0,
valor_imposto_substituto numeric(18,6),
data_valid date,
CONSTRAINT pk_fis_tributacao PRIMARY KEY (id) ,
CONSTRAINT chk_mov_id_mov_itemserv_id CHECK ((((mov_id IS NOT NULL) AND (mov_itemserv_id IS NULL)) OR ((mov_id IS NULL) AND (mov_itemserv_id IS NOT NULL))))
)
WITHOUT OIDS;
COMMENT ON TABLE fis_tributacao IS 'Fiscal-Tributação';
COMMENT ON COLUMN fis_tributacao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fis_tributacao.id IS 'ID da Tribução';
COMMENT ON COLUMN fis_tributacao.fis_tributo_id IS 'ID do Tributo';
COMMENT ON COLUMN fis_tributacao.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN fis_tributacao.mov_itemserv_id IS 'ID do Item/Serv do Movimento';
COMMENT ON COLUMN fis_tributacao.cst IS 'CST/CSOSN';
COMMENT ON COLUMN fis_tributacao.modalidade_base_calc IS 'Modalidade da Base de Calculo';
COMMENT ON COLUMN fis_tributacao.valor_base_calc IS 'Valor da Base de Calculo';
COMMENT ON COLUMN fis_tributacao.perc_aliquota IS 'Percentual da Aliquota';
COMMENT ON COLUMN fis_tributacao.valor_imposto IS 'Valor do Imposto';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_isento IS 'Valor da Base de Calculo Insento';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_isento IS 'Percentual da Aliquota Insento';
COMMENT ON COLUMN fis_tributacao.valor_imposto_isento IS 'Valor do Imposto Isento';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_st IS 'Valor da Base de Calculo ST';
COMMENT ON COLUMN fis_tributacao.margem_agregada_st IS 'Margem de Valor Agregado ST';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_st IS 'Percentual da Aliquota do Imposto ST';
COMMENT ON COLUMN fis_tributacao.valor_imposto_st IS 'Valor do Imposto ST';
COMMENT ON COLUMN fis_tributacao.perc_reducao_base_calc IS 'Percentual de Reduçao de Base de Calculo ICMS';
COMMENT ON COLUMN fis_tributacao.observacao IS 'Observação';
COMMENT ON COLUMN fis_tributacao.valor_imposto_operacao IS 'Valor do Imposto da Operacao';
COMMENT ON COLUMN fis_tributacao.valor_imposto_diferido IS 'Valor do Imposto Diferido';
COMMENT ON COLUMN fis_tributacao.perc_credito_sn IS 'Percentual de crédito aplicavel ao SN';
COMMENT ON COLUMN fis_tributacao.valor_credito_sn IS 'Valor do crédito do ICMS';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_fcp IS 'Valor da Base de Calculo FCP';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_fcp IS 'Percentual da Aliquota FCP';
COMMENT ON COLUMN fis_tributacao.valor_imposto_fcp IS 'Valor do FCP';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_fcp_st IS 'Valor da Base de Calculo FCP ST';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_fcp_st IS 'Percentual da Aliquota FCP ST';
COMMENT ON COLUMN fis_tributacao.valor_imposto_fcp_st IS 'Valor do FCP ST';
COMMENT ON COLUMN fis_tributacao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_tributacao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_tributacao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_tributacao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fis_tributacao.fin_pagrec_id IS 'ID do Pag/Rec';
COMMENT ON COLUMN fis_tributacao.ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa';
COMMENT ON COLUMN fis_tributacao.perc_uf_fim_fcp IS 'Percentual do ICMS relativo ao Fundo de Combate à pobreza (FCP) na UF de término da prestação do serviço de transporte';
COMMENT ON COLUMN fis_tributacao.valor_total_uf_fim_fcp IS 'Valor do ICMS relativo ao Fundo de Combate á Pobreza (FCP) da UF de término da prestação';
COMMENT ON COLUMN fis_tributacao.valor_imposto_fcp_st_ret IS 'Valor do FCP ST retido anteriormente';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_fcp_st_ret IS 'Valor da Base de Calculo FCP ST retido anteriormente';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_fcp_st_ret IS 'Percentual da Aliquota FCP ST retido anteriormente';
COMMENT ON COLUMN fis_tributacao.valor_imposto_desonerado IS 'Valor do desonerado';
COMMENT ON COLUMN fis_tributacao.motivo_imposto_desonerado IS 'Motivo da desoneração do ICMS Valores permitidos: 1-táxi, 3-produtor agropecuário, 4-frotista/locadora, 5-diplomático/consular, 6-utilitários e motocicletas, 7-SUFRAMA, 9-outros, 10-deficiente condutor, 11-deficiente não condutor, 12-órgão de fomento e desenvolvimento agropecuário, 16-Olimpíadas Rio 2016';
COMMENT ON COLUMN fis_tributacao.modalidade_base_calc_st IS 'Modalidade de determinação da base de cálculo do ICMS ST. Valores permitidos 0-preço tabelado ou máximo sugerido, 1-lista negativa (valor), 2-lista positiva (valor), 3-lista neutra (valor), 4-margem de valor agregado (%), 5-pauta (valor)';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_st_ret IS 'Valor da base de cálculo do ICMS retido anteriormente';
COMMENT ON COLUMN fis_tributacao.valor_imposto_st_ret IS 'Valor do ICMS retido anteriormente';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_red_base_calc_efetiva IS 'Informado apenas para icms_situacao_tributaria = 60 ou 500. Percentual de redução, caso estivesse submetida ao regime comum de tributação, para obtenção da base de cálculo efetiva (icms_base_calculo_efetiva). Obs.: opcional a critério da UF';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_efetiva IS 'Informado apenas para icms_situacao_tributaria = 60 ou 500. Valor da base de cálculo que seria atribuída à operação própria do contribuinte substituído, caso estivesse submetida ao regime comum de tributação, obtida pelo produto do valor_bruto do item por (1- icms_reducao_base_calculo_efetiva/100.0). Obs.: opcional a critério da UF';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_efetiva IS 'Informado apenas para icms_situacao_tributaria = 60 ou 500. Alíquota do ICMS na operação a consumidor final, caso estivesse submetida ao regime comum de tributação. Obs.: opcional a critério da UF';
COMMENT ON COLUMN fis_tributacao.valor_imposto_efetiva IS 'Informado apenas para icms_situacao_tributaria = 60 ou 500. Obtido pelo produto do valor do campo icms_aliquota_efetiva pelo valor do campo icms_base_calculo_efetiva, caso estivesse submetida ao regime comum de tributação. Obs.: opcional a critério da UF';
COMMENT ON COLUMN fis_tributacao.perc_aliquota_credito IS 'Alíquota aplicável de cálculo do crédito (Apenas Simples Nacional)';
COMMENT ON COLUMN fis_tributacao.valor_imposto_credito IS 'Valor crédito do ICMS que pode ser aproveitado nos termos do art. 23 da LC 123 (Apenas Simples Nacional)';
COMMENT ON COLUMN fis_tributacao.valor_base_calc_uf_fim IS 'Valor da BC do ICMS na UF de término da prestação do serviço de transporte';
COMMENT ON COLUMN fis_tributacao.perc_interna_uf_fim IS 'Alíquota interna da UF de término da prestação do serviço de transporte';
COMMENT ON COLUMN fis_tributacao.perc_interestadual_uf_fim IS 'Alíquota interestadual das UF envolvidas';
COMMENT ON COLUMN fis_tributacao.perc_partilha_uf_fim IS 'Percentual provisório de partilha entre os estados. (Valor padrão de 100% a partir de 2019)';
COMMENT ON COLUMN fis_tributacao.valor_partilha_uf_fim IS 'Valor do ICMS de partilha para a UF de término da prestação do serviço de transporte';
COMMENT ON COLUMN fis_tributacao.valor_partilha_uf_inicio IS 'Valor do ICMS de partilha para a UF de início da prestação do serviço de transporte';
COMMENT ON COLUMN fis_tributacao.valor_imposto_substituto IS 'Valor do Imposto Substituto';
COMMENT ON COLUMN fis_tributacao.data_valid IS 'Data de Validação';
ALTER TABLE fis_tributacao OWNER TO postgres;

CREATE TABLE ger_numeracao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
serie varchar(3)  NOT NULL,
ultimo_nr int4 NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_numeracao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_numeracao IS 'Geral-Numeração';
COMMENT ON COLUMN ger_numeracao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_numeracao.id IS 'ID da Numeração';
COMMENT ON COLUMN ger_numeracao.nome IS 'Nome';
COMMENT ON COLUMN ger_numeracao.ativo IS 'Ativo';
COMMENT ON COLUMN ger_numeracao.serie IS 'Série';
COMMENT ON COLUMN ger_numeracao.ultimo_nr IS 'Ultimo Número';
COMMENT ON COLUMN ger_numeracao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_numeracao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_numeracao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_numeracao.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_numeracao OWNER TO postgres;

CREATE TABLE mov (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
nr_externo varchar(50) ,
ger_pessoa_id varchar(36) NOT NULL,
ger_pessoa_endereco_id_fiscal varchar(36) NOT NULL,
mov_operacao_id varchar(36),
fin_cond_pagrec_id varchar(36),
data_mov timestamp(6),
numero_mov int4,
data_emissao timestamp(6),
fis_doc_tipo_id varchar(36),
serie_mov varchar(3) ,
mov_status_id varchar(36),
valor_total numeric(18,6) NOT NULL,
observacao varchar(250) ,
tipo_frete int4 NOT NULL,
data_entrega date,
data_entrada_saida date,
ger_pessoa_endereco_id_entrega varchar(36) NOT NULL,
ger_cidade_id_carreg varchar(36),
ger_cidade_id_descarreg varchar(36),
tipo_emissao_carga int4,
tipo_modal_carga varchar(2),
tipo_transportador_carga int4,
valor_carga numeric(18,6),
tipo_umedida_carga varchar(2) ,
qnt_carga numeric(18,6),
ger_pessoa_endereco_id_reme varchar(36),
ger_pessoa_endereco_id_dest varchar(36),
ger_pessoa_endereco_id_rece varchar(36),
ger_pessoa_endereco_id_expe varchar(36),
observacao_transp varchar(250),
observacao_serv varchar(250),
tipo_fretamento int4,
tipo_serv_frete int4,
tipo_tomador_serv_frete int4,
taf varchar(50),
data_anulacao date,
observacao_item varchar(250),
valor_financeiro_total numeric(18,6),
valor_item_frete_total numeric(18,6),
observacao_fiscal varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ger_pessoa_endereco_id_inter varchar(36),
fis_tipo_resp_reten varchar(1),
fis_exig_iss_nfs varchar(1),
fis_iss_retido_nfs varchar(1),
fis_nat_ope_nfs varchar(1),
numero_mov_pre int4,
serio_mov_pre varchar(3),
cep_carreg varchar(50),
cep_descarreg varchar(50),
tipo_carga varchar(2),
system_user_id_resp varchar(36),
data_valid date,
CONSTRAINT pk_mov PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov IS 'Movimentação-Movimento';
COMMENT ON COLUMN mov.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov.id IS 'ID do Movimento';
COMMENT ON COLUMN mov.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN mov.nr_externo IS 'Número Externo';
COMMENT ON COLUMN mov.ger_pessoa_id IS 'ID da Pessoa - Cliente/Fornecedor';
COMMENT ON COLUMN mov.ger_pessoa_endereco_id_fiscal IS 'ID do Endereço da Pessoa - Fiscal';
COMMENT ON COLUMN mov.mov_operacao_id IS 'ID da Opeação do Movimento';
COMMENT ON COLUMN mov.fin_cond_pagrec_id IS 'ID da Condição de Pag/Rec';
COMMENT ON COLUMN mov.data_mov IS 'Data Movimento';
COMMENT ON COLUMN mov.numero_mov IS 'Numero do Movimento';
COMMENT ON COLUMN mov.data_emissao IS 'Data de Emissao do Movimento';
COMMENT ON COLUMN mov.fis_doc_tipo_id IS 'ID do Tipo de Documento';
COMMENT ON COLUMN mov.serie_mov IS 'Serie do Movimento';
COMMENT ON COLUMN mov.mov_status_id IS 'ID do Status do Movimento';
COMMENT ON COLUMN mov.valor_total IS 'Valor Total do Movimento';
COMMENT ON COLUMN mov.observacao IS 'Observação do Movimento';
COMMENT ON COLUMN mov.tipo_frete IS 'Tipo de Frete (0 - Por conta do emitente; 1 - Por conta do destinatário/remetente; 2 - Por conta de terceiros; 9 - Sem frete)';
COMMENT ON COLUMN mov.data_entrega IS 'Data de Entrega';
COMMENT ON COLUMN mov.data_entrada_saida IS 'Data de Entrada/Saída';
COMMENT ON COLUMN mov.ger_pessoa_endereco_id_entrega IS 'ID do Endereço da Pessoa - Entrega';
COMMENT ON COLUMN mov.ger_cidade_id_carreg IS 'ID da Cidade - Carregamento da Carga';
COMMENT ON COLUMN mov.ger_cidade_id_descarreg IS 'ID da Cidade - Descarregamento da Carga';
COMMENT ON COLUMN mov.tipo_emissao_carga IS 'Tipo de Emissao da Carga (1 - Prestador de serviço de transporte; 2 - Transportador de Carga Própria)';
COMMENT ON COLUMN mov.tipo_modal_carga IS 'Tipo do Modal da Carga';
COMMENT ON COLUMN mov.tipo_transportador_carga IS 'Tipo de Transportador da Carga';
COMMENT ON COLUMN mov.valor_carga IS 'Valor total da Carga';
COMMENT ON COLUMN mov.tipo_umedida_carga IS 'Tipo de Unidade Medida da Carga (01-KG; 02-TON)';
COMMENT ON COLUMN mov.qnt_carga IS 'Quantidade da Carga';
COMMENT ON COLUMN mov.ger_pessoa_endereco_id_reme IS 'ID do Endereço da Pessoa - Remetente';
COMMENT ON COLUMN mov.ger_pessoa_endereco_id_dest IS 'ID do Endereço da Pessoa - Destinatário';
COMMENT ON COLUMN mov.ger_pessoa_endereco_id_rece IS 'ID do Endereço da Pessoa - Recebedor';
COMMENT ON COLUMN mov.ger_pessoa_endereco_id_expe IS 'ID do Endereço da Pessoa - Expedidor';
COMMENT ON COLUMN mov.observacao_transp IS 'Obervação - Transporte';
COMMENT ON COLUMN mov.observacao_serv IS 'Observação - Serviço';
COMMENT ON COLUMN mov.tipo_fretamento IS 'Tipo de Fretamento';
COMMENT ON COLUMN mov.tipo_serv_frete IS 'Tipo do Serviço de Frete';
COMMENT ON COLUMN mov.tipo_tomador_serv_frete IS 'Tipo Tomador de Serviço de Frete';
COMMENT ON COLUMN mov.taf IS 'Termo de Autorização de Fretamento';
COMMENT ON COLUMN mov.data_anulacao IS 'Data Anulação';
COMMENT ON COLUMN mov.observacao_item IS 'Observação do Item predominante';
COMMENT ON COLUMN mov.valor_financeiro_total IS 'Valor Financeiro Total';
COMMENT ON COLUMN mov.valor_item_frete_total IS 'Valor de Item do Frete';
COMMENT ON COLUMN mov.observacao_fiscal IS 'Observação Fiscal';
COMMENT ON COLUMN mov.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov.log_user_upd IS 'Log - Usuário de Alteraçao';
COMMENT ON COLUMN mov.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN mov.ger_pessoa_endereco_id_inter IS 'ID do Endereço da Pessoa - Intermediário';
COMMENT ON COLUMN mov.fis_tipo_resp_reten IS 'Tipo Responsável pela Retençao do ISS: 1 – Tomador, 2 – Intermediário';
COMMENT ON COLUMN mov.fis_exig_iss_nfs IS 'Tipo Exigibilidade ISS da NFS: 1 - Exigível, 2 - Não incidência, 3 - Isenção, 4 - Exportação, 5 - Imunidade, 6 - Exigibilidade Suspensa por Decisão Judicial, 7 - Exigibilidade Suspensa por Processo Administrativo';
COMMENT ON COLUMN mov.fis_iss_retido_nfs IS 'ISS retido na NFS: S-Sim, N-Não';
COMMENT ON COLUMN mov.fis_nat_ope_nfs IS 'Natureza Operação da NFS: 1 – Tributação no município, 2 - Tributação fora do município, 3 - Isenção, 4 - Imune, 5 – Exigibilidade suspensa por decisão judicial, 6 – Exigibilidade suspensa por procedimento administrativo';
COMMENT ON COLUMN mov.numero_mov_pre IS 'Numero do Movimento Pré';
COMMENT ON COLUMN mov.serio_mov_pre IS 'Série do Movimento Pré';
COMMENT ON COLUMN mov.cep_carreg IS 'Cep - Carregamento da Carga';
COMMENT ON COLUMN mov.cep_descarreg IS 'Cep - Descarregamento da Carga';
COMMENT ON COLUMN mov.tipo_carga IS 'Tipo Carga: 01-Granel sólido, 02-Granel líquido, 03-Frigorificada, 04-Conteinerizada, 05-Carga Geral, 06-Neogranel, 07-Perigosa (granel sólido), 08-Perigosa (granel líquido), 09-Perigosa (carga frigorificada), 10-Perigosa (conteinerizada), 11-Perigosa (carga geral)';
COMMENT ON COLUMN mov.system_user_id_resp IS 'ID do Usuário - Responsável';
COMMENT ON COLUMN mov.data_valid IS 'Data de Validação';
ALTER TABLE mov OWNER TO postgres;

CREATE TABLE mov_ciot (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_pessoa_id_responsavel varchar(36) NOT NULL,
nr_ciot varchar(50) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_ciot PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_ciot IS 'Movimentação-CIOT do Movimento';
COMMENT ON COLUMN mov_ciot.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_ciot.id IS 'ID da CIOT do Movimento';
COMMENT ON COLUMN mov_ciot.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_ciot.ger_pessoa_id_responsavel IS 'ID da Pessoal - Responsável';
COMMENT ON COLUMN mov_ciot.nr_ciot IS 'Numero do CIOT';
COMMENT ON COLUMN mov_ciot.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_ciot.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_ciot.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_ciot.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_ciot OWNER TO postgres;

CREATE TABLE mov_condutor (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_pessoa_id_condutor varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_condutor PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_condutor IS 'Movimentação-Condutor do Movimento';
COMMENT ON COLUMN mov_condutor.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_condutor.id IS 'ID do Condutor do Movimento';
COMMENT ON COLUMN mov_condutor.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_condutor.ger_pessoa_id_condutor IS 'ID da Pessoal - Condutor';
COMMENT ON COLUMN mov_condutor.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_condutor.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_condutor.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_condutor.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_condutor OWNER TO postgres;

CREATE TABLE mov_entrega (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_cidade_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_entrega PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_entrega IS 'Movimentação-Entrega do Movimento';
COMMENT ON COLUMN mov_entrega.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_entrega.id IS 'ID da Entrega do Movimento';
COMMENT ON COLUMN mov_entrega.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_entrega.ger_cidade_id IS 'ID da Cidade';
COMMENT ON COLUMN mov_entrega.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_entrega.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_entrega.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_entrega.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_entrega OWNER TO postgres;

CREATE TABLE mov_entrega_doc (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36),
mov_entrega_id varchar(36),
valor_total numeric(18,6) DEFAULT 0,
mov_id_interno varchar(36),
chave_documento varchar(50) ,
modelo_documento varchar(2) ,
serie_documento varchar(3) ,
nr_documento varchar(50) ,
subserie_documento varchar(2),
data_emissao date,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_entrega_doc PRIMARY KEY (id) ,
CONSTRAINT chk_mov_id_mov_entrega_id CHECK ((((mov_id IS NOT NULL) AND (mov_entrega_id IS NULL)) OR ((mov_id IS NULL) AND (mov_entrega_id IS NOT NULL))))
)
WITHOUT OIDS;
COMMENT ON TABLE mov_entrega_doc IS 'Movimentação-Documento da Entrega do Movimento';
COMMENT ON COLUMN mov_entrega_doc.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_entrega_doc.id IS 'ID do Documento da Entrega do Movimento';
COMMENT ON COLUMN mov_entrega_doc.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_entrega_doc.mov_entrega_id IS 'ID da Entrega do Movimento';
COMMENT ON COLUMN mov_entrega_doc.valor_total IS 'Valor Total do Documento';
COMMENT ON COLUMN mov_entrega_doc.mov_id_interno IS 'ID do Movimento - Interno';
COMMENT ON COLUMN mov_entrega_doc.chave_documento IS 'Chave do Documento';
COMMENT ON COLUMN mov_entrega_doc.modelo_documento IS 'Modelo do Documento';
COMMENT ON COLUMN mov_entrega_doc.serie_documento IS 'Serie do Documento';
COMMENT ON COLUMN mov_entrega_doc.nr_documento IS 'Numero do Documento';
COMMENT ON COLUMN mov_entrega_doc.subserie_documento IS 'Subsérie do Documento';
COMMENT ON COLUMN mov_entrega_doc.data_emissao IS 'Data Emissão';
COMMENT ON COLUMN mov_entrega_doc.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_entrega_doc.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_entrega_doc.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_entrega_doc.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_entrega_doc OWNER TO postgres;

CREATE TABLE mov_frete (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ope_centro2_id_equip varchar(36),
ger_pessoa_endereco_id_condutor varchar(36),
ger_pessoa_endereco_id_transp varchar(36),
valor_frete numeric(18,6) NOT NULL,
adic_frete_base_cal_icms varchar(1)  NOT NULL,
valor_base_calc numeric(18,6) NOT NULL,
perc_aliquota numeric(18,6) NOT NULL,
valor_imposto numeric(18,6) NOT NULL,
valor_pis numeric(18,6) NOT NULL,
valor_cofins numeric(18,6) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_frete PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_frete IS 'Movimentação-Frete do Movimento';
COMMENT ON COLUMN mov_frete.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_frete.id IS 'ID do Frete do Movimento';
COMMENT ON COLUMN mov_frete.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_frete.ope_centro2_id_equip IS 'ID do Entrada/Saida - Nível2 - Veiculo';
COMMENT ON COLUMN mov_frete.ger_pessoa_endereco_id_condutor IS 'ID da Pessoa - Condutor';
COMMENT ON COLUMN mov_frete.ger_pessoa_endereco_id_transp IS 'ID da Pessoa - Tranportador';
COMMENT ON COLUMN mov_frete.valor_frete IS 'Valor do Frete';
COMMENT ON COLUMN mov_frete.adic_frete_base_cal_icms IS 'Adiciona Frete Base de Calculo - ICMS';
COMMENT ON COLUMN mov_frete.valor_base_calc IS 'Valor da Base de Calculo - ICMS';
COMMENT ON COLUMN mov_frete.perc_aliquota IS 'Percentual da Aliquota - ICMS';
COMMENT ON COLUMN mov_frete.valor_imposto IS 'Valor do Imposto - ICMS';
COMMENT ON COLUMN mov_frete.valor_pis IS 'Valor do Imposto - PIS';
COMMENT ON COLUMN mov_frete.valor_cofins IS 'Valor do Imposto - COFINS';
COMMENT ON COLUMN mov_frete.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_frete.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_frete.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_frete.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_frete OWNER TO postgres;

CREATE TABLE mov_itemserv (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_itemserv_id varchar(36) NOT NULL,
qnt_orig numeric(18,6) NOT NULL DEFAULT 0,
valor_unit_orig numeric(18,6) NOT NULL DEFAULT 0,
ger_umedida_id_conv varchar(36) NOT NULL,
qnt_conv numeric(18,6) NOT NULL DEFAULT 0,
valor_unit_conv numeric(18,6) NOT NULL DEFAULT 0,
valor_bruto numeric(18,6) NOT NULL DEFAULT 0,
valor_desconto numeric(18,6) NOT NULL DEFAULT 0,
valor_acrecimo numeric(18,6) NOT NULL DEFAULT 0,
valor_outros numeric(18,6) NOT NULL DEFAULT 0,
valor_liquido numeric(18,6) NOT NULL DEFAULT 0,
qnt_devolvida numeric(18,6) NOT NULL DEFAULT 0,
valor_frete numeric(18,6) NOT NULL,
valor_seguro numeric(18,6) NOT NULL,
observacao varchar(250) ,
valor_tributo_retido numeric(18,6) NOT NULL DEFAULT 0,
fis_cfop_id varchar(36),
valor_tributo_total numeric(18,6) DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
qnt_altura numeric(18,6) DEFAULT 0,
qnt_largura numeric(18,6) DEFAULT 0,
qnt_comprimento numeric(18,6) DEFAULT 0,
nome_itemserv varchar(250),
ger_itemserv_var_id varchar(36),
ger_itemserv_lote_id varchar(36),
fis_obra_art varchar(50),
fis_obra_cei varchar(50),
fis_numero_proc_susp_nfs varchar(50),
fis_doc_cnae_nfs varchar(50),
valor_outros_tributo_ret numeric(18,6) DEFAULT 0,
valor_desconto_cond numeric(18,6) DEFAULT 0,
valor_desconto_incond numeric(18,6) DEFAULT 0,
valor_deducao numeric(18,6) DEFAULT 0,
qnt_min_pessoa_cot int4 DEFAULT 0,
data_valid date,
CONSTRAINT pk_mov_itemserv PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_itemserv IS 'Movimentação-Item/Serviço';
COMMENT ON COLUMN mov_itemserv.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_itemserv.id IS 'ID do Movimento de Item/Serviço';
COMMENT ON COLUMN mov_itemserv.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_itemserv.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN mov_itemserv.qnt_orig IS 'Quantidade Original';
COMMENT ON COLUMN mov_itemserv.valor_unit_orig IS 'Valor Unitário Original';
COMMENT ON COLUMN mov_itemserv.ger_umedida_id_conv IS 'ID da U.Medida - Conversão';
COMMENT ON COLUMN mov_itemserv.qnt_conv IS 'Quantidade - Convertido';
COMMENT ON COLUMN mov_itemserv.valor_unit_conv IS 'Valor Unitário - Convertido';
COMMENT ON COLUMN mov_itemserv.valor_bruto IS 'Valor Bruto';
COMMENT ON COLUMN mov_itemserv.valor_desconto IS 'Valor Desconto';
COMMENT ON COLUMN mov_itemserv.valor_acrecimo IS 'Valor Acrecimo';
COMMENT ON COLUMN mov_itemserv.valor_outros IS 'Valor Outros';
COMMENT ON COLUMN mov_itemserv.valor_liquido IS 'Valor Liquido';
COMMENT ON COLUMN mov_itemserv.qnt_devolvida IS 'Quantidade Devolvida';
COMMENT ON COLUMN mov_itemserv.valor_frete IS 'Valor Frete';
COMMENT ON COLUMN mov_itemserv.valor_seguro IS 'Valor Seguro';
COMMENT ON COLUMN mov_itemserv.observacao IS 'Observação';
COMMENT ON COLUMN mov_itemserv.valor_tributo_retido IS 'Valor Tributo Retido';
COMMENT ON COLUMN mov_itemserv.fis_cfop_id IS 'ID do CFOP';
COMMENT ON COLUMN mov_itemserv.valor_tributo_total IS 'Valor de Tributos Total';
COMMENT ON COLUMN mov_itemserv.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_itemserv.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_itemserv.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_itemserv.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN mov_itemserv.qnt_altura IS 'Quantidade - Altura';
COMMENT ON COLUMN mov_itemserv.qnt_largura IS 'Quantidade - Largura';
COMMENT ON COLUMN mov_itemserv.qnt_comprimento IS 'Quantidade - Comprimento';
COMMENT ON COLUMN mov_itemserv.nome_itemserv IS 'Nome Item/Serv - Genérico';
COMMENT ON COLUMN mov_itemserv.ger_itemserv_var_id IS 'ID da Variação do Item/Serviço';
COMMENT ON COLUMN mov_itemserv.ger_itemserv_lote_id IS 'ID do Lote do Item/Serviço';
COMMENT ON COLUMN mov_itemserv.fis_obra_art IS 'Art da Obra do Serviço';
COMMENT ON COLUMN mov_itemserv.fis_obra_cei IS 'Cei da Obra do Serviço';
COMMENT ON COLUMN mov_itemserv.fis_numero_proc_susp_nfs IS 'Numero do processo suspenção NFS';
COMMENT ON COLUMN mov_itemserv.fis_doc_cnae_nfs IS 'Documento Cnae da NFS';
COMMENT ON COLUMN mov_itemserv.valor_outros_tributo_ret IS 'Valor de outros Tributos Retidos';
COMMENT ON COLUMN mov_itemserv.valor_desconto_cond IS 'Valor Desconto Condicionado';
COMMENT ON COLUMN mov_itemserv.valor_desconto_incond IS 'Valor Desconto Incondicionado';
COMMENT ON COLUMN mov_itemserv.valor_deducao IS 'Valor de Dedução';
COMMENT ON COLUMN mov_itemserv.qnt_min_pessoa_cot IS 'Quantidade Minima de Cli/For para Cotação';
COMMENT ON COLUMN mov_itemserv.data_valid IS 'Data de Validação';
ALTER TABLE mov_itemserv OWNER TO postgres;

CREATE TABLE mov_lacre (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL,
mov_id varchar(36) NOT NULL,
lacres varchar(250) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_lacre PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_lacre IS 'Movimentação-Lacre do Movimento';
COMMENT ON COLUMN mov_lacre.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_lacre.id IS 'ID do Lacre do Movimento';
COMMENT ON COLUMN mov_lacre.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_lacre.lacres IS 'Lacre';
COMMENT ON COLUMN mov_lacre.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_lacre.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_lacre.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_lacre.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_lacre OWNER TO postgres;

CREATE TABLE mov_operacao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_mov_operacao varchar(50)  NOT NULL,
mov_tipo_id varchar(36) NOT NULL,
ger_numeracao_id varchar(36) NOT NULL,
finalidade_doc int4 NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_es varchar(1),
configuracao text,
CONSTRAINT pk_mov_operacao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_operacao IS 'Movimentação-Operação do Movimento';
COMMENT ON COLUMN mov_operacao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_operacao.id IS 'ID da Operação do Movimento';
COMMENT ON COLUMN mov_operacao.nome IS 'Nome';
COMMENT ON COLUMN mov_operacao.ativo IS 'Ativo';
COMMENT ON COLUMN mov_operacao.sigla_mov_operacao IS 'Sigla do Operação do Movimento';
COMMENT ON COLUMN mov_operacao.mov_tipo_id IS 'ID do Tipo Movimento';
COMMENT ON COLUMN mov_operacao.ger_numeracao_id IS 'ID de Numeração';
COMMENT ON COLUMN mov_operacao.finalidade_doc IS '(1-NF-e normal,2-NF-e complementar,3-NF-e de ajuste,4-Devolução de mercadoria)';
COMMENT ON COLUMN mov_operacao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_operacao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_operacao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_operacao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN mov_operacao.tipo_es IS 'Tipo: E-Entrada, S-Saída, T-Transferência';
COMMENT ON COLUMN mov_operacao.configuracao IS 'Configuração da Operação';
ALTER TABLE mov_operacao OWNER TO postgres;

CREATE TABLE mov_operacao_status (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_operacao_id varchar(36) NOT NULL,
mov_status_id varchar(36) NOT NULL,
mov_status_id_prox varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
mov_operacao_id_prox varchar(36),
CONSTRAINT pk_mov_operacao_status PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_operacao_status IS 'Movimentação-Operação x Status do Movimento';
COMMENT ON COLUMN mov_operacao_status.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_operacao_status.id IS 'ID da Operação x Status do Movimento';
COMMENT ON COLUMN mov_operacao_status.mov_operacao_id IS 'ID da Operação do Movimento';
COMMENT ON COLUMN mov_operacao_status.mov_status_id IS 'ID do Status do Movimento';
COMMENT ON COLUMN mov_operacao_status.mov_status_id_prox IS 'ID do Status do Movimento - Próximo';
COMMENT ON COLUMN mov_operacao_status.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_operacao_status.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_operacao_status.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_operacao_status.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN mov_operacao_status.mov_operacao_id_prox IS 'ID do Status do Movimento - Próximo';
ALTER TABLE mov_operacao_status OWNER TO postgres;

CREATE TABLE mov_pedagio (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_pessoa_id_emp_pedagio varchar(36) NOT NULL,
ger_pessoa_id_responsavel varchar(36) NOT NULL,
valor_pedagio numeric(18,6) NOT NULL,
nr_comprovante varchar(50) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_pedagio PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_pedagio IS 'Movimentação-Pedagio do Movimento';
COMMENT ON COLUMN mov_pedagio.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_pedagio.id IS 'ID do Pedagio do Movimento';
COMMENT ON COLUMN mov_pedagio.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_pedagio.ger_pessoa_id_emp_pedagio IS 'ID da Pessoal - Empresa do Pedágio';
COMMENT ON COLUMN mov_pedagio.ger_pessoa_id_responsavel IS 'ID da Pessoal - Responsável';
COMMENT ON COLUMN mov_pedagio.valor_pedagio IS 'Valor do Vale Pedagio';
COMMENT ON COLUMN mov_pedagio.nr_comprovante IS 'Numero do Comprovante';
COMMENT ON COLUMN mov_pedagio.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_pedagio.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_pedagio.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_pedagio.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_pedagio OWNER TO postgres;

CREATE TABLE mov_reboque (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ope_centro2_id_equip varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_reboque PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_reboque IS 'Movimentação-Reboque';
COMMENT ON COLUMN mov_reboque.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_reboque.id IS 'ID do Reboque do Movimento';
COMMENT ON COLUMN mov_reboque.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_reboque.ope_centro2_id_equip IS 'ID do Entrada/Saida - Nível2 - Veiculo Reboque';
COMMENT ON COLUMN mov_reboque.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_reboque.log_date_ins IS ' Log - Data de Inserção';
COMMENT ON COLUMN mov_reboque.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_reboque.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_reboque OWNER TO postgres;

CREATE TABLE mov_seguradora (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_pessoa_id_responsavel varchar(36) NOT NULL,
ger_pessoa_id_seguradora varchar(36) NOT NULL,
nr_apolice varchar(50) ,
nr_averbacao varchar(50) ,
valor numeric(18,6),
tipo_responsavel int4,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_seguradora PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_seguradora IS 'Movimentação-Seguro do Movimento';
COMMENT ON COLUMN mov_seguradora.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_seguradora.id IS 'ID do Seguro do Movimento';
COMMENT ON COLUMN mov_seguradora.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_seguradora.ger_pessoa_id_responsavel IS 'ID da Pessoal - Responsável';
COMMENT ON COLUMN mov_seguradora.ger_pessoa_id_seguradora IS 'ID da Pessoal - Seguradora';
COMMENT ON COLUMN mov_seguradora.nr_apolice IS 'Numero da Apolice';
COMMENT ON COLUMN mov_seguradora.nr_averbacao IS 'Numero da Averbacao';
COMMENT ON COLUMN mov_seguradora.valor IS 'Valor Seguro';
COMMENT ON COLUMN mov_seguradora.tipo_responsavel IS 'Tipo Responsável';
COMMENT ON COLUMN mov_seguradora.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_seguradora.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_seguradora.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_seguradora.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_seguradora OWNER TO postgres;

CREATE TABLE mov_tomador (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_pessoa_id_responsavel varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_tomador PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_tomador IS 'Movimentação-Tomador do Movimento';
COMMENT ON COLUMN mov_tomador.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_tomador.id IS 'ID de Tomador do Movimento';
COMMENT ON COLUMN mov_tomador.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_tomador.ger_pessoa_id_responsavel IS 'ID da Pessoal - Responsável';
COMMENT ON COLUMN mov_tomador.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_tomador.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_tomador.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_tomador.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_tomador OWNER TO postgres;

CREATE TABLE mov_status (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_mov_status varchar(50)  NOT NULL,
tipo_status varchar(1)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_status PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_status IS 'Movimentação-Status do Movimento';
COMMENT ON COLUMN mov_status.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_status.id IS 'ID do Status do Movimento';
COMMENT ON COLUMN mov_status.nome IS 'Nome';
COMMENT ON COLUMN mov_status.ativo IS 'Ativo';
COMMENT ON COLUMN mov_status.sigla_mov_status IS 'Sigla do Status do Movimento';
COMMENT ON COLUMN mov_status.tipo_status IS 'Tipo do Status (F - Finalizado; P - Pendente; C - Cancelado, E-Erro)';
COMMENT ON COLUMN mov_status.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_status.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_status.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_status.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_status OWNER TO postgres;
    
CREATE TABLE system_email_log (
unit_id varchar(36),
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
type_in_out varchar(2) NOT NULL,
date_log timestamp(6) NOT NULL DEFAULT now(),
email_from text NOT NULL,
subject text NOT NULL,
body text,
error_message text,
email_to text NOT NULL,
login varchar(50),
date_send timestamp(6),
body_type varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_email_log PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_email_log IS 'System-Log de envio de Email';
COMMENT ON COLUMN system_email_log.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN system_email_log.id IS 'ID do Log de envio de Email';
COMMENT ON COLUMN system_email_log.type_in_out IS 'Tipo Entrada ou Saída';
COMMENT ON COLUMN system_email_log.date_log IS 'Data/Hora do Log';
COMMENT ON COLUMN system_email_log.email_from IS 'Email - De';
COMMENT ON COLUMN system_email_log.subject IS 'Assunto';
COMMENT ON COLUMN system_email_log.body IS 'Corpo';
COMMENT ON COLUMN system_email_log.error_message IS 'Mensagem de Erro';
COMMENT ON COLUMN system_email_log.email_to IS 'Email - Para';
COMMENT ON COLUMN system_email_log.login IS 'Login';
COMMENT ON COLUMN system_email_log.date_send IS 'Data/Hora de Envio';
COMMENT ON COLUMN system_email_log.body_type IS 'Tipo do Corpo: text;html';
COMMENT ON COLUMN system_email_log.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_email_log.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_email_log.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_email_log.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_email_log OWNER TO postgres;

CREATE TABLE bor_dispositivo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100),
ativo varchar(1),
numero_serie varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro2_equip_id varchar(36),
tipo varchar(1),
ope_centro2_pessoa_id varchar(36),
CONSTRAINT pk_bor_dispositivo PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE UNIQUE INDEX idx_bor_dispositivo_01 ON bor_dispositivo USING btree (numero_serie pg_catalog.text_ops ASC NULLS LAST);
COMMENT ON TABLE bor_dispositivo IS 'Bordo-Dispositivos';
COMMENT ON COLUMN bor_dispositivo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN bor_dispositivo.id IS 'ID do Dispositivo de Bordo';
COMMENT ON COLUMN bor_dispositivo.nome IS 'Nome';
COMMENT ON COLUMN bor_dispositivo.ativo IS 'Ativo';
COMMENT ON COLUMN bor_dispositivo.numero_serie IS 'Número de Série';
COMMENT ON COLUMN bor_dispositivo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN bor_dispositivo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN bor_dispositivo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN bor_dispositivo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN bor_dispositivo.ope_centro2_equip_id IS 'ID do Centro Nível 2 - Equipamento';
COMMENT ON COLUMN bor_dispositivo.tipo IS 'Tipo Dispositivo: 1-Bordo, 2-IButton';
COMMENT ON COLUMN bor_dispositivo.ope_centro2_pessoa_id IS 'ID do Centro Nível 2 - Pessoal';
ALTER TABLE bor_dispositivo OWNER TO postgres;

CREATE TABLE ope_frente_trabalho (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
ger_empresa_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
sigla_frente_trabalho varchar(50),
CONSTRAINT pk_ope_frente_trabalho PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_frente_trabalho IS 'Operação-Frente de Trabalho';
COMMENT ON COLUMN ope_frente_trabalho.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_frente_trabalho.id IS 'ID da Frente de Trabalho';
COMMENT ON COLUMN ope_frente_trabalho.nome IS 'Nome';
COMMENT ON COLUMN ope_frente_trabalho.ativo IS 'Ativo';
COMMENT ON COLUMN ope_frente_trabalho.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_frente_trabalho.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_frente_trabalho.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_frente_trabalho.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_frente_trabalho.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_frente_trabalho.sigla_frente_trabalho IS 'Sigla da Frente de Trabalho';
ALTER TABLE ope_frente_trabalho OWNER TO postgres;

CREATE TABLE fis_certificado (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
nome_arq_certificado varchar(250),
senha varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_certificado PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_certificado IS 'Fiscal-Certificado de Transmissão';
COMMENT ON COLUMN fis_certificado.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fis_certificado.id IS 'ID do Certificado';
COMMENT ON COLUMN fis_certificado.nome IS 'Nome';
COMMENT ON COLUMN fis_certificado.ativo IS 'Ativo';
COMMENT ON COLUMN fis_certificado.nome_arq_certificado IS 'Arquivo do Certificado';
COMMENT ON COLUMN fis_certificado.senha IS 'Senha';
COMMENT ON COLUMN fis_certificado.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_certificado.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_certificado.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_certificado.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_certificado OWNER TO postgres;

CREATE TABLE fis_cest (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nr_cest varchar(50) NOT NULL,
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
data_validade date NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_cest PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_cest IS 'Fiscal-Cest';
COMMENT ON COLUMN fis_cest.id IS 'ID do CEST';
COMMENT ON COLUMN fis_cest.nr_cest IS 'Numero CEST';
COMMENT ON COLUMN fis_cest.nome IS 'Nome';
COMMENT ON COLUMN fis_cest.ativo IS 'Ativo';
COMMENT ON COLUMN fis_cest.data_validade IS 'Data Validade';
COMMENT ON COLUMN fis_cest.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_cest.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_cest.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_cest.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_cest OWNER TO postgres;

CREATE TABLE fis_cest_ncm (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fis_cest_id varchar(36) NOT NULL,
fis_ncm_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_cest_ncm PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_cest_ncm IS 'Fiscal-Cest x Ncm';
COMMENT ON COLUMN fis_cest_ncm.id IS 'ID do CEST NCM';
COMMENT ON COLUMN fis_cest_ncm.fis_cest_id IS 'ID do CEST';
COMMENT ON COLUMN fis_cest_ncm.fis_ncm_id IS 'ID do NCM';
COMMENT ON COLUMN fis_cest_ncm.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_cest_ncm.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_cest_ncm.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_cest_ncm.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_cest_ncm OWNER TO postgres;

CREATE TABLE fis_nbs (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nr_nbs varchar(50) NOT NULL,
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
data_validade date NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_nbs PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_nbs IS 'Fiscal-Nbs';
COMMENT ON COLUMN fis_nbs.id IS 'ID do NBS';
COMMENT ON COLUMN fis_nbs.nr_nbs IS 'Numero NBS';
COMMENT ON COLUMN fis_nbs.nome IS 'Nome';
COMMENT ON COLUMN fis_nbs.ativo IS 'Ativo';
COMMENT ON COLUMN fis_nbs.data_validade IS 'Data Validade';
COMMENT ON COLUMN fis_nbs.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_nbs.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_nbs.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_nbs.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_nbs OWNER TO postgres;

CREATE TABLE fis_ibpt (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
data_validade_ini date NOT NULL,
data_validade_fin date NOT NULL,
fis_nbs_id varchar(36),
fis_ncm_id varchar(36),
ger_uf_id varchar(36) NOT NULL,
perc_nacional numeric(18,6) NOT NULL DEFAULT 0,
perc_importado numeric(18,6) NOT NULL DEFAULT 0,
perc_municipal numeric(18,6) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fis_ibpt PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fis_ibpt IS 'Fiscal-Ibpt';
COMMENT ON COLUMN fis_ibpt.id IS 'ID do IBPT';
COMMENT ON COLUMN fis_ibpt.data_validade_ini IS 'Data Validade Inicial';
COMMENT ON COLUMN fis_ibpt.data_validade_fin IS 'Data Validade Final';
COMMENT ON COLUMN fis_ibpt.fis_nbs_id IS 'ID do NBS';
COMMENT ON COLUMN fis_ibpt.fis_ncm_id IS 'ID da NCM';
COMMENT ON COLUMN fis_ibpt.ger_uf_id IS 'ID da Uf';
COMMENT ON COLUMN fis_ibpt.perc_nacional IS 'Percentual Aliquota Nacional';
COMMENT ON COLUMN fis_ibpt.perc_importado IS 'Percentual Aliquota Importado';
COMMENT ON COLUMN fis_ibpt.perc_municipal IS 'Percentual Aliquota Municipal';
COMMENT ON COLUMN fis_ibpt.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fis_ibpt.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fis_ibpt.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fis_ibpt.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fis_ibpt OWNER TO postgres;

CREATE TABLE ger_itemserv_barra (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
codigo_barra varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
ger_itemserv_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_itemserv_barra PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_barra IS 'Geral-Código de Barra do Item/Serv';
COMMENT ON COLUMN ger_itemserv_barra.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_barra.id IS 'ID do Código de Barra do Item/Serv';
COMMENT ON COLUMN ger_itemserv_barra.codigo_barra IS 'Código de Barra';
COMMENT ON COLUMN ger_itemserv_barra.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv_barra.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_barra.log_user_ins IS ' Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_barra.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_barra.log_user_upd IS ' Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_barra.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_itemserv_barra OWNER TO postgres;

CREATE TABLE mov_origem (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
mov_id_origem varchar(36),
mov_itemserv_id varchar(36),
mov_itemserv_id_origem varchar(36),
tipo varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_origem PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_origem IS 'Movimentação-Tomador do Movimento';
COMMENT ON COLUMN mov_origem.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_origem.id IS 'ID do Origem de Movimento';
COMMENT ON COLUMN mov_origem.mov_id IS 'ID do Movimento - Atual';
COMMENT ON COLUMN mov_origem.mov_id_origem IS 'ID do Movimento - Origem';
COMMENT ON COLUMN mov_origem.mov_itemserv_id IS 'ID do Movimento de Item/Serviço - Atual';
COMMENT ON COLUMN mov_origem.mov_itemserv_id_origem IS 'ID do Movimento de Item/Serviço - Origem';
COMMENT ON COLUMN mov_origem.tipo IS 'Tipo Origem';
COMMENT ON COLUMN mov_origem.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_origem.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_origem.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_origem.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_origem OWNER TO postgres;

CREATE TABLE mov_medida (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_umedida_id varchar(36) NOT NULL,
tipo_medida varchar(50) NOT NULL,
qnt_medida numeric(18,6) NOT NULL,
marca varchar(50),
nr_volume numeric(18,6),
peso_liquido numeric(18,6) DEFAULT 0,
peso_bruto numeric(18,6) DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_medida PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_medida IS 'Movimentação-Entrega do Movimento';
COMMENT ON COLUMN mov_medida.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_medida.id IS 'ID da Medida do Movimento';
COMMENT ON COLUMN mov_medida.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_medida.ger_umedida_id IS 'ID da Unidade Medida';
COMMENT ON COLUMN mov_medida.tipo_medida IS 'Tipo da Medida';
COMMENT ON COLUMN mov_medida.qnt_medida IS 'Quantidade da Medida';
COMMENT ON COLUMN mov_medida.marca IS 'Marca';
COMMENT ON COLUMN mov_medida.nr_volume IS 'Número de Volume';
COMMENT ON COLUMN mov_medida.peso_liquido IS 'Peso Liquido';
COMMENT ON COLUMN mov_medida.peso_bruto IS 'Peso Bruto';
COMMENT ON COLUMN mov_medida.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_medida.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_medida.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_medida.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_medida OWNER TO postgres;

CREATE TABLE mov_comp (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
nome_comp varchar(50) NOT NULL,
qnt_comp numeric(18,6) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_comp PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_comp IS 'Movimentação-Entrega do Movimento';
COMMENT ON COLUMN mov_comp.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_comp.id IS 'ID da Componente do Movimento';
COMMENT ON COLUMN mov_comp.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_comp.nome_comp IS 'Nome do Componente';
COMMENT ON COLUMN mov_comp.qnt_comp IS 'Quantidade Componente';
COMMENT ON COLUMN mov_comp.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_comp.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_comp.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_comp.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_comp OWNER TO postgres;

CREATE TABLE ger_device (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_device varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_device PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_device IS 'Geral-Device';
COMMENT ON COLUMN ger_device.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_device.id IS 'ID do Device';
COMMENT ON COLUMN ger_device.nome IS 'Nome';
COMMENT ON COLUMN ger_device.ativo IS 'Ativo';
COMMENT ON COLUMN ger_device.sigla_device IS 'Sigla Device';
COMMENT ON COLUMN ger_device.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_device.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_device.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_device.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_device OWNER TO postgres;

CREATE TABLE ger_device_param (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
sigla_param varchar(50) NOT NULL,
ger_device_id varchar(36) NOT NULL,
valor_tx varchar(250),
valor_dt date,
valor_nm decimal(18,6),
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_device_param PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_device_param IS 'Geral-Parâmetros do Device';
COMMENT ON COLUMN ger_device_param.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_device_param.id IS 'ID do Parâmetro da Empresa';
COMMENT ON COLUMN ger_device_param.sigla_param IS 'Sigla do Parametro';
COMMENT ON COLUMN ger_device_param.ger_device_id IS 'ID da Empresa';
COMMENT ON COLUMN ger_device_param.valor_tx IS 'Valor Texto';
COMMENT ON COLUMN ger_device_param.valor_dt IS 'Valor Data';
COMMENT ON COLUMN ger_device_param.valor_nm IS 'Valor Numero';
COMMENT ON COLUMN ger_device_param.observacao IS 'Observação';
COMMENT ON COLUMN ger_device_param.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_device_param.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_device_param.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_device_param.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_device_param OWNER TO postgres;

CREATE TABLE ind (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
sigla_ind varchar(50),
nome varchar(100),
ger_umedida_id varchar(36),
casas_dec int4,
campo_ordenacao varchar(50),
metodo_ordenacao int4,
totalizador_atributo int4,
exibir_media_real varchar(1),
exibir_media_meta varchar(1),
exibir_dia varchar(1),
exibir_semana varchar(1),
exibir_quinzena varchar(1),
exibir_mes varchar(1),
exibir_bimestre varchar(1),
exibir_trimestre varchar(1),
exibir_quadrimestre varchar(1),
exibir_semestre varchar(1),
exibir_ano varchar(1),
acumular_semana varchar(1),
acumular_quinzena varchar(1),
acumular_mes varchar(1),
acumular_bimestre varchar(1),
acumular_trimestre varchar(1),
acumular_quadrimestre varchar(1),
acumular_semestre varchar(1),
acumular_ano varchar(1),
tipo_acumulo int4,
ind_id_ponderacao varchar(36),
grafico_tipo_atributo int4,
grafico_valor_vazio_zero varchar(1),
grafico_tipo_ind int4,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind IS 'Indicador-Configuração de Indicadores';
COMMENT ON COLUMN ind.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind.id IS 'ID do Indicador';
COMMENT ON COLUMN ind.sigla_ind IS 'Sigla Indicador';
COMMENT ON COLUMN ind.nome IS 'Nome';
COMMENT ON COLUMN ind.ger_umedida_id IS 'ID da U.Medida';
COMMENT ON COLUMN ind.casas_dec IS 'Casas Decimais';
COMMENT ON COLUMN ind.campo_ordenacao IS 'Campo Ordenação';
COMMENT ON COLUMN ind.metodo_ordenacao IS 'Metodo: 1-Crescente: 2-Descrescente';
COMMENT ON COLUMN ind.totalizador_atributo IS '1-Nenhum; 2-Soma; 3-Média';
COMMENT ON COLUMN ind.exibir_media_real IS 'Exibir Media do Valor Real';
COMMENT ON COLUMN ind.exibir_media_meta IS 'Exibir Media do Valor Meta';
COMMENT ON COLUMN ind.exibir_dia IS 'Exibir Dia';
COMMENT ON COLUMN ind.exibir_semana IS 'Exibir Semana';
COMMENT ON COLUMN ind.exibir_quinzena IS 'Exibir Quinzena';
COMMENT ON COLUMN ind.exibir_mes IS 'Exibir Mês';
COMMENT ON COLUMN ind.exibir_bimestre IS 'Exibir Bimestre';
COMMENT ON COLUMN ind.exibir_trimestre IS 'Exibir Trimestre';
COMMENT ON COLUMN ind.exibir_quadrimestre IS 'Exibir Quadrimestre';
COMMENT ON COLUMN ind.exibir_semestre IS 'Exibir Semestre';
COMMENT ON COLUMN ind.exibir_ano IS 'Exibir Ano';
COMMENT ON COLUMN ind.acumular_semana IS 'Acumular Valores na Semana';
COMMENT ON COLUMN ind.acumular_quinzena IS 'Acumular Valores na Quinzena';
COMMENT ON COLUMN ind.acumular_mes IS 'Acumular Valores na Mês';
COMMENT ON COLUMN ind.acumular_bimestre IS 'Acumular Valores na Bimestre';
COMMENT ON COLUMN ind.acumular_trimestre IS 'Acumular Valores na Trimestre';
COMMENT ON COLUMN ind.acumular_quadrimestre IS 'Acumular Valores na Quadrimestre';
COMMENT ON COLUMN ind.acumular_semestre IS 'Acumular Valores na Semestre';
COMMENT ON COLUMN ind.acumular_ano IS 'Acumular Valores na Ano';
COMMENT ON COLUMN ind.tipo_acumulo IS 'Tipo de Acumulo: 1-Manual; 2-Soma; 3-Média; 4-Media Ponderada; 5-Ultimo; 6-Maior; 7-Menor';
COMMENT ON COLUMN ind.ind_id_ponderacao IS 'ID do Indicador para Ponderação';
COMMENT ON COLUMN ind.grafico_tipo_atributo IS 'Tipo de Grafico para Atributos: 1-Coluna; 2-Linha; 3-Area';
COMMENT ON COLUMN ind.grafico_valor_vazio_zero IS 'Exibir Zero para valores vazios do Gráfico';
COMMENT ON COLUMN ind.grafico_tipo_ind IS 'Tipo de Gráfico para Indicador: 1-Coluna; 2-Pizza';
COMMENT ON COLUMN ind.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind OWNER TO postgres;

CREATE TABLE ind_relac (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ind_id varchar(36) NOT NULL,
ind_id_relac varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_relac PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_relac IS 'Indicador-Relacionamento de Indicadores';
COMMENT ON COLUMN ind_relac.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_relac.id IS 'ID do Relacionamento de Indicadores';
COMMENT ON COLUMN ind_relac.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_relac.ind_id_relac IS 'ID do Indicador - Relacionado';
COMMENT ON COLUMN ind_relac.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_relac.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_relac.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_relac.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_relac OWNER TO postgres;

CREATE TABLE ind_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
ordem_exibicao int4 NOT NULL,
sigla_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_grupo IS 'Indicador-Grupo';
COMMENT ON COLUMN ind_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_grupo.id IS 'ID do Grupo de Indicador';
COMMENT ON COLUMN ind_grupo.nome IS 'Nome';
COMMENT ON COLUMN ind_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ind_grupo.ordem_exibicao IS 'Ordem_Exibição';
COMMENT ON COLUMN ind_grupo.sigla_grupo IS 'Sigla do Grupo';
COMMENT ON COLUMN ind_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_grupo OWNER TO postgres;

CREATE TABLE ind_subgrupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
ordem_exibicao int4 NOT NULL,
sigla_subgrupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_subgrupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_subgrupo IS 'Indicador-Sub-Grupo';
COMMENT ON COLUMN ind_subgrupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_subgrupo.id IS 'ID do Sub-Grupo de Indicador';
COMMENT ON COLUMN ind_subgrupo.nome IS 'Nome';
COMMENT ON COLUMN ind_subgrupo.ativo IS 'Ativo';
COMMENT ON COLUMN ind_subgrupo.ordem_exibicao IS 'Ordem_Exibição';
COMMENT ON COLUMN ind_subgrupo.sigla_subgrupo IS 'Sigla do Sub-Grupo';
COMMENT ON COLUMN ind_subgrupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_subgrupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_subgrupo.log_user_upd IS ' Log - Usuário de Alteração';
COMMENT ON COLUMN ind_subgrupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_subgrupo OWNER TO postgres;

CREATE TABLE ind_grupo_relac_sub (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ind_id_grupo varchar(36) NOT NULL,
ind_id_subgrupo varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_grupo_relac_sub PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_grupo_relac_sub IS 'Indicador-Relacionamento de Grupo x Sub-Grupo de Indicadores';
COMMENT ON COLUMN ind_grupo_relac_sub.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_grupo_relac_sub.id IS 'ID do Relacionamento de Grupo x Sub-Grupo de Indicadores';
COMMENT ON COLUMN ind_grupo_relac_sub.ind_id_grupo IS 'ID do Grupo de Indicador';
COMMENT ON COLUMN ind_grupo_relac_sub.ind_id_subgrupo IS 'ID do Sub-Grupo de Indicador';
COMMENT ON COLUMN ind_grupo_relac_sub.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_grupo_relac_sub.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_grupo_relac_sub.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_grupo_relac_sub.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_grupo_relac_sub OWNER TO postgres;

CREATE TABLE ger_per (
unit_id varchar(36) NOT NULL,
id varchar(50) NOT NULL DEFAULT uuid_generate_v4(),
data_dia_inicial date,
dia_nome varchar(50),
data_semana_inicial date,
semana_nome varchar(50),
data_quinzena_inicial date,
quinzena_nome varchar(50),
data_mes_inicial date,
mes_nome varchar(50),
data_bimestre_inicial date,
bimestre_nome varchar(50),
data_trimestre_inicial date,
trimestre_nome varchar(50),
data_quadrimestre_inicial date,
quadrimestre_nome varchar(50),
data_semestre_inicial date,
semestre_nome varchar(50),
data_ano_inicial date,
ano_nome varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_per PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_per IS 'Geral-Períodos';
COMMENT ON COLUMN ger_per.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_per.id IS 'ID da Período';
COMMENT ON COLUMN ger_per.data_dia_inicial IS 'Dia';
COMMENT ON COLUMN ger_per.dia_nome IS 'Nome do Dia';
COMMENT ON COLUMN ger_per.data_semana_inicial IS 'Dia Inicial da Semana';
COMMENT ON COLUMN ger_per.semana_nome IS 'Nome da Semana';
COMMENT ON COLUMN ger_per.data_quinzena_inicial IS 'Dia Inicial da Quinzena';
COMMENT ON COLUMN ger_per.quinzena_nome IS 'Nome da Quinzena';
COMMENT ON COLUMN ger_per.data_mes_inicial IS 'Dia Inicial da Mês';
COMMENT ON COLUMN ger_per.mes_nome IS 'Nome da Mês';
COMMENT ON COLUMN ger_per.data_bimestre_inicial IS 'Dia Inicial da Bimestre';
COMMENT ON COLUMN ger_per.bimestre_nome IS 'Nome da Bimestre';
COMMENT ON COLUMN ger_per.data_trimestre_inicial IS 'Dia Inicial da Trimestre';
COMMENT ON COLUMN ger_per.trimestre_nome IS 'Nome da Trimestre';
COMMENT ON COLUMN ger_per.data_quadrimestre_inicial IS 'Dia Inicial da Quadrimestre';
COMMENT ON COLUMN ger_per.quadrimestre_nome IS 'Nome da Quadrimestre';
COMMENT ON COLUMN ger_per.data_semestre_inicial IS 'Dia Inicial da Semestre';
COMMENT ON COLUMN ger_per.semestre_nome IS 'Nome da Semestre';
COMMENT ON COLUMN ger_per.data_ano_inicial IS 'Dia Inicial da Ano';
COMMENT ON COLUMN ger_per.ano_nome IS 'Nome da Ano';
COMMENT ON COLUMN ger_per.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_per.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_per.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_per.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_per OWNER TO postgres;

CREATE TABLE ind_vr_dia (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(50) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_dia PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_dia IS 'Indicador-Valores Indicador por Dia';
COMMENT ON COLUMN ind_vr_dia.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_dia.id IS 'ID do Valor do Indicador por Dia';
COMMENT ON COLUMN ind_vr_dia.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_dia.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_dia.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_dia.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_dia.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_dia.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_dia.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_dia.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_dia.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_dia.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_dia.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_dia OWNER TO postgres;

CREATE TABLE ind_vr_semana (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(36) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_semana PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_semana IS 'Indicador-Valores Indicador por Semana';
COMMENT ON COLUMN ind_vr_semana.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_semana.id IS 'ID do Valor do Indicador por Semana';
COMMENT ON COLUMN ind_vr_semana.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_semana.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_semana.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_semana.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_semana.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_semana.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_semana.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_semana.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_semana.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_semana.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_semana.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_semana OWNER TO postgres;

CREATE TABLE ind_vr_quinzena (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(50) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_quinzena PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_quinzena IS 'Indicador-Valores Indicador por Quinzena';
COMMENT ON COLUMN ind_vr_quinzena.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_quinzena.id IS 'ID do Valor do Indicador por Quinzena';
COMMENT ON COLUMN ind_vr_quinzena.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_quinzena.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_quinzena.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_quinzena.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_quinzena.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_quinzena.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_quinzena.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_quinzena.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_quinzena.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_quinzena.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_quinzena.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_quinzena OWNER TO postgres;

CREATE TABLE ind_vr_mes (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(36) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_mes PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_mes IS 'Indicador-Valores Indicador por Mês';
COMMENT ON COLUMN ind_vr_mes.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_mes.id IS 'ID do Valor do Indicador por Mês';
COMMENT ON COLUMN ind_vr_mes.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_mes.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_mes.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_mes.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_mes.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_mes.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_mes.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_mes.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_mes.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_mes.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_mes.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_mes OWNER TO postgres;

CREATE TABLE ind_vr_bimestre (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(50) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_bimestre PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_bimestre IS 'Indicador-Valores Indicador por Bimestre';
COMMENT ON COLUMN ind_vr_bimestre.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_bimestre.id IS 'ID do Valor do Indicador por Bimestre';
COMMENT ON COLUMN ind_vr_bimestre.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_bimestre.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_bimestre.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_bimestre.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_bimestre.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_bimestre.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_bimestre.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_bimestre.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_bimestre.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_bimestre.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_bimestre.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_bimestre OWNER TO postgres;

CREATE TABLE ind_vr_trimestre (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(50) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_trimestre PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_trimestre IS 'Indicador-Valores Indicador por Trimestre';
COMMENT ON COLUMN ind_vr_trimestre.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_trimestre.id IS 'ID do Valor do Indicador por Trimestre';
COMMENT ON COLUMN ind_vr_trimestre.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_trimestre.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_trimestre.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_trimestre.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_trimestre.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_trimestre.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_trimestre.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_trimestre.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_trimestre.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_trimestre.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_trimestre.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_trimestre OWNER TO postgres;

CREATE TABLE ind_vr_quadrimestre (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(36) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_quadrimestre PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_quadrimestre IS 'Indicador-Valores Indicador por Quadrimestre';
COMMENT ON COLUMN ind_vr_quadrimestre.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_quadrimestre.id IS 'ID do Valor do Indicador por Quadrimestre';
COMMENT ON COLUMN ind_vr_quadrimestre.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_quadrimestre.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_quadrimestre.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_quadrimestre.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_quadrimestre.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_quadrimestre.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_quadrimestre.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_quadrimestre.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_quadrimestre.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_quadrimestre.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_quadrimestre.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_quadrimestre OWNER TO postgres;

CREATE TABLE ind_vr_semestre (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(36) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_semestre PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_semestre IS 'Indicador-Valores Indicador por Semestre';
COMMENT ON COLUMN ind_vr_semestre.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_semestre.id IS 'ID do Valor do Indicador por Semestre';
COMMENT ON COLUMN ind_vr_semestre.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_semestre.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_semestre.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_semestre.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_semestre.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_semestre.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_semestre.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_semestre.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_semestre.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_semestre.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_semestre.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_semestre OWNER TO postgres;

CREATE TABLE ind_vr_ano (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
ger_per_id varchar(50) NOT NULL,
ind_id varchar(36) NOT NULL,
atributo varchar(100) NOT NULL,
valor_real numeric(18,6) NOT NULL DEFAULT 0,
valor_meta numeric(18,6) NOT NULL DEFAULT 0,
aprovado_exibicao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ind_vr_ano PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_vr_ano IS 'Indicador-Valores Indicador por Ano';
COMMENT ON COLUMN ind_vr_ano.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ind_vr_ano.id IS 'ID do Valor do Indicador por Ano';
COMMENT ON COLUMN ind_vr_ano.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ind_vr_ano.ger_per_id IS 'ID do Período';
COMMENT ON COLUMN ind_vr_ano.ind_id IS 'ID do Indicador';
COMMENT ON COLUMN ind_vr_ano.atributo IS 'Atributo';
COMMENT ON COLUMN ind_vr_ano.valor_real IS 'Valor Real';
COMMENT ON COLUMN ind_vr_ano.valor_meta IS 'Valor da Meta';
COMMENT ON COLUMN ind_vr_ano.aprovado_exibicao IS 'Aprovado para Exibição';
COMMENT ON COLUMN ind_vr_ano.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_vr_ano.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_vr_ano.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_vr_ano.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_vr_ano OWNER TO postgres;

CREATE TABLE mov_percurso (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
ger_cidade_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_percurso PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_percurso IS 'Movimentação-Percurso do Movimento';
COMMENT ON COLUMN mov_percurso.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_percurso.id IS 'ID da Percurso do Movimento';
COMMENT ON COLUMN mov_percurso.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_percurso.ger_cidade_id IS 'ID da Cidade';
COMMENT ON COLUMN mov_percurso.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_percurso.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_percurso.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_percurso.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_percurso OWNER TO postgres;

CREATE TABLE fin_pagrec (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
fin_cond_pagrec_id varchar(36) NOT NULL,
numero_parc_total int4 NOT NULL DEFAULT 1,
tipo_es varchar(1) NOT NULL,
fin_pagrec_tipo_id varchar(36) NOT NULL,
numero_doc_pagrec varchar(50) NOT NULL,
ger_pessoa_id varchar(36) NOT NULL,
ger_pessoa_id_pagrec varchar(36) NOT NULL,
observacao varchar(250),
data_mov date NOT NULL,
valor_pagrec numeric(18,2) NOT NULL DEFAULT 0,
ope_centro_rat_tipo_id varchar(36),
fin_doc_tipo_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
process_id varchar(36),
data_valid date,
CONSTRAINT pk_fin_pagrec PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec IS 'Financeiro-Titulos Pag / Rec';
COMMENT ON COLUMN fin_pagrec.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec.id IS 'ID do Pag/Rec';
COMMENT ON COLUMN fin_pagrec.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN fin_pagrec.fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec';
COMMENT ON COLUMN fin_pagrec.numero_parc_total IS 'Numero Total de Parcelas';
COMMENT ON COLUMN fin_pagrec.tipo_es IS 'Tipo: E-Entrada; S-Saída';
COMMENT ON COLUMN fin_pagrec.fin_pagrec_tipo_id IS 'ID do Tipo de Pag/Rec';
COMMENT ON COLUMN fin_pagrec.numero_doc_pagrec IS 'Numero Documento do Pag/Rec';
COMMENT ON COLUMN fin_pagrec.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN fin_pagrec.ger_pessoa_id_pagrec IS 'ID da Pessoa - Pag/Rec';
COMMENT ON COLUMN fin_pagrec.observacao IS 'Observação';
COMMENT ON COLUMN fin_pagrec.data_mov IS 'Data Movimento';
COMMENT ON COLUMN fin_pagrec.valor_pagrec IS 'Valor do Pag/Rec';
COMMENT ON COLUMN fin_pagrec.ope_centro_rat_tipo_id IS 'ID do Tipo de Rateio de Centro de Entrada/Saída';
COMMENT ON COLUMN fin_pagrec.fin_doc_tipo_id IS 'ID do Tipo de Documento';
COMMENT ON COLUMN fin_pagrec.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec.process_id IS 'ID do Processo';
COMMENT ON COLUMN fin_pagrec.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec OWNER TO postgres;

CREATE TABLE fin_pagrec_parc (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
numero_parc int4 NOT NULL,
fin_pagrec_id varchar(36) NOT NULL,
fin_doc_tipo_id varchar(36) NOT NULL,
valor_pagrec numeric(18,2) NOT NULL DEFAULT 0,
valor_juro numeric(18,2) NOT NULL DEFAULT 0,
valor_desconto numeric(18,2) NOT NULL DEFAULT 0,
valor_multa numeric(18,2) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
data_venc date,
data_valid date,
CONSTRAINT pk_fin_pagrec_parc PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_parc IS 'Financeiro-Baixa de Parcela de Titulos Pag/Rec';
COMMENT ON COLUMN fin_pagrec_parc.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_parc.id IS 'ID da Parcela Pag/Rec';
COMMENT ON COLUMN fin_pagrec_parc.numero_parc IS 'Numero Parcela';
COMMENT ON COLUMN fin_pagrec_parc.fin_pagrec_id IS 'ID do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_parc.fin_doc_tipo_id IS 'ID do Tipo de Documento';
COMMENT ON COLUMN fin_pagrec_parc.valor_pagrec IS 'Valor do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_parc.valor_juro IS 'Valor do Juro';
COMMENT ON COLUMN fin_pagrec_parc.valor_desconto IS 'Valor do Desconto';
COMMENT ON COLUMN fin_pagrec_parc.valor_multa IS 'Valor da Multa';
COMMENT ON COLUMN fin_pagrec_parc.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_parc.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_parc.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_parc.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_parc.data_venc IS 'Data Vencimento';
COMMENT ON COLUMN fin_pagrec_parc.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_parc OWNER TO postgres;

CREATE TABLE fin_pagrec_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
aceita_entrada varchar(1) NOT NULL,
aceita_saida varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_tipo_pagrec PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_tipo IS 'Financeiro-Tipo de Pag/Rec';
COMMENT ON COLUMN fin_pagrec_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_tipo.id IS 'ID do Tipo de Baixa';
COMMENT ON COLUMN fin_pagrec_tipo.nome IS 'Nome';
COMMENT ON COLUMN fin_pagrec_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN fin_pagrec_tipo.aceita_entrada IS 'Aceita Entrada';
COMMENT ON COLUMN fin_pagrec_tipo.aceita_saida IS 'Aceita Saida';
COMMENT ON COLUMN fin_pagrec_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_tipo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_pagrec_tipo OWNER TO postgres;

CREATE TABLE fin_lote (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
nome varchar(100) NOT NULL,
data_lote date NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_lote PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_lote IS 'Financeiro-Lote';
COMMENT ON COLUMN fin_lote.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_lote.id IS 'ID do Lote';
COMMENT ON COLUMN fin_lote.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN fin_lote.nome IS 'Nome';
COMMENT ON COLUMN fin_lote.data_lote IS 'Data do Lote';
COMMENT ON COLUMN fin_lote.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_lote.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_lote.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_lote.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_lote OWNER TO postgres;

CREATE TABLE fin_pagrec_baixa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
tipo varchar(1) NOT NULL,
fin_pagrec_parc_id varchar(36) NOT NULL,
fin_conta_id varchar(36) NOT NULL,
fin_doc_tipo_id varchar(36) NOT NULL,
fin_lote_id varchar(36) NOT NULL,
numero_doc_pagrec varchar(50) NOT NULL,
valor_pagrec numeric(18,2) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
data_baixa date,
data_valid date,
CONSTRAINT pk_fin_pagrec_baixa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_baixa IS 'Financeiro-Baixa de Titulo Pag/Rec';
COMMENT ON COLUMN fin_pagrec_baixa.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_baixa.id IS 'ID da Baixa Pag/Rec';
COMMENT ON COLUMN fin_pagrec_baixa.tipo IS 'Tipo de Baixa: N-Normal; A-Agrupamento; E-Encontro';
COMMENT ON COLUMN fin_pagrec_baixa.fin_pagrec_parc_id IS 'ID da Parcela do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_baixa.fin_conta_id IS 'ID da Conta';
COMMENT ON COLUMN fin_pagrec_baixa.fin_doc_tipo_id IS 'ID do Tipo de Documento';
COMMENT ON COLUMN fin_pagrec_baixa.fin_lote_id IS 'ID do Lote';
COMMENT ON COLUMN fin_pagrec_baixa.numero_doc_pagrec IS 'Numero Documento do Pag/Rec (Cheque,Outros)';
COMMENT ON COLUMN fin_pagrec_baixa.valor_pagrec IS 'Valor do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_baixa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_baixa.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_baixa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_baixa.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_baixa.data_baixa IS 'Data da Baixa';
COMMENT ON COLUMN fin_pagrec_baixa.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_baixa OWNER TO postgres;

CREATE TABLE fin_tipo_variacao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
tipo varchar(1) NOT NULL,
valor_positivo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_tipo_variacao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_tipo_variacao IS 'Financeiro-Tipo de Variação';
COMMENT ON COLUMN fin_tipo_variacao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_tipo_variacao.id IS 'ID do Tipo de Variação';
COMMENT ON COLUMN fin_tipo_variacao.nome IS 'Nome';
COMMENT ON COLUMN fin_tipo_variacao.ativo IS 'Ativo';
COMMENT ON COLUMN fin_tipo_variacao.tipo IS 'Tipo de Baixa: J-Juros; D-Descontos; A-Abatimento; M-Multa';
COMMENT ON COLUMN fin_tipo_variacao.valor_positivo IS 'Valor Positivo';
COMMENT ON COLUMN fin_tipo_variacao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_tipo_variacao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_tipo_variacao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_tipo_variacao.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_tipo_variacao OWNER TO postgres;

CREATE TABLE fin_pagrec_parc_var (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fin_pagrec_parc_id varchar(36) NOT NULL,
fin_tipo_variacao_id varchar(36) NOT NULL,
valor numeric(18,2) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
data_valid date,
CONSTRAINT pk_fin_pagrec_parc_var PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_parc_var IS 'Financeiro-Variação da Baixa de Parcela ';
COMMENT ON COLUMN fin_pagrec_parc_var.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_parc_var.id IS 'ID da Variação da Parcela';
COMMENT ON COLUMN fin_pagrec_parc_var.fin_pagrec_parc_id IS 'ID da Parcela de Pag/Rec';
COMMENT ON COLUMN fin_pagrec_parc_var.fin_tipo_variacao_id IS 'ID do Tipo de Variação';
COMMENT ON COLUMN fin_pagrec_parc_var.valor IS 'Valor';
COMMENT ON COLUMN fin_pagrec_parc_var.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_parc_var.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_parc_var.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_parc_var.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_parc_var.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_parc_var OWNER TO postgres;

CREATE TABLE fin_pagrec_origem (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fin_pagrec_id varchar(36) NOT NULL,
fin_pagrec_id_origem varchar(36),
fin_pagrec_parc_id varchar(36),
fin_pagrec_parc_id_origem varchar(36),
tipo varchar(50),
mov_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
fin_pagrec_baixa_id varchar(36),
fin_extrato_id varchar(36),
fin_recibo_id varchar(36),
fin_pagrec_banco_id varchar(36),
CONSTRAINT pk_fin_pagrec_origem PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_origem IS 'Financeiro-Origem de Pag/Rec';
COMMENT ON COLUMN fin_pagrec_origem.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_origem.id IS 'ID do Origem de Pag/Rec';
COMMENT ON COLUMN fin_pagrec_origem.fin_pagrec_id IS 'ID do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_origem.fin_pagrec_id_origem IS 'ID do Pag/Rec - Origem';
COMMENT ON COLUMN fin_pagrec_origem.fin_pagrec_parc_id IS 'ID da Parcela do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_origem.fin_pagrec_parc_id_origem IS 'ID da Parcela do Pag/Rec - Origem';
COMMENT ON COLUMN fin_pagrec_origem.tipo IS 'Tipo Origem';
COMMENT ON COLUMN fin_pagrec_origem.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN fin_pagrec_origem.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_origem.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_origem.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_origem.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_origem.fin_pagrec_baixa_id IS 'ID da Baixa Pag/Rec';
COMMENT ON COLUMN fin_pagrec_origem.fin_extrato_id IS 'ID da Extrato Mov. Bancario';
COMMENT ON COLUMN fin_pagrec_origem.fin_recibo_id IS 'ID do Recibo';
COMMENT ON COLUMN fin_pagrec_origem.fin_pagrec_banco_id IS 'ID da Movimento Bancário de Pag/Rec';
ALTER TABLE fin_pagrec_origem OWNER TO postgres;

CREATE TABLE fin_doc_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
nr_doc varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ger_numeracao_id varchar(36),
CONSTRAINT pk_fin_doc_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_doc_tipo IS 'Financeiro-Tipo de Documento';
COMMENT ON COLUMN fin_doc_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_doc_tipo.id IS 'ID do Tipo de Documento';
COMMENT ON COLUMN fin_doc_tipo.nome IS 'Nome';
COMMENT ON COLUMN fin_doc_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN fin_doc_tipo.nr_doc IS 'Numero Documento';
COMMENT ON COLUMN fin_doc_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_doc_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_doc_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_doc_tipo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_doc_tipo.ger_numeracao_id IS 'ID da Numeração';
ALTER TABLE fin_doc_tipo OWNER TO postgres;

CREATE TABLE fin_pagrec_class (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fin_pagrec_id varchar(36),
fin_class_id varchar(36) NOT NULL,
valor numeric(18,2) NOT NULL DEFAULT 0,
fator_rat numeric(18,6) NOT NULL DEFAULT 0,
perc_rat numeric(18,6) NOT NULL DEFAULT 0,
fin_pagrec_banco_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
data_valid date,
CONSTRAINT pk_fin_pagrec_class PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_class IS 'Financeiro-Classificação do Titulo Pag/Rec';
COMMENT ON COLUMN fin_pagrec_class.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_class.id IS 'ID da Classificação do Titulo Pag/Rec';
COMMENT ON COLUMN fin_pagrec_class.fin_pagrec_id IS 'ID do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_class.fin_class_id IS 'ID da Classificação ';
COMMENT ON COLUMN fin_pagrec_class.valor IS 'Valor';
COMMENT ON COLUMN fin_pagrec_class.fator_rat IS 'Fator de Rateio';
COMMENT ON COLUMN fin_pagrec_class.perc_rat IS 'Percentual de Rateio';
COMMENT ON COLUMN fin_pagrec_class.fin_pagrec_banco_id IS 'ID da Movimento Bancário de Pag/Rec ';
COMMENT ON COLUMN fin_pagrec_class.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_class.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_class.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_class.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_class.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_class OWNER TO postgres;

CREATE TABLE fin_pagrec_banco_transf (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
data_mov date NOT NULL,
fin_conta_id_origem varchar(36) NOT NULL,
fin_conta_id_destino varchar(36) NOT NULL,
valor numeric(18,2) NOT NULL DEFAULT 0,
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
process_id varchar(36),
data_valid date,
CONSTRAINT pk_fin_pagrec_banco_transf PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_banco_transf IS 'Financeiro-Transferência de Pag/Rec ';
COMMENT ON COLUMN fin_pagrec_banco_transf.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_banco_transf.id IS 'ID da Transferência Bancária de Pag/Rec';
COMMENT ON COLUMN fin_pagrec_banco_transf.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN fin_pagrec_banco_transf.data_mov IS 'Data Movimento';
COMMENT ON COLUMN fin_pagrec_banco_transf.fin_conta_id_origem IS 'ID da Conta Bancária - Origem';
COMMENT ON COLUMN fin_pagrec_banco_transf.fin_conta_id_destino IS 'ID da Conta Bancária - Destino';
COMMENT ON COLUMN fin_pagrec_banco_transf.valor IS 'Valor';
COMMENT ON COLUMN fin_pagrec_banco_transf.observacao IS 'Observação';
COMMENT ON COLUMN fin_pagrec_banco_transf.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_banco_transf.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_banco_transf.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_banco_transf.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_banco_transf.process_id IS 'ID do Processo';
COMMENT ON COLUMN fin_pagrec_banco_transf.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_banco_transf OWNER TO postgres;

CREATE TABLE fin_pagrec_banco (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
data_mov date NOT NULL,
fin_conta_id varchar(36) NOT NULL,
numero_doc_pagrec varchar(50) NOT NULL,
valor numeric(18,2) NOT NULL DEFAULT 0,
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
data_valid date,
CONSTRAINT pk_fin_pagrec_banco PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_banco IS 'Financeiro-Movimento Bancário de Pag/Rec ';
COMMENT ON COLUMN fin_pagrec_banco.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_banco.id IS 'ID da Movimento Bancário de Pag/Rec ';
COMMENT ON COLUMN fin_pagrec_banco.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN fin_pagrec_banco.data_mov IS 'Data Movimento';
COMMENT ON COLUMN fin_pagrec_banco.fin_conta_id IS 'ID da Conta Bancária';
COMMENT ON COLUMN fin_pagrec_banco.numero_doc_pagrec IS 'Numero Documento do Pag/Rec';
COMMENT ON COLUMN fin_pagrec_banco.valor IS 'Valor';
COMMENT ON COLUMN fin_pagrec_banco.observacao IS 'Observação';
COMMENT ON COLUMN fin_pagrec_banco.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_banco.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_banco.log_user_upd IS 'Log - Usuário de Alteração ';
COMMENT ON COLUMN fin_pagrec_banco.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_banco.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_banco OWNER TO postgres;

CREATE TABLE ger_empresa_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_empresa_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_empresa_grupo IS 'Geral-Grupo de Empresa';
COMMENT ON COLUMN ger_empresa_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_empresa_grupo.id IS 'ID do Grupo de Empresa';
COMMENT ON COLUMN ger_empresa_grupo.nome IS 'Nome';
COMMENT ON COLUMN ger_empresa_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ger_empresa_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_empresa_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_empresa_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_empresa_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_empresa_grupo OWNER TO postgres;

CREATE TABLE ger_empresa_pessoa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
tipo varchar(50) NOT NULL,
ger_empresa_id varchar(36) NOT NULL,
observacao varchar(250) NOT NULL,
ger_pessoa_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_empresa_pessoa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_empresa_pessoa IS 'Geral-Pessoas da Empresa';
COMMENT ON COLUMN ger_empresa_pessoa.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_empresa_pessoa.id IS 'ID do Parâmetro da Empresa';
COMMENT ON COLUMN ger_empresa_pessoa.tipo IS 'Tipo: 1-Contador,2-Responsável';
COMMENT ON COLUMN ger_empresa_pessoa.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ger_empresa_pessoa.observacao IS 'Observação';
COMMENT ON COLUMN ger_empresa_pessoa.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN ger_empresa_pessoa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_empresa_pessoa.log_date_ins IS ' Log - Data de Inserção';
COMMENT ON COLUMN ger_empresa_pessoa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_empresa_pessoa.log_date_upd IS ' Log - Data de Alteração';
ALTER TABLE ger_empresa_pessoa OWNER TO postgres;

CREATE TABLE ger_itemserv_pessoa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_itemserv_id varchar(36) NOT NULL,
ger_pessoa_id varchar NOT NULL,
cod_itemserv_ext varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_itemserv_pessoa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_pessoa IS 'Geral-Item/Serviço x Pessoa';
COMMENT ON COLUMN ger_itemserv_pessoa.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_pessoa.id IS 'ID do Item/Serviço x Pessoa';
COMMENT ON COLUMN ger_itemserv_pessoa.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_pessoa.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN ger_itemserv_pessoa.cod_itemserv_ext IS 'Código Externo Item/Serviço da Pessoa';
COMMENT ON COLUMN ger_itemserv_pessoa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_pessoa.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_pessoa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_pessoa.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_itemserv_pessoa OWNER TO postgres;

CREATE TABLE ope_centro2_mapa_coord (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ope_centro2_id_area varchar(36) NOT NULL,
lat_x varchar(100) NOT NULL,
long_y varchar(100) NOT NULL,
ordem int4 NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_centro_mapa_coord PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_mapa_coord IS 'Operação-Dados de Mapa Long = X, Lat = Y';
COMMENT ON COLUMN ope_centro2_mapa_coord.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_mapa_coord.id IS 'ID do Coordenadas do Mapa Centro 2';
COMMENT ON COLUMN ope_centro2_mapa_coord.ope_centro2_id_area IS 'ID do Centro Nível 2 - Area';
COMMENT ON COLUMN ope_centro2_mapa_coord.lat_x IS 'Latitude X';
COMMENT ON COLUMN ope_centro2_mapa_coord.long_y IS 'Longitude Y';
COMMENT ON COLUMN ope_centro2_mapa_coord.ordem IS 'Ordem';
COMMENT ON COLUMN ope_centro2_mapa_coord.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_mapa_coord.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_mapa_coord.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_mapa_coord.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_centro2_mapa_coord OWNER TO postgres;

CREATE TABLE system (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
name varchar(100) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system IS 'System-Sistema';
COMMENT ON COLUMN system.id IS 'ID da Sistema';
COMMENT ON COLUMN system.name IS 'Nome';
COMMENT ON COLUMN system.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system OWNER TO postgres;

CREATE TABLE system_licence (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
tipo_doc varchar(100) NOT NULL,
nome_solicitante varchar(100) NOT NULL,
doc varchar(100) ,
end_logradouro varchar(100),
end_bairro varchar(100),
end_numero varchar(100),
end_cidade varchar(100),
end_uf varchar(100),
end_pais varchar(100),
log_date_ins timestamp(0) NOT NULL DEFAULT now(),
log_user_ins varchar(100),
log_date_upd timestamp(0),
log_user_upd varchar(100),
chamado_id varchar(100) NOT NULL,
status varchar(2) NOT NULL,
status_data timestamp(0) NOT NULL DEFAULT now(),
status_observacao varchar(250) NOT NULL,
system_plan_id varchar(36) NOT NULL,
system_id varchar(36) NOT NULL,
system_user_id varchar(36),
system_version varchar(50),
CONSTRAINT pk_system_licence PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_licence IS 'System-Licenças';
COMMENT ON COLUMN system_licence.id IS 'ID de Licença';
COMMENT ON COLUMN system_licence.tipo_doc IS 'Tipo Documento';
COMMENT ON COLUMN system_licence.nome_solicitante IS 'Nome da Solicitante';
COMMENT ON COLUMN system_licence.doc IS 'Documento';
COMMENT ON COLUMN system_licence.end_logradouro IS 'Endereço - Logradouro';
COMMENT ON COLUMN system_licence.end_bairro IS 'Endereço - Bairro';
COMMENT ON COLUMN system_licence.end_numero IS 'Endereço - Número';
COMMENT ON COLUMN system_licence.end_cidade IS 'Endereço - Cidade';
COMMENT ON COLUMN system_licence.end_uf IS 'Endereço - Unidade Federação';
COMMENT ON COLUMN system_licence.end_pais IS 'Endereço - País';
COMMENT ON COLUMN system_licence.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_licence.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_licence.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_licence.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_licence.chamado_id IS 'ID do Chamado';
COMMENT ON COLUMN system_licence.status IS 'Status: AT-Ativo, PA-Pend. Ativação, PF-Pend. Financeira, IN-Inativa';
COMMENT ON COLUMN system_licence.status_data IS 'Data do Status';
COMMENT ON COLUMN system_licence.status_observacao IS 'Status Observação';
COMMENT ON COLUMN system_licence.system_plan_id IS 'ID do Plano de Utilização do Sistema';
COMMENT ON COLUMN system_licence.system_id IS 'ID do Sistema';
COMMENT ON COLUMN system_licence.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_licence.system_version IS 'Versão do Cliente';
ALTER TABLE system_licence OWNER TO postgres;

CREATE TABLE system_restriction (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
name varchar(100) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_restriction PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_restriction IS 'System-Restrição de Sistema';
COMMENT ON COLUMN system_restriction.id IS 'ID da Restrição do Sistema';
COMMENT ON COLUMN system_restriction.name IS 'Nome';
COMMENT ON COLUMN system_restriction.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_restriction.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_restriction.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_restriction.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_restriction OWNER TO postgres;

CREATE TABLE system_restriction_licence (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
system_restriction_id varchar(36) NOT NULL,
system_licence_id varchar(36) NOT NULL,
value_restriction int4 NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_restriction_licence PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_restriction_licence IS 'System-Restrição do Sistema x Licença';
COMMENT ON COLUMN system_restriction_licence.id IS 'ID da Restrição de Sistema x Licença';
COMMENT ON COLUMN system_restriction_licence.system_restriction_id IS 'ID de Restrição do Sistema';
COMMENT ON COLUMN system_restriction_licence.system_licence_id IS 'ID de Licença';
COMMENT ON COLUMN system_restriction_licence.value_restriction IS 'Valor de Restrição';
COMMENT ON COLUMN system_restriction_licence.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_restriction_licence.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_restriction_licence.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_restriction_licence.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_restriction_licence OWNER TO postgres;

CREATE TABLE system_licence_device (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
system_licence_id varchar(36) NOT NULL,
sigla_device varchar(100) NOT NULL,
log_user_ins varchar(100) NOT NULL,
log_date_ins timestamp(0) NOT NULL DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_licence_device PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_licence_device IS 'System-Dispositivos da Licença';
COMMENT ON COLUMN system_licence_device.id IS 'ID de Dipositivos da Licenças';
COMMENT ON COLUMN system_licence_device.system_licence_id IS 'ID da Licença';
COMMENT ON COLUMN system_licence_device.sigla_device IS 'Identifcador do Dispositivo (Mac,UUid,Etc)';
COMMENT ON COLUMN system_licence_device.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_licence_device.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_licence_device.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_licence_device.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_licence_device OWNER TO postgres;

CREATE TABLE ope_atividade_sistema (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
sigla_atividade_grupo varchar(50),
CONSTRAINT pk_ope_atividade_sistema PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_atividade_sistema IS 'Operação-Sistema da Atividade';
COMMENT ON COLUMN ope_atividade_sistema.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_atividade_sistema.id IS 'ID do Sistema da Atividade';
COMMENT ON COLUMN ope_atividade_sistema.nome IS 'Nome';
COMMENT ON COLUMN ope_atividade_sistema.ativo IS 'Ativo';
COMMENT ON COLUMN ope_atividade_sistema.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_atividade_sistema.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_atividade_sistema.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_atividade_sistema.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_atividade_sistema.sigla_atividade_grupo IS 'Sigla do Sistema da Atividade';
ALTER TABLE ope_atividade_sistema OWNER TO postgres;

CREATE TABLE ope_centro2_area (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ativo varchar(1)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
ope_centro2_id varchar(36) NOT NULL,
ope_periodo_id varchar(36),
ger_umedida_id varchar(36) NOT NULL,
ope_tipo_solo_id varchar(36),
ope_espac_id varchar(36),
ope_atividade_sistema_id_cult varchar(36),
ger_itemserv_id varchar(36) NOT NULL,
ger_itemserv_var_id varchar(36),
ger_itemserv_id_ult varchar(36),
ger_itemserv_var_id_ult varchar(36),
qnt_area_prod numeric(18,6) NOT NULL DEFAULT 0,
qnt_area_improd numeric(18,6) NOT NULL DEFAULT 0,
qnt_plantas_estande numeric(18,6) DEFAULT 0,
bloco_col varchar(100) ,
observacao varchar(250) ,
lat_x varchar(100) ,
long_y varchar(100) ,
alt_z varchar(100) ,
data_ini_plan date,
data_fin_plan date,
data_ult_plan date,
data_ini_col date,
data_fin_col date,
data_ult_col date,
data_emerg date,
data_florada_1 date,
ope_atividade_sistema_id_plan varchar(36),
ope_atividade_sistema_id_col varchar(36),
ope_estagio_id varchar(36),
CONSTRAINT pk_ope_centro2_area PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_area IS 'Operação-Sistema da Atividade';
COMMENT ON COLUMN ope_centro2_area.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_area.id IS 'ID do Centro Nível 2 - Área';
COMMENT ON COLUMN ope_centro2_area.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro2_area.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_area.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_area.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_area.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_area.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_area.ope_periodo_id IS 'ID do Período da Operação';
COMMENT ON COLUMN ope_centro2_area.ger_umedida_id IS 'ID da U.Medida';
COMMENT ON COLUMN ope_centro2_area.ope_tipo_solo_id IS 'ID do Tipo de Solo';
COMMENT ON COLUMN ope_centro2_area.ope_espac_id IS 'ID do Espacamento';
COMMENT ON COLUMN ope_centro2_area.ope_atividade_sistema_id_cult IS 'ID do Sistema da Atividade - Cultivo';
COMMENT ON COLUMN ope_centro2_area.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ope_centro2_area.ger_itemserv_var_id IS 'ID da Variação do Item/Serviço';
COMMENT ON COLUMN ope_centro2_area.ger_itemserv_id_ult IS 'ID do Item/Serviço - Ultimo';
COMMENT ON COLUMN ope_centro2_area.ger_itemserv_var_id_ult IS 'ID da Variação do Item/Serviço - Ultimo';
COMMENT ON COLUMN ope_centro2_area.qnt_area_prod IS 'Quantidade Área - Produtiva';
COMMENT ON COLUMN ope_centro2_area.qnt_area_improd IS 'Quantidade Área - Improdutiva';
COMMENT ON COLUMN ope_centro2_area.qnt_plantas_estande IS 'Quantidade de Plantas Estande';
COMMENT ON COLUMN ope_centro2_area.bloco_col IS 'Bloco de Colheita';
COMMENT ON COLUMN ope_centro2_area.observacao IS 'Observação';
COMMENT ON COLUMN ope_centro2_area.lat_x IS 'Latitude X';
COMMENT ON COLUMN ope_centro2_area.long_y IS 'Longitude Y';
COMMENT ON COLUMN ope_centro2_area.alt_z IS 'Altitude Z';
COMMENT ON COLUMN ope_centro2_area.data_ini_plan IS 'Data Inicial de Plantio';
COMMENT ON COLUMN ope_centro2_area.data_fin_plan IS 'Data Final de Plantio';
COMMENT ON COLUMN ope_centro2_area.data_ult_plan IS 'Ultima Data de Plantio';
COMMENT ON COLUMN ope_centro2_area.data_ini_col IS 'Data Inicial de Colheita';
COMMENT ON COLUMN ope_centro2_area.data_fin_col IS 'Data Final de Colheita';
COMMENT ON COLUMN ope_centro2_area.data_ult_col IS 'Ultima Data de Colheita';
COMMENT ON COLUMN ope_centro2_area.data_emerg IS 'Data de Emergencia';
COMMENT ON COLUMN ope_centro2_area.data_florada_1 IS 'Data de 1 Florada';
COMMENT ON COLUMN ope_centro2_area.ope_atividade_sistema_id_plan IS 'ID do Sistema da Atividade - Plantio';
COMMENT ON COLUMN ope_centro2_area.ope_atividade_sistema_id_col IS 'ID do Sistema da Atividade - Colheita';
COMMENT ON COLUMN ope_centro2_area.ope_estagio_id IS 'ID do Estágio';
ALTER TABLE ope_centro2_area OWNER TO postgres;

CREATE TABLE ope_centro2_mapa_geometria (
unit_id varchar(36) NOT NULL,
ope_centro2_id_area varchar(36) NOT NULL,
geom public.geometry,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
CONSTRAINT pk_ope_centro_mapa_geometria PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_ope_centro2_mapa_geometria_geom ON ope_centro2_mapa_geometria USING gist (geom public.gist_geometry_ops_2d);
CREATE INDEX idx_ope_centro2_mapa_geometria_centro2_id_area ON ope_centro2_mapa_geometria USING btree (ope_centro2_id_area pg_catalog.text_ops ASC NULLS LAST);
COMMENT ON TABLE ope_centro2_mapa_geometria IS 'Operação-Dados de Mapa Geometria';
COMMENT ON COLUMN ope_centro2_mapa_geometria.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_mapa_geometria.ope_centro2_id_area IS 'ID do Centro Nível 2 - Área';
COMMENT ON COLUMN ope_centro2_mapa_geometria.geom IS 'Geometria';
COMMENT ON COLUMN ope_centro2_mapa_geometria.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_mapa_geometria.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_mapa_geometria.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_mapa_geometria.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_mapa_geometria.id IS 'ID da Geometria do Mapa Centro 2';
ALTER TABLE ope_centro2_mapa_geometria OWNER TO postgres;

CREATE TABLE ope_centro2_pessoa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL,
ope_centro2_id varchar(36) NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
ope_frente_trabalho_id varchar(36),
pto_idenf_tipo varchar(1),
pto_idenf varchar(50),
CONSTRAINT pk_ope_centro2_pessoa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_pessoa IS 'Operação-Dados de Pessoa do Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2_pessoa.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_pessoa.id IS 'ID do Centro Nível 2 - Pessoa';
COMMENT ON COLUMN ope_centro2_pessoa.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_pessoa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_pessoa.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_pessoa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_pessoa.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_pessoa.ope_frente_trabalho_id IS 'ID da Frente de Trabalho';
COMMENT ON COLUMN ope_centro2_pessoa.pto_idenf_tipo IS 'Tipo de Identificação do Ponto: 1-Cpf / Senha';
COMMENT ON COLUMN ope_centro2_pessoa.pto_idenf IS 'Identificação do Ponto';
ALTER TABLE ope_centro2_pessoa OWNER TO postgres;

CREATE TABLE ope_ciclo_var (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
sigla_ope_ciclo_var varchar(50),
CONSTRAINT pk_ope_ciclo_var PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ciclo_var IS 'Operação-Ciclo da Variedade';
COMMENT ON COLUMN ope_ciclo_var.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ciclo_var.id IS 'ID do Cliclo da Variedade';
COMMENT ON COLUMN ope_ciclo_var.nome IS 'Nome';
COMMENT ON COLUMN ope_ciclo_var.ativo IS 'Ativo';
COMMENT ON COLUMN ope_ciclo_var.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ciclo_var.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ciclo_var.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ciclo_var.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_ciclo_var.sigla_ope_ciclo_var IS 'Sigla do Cliclo da Variedade';
ALTER TABLE ope_ciclo_var OWNER TO postgres;

CREATE TABLE ope_espac (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
sigla_espac varchar(50),
CONSTRAINT pk_ope_espac PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_espac IS 'Operação-Espaçamento';
COMMENT ON COLUMN ope_espac.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_espac.id IS 'ID do Espacamento';
COMMENT ON COLUMN ope_espac.nome IS 'Nome';
COMMENT ON COLUMN ope_espac.ativo IS 'Ativo';
COMMENT ON COLUMN ope_espac.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_espac.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_espac.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_espac.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_espac.sigla_espac IS 'Sigla do Espacamento';
ALTER TABLE ope_espac OWNER TO postgres;

CREATE TABLE ope_tipo_solo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
sigla_tipo_solo varchar(50),
CONSTRAINT pk_ope_tipo_solo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_tipo_solo IS 'Operação-Tipo de Solo';
COMMENT ON COLUMN ope_tipo_solo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_tipo_solo.id IS 'ID do Tipo de Solo';
COMMENT ON COLUMN ope_tipo_solo.nome IS 'Nome';
COMMENT ON COLUMN ope_tipo_solo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_tipo_solo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_tipo_solo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_tipo_solo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_tipo_solo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_tipo_solo.sigla_tipo_solo IS 'Sigla do Tipo de Solo';
ALTER TABLE ope_tipo_solo OWNER TO postgres;

CREATE TABLE ope_centro2_estoque (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL,
ope_centro2_id varchar(36) NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
tipo varchar(1) ,
CONSTRAINT pk_ope_centro2_estoque PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_estoque IS 'Operação-Dados de Estoque do Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2_estoque.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_estoque.id IS 'ID do Centro Nível 2 - Pessoa';
COMMENT ON COLUMN ope_centro2_estoque.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_estoque.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_estoque.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_estoque.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_estoque.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_estoque.tipo IS 'Tipo: E-Externo, I-Interno';
ALTER TABLE ope_centro2_estoque OWNER TO postgres;

CREATE TABLE bor_mov (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
id_tipo varchar(36)  NOT NULL,
numero_serie varchar(50)  NOT NULL,
ibutton_rfid varchar(50) ,
dthr_track timestamp(0) NOT NULL,
gps_altitude varchar(50) ,
gps_altitude_status varchar(50) ,
gps_lat varchar(50) ,
gps_long varchar(50) ,
gps_angulo_norte varchar(50) ,
gps_posicao_status varchar(50) ,
gps_velocidade varchar(50) ,
gps_velocidade_media varchar(50) ,
equipamento_ignicao varchar(50) ,
equipamento_bateria varchar(50) ,
equipamento_odometro varchar(50) ,
equipamento_rpm varchar(50) ,
equipamento_veloc varchar(50) ,
equipamento_veloc_odom varchar(50) ,
equipamento_veloc_odom_media varchar(50) ,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
geom public.geometry,
ope_centro2_equip_id_1 varchar(36),
ope_centro2_equip_id_2 varchar(36),
ope_centro2_pessoa_id varchar(36),
ger_empresa_id varchar(36),
ope_centro2_area_id varchar(36),
geom_circle geometry,
id_realtime varchar(100) ,
buzzer varchar(4) ,
unit_id varchar(36) NOT NULL,
status varchar(2),
dthr_status timestamp(0),
ope_atividade_id varchar(36),
qnt_ha_trab numeric(18,6) DEFAULT 0,
geom_line geometry,
duracao numeric(18,6),
CONSTRAINT pk_bor_mov PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_bor_mov_01 ON bor_mov USING btree (id_tipo pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
CREATE INDEX idx_bor_mov_02 ON bor_mov USING btree (numero_serie pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
CREATE INDEX idx_bor_mov_03 ON bor_mov USING btree (ibutton_rfid pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
CREATE INDEX idx_bor_mov_04 ON bor_mov USING btree (dthr_track pg_catalog.timestamp_ops ASC NULLS LAST);
CREATE INDEX idx_bor_mov_geom ON bor_mov USING gist (geom public.gist_geometry_ops_2d);
CREATE INDEX idx_bor_mov_geom_circle ON bor_mov USING gist (geom_circle public.gist_geometry_ops_2d);
COMMENT ON TABLE bor_mov IS 'Bordo-Movimento';
COMMENT ON COLUMN bor_mov.id IS 'ID Interno do Movimento';
COMMENT ON COLUMN bor_mov.id_tipo IS 'ID do Tipo da Movimento';
COMMENT ON COLUMN bor_mov.numero_serie IS 'Numero Sério Dispositivo';
COMMENT ON COLUMN bor_mov.ibutton_rfid IS 'Numero IButton ou RFid';
COMMENT ON COLUMN bor_mov.dthr_track IS 'Data/Hora Movimento';
COMMENT ON COLUMN bor_mov.gps_altitude IS 'GPS - Altitude';
COMMENT ON COLUMN bor_mov.gps_altitude_status IS 'GPS - Status da Altitude';
COMMENT ON COLUMN bor_mov.gps_lat IS 'GPS - Latitude X';
COMMENT ON COLUMN bor_mov.gps_long IS 'GPS - Longitude Y';
COMMENT ON COLUMN bor_mov.gps_angulo_norte IS 'GPS - Angulo Norte';
COMMENT ON COLUMN bor_mov.gps_posicao_status IS 'GPS - Status da Posição';
COMMENT ON COLUMN bor_mov.gps_velocidade IS 'GPS - Velocidade';
COMMENT ON COLUMN bor_mov.gps_velocidade_media IS 'GPS - Velocidade Média';
COMMENT ON COLUMN bor_mov.equipamento_ignicao IS 'Equipamento - Ignição';
COMMENT ON COLUMN bor_mov.equipamento_bateria IS 'Equipamento - Bateria';
COMMENT ON COLUMN bor_mov.equipamento_odometro IS 'Equipamento - Odometro';
COMMENT ON COLUMN bor_mov.equipamento_rpm IS 'Equipamento - RPM';
COMMENT ON COLUMN bor_mov.equipamento_veloc IS 'Equipamento - Velocidade';
COMMENT ON COLUMN bor_mov.equipamento_veloc_odom IS 'Equipamento - Velocidade Odometro';
COMMENT ON COLUMN bor_mov.equipamento_veloc_odom_media IS 'Equipamento - Velocidade Média Odometro';
COMMENT ON COLUMN bor_mov.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN bor_mov.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN bor_mov.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN bor_mov.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN bor_mov.geom IS 'Geometria';
COMMENT ON COLUMN bor_mov.ope_centro2_equip_id_1 IS 'ID do Centro Nível 2 - Equipamento 1';
COMMENT ON COLUMN bor_mov.ope_centro2_equip_id_2 IS 'ID do Centro Nível 2 - Equipamento 2';
COMMENT ON COLUMN bor_mov.ope_centro2_pessoa_id IS 'ID do Centro Nível 2 - Pessoa';
COMMENT ON COLUMN bor_mov.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN bor_mov.ope_centro2_area_id IS 'ID do Centro Nível 2 - Area';
COMMENT ON COLUMN bor_mov.geom_circle IS 'Geometria - Criculo Click';
COMMENT ON COLUMN bor_mov.id_realtime IS 'ID RealTime - Redis';
COMMENT ON COLUMN bor_mov.buzzer IS 'Sirene';
COMMENT ON COLUMN bor_mov.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN bor_mov.status IS 'Status OK-Processada com sucesso, NP-Não processada, EP-Em processamento';
COMMENT ON COLUMN bor_mov.dthr_status IS 'Data do status';
COMMENT ON COLUMN bor_mov.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN bor_mov.qnt_ha_trab IS 'Quantidade de hectares trabalhados';
COMMENT ON COLUMN bor_mov.geom_line IS 'Geometria - Line';
COMMENT ON COLUMN bor_mov.duracao IS 'Duração';
ALTER TABLE bor_mov OWNER TO postgres;

CREATE TABLE bor_mov_atual (
ope_centro2_equip_id varchar(36) NOT NULL,
id_tipo varchar(50)  NOT NULL,
numero_serie varchar(50)  NOT NULL,
ibutton_rfid varchar(50) ,
dthr_track timestamp(0) NOT NULL,
gps_altitude varchar(50) ,
gps_altitude_status varchar(50) ,
gps_lat varchar(50) ,
gps_long varchar(50) ,
gps_angulo_norte varchar(50) ,
gps_posicao_status varchar(50) ,
gps_velocidade varchar(50) ,
gps_velocidade_media varchar(50) ,
equipamento_ignicao varchar(50) ,
equipamento_bateria varchar(50) ,
equipamento_odometro varchar(50) ,
equipamento_rpm varchar(50) ,
equipamento_veloc varchar(50) ,
equipamento_veloc_odom varchar(50) ,
equipamento_veloc_odom_media varchar(50) ,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
geom public.geometry,
ope_centro2_pessoa_id varchar(36),
ger_empresa_id varchar(36),
ope_centro2_area_id varchar(36),
id varchar(36) NOT NULL,
unit_id varchar(36),
dthr_ignicao_last_off timestamp(0),
CONSTRAINT pk_bor_mov_atual PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_bor_mov_atual_01 ON bor_mov_atual USING btree (id_tipo pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
CREATE INDEX idx_bor_mov_atual_02 ON bor_mov_atual USING btree (numero_serie pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
CREATE INDEX idx_bor_mov_atual_03 ON bor_mov_atual USING btree (ibutton_rfid pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
CREATE INDEX idx_bor_mov_atual_04 ON bor_mov_atual USING btree (dthr_track pg_catalog.timestamp_ops ASC NULLS LAST);
CREATE INDEX idx_bor_mov_atual_geom ON bor_mov_atual USING gist (geom public.gist_geometry_ops_2d);
COMMENT ON TABLE bor_mov_atual IS 'Bordo-Movimento Atual';
COMMENT ON COLUMN bor_mov_atual.ope_centro2_equip_id IS 'ID do Centro Nível 2 - Equipamento 1';
COMMENT ON COLUMN bor_mov_atual.id_tipo IS 'ID do Tipo da Movimento';
COMMENT ON COLUMN bor_mov_atual.numero_serie IS 'Numero Sério Dispositivo';
COMMENT ON COLUMN bor_mov_atual.ibutton_rfid IS 'Numero IButton ou RFid';
COMMENT ON COLUMN bor_mov_atual.dthr_track IS 'Data/Hora Movimento';
COMMENT ON COLUMN bor_mov_atual.gps_altitude IS 'GPS - Altitude';
COMMENT ON COLUMN bor_mov_atual.gps_altitude_status IS 'GPS - Status da Altitude';
COMMENT ON COLUMN bor_mov_atual.gps_lat IS 'GPS - Latitude X';
COMMENT ON COLUMN bor_mov_atual.gps_long IS 'GPS - Longitude Y';
COMMENT ON COLUMN bor_mov_atual.gps_angulo_norte IS 'GPS - Angulo Norte';
COMMENT ON COLUMN bor_mov_atual.gps_posicao_status IS 'GPS - Status da Posição';
COMMENT ON COLUMN bor_mov_atual.gps_velocidade IS 'GPS - Velocidade';
COMMENT ON COLUMN bor_mov_atual.gps_velocidade_media IS 'GPS - Velocidade Média';
COMMENT ON COLUMN bor_mov_atual.equipamento_ignicao IS 'Equipamento - Ignição';
COMMENT ON COLUMN bor_mov_atual.equipamento_bateria IS 'Equipamento - Bateria';
COMMENT ON COLUMN bor_mov_atual.equipamento_odometro IS 'Equipamento - Odometro';
COMMENT ON COLUMN bor_mov_atual.equipamento_rpm IS 'Equipamento - RPM';
COMMENT ON COLUMN bor_mov_atual.equipamento_veloc IS 'Equipamento - Velocidade';
COMMENT ON COLUMN bor_mov_atual.equipamento_veloc_odom IS 'Equipamento - Velocidade Odometro';
COMMENT ON COLUMN bor_mov_atual.equipamento_veloc_odom_media IS 'Equipamento - Velocidade Média Odometro';
COMMENT ON COLUMN bor_mov_atual.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN bor_mov_atual.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN bor_mov_atual.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN bor_mov_atual.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN bor_mov_atual.geom IS 'Geometria';
COMMENT ON COLUMN bor_mov_atual.ope_centro2_pessoa_id IS 'ID do Centro Nível 2 - Pessoa';
COMMENT ON COLUMN bor_mov_atual.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN bor_mov_atual.ope_centro2_area_id IS 'ID do Centro Nível 2 - Area';
COMMENT ON COLUMN bor_mov_atual.id IS 'ID Interno do Movimento Atual';
COMMENT ON COLUMN bor_mov_atual.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN bor_mov_atual.dthr_ignicao_last_off IS 'Ultima data de desligamento da Ignição';
ALTER TABLE bor_mov_atual OWNER TO postgres;

CREATE TABLE bor_msg (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
id_tipo varchar(50)  NOT NULL,
numero_serie varchar(50)  NOT NULL,
dthr_trans_msg_rast timestamp(0) NOT NULL,
dthr_msg_gerada timestamp(0) NOT NULL,
grupo_msg varchar(30)  NOT NULL,
index_msg varchar(30)  NOT NULL,
dthr_posicao timestamp(0) NOT NULL,
latitude varchar(50)  NOT NULL,
longitude varchar(50)  NOT NULL,
qualidade_posi varchar(10)  NOT NULL,
valor_msg varchar(100)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
status_msg varchar(50)  DEFAULT 'NP'::character varying,
dthr_status timestamp(0),
ger_empresa_id varchar(36),
ope_centro2_equip_id_1 varchar(50) ,
unit_id varchar(36) NOT NULL,
corpo_msg varchar(250),
ope_atividade_id varchar(36),
CONSTRAINT pk_bor_msg PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE bor_msg IS 'Bordo-Mensagens';
COMMENT ON COLUMN bor_msg.id IS 'ID Interno do Movimento';
COMMENT ON COLUMN bor_msg.id_tipo IS 'ID do Tipo da Movimento';
COMMENT ON COLUMN bor_msg.numero_serie IS 'Numero Série Dispositivo';
COMMENT ON COLUMN bor_msg.dthr_trans_msg_rast IS 'Data e Hora Que O Rastreador Trasmitiu a Mensagem ';
COMMENT ON COLUMN bor_msg.dthr_msg_gerada IS 'Data e Hora Que A Mensagem Foi Gerada';
COMMENT ON COLUMN bor_msg.grupo_msg IS 'Grupo Mensagem';
COMMENT ON COLUMN bor_msg.index_msg IS 'Índice do formulário na memória do terminal';
COMMENT ON COLUMN bor_msg.dthr_posicao IS 'Data e Hora da posição';
COMMENT ON COLUMN bor_msg.latitude IS 'Valor da latitude em graus';
COMMENT ON COLUMN bor_msg.longitude IS 'Valor da longitude em graus.';
COMMENT ON COLUMN bor_msg.qualidade_posi IS 'Qualida Da Posição OK-Boa;BAD-Ruim)';
COMMENT ON COLUMN bor_msg.valor_msg IS 'Texto da Msg';
COMMENT ON COLUMN bor_msg.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN bor_msg.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN bor_msg.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN bor_msg.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN bor_msg.status_msg IS 'Status OK-Processada com sucesso, NP-Não processada, EP-Em processamento';
COMMENT ON COLUMN bor_msg.dthr_status IS 'Data  do status ';
COMMENT ON COLUMN bor_msg.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN bor_msg.ope_centro2_equip_id_1 IS 'ID do Centro Nível 2 - Equipamento 1';
COMMENT ON COLUMN bor_msg.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN bor_msg.corpo_msg IS 'Corpo da Mensagem';
COMMENT ON COLUMN bor_msg.ope_atividade_id IS 'ID da Atividade';
ALTER TABLE bor_msg OWNER TO postgres;

CREATE TABLE pto_medidor (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_medidor varchar(50),
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
CONSTRAINT pk_pto_medidor PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE pto_medidor IS 'Ponto-Medidor / Relógio';
COMMENT ON COLUMN pto_medidor.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN pto_medidor.id IS 'ID do Medidor / Relógio';
COMMENT ON COLUMN pto_medidor.nome IS 'Nome';
COMMENT ON COLUMN pto_medidor.ativo IS 'Ativo';
COMMENT ON COLUMN pto_medidor.sigla_medidor IS 'Sigla do Medidor / Relógio';
COMMENT ON COLUMN pto_medidor.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN pto_medidor.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN pto_medidor.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN pto_medidor.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE pto_medidor OWNER TO postgres;

CREATE TABLE pto_marcacao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
pto_medidor_id varchar(36),
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
marc_data timestamp(0),
marc_dia int4,
marc_mes int4,
marc_ano int4,
marc_hora int4,
marc_minuto int4,
process_id varchar(36),
CONSTRAINT pk_pto_marcacao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE pto_marcacao IS 'Ponto-Marcações';
COMMENT ON COLUMN pto_marcacao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN pto_marcacao.id IS 'ID do Medidor / Relógio';
COMMENT ON COLUMN pto_marcacao.pto_medidor_id IS 'ID do Medidor / Relógio';
COMMENT ON COLUMN pto_marcacao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN pto_marcacao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN pto_marcacao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN pto_marcacao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN pto_marcacao.marc_data IS 'Data - Marcação';
COMMENT ON COLUMN pto_marcacao.marc_dia IS 'Dia - Marcação';
COMMENT ON COLUMN pto_marcacao.marc_mes IS 'Mes - Marcação';
COMMENT ON COLUMN pto_marcacao.marc_ano IS 'Ano - Marcação';
COMMENT ON COLUMN pto_marcacao.marc_hora IS 'Hora - Marcação';
COMMENT ON COLUMN pto_marcacao.marc_minuto IS 'Minuto - Marcação';
COMMENT ON COLUMN pto_marcacao.process_id IS 'ID do Processo';
ALTER TABLE pto_marcacao OWNER TO postgres;

CREATE TABLE ope_centro2_ord_status (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_ord_status varchar(50)  NOT NULL,
tipo_status varchar(1)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_centro2_ord_status PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_ord_status IS 'Operação-Status da Ordem';
COMMENT ON COLUMN ope_centro2_ord_status.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_ord_status.id IS 'ID da Ordem - Status';
COMMENT ON COLUMN ope_centro2_ord_status.nome IS 'Nome';
COMMENT ON COLUMN ope_centro2_ord_status.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro2_ord_status.sigla_ord_status IS 'Sigla do Status da Ordem de Operação';
COMMENT ON COLUMN ope_centro2_ord_status.tipo_status IS 'Tipo do Status (L - Liquidada; F - Finalizado; P - Pendente; C - Cancelado, A-Andamento)';
COMMENT ON COLUMN ope_centro2_ord_status.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_ord_status.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_ord_status.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_ord_status.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_centro2_ord_status OWNER TO postgres;

CREATE TABLE ope_centro2_ord (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ger_empresa_id varchar(36) NOT NULL,
ope_periodo_id varchar(36) NOT NULL,
ope_centro2_pessoa_id_solic varchar(36),
data_ini_exec date NOT NULL,
data_fin_exec date NOT NULL,
ope_centro2_ord_status_id varchar(36) NOT NULL,
data_status date NOT NULL,
observacao_interna varchar(250),
observacao_externa varchar(250),
ger_pessoa_endereco_id_exec varchar(36),
ope_centro2_ord_tipo_id varchar(36) NOT NULL,
ope_centro2_id varchar(36) NOT NULL,
ope_frente_trabalho_id varchar(36),
data_ini_exec_prev date,
data_fin_exec_prev date,
ope_centro_versao_id varchar(36),
process_id varchar(36),
numero_ord varchar(50),
data_valid date,
CONSTRAINT pk_ope_centro2_ord PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_ord IS 'Operação-Ordem';
COMMENT ON COLUMN ope_centro2_ord.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_ord.id IS 'ID da Ordem';
COMMENT ON COLUMN ope_centro2_ord.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_ord.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_ord.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_ord.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_ord.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_centro2_ord.ope_periodo_id IS 'ID do Período da Operação';
COMMENT ON COLUMN ope_centro2_ord.ope_centro2_pessoa_id_solic IS 'ID do Centro Nível 2 - Pessoa - Solicitante';
COMMENT ON COLUMN ope_centro2_ord.data_ini_exec IS 'Data Inicial Execução';
COMMENT ON COLUMN ope_centro2_ord.data_fin_exec IS 'Data Final Execução';
COMMENT ON COLUMN ope_centro2_ord.ope_centro2_ord_status_id IS 'ID da Ordem - Status';
COMMENT ON COLUMN ope_centro2_ord.data_status IS 'Data Status';
COMMENT ON COLUMN ope_centro2_ord.observacao_interna IS 'Observacao Interna';
COMMENT ON COLUMN ope_centro2_ord.observacao_externa IS 'Observação Externa';
COMMENT ON COLUMN ope_centro2_ord.ger_pessoa_endereco_id_exec IS 'ID do Endereço da Pessoal - Proprietário / Terceirizado';
COMMENT ON COLUMN ope_centro2_ord.ope_centro2_ord_tipo_id IS 'ID do Tipo da Ordem';
COMMENT ON COLUMN ope_centro2_ord.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_ord.ope_frente_trabalho_id IS 'ID da Frente de Trabalho';
COMMENT ON COLUMN ope_centro2_ord.data_ini_exec_prev IS 'Data Inicial Execução Prevista';
COMMENT ON COLUMN ope_centro2_ord.data_fin_exec_prev IS 'Data Final Execução Prevista';
COMMENT ON COLUMN ope_centro2_ord.ope_centro_versao_id IS 'ID da Versão da Operação';
COMMENT ON COLUMN ope_centro2_ord.process_id IS 'ID do Processo';
COMMENT ON COLUMN ope_centro2_ord.numero_ord IS 'Número Ordem';
COMMENT ON COLUMN ope_centro2_ord.data_valid IS 'Data de Validação';
ALTER TABLE ope_centro2_ord OWNER TO postgres;

CREATE TABLE ope_centro2_ord_dest (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro2_ord_id varchar(36),
ope_centro2_id_dest varchar(36),
ger_umedida_id_dest varchar(36),
qnt_obj numeric(18,6),
qnt_prev_obj numeric(18,6),
valor_unit_prev numeric(18,6),
valor_total_prev numeric(18,6),
observacao_interna varchar(250),
observacao_externa varchar(250),
valor_unit numeric(18,6),
valor_total numeric(18,6),
data_valid date,
CONSTRAINT pk_ope_centro2_ord_dest PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_ord_dest IS 'Operação-Destino da Ordem';
COMMENT ON COLUMN ope_centro2_ord_dest.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_ord_dest.id IS 'ID da Ordem - Destinação';
COMMENT ON COLUMN ope_centro2_ord_dest.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_ord_dest.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_ord_dest.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_ord_dest.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_ord_dest.ope_centro2_ord_id IS 'ID da Ordem de Operação';
COMMENT ON COLUMN ope_centro2_ord_dest.ope_centro2_id_dest IS 'ID do Centro Nível 2 - Objeto';
COMMENT ON COLUMN ope_centro2_ord_dest.ger_umedida_id_dest IS 'ID da U.Medida - Objeto';
COMMENT ON COLUMN ope_centro2_ord_dest.qnt_obj IS 'Quantidade - Real - Objeto - Hec/Hs/Ton/Etc';
COMMENT ON COLUMN ope_centro2_ord_dest.qnt_prev_obj IS 'Quantidade - Prevista - Objeto - Hec/Hs/Ton/Etc';
COMMENT ON COLUMN ope_centro2_ord_dest.valor_unit_prev IS 'Valor Unitário - Previsto';
COMMENT ON COLUMN ope_centro2_ord_dest.valor_total_prev IS 'Valor Total - Previsto';
COMMENT ON COLUMN ope_centro2_ord_dest.observacao_interna IS 'Observação Interna';
COMMENT ON COLUMN ope_centro2_ord_dest.observacao_externa IS 'Observação Externa';
COMMENT ON COLUMN ope_centro2_ord_dest.valor_unit IS 'Valor Unitário - Real';
COMMENT ON COLUMN ope_centro2_ord_dest.valor_total IS 'Valor Total - Real';
COMMENT ON COLUMN ope_centro2_ord_dest.data_valid IS 'Data de Validação';
ALTER TABLE ope_centro2_ord_dest OWNER TO postgres;

CREATE TABLE ope_centro2_ord_ativ (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro2_ord_id varchar(36) NOT NULL,
observacao_interna varchar(250),
observacao_externa varchar(250),
ope_atividade_id varchar(36) NOT NULL,
ordem_exec varchar(3) NOT NULL,
ope_frente_trabalho_id varchar(36),
tipo_executor varchar(1) NOT NULL,
data_valid date,
CONSTRAINT pk_ope_centro2_ord_ativ PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_ord_ativ IS 'Operação-Atividades da Ordem';
COMMENT ON COLUMN ope_centro2_ord_ativ.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_ord_ativ.id IS 'ID da Ordem - Atividades';
COMMENT ON COLUMN ope_centro2_ord_ativ.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_ord_ativ.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_ord_ativ.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_ord_ativ.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_ord_ativ.ope_centro2_ord_id IS 'ID da Ordem de Operação';
COMMENT ON COLUMN ope_centro2_ord_ativ.observacao_interna IS 'Observação Interna';
COMMENT ON COLUMN ope_centro2_ord_ativ.observacao_externa IS 'Observação Externa';
COMMENT ON COLUMN ope_centro2_ord_ativ.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN ope_centro2_ord_ativ.ordem_exec IS 'Ordem Execução';
COMMENT ON COLUMN ope_centro2_ord_ativ.ope_frente_trabalho_id IS 'ID da Frente de Trabalho';
COMMENT ON COLUMN ope_centro2_ord_ativ.tipo_executor IS 'Tipo Executor: P-Próprio / T-Terceiro';
COMMENT ON COLUMN ope_centro2_ord_ativ.data_valid IS 'Data de Validação';
ALTER TABLE ope_centro2_ord_ativ OWNER TO postgres;

CREATE TABLE ope_centro2_ord_itemserv (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
observacao_interna varchar(250),
observacao_externa varchar(250),
ope_centro2_ord_ativ_id varchar(36) NOT NULL,
ger_itemserv_id varchar(36),
qnt_rend numeric(18,6) NOT NULL DEFAULT 0,
perc_util numeric(18,6) NOT NULL DEFAULT 0,
qnt_total_util numeric(18,6) NOT NULL DEFAULT 0,
valor_unit_util numeric(18,6) NOT NULL DEFAULT 0,
valor_total_util numeric(18,6) NOT NULL DEFAULT 0,
ctb_comp_id varchar(36) NOT NULL,
data_valid date,
CONSTRAINT pk_ope_centro2_ord_itemserv PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_ord_itemserv IS 'Operação-Item/Serviço das Atividades da Ordem';
COMMENT ON COLUMN ope_centro2_ord_itemserv.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_ord_itemserv.id IS 'ID da Ordem - Item/Serviço';
COMMENT ON COLUMN ope_centro2_ord_itemserv.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_ord_itemserv.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_ord_itemserv.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_ord_itemserv.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_ord_itemserv.observacao_interna IS 'Observação Interna';
COMMENT ON COLUMN ope_centro2_ord_itemserv.observacao_externa IS 'Observação Externa';
COMMENT ON COLUMN ope_centro2_ord_itemserv.ope_centro2_ord_ativ_id IS 'ID da Atividade da Ordem de Operação';
COMMENT ON COLUMN ope_centro2_ord_itemserv.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ope_centro2_ord_itemserv.qnt_rend IS 'Rendimento / Dosagem';
COMMENT ON COLUMN ope_centro2_ord_itemserv.perc_util IS 'Percentual de utilização';
COMMENT ON COLUMN ope_centro2_ord_itemserv.qnt_total_util IS 'Quantidade total de utilização';
COMMENT ON COLUMN ope_centro2_ord_itemserv.valor_unit_util IS 'Valor unitário de utilização';
COMMENT ON COLUMN ope_centro2_ord_itemserv.valor_total_util IS 'Valor total de utilização';
COMMENT ON COLUMN ope_centro2_ord_itemserv.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ope_centro2_ord_itemserv.data_valid IS 'Data de Validação';
ALTER TABLE ope_centro2_ord_itemserv OWNER TO postgres;

CREATE TABLE ope_centro2_ord_rec (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
observacao_interna varchar(250),
observacao_externa varchar(250),
ope_centro2_ord_ativ_id varchar(36) NOT NULL,
ope_centro1_id varchar(36),
ope_centro2_id varchar(36),
ger_pessoa_endereco_id_exec varchar(36) NOT NULL,
qnt_rend numeric(18,6) NOT NULL DEFAULT 0,
perc_util numeric(18,6) NOT NULL DEFAULT 0,
qnt_total_util numeric(18,6) NOT NULL DEFAULT 0,
valor_unit_util numeric(18,6) NOT NULL DEFAULT 0,
valor_total_util numeric(18,6) NOT NULL DEFAULT 0,
ope_centro1_id_imp01 varchar(36),
ope_centro2_id_imp01 varchar(36),
ctb_comp_id varchar(36) NOT NULL,
ope_compart_id varchar(36),
ctb_comp_id_imp01 varchar(36),
data_valid date,
CONSTRAINT pk_ope_centro2_ord_rec PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_ord_rec IS 'Operação-Recursos das Atividades da Ordem';
COMMENT ON COLUMN ope_centro2_ord_rec.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_ord_rec.id IS 'ID da Ordem - Recursos';
COMMENT ON COLUMN ope_centro2_ord_rec.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_ord_rec.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_ord_rec.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_ord_rec.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_ord_rec.observacao_interna IS 'Observação Interna';
COMMENT ON COLUMN ope_centro2_ord_rec.observacao_externa IS 'Observação Externa';
COMMENT ON COLUMN ope_centro2_ord_rec.ope_centro2_ord_ativ_id IS 'ID da Atividade da Ordem de Operação';
COMMENT ON COLUMN ope_centro2_ord_rec.ope_centro1_id IS 'ID do Centro Nível 1 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_ord_rec.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_ord_rec.ger_pessoa_endereco_id_exec IS 'ID do Endereço da Pessoal - Proprietário / Terceirizado';
COMMENT ON COLUMN ope_centro2_ord_rec.qnt_rend IS 'Rendimento / Dosagem';
COMMENT ON COLUMN ope_centro2_ord_rec.perc_util IS 'Percentual de utilização';
COMMENT ON COLUMN ope_centro2_ord_rec.qnt_total_util IS 'Quantidade total de utilização';
COMMENT ON COLUMN ope_centro2_ord_rec.valor_unit_util IS 'Valor unitário de utilização';
COMMENT ON COLUMN ope_centro2_ord_rec.valor_total_util IS 'Valor total de utilização';
COMMENT ON COLUMN ope_centro2_ord_rec.ope_centro1_id_imp01 IS 'ID do Centro Nível 1 Entrada/Saída - Implemento 01';
COMMENT ON COLUMN ope_centro2_ord_rec.ope_centro2_id_imp01 IS 'ID do Centro Nível 2 Entrada/Saída - Implemento 01';
COMMENT ON COLUMN ope_centro2_ord_rec.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ope_centro2_ord_rec.ope_compart_id IS 'ID do Compartimento';
COMMENT ON COLUMN ope_centro2_ord_rec.ctb_comp_id_imp01 IS 'ID do Componente Contábil - Implemento 01';
COMMENT ON COLUMN ope_centro2_ord_rec.data_valid IS 'Data de Validação';
ALTER TABLE ope_centro2_ord_rec OWNER TO postgres;

CREATE TABLE ind_cnd (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(250),
ativo varchar(1),
tipo varchar(2),
config_cnd text ,
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
CONSTRAINT pk_ind_cnd PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_cnd IS 'Indicador-Conexão de Ind/Rel';
COMMENT ON COLUMN ind_cnd.id IS 'ID da Conexão de Ind/Rel';
COMMENT ON COLUMN ind_cnd.nome IS 'Nome';
COMMENT ON COLUMN ind_cnd.ativo IS 'Ativo';
COMMENT ON COLUMN ind_cnd.tipo IS 'Tipo: S1-SQL postgres - Externo, S2-SQL postrgres - Interno';
COMMENT ON COLUMN ind_cnd.config_cnd IS 'Configuração Conexão (JSON)';
COMMENT ON COLUMN ind_cnd.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_cnd.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_cnd.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_cnd.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_cnd OWNER TO postgres;

CREATE TABLE ind_cjd (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(250),
ativo varchar(1),
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
nome_tecnico varchar(50),
CONSTRAINT pk_ind_cjd PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_cjd IS ' Indicador-Conjuntos de Dados';
COMMENT ON COLUMN ind_cjd.id IS 'ID do Conjunto de Dados Ind/Rel';
COMMENT ON COLUMN ind_cjd.nome IS 'Nome';
COMMENT ON COLUMN ind_cjd.ativo IS 'Ativo';
COMMENT ON COLUMN ind_cjd.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_cjd.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_cjd.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_cjd.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ind_cjd.nome_tecnico IS 'Nome técnico';
ALTER TABLE ind_cjd OWNER TO postgres;

CREATE TABLE ind_rel (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(250),
ativo varchar(1),
nome_tecnico varchar(100),
ind_cjd_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
tipo varchar(1) DEFAULT 'R',
ind_ftd_id varchar(36),
CONSTRAINT pk_ind_rel PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_rel IS 'Indicador-Relatórios';
COMMENT ON COLUMN ind_rel.id IS 'ID do Relatório';
COMMENT ON COLUMN ind_rel.nome IS 'Nome';
COMMENT ON COLUMN ind_rel.ativo IS 'Ativo';
COMMENT ON COLUMN ind_rel.nome_tecnico IS 'Nome Técnico';
COMMENT ON COLUMN ind_rel.ind_cjd_id IS 'ID do Conjunto de Dados Ind/Rel';
COMMENT ON COLUMN ind_rel.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_rel.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_rel.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_rel.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ind_rel.tipo IS 'Tipo: R-Report, D-Dashboard, C-Report Config, L-Lista Simples, F-Fonte de Dados';
COMMENT ON COLUMN ind_rel.ind_ftd_id IS 'ID da Fonte de Dados Ind/Rel';
ALTER TABLE ind_rel OWNER TO postgres;

CREATE TABLE ind_ftd (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(250),
ativo varchar(1),
ind_cnd_id varchar(36),
config_ftd text ,
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
nome_tecnico varchar(50),
CONSTRAINT pk_ind_ftd PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_ftd IS 'Indicador-Fonte de Dados de Ind/Rel';
COMMENT ON COLUMN ind_ftd.id IS 'ID da Fonte de Dados Ind/Rel';
COMMENT ON COLUMN ind_ftd.nome IS 'Nome';
COMMENT ON COLUMN ind_ftd.ativo IS 'Ativo';
COMMENT ON COLUMN ind_ftd.ind_cnd_id IS 'ID da Conexão de Ind/Rel   ';
COMMENT ON COLUMN ind_ftd.config_ftd IS 'Configuração SQL,Etc (JSON)';
COMMENT ON COLUMN ind_ftd.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_ftd.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_ftd.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_ftd.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ind_ftd.nome_tecnico IS 'Nome técnico';
ALTER TABLE ind_ftd OWNER TO postgres;

CREATE TABLE ind_prm (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(250),
ativo varchar(1),
nome_tecnico varchar(100),
tipo_dado varchar(2) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
tipo_entrada varchar(2),
internal varchar(1) DEFAULT 'N',
busca_tabela varchar(50),
busca_campo_nome varchar(50),
busca_campo_id varchar(50),
busca_valores varchar(250),
obrigatorio varchar(1),
valor_padrao text,
visivel varchar(1),
busca_tabela_classe varchar(50),
busca_campo_nome_classe varchar(50),
busca_campo_id_classe varchar(50),
valor_prefixo varchar(250),
valor_sufixo varchar(250),
CONSTRAINT pk_ind_prm PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_prm IS 'Indicador-Parametros de Ind/Rel';
COMMENT ON COLUMN ind_prm.id IS 'ID do Parâmetro Ind/Rel';
COMMENT ON COLUMN ind_prm.nome IS 'Nome';
COMMENT ON COLUMN ind_prm.ativo IS 'Ativo';
COMMENT ON COLUMN ind_prm.nome_tecnico IS 'Nome Técnico';
COMMENT ON COLUMN ind_prm.tipo_dado IS 'Tipo de Dados: TX-Texto, DT-Data, NM-Numero';
COMMENT ON COLUMN ind_prm.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_prm.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_prm.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_prm.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ind_prm.tipo_entrada IS 'Tipo Entrada: IS-Input Simples, CS-Combo Simples, CF-Combo Fonte de Dados, SP-Separador, VL-Variável';
COMMENT ON COLUMN ind_prm.internal IS 'Acesso - Interno';
COMMENT ON COLUMN ind_prm.busca_tabela IS 'Busca - Tabela';
COMMENT ON COLUMN ind_prm.busca_campo_nome IS 'Busca - Campo Nome';
COMMENT ON COLUMN ind_prm.busca_campo_id IS 'Busca - Campo ID';
COMMENT ON COLUMN ind_prm.busca_valores IS 'Busca - Valores';
COMMENT ON COLUMN ind_prm.obrigatorio IS 'Obrigatório: S-Sim, N-Não';
COMMENT ON COLUMN ind_prm.valor_padrao IS 'Valor Padrão';
COMMENT ON COLUMN ind_prm.visivel IS 'Visível: S-Sim, N-Não';
COMMENT ON COLUMN ind_prm.busca_tabela_classe IS 'Busca - Tabela - Classe';
COMMENT ON COLUMN ind_prm.busca_campo_nome_classe IS 'Busca - Campo Nome - Classe';
COMMENT ON COLUMN ind_prm.busca_campo_id_classe IS 'Busca - Campo ID - Classe';
COMMENT ON COLUMN ind_prm.valor_prefixo IS 'Valor Prefixo';
COMMENT ON COLUMN ind_prm.valor_sufixo IS 'Valor Sufixo';
ALTER TABLE ind_prm OWNER TO postgres;

CREATE TABLE ind_cjd_relac_ftd (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ind_cjd_id varchar(36),
ind_ftd_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
CONSTRAINT pk_ind_cjd_relac_ftd PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_cjd_relac_ftd IS 'Indicador-Conjunto de Dados x Fonte de Dados Ind/Rel';
COMMENT ON COLUMN ind_cjd_relac_ftd.id IS 'ID do Conjunto de Dados x Fonte de Dados Ind/Rel';
COMMENT ON COLUMN ind_cjd_relac_ftd.ind_cjd_id IS 'ID do Conjunto de Dados Ind/Rel';
COMMENT ON COLUMN ind_cjd_relac_ftd.ind_ftd_id IS 'ID da Fonte de Dados Ind/Rel';
COMMENT ON COLUMN ind_cjd_relac_ftd.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_cjd_relac_ftd.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_cjd_relac_ftd.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_cjd_relac_ftd.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_cjd_relac_ftd OWNER TO postgres;

CREATE TABLE ind_ftd_relac_prm (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ind_prm_id varchar(36),
ind_ftd_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
CONSTRAINT pk_ind_ftd_relac_prm PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_ftd_relac_prm IS 'Indicador-Fonte de Dados x Parâmetros Ind/Rel';
COMMENT ON COLUMN ind_ftd_relac_prm.id IS 'ID do Fonte de Dados x Parâmetros Ind/Rel';
COMMENT ON COLUMN ind_ftd_relac_prm.ind_prm_id IS 'ID do Parâmetro Ind/Rel';
COMMENT ON COLUMN ind_ftd_relac_prm.ind_ftd_id IS 'ID da Fonte de Dados Ind/Rel';
COMMENT ON COLUMN ind_ftd_relac_prm.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_ftd_relac_prm.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_ftd_relac_prm.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_ftd_relac_prm.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_ftd_relac_prm OWNER TO postgres;

CREATE TABLE ind_pnl (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(250),
tipo varchar(1),
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
icon varchar(50),
CONSTRAINT pk_ind_pnl PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_pnl IS 'Indicador-Painel de Relatórios';
COMMENT ON COLUMN ind_pnl.id IS 'ID do Painel Ind/Rel';
COMMENT ON COLUMN ind_pnl.nome IS 'Nome';
COMMENT ON COLUMN ind_pnl.tipo IS 'Tipo: 1-Painel de Relatórios';
COMMENT ON COLUMN ind_pnl.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_pnl.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_pnl.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_pnl.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ind_pnl.icon IS 'Icone do Painel';
ALTER TABLE ind_pnl OWNER TO postgres;

CREATE TABLE ind_pnl_relac_rel (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ind_pnl_id varchar(36),
ind_rel_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
CONSTRAINT pk_ind_pnl_relac_rel PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_pnl_relac_rel IS 'Indicador-Painel x Relatório Ind/Rel';
COMMENT ON COLUMN ind_pnl_relac_rel.id IS 'ID do Painel x Relatório Ind/Rel';
COMMENT ON COLUMN ind_pnl_relac_rel.ind_pnl_id IS 'ID do Painel Ind/Rel';
COMMENT ON COLUMN ind_pnl_relac_rel.ind_rel_id IS 'ID do Relatório';
COMMENT ON COLUMN ind_pnl_relac_rel.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_pnl_relac_rel.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_pnl_relac_rel.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_pnl_relac_rel.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ind_pnl_relac_rel OWNER TO postgres;

CREATE TABLE system_user_ind_pnl (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
system_user_id varchar(36),
ind_pnl_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_user_ind_pnl PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_system_user_ind_pnl_pnl ON system_user_ind_pnl USING btree (ind_pnl_id pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
CREATE INDEX idx_system_user_ind_pnl_user ON system_user_ind_pnl USING btree (system_user_id pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
COMMENT ON TABLE system_user_ind_pnl IS 'System-Usuário x Relatórios Ind/Rel';
COMMENT ON COLUMN system_user_ind_pnl.id IS 'ID do Grupo x Usuário';
COMMENT ON COLUMN system_user_ind_pnl.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_user_ind_pnl.ind_pnl_id IS 'ID do Painel Ind/Rel';
COMMENT ON COLUMN system_user_ind_pnl.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_user_ind_pnl.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_user_ind_pnl.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_user_ind_pnl.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_user_ind_pnl OWNER TO postgres;

CREATE TABLE system_plan (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
name varchar(100) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
type_plan varchar(2) NOT NULL,
system_id varchar(36) NOT NULL,
description text NOT NULL,
CONSTRAINT pk_system_plan PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_plan IS 'System-Plano de Utilização do Sistema';
COMMENT ON COLUMN system_plan.id IS 'ID do Plano de Utilização do Sistema';
COMMENT ON COLUMN system_plan.name IS 'Nome';
COMMENT ON COLUMN system_plan.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_plan.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_plan.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_plan.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_plan.type_plan IS 'Tipo: FR-Free, TR-Trial, PG-Pago';
COMMENT ON COLUMN system_plan.system_id IS 'ID do Sistema';
COMMENT ON COLUMN system_plan.description IS 'Descrição do Plano';
ALTER TABLE system_plan OWNER TO postgres;

CREATE TABLE system_plan_restriction (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
system_plan_id varchar(36) NOT NULL,
system_restriction_id varchar(36) NOT NULL,
value_restriction int4 NOT NULL DEFAULT 1,
CONSTRAINT pk_system_plan_restriction PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_plan_restriction IS 'System-Plano de Utilização x Restrição';
COMMENT ON COLUMN system_plan_restriction.id IS 'ID do Plano de Utilização x Restrição';
COMMENT ON COLUMN system_plan_restriction.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_plan_restriction.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_plan_restriction.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_plan_restriction.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_plan_restriction.system_plan_id IS 'ID do Plano de Utilização do Sistema';
COMMENT ON COLUMN system_plan_restriction.system_restriction_id IS 'ID da Restrição do Sistema';
COMMENT ON COLUMN system_plan_restriction.value_restriction IS 'Valor da Restrição';
ALTER TABLE system_plan_restriction OWNER TO postgres;

CREATE TABLE fin_pagrec_banco_extrato (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
data_extrato date NOT NULL,
fin_conta_id varchar(36) NOT NULL,
numero_doc varchar(50) NOT NULL,
descricao varchar(250),
valor numeric(18,2) NOT NULL DEFAULT 0,
status varchar(2) NOT NULL DEFAULT 'PD',
status_observacao varchar(250),
process_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_pagrec_banco_extrato PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_banco_extrato IS 'Financeiro-Extrato Mov. Bancario';
COMMENT ON COLUMN fin_pagrec_banco_extrato.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_banco_extrato.id IS 'ID da Extrato Mov. Bancario';
COMMENT ON COLUMN fin_pagrec_banco_extrato.data_extrato IS 'Data do Extrato';
COMMENT ON COLUMN fin_pagrec_banco_extrato.fin_conta_id IS 'ID da Conta';
COMMENT ON COLUMN fin_pagrec_banco_extrato.numero_doc IS 'Numero Documento do Extrato';
COMMENT ON COLUMN fin_pagrec_banco_extrato.descricao IS 'Descrição do Extrato';
COMMENT ON COLUMN fin_pagrec_banco_extrato.valor IS 'Valor do Extrato';
COMMENT ON COLUMN fin_pagrec_banco_extrato.status IS 'Satus: PD-Pendente, EA-Em analise, CD-Consciliado';
COMMENT ON COLUMN fin_pagrec_banco_extrato.status_observacao IS 'Observação do Status';
COMMENT ON COLUMN fin_pagrec_banco_extrato.process_id IS 'ID do Processo';
COMMENT ON COLUMN fin_pagrec_banco_extrato.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_banco_extrato.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_banco_extrato.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_banco_extrato.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_pagrec_banco_extrato OWNER TO postgres;

CREATE TABLE fin_recibo_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
padrao varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_fin_recibo_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_recibo_tipo IS 'Financeiro-Tipo de Recibo';
COMMENT ON COLUMN fin_recibo_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_recibo_tipo.id IS 'ID do Tipo de Recibo';
COMMENT ON COLUMN fin_recibo_tipo.nome IS 'Nome';
COMMENT ON COLUMN fin_recibo_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN fin_recibo_tipo.padrao IS 'Padrão';
COMMENT ON COLUMN fin_recibo_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_recibo_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_recibo_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_recibo_tipo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE fin_recibo_tipo OWNER TO postgres;

CREATE TABLE fin_recibo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
data_recibo date,
conteudo text NOT NULL,
valor numeric(18,2) NOT NULL,
ger_pessoa_endereco_id varchar(36),
nome_pessoa varchar(100),
nr_doc_pessoa varchar(50),
tipo_doc_pessoa varchar(50),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
status varchar(2) NOT NULL,
status_observacao varchar(250),
CONSTRAINT pk_fin_recibo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_recibo IS 'Financeiro-Recibo';
COMMENT ON COLUMN fin_recibo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_recibo.id IS 'ID do Recibo';
COMMENT ON COLUMN fin_recibo.data_recibo IS 'Data do Recibo';
COMMENT ON COLUMN fin_recibo.conteudo IS 'Conteudo do Recido';
COMMENT ON COLUMN fin_recibo.valor IS 'Valor';
COMMENT ON COLUMN fin_recibo.ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa';
COMMENT ON COLUMN fin_recibo.nome_pessoa IS 'Nome - Pessoa';
COMMENT ON COLUMN fin_recibo.nr_doc_pessoa IS 'Número do Documento - Pessoa';
COMMENT ON COLUMN fin_recibo.tipo_doc_pessoa IS 'Tipo do Documento - Pessoa';
COMMENT ON COLUMN fin_recibo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_recibo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_recibo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_recibo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_recibo.status IS 'Status: PD-Pendente, AS-Assinado, EA-Enviado para Assinatura';
COMMENT ON COLUMN fin_recibo.status_observacao IS 'Observação do Status';
ALTER TABLE fin_recibo OWNER TO postgres;

CREATE TABLE ger_itemserv_local (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_itemserv_id varchar(36) NOT NULL,
desc_local1 varchar(50) NOT NULL,
desc_local2 varchar(100),
desc_local3 varchar(100),
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_itemserv_localizacao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_local IS 'Geral-Item/Serviço x Localização';
COMMENT ON COLUMN ger_itemserv_local.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_local.id IS 'ID do Item/Serviço x Localização';
COMMENT ON COLUMN ger_itemserv_local.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_local.desc_local1 IS 'Local 1';
COMMENT ON COLUMN ger_itemserv_local.desc_local2 IS 'Local 2';
COMMENT ON COLUMN ger_itemserv_local.desc_local3 IS 'Local 3';
COMMENT ON COLUMN ger_itemserv_local.observacao IS 'Observação';
COMMENT ON COLUMN ger_itemserv_local.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_local.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_local.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_local.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_itemserv_local OWNER TO postgres;

CREATE TABLE ger_est_nivel (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
observacao varchar(250),
bloq_mov_solic varchar(1) DEFAULT 'N',
bloq_mov_pedido varchar(1) DEFAULT 'N',
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_est_nivel PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_est_nivel IS 'Geral-Nivel de Estoque';
COMMENT ON COLUMN ger_est_nivel.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_est_nivel.id IS 'ID do Nivel de Estoque';
COMMENT ON COLUMN ger_est_nivel.nome IS 'Nome';
COMMENT ON COLUMN ger_est_nivel.ativo IS 'Ativo';
COMMENT ON COLUMN ger_est_nivel.observacao IS 'Observação';
COMMENT ON COLUMN ger_est_nivel.bloq_mov_solic IS 'Bloqueia Movimento de Solicitação';
COMMENT ON COLUMN ger_est_nivel.bloq_mov_pedido IS 'Bloqueia Movimento de Pedido';
COMMENT ON COLUMN ger_est_nivel.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_est_nivel.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_est_nivel.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_est_nivel.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_est_nivel OWNER TO postgres;

CREATE TABLE mov_est_nivel (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_itemserv_id varchar(36) NOT NULL,
ger_est_nivel_id varchar(36) NOT NULL,
qnt_min numeric(18,6) NOT NULL,
qnt_max numeric(18,6) NOT NULL,
qnt_nesc numeric(18,6) NOT NULL,
observacao varchar(250) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_mov_est_nivel PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_est_nivel IS 'Movimentação-Nivel de Estoque do Item/Serviço';
COMMENT ON COLUMN mov_est_nivel.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_est_nivel.id IS 'ID do Nivel de Estoque do Item/Serviço';
COMMENT ON COLUMN mov_est_nivel.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN mov_est_nivel.ger_est_nivel_id IS 'ID do Nivel de Estoque';
COMMENT ON COLUMN mov_est_nivel.qnt_min IS 'Quantidade Minima';
COMMENT ON COLUMN mov_est_nivel.qnt_max IS 'Quantidade Maxima';
COMMENT ON COLUMN mov_est_nivel.qnt_nesc IS 'Quantidade Necessária';
COMMENT ON COLUMN mov_est_nivel.observacao IS 'Observação';
COMMENT ON COLUMN mov_est_nivel.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_est_nivel.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_est_nivel.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_est_nivel.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE mov_est_nivel OWNER TO postgres;

CREATE TABLE ger_itemserv_compos (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_itemserv_compos_tipo_id varchar(36) NOT NULL,
ger_itemserv_id_de varchar(36) NOT NULL,
ger_itemserv_id_para varchar(36) NOT NULL,
fator_mult numeric(18,6) NOT NULL DEFAULT 0,
qnt_compos numeric(18,6) NOT NULL DEFAULT 0,
ativo varchar(1) NOT NULL,
observacao varchar(250),
ordem varchar(50) NOT NULL,
qnt_altura numeric(18,6) DEFAULT 0,
qnt_largura numeric(18,6),
qnt_comprimento numeric(18,6),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_itemserv_compos PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_compos IS 'Geral-Item/Serviço x Composição';
COMMENT ON COLUMN ger_itemserv_compos.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ger_itemserv_compos.id IS 'ID do Item/Serviço x Composição';
COMMENT ON COLUMN ger_itemserv_compos.ger_itemserv_compos_tipo_id IS 'ID do Tipo de Composição do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_compos.ger_itemserv_id_de IS 'ID do Item/Serviço - De';
COMMENT ON COLUMN ger_itemserv_compos.ger_itemserv_id_para IS 'ID do Item/Serviço - Para';
COMMENT ON COLUMN ger_itemserv_compos.fator_mult IS 'Fator Multiplacao';
COMMENT ON COLUMN ger_itemserv_compos.qnt_compos IS 'Quantidade de Composicao';
COMMENT ON COLUMN ger_itemserv_compos.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv_compos.observacao IS 'Observação';
COMMENT ON COLUMN ger_itemserv_compos.ordem IS 'Ordem';
COMMENT ON COLUMN ger_itemserv_compos.qnt_altura IS 'Quantidade - Altura';
COMMENT ON COLUMN ger_itemserv_compos.qnt_largura IS 'Quantidade - Largura';
COMMENT ON COLUMN ger_itemserv_compos.qnt_comprimento IS 'Quantidade - Cumprimento';
COMMENT ON COLUMN ger_itemserv_compos.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_compos.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_compos.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_compos.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_itemserv_compos OWNER TO postgres;

CREATE TABLE ger_itemserv_compos_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_itemserv_compos_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_itemserv_compos_tipo IS 'Geral-Tipo de Composição do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_compos_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_itemserv_compos_tipo.id IS 'ID do Tipo de Composição do Item/Serviço';
COMMENT ON COLUMN ger_itemserv_compos_tipo.nome IS 'Nome';
COMMENT ON COLUMN ger_itemserv_compos_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN ger_itemserv_compos_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_itemserv_compos_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_itemserv_compos_tipo.log_user_upd IS ' Log - Usuário de Alteração';
COMMENT ON COLUMN ger_itemserv_compos_tipo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ger_itemserv_compos_tipo OWNER TO postgres;

CREATE TABLE ger_processo_bloq (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
tipo_processo varchar(50) NOT NULL,
ger_empresa_id varchar(36) NOT NULL,
data_lib_inicial date,
data_lib_final date,
observacao varchar(250) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_processo_bloq PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_processo_bloq IS 'Geral-Bloqueio de Processo por Data';
COMMENT ON COLUMN ger_processo_bloq.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_processo_bloq.id IS 'ID do Bloqueio de Processo';
COMMENT ON COLUMN ger_processo_bloq.tipo_processo IS 'Tipo de Processo';
COMMENT ON COLUMN ger_processo_bloq.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ger_processo_bloq.data_lib_inicial IS 'Data liberada - Inicial';
COMMENT ON COLUMN ger_processo_bloq.data_lib_final IS 'Data liberada - Final';
COMMENT ON COLUMN ger_processo_bloq.observacao IS 'Observação';
COMMENT ON COLUMN ger_processo_bloq.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_processo_bloq.log_date_ins IS ' Log - Data de Inserção';
COMMENT ON COLUMN ger_processo_bloq.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_processo_bloq.log_date_upd IS ' Log - Data de Alteração';
ALTER TABLE ger_processo_bloq OWNER TO postgres;

CREATE TABLE ope_centro_dest (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL,
ope_centro1_id_dest_pri varchar(36) NOT NULL,
ope_centro2_id_dest_pri varchar(36),
ope_centro1_id_dest_sec varchar(36),
ope_centro2_id_dest_sec varchar(36),
valor numeric(18,2) NOT NULL DEFAULT 0,
qnt numeric(18,6) NOT NULL,
ope_atividade_id varchar(36),
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
mov_itemserv_id varchar(36),
fin_pagrec_id varchar(36),
fin_pagrec_banco_id varchar(36),
ope_centro1_id varchar(36),
ope_centro2_id varchar(36),
tipo_es varchar(1) NOT NULL,
ope_periodo_id_desc_pri varchar(36),
ope_periodo_id_desc_sec varchar(36),
ope_compart_id_pri varchar(36),
ope_compart_id_sec varchar(36),
CONSTRAINT pk_ope_centro_dest PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_dest IS 'Operação-Destinação de Valores/Quantidade';
COMMENT ON COLUMN ope_centro_dest.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_dest.id IS 'ID da Destinação de Valores/Quantidade';
COMMENT ON COLUMN ope_centro_dest.ope_centro1_id_dest_pri IS 'ID do Centro Nível 1 Entrada/Saída - Destino Primário';
COMMENT ON COLUMN ope_centro_dest.ope_centro2_id_dest_pri IS 'ID do Centro Nível 2 Entrada/Saída - Destino Primário';
COMMENT ON COLUMN ope_centro_dest.ope_centro1_id_dest_sec IS 'ID do Centro Nível 1 Entrada/Saída - Destino Secundário';
COMMENT ON COLUMN ope_centro_dest.ope_centro2_id_dest_sec IS 'ID do Centro Nível 2 Entrada/Saída - Destino Secundário';
COMMENT ON COLUMN ope_centro_dest.valor IS 'Valor';
COMMENT ON COLUMN ope_centro_dest.qnt IS 'Quantidade';
COMMENT ON COLUMN ope_centro_dest.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN ope_centro_dest.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_dest.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_dest.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_dest.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_dest.mov_itemserv_id IS 'ID do Movimento de Item/Serviço - Origem';
COMMENT ON COLUMN ope_centro_dest.fin_pagrec_id IS 'ID do Pag/Rec - Origem';
COMMENT ON COLUMN ope_centro_dest.fin_pagrec_banco_id IS 'ID da Movimento Bancário de Pag/Rec - Origem';
COMMENT ON COLUMN ope_centro_dest.ope_centro1_id IS 'ID do Centro Nível 1 Entrada/Saída - Origem';
COMMENT ON COLUMN ope_centro_dest.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída - Origem';
COMMENT ON COLUMN ope_centro_dest.tipo_es IS 'Tipo: E-Entrada, S-Saída';
COMMENT ON COLUMN ope_centro_dest.ope_periodo_id_desc_pri IS 'ID do Período da Operação - Destino Primário';
COMMENT ON COLUMN ope_centro_dest.ope_periodo_id_desc_sec IS 'ID do Período da Operação - Destino Secundário';
COMMENT ON COLUMN ope_centro_dest.ope_compart_id_pri IS 'ID do Compartimento - Primário';
COMMENT ON COLUMN ope_centro_dest.ope_compart_id_sec IS 'ID do Compartimento - Secundário';
ALTER TABLE ope_centro_dest OWNER TO postgres;

CREATE TABLE ger_processo_bloq_user (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_processo_bloq_id varchar(36) NOT NULL,
system_user_id varchar(36),
tipo_bloq varchar(255),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ger_processo_bloq_user PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_processo_bloq_user IS 'Geral-Bloqueio de Processo por Data - Usuário';
COMMENT ON COLUMN ger_processo_bloq_user.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_processo_bloq_user.id IS 'ID do Parâmetro da Empresa';
COMMENT ON COLUMN ger_processo_bloq_user.ger_processo_bloq_id IS 'ID do Bloqueio de Processo';
COMMENT ON COLUMN ger_processo_bloq_user.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN ger_processo_bloq_user.tipo_bloq IS 'Tipo: E-Excluir do Bloqueio, I-Incluir no Bloqueio';
COMMENT ON COLUMN ger_processo_bloq_user.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_processo_bloq_user.log_date_ins IS ' Log - Data de Inserção';
COMMENT ON COLUMN ger_processo_bloq_user.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_processo_bloq_user.log_date_upd IS ' Log - Data de Alteração';
ALTER TABLE ger_processo_bloq_user OWNER TO postgres;

CREATE TABLE fin_pagrec_baixa_var (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
fin_pagrec_baixa_id varchar(36) NOT NULL,
fin_tipo_variacao_id varchar(36) NOT NULL,
valor numeric(18,2) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
observacao varchar(250),
data_valid date,
CONSTRAINT pk_fin_pagrec_baixa_var PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_baixa_var IS 'Financeiro-Variação da Baixa';
COMMENT ON COLUMN fin_pagrec_baixa_var.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_baixa_var.id IS 'ID da Variação da Parcela';
COMMENT ON COLUMN fin_pagrec_baixa_var.fin_pagrec_baixa_id IS 'ID da Baixa de Pag/Rec';
COMMENT ON COLUMN fin_pagrec_baixa_var.fin_tipo_variacao_id IS 'ID do Tipo de Variação';
COMMENT ON COLUMN fin_pagrec_baixa_var.valor IS 'Valor';
COMMENT ON COLUMN fin_pagrec_baixa_var.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_baixa_var.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_baixa_var.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_baixa_var.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_baixa_var.observacao IS 'Observação';
COMMENT ON COLUMN fin_pagrec_baixa_var.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_baixa_var OWNER TO postgres;

CREATE TABLE ope_centro2_ord_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_ord_tipo varchar(50)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
valida_saldo_area_aberta varchar(1) DEFAULT 'S',
valida_prev_itemserv varchar(1) DEFAULT 'S',
valida_prev_rec varchar(1) DEFAULT 'S',
valida_regra_config varchar(1) DEFAULT 'S',
valida_tipo_executor varchar(2) DEFAULT 'S',
valida_rec_equip varchar(1) DEFAULT 'S',
valida_rec_pessoa varchar(1) DEFAULT 'S',
valida_itemserv_i varchar(1) DEFAULT 'S',
valida_itemserv_s varchar(1) DEFAULT 'S',
valida_tipo_prop_rec_equip varchar(2) DEFAULT 'S',
valida_tipo_prop_rec_pessoa varchar(2) DEFAULT 'S',
CONSTRAINT pk_ope_centro2_ord_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_ord_tipo IS 'Operação-Tipo da Ordem';
COMMENT ON COLUMN ope_centro2_ord_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_ord_tipo.id IS 'ID do Tipo da Ordem';
COMMENT ON COLUMN ope_centro2_ord_tipo.nome IS 'Nome';
COMMENT ON COLUMN ope_centro2_ord_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro2_ord_tipo.sigla_ord_tipo IS 'Sigla do Tipo da Ordem';
COMMENT ON COLUMN ope_centro2_ord_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_ord_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_ord_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_ord_tipo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_saldo_area_aberta IS 'Valida saldo Área em aberto: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_prev_itemserv IS 'Valida previsão Item/Serviço: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_prev_rec IS 'Valida previsão Recurso: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_regra_config IS 'Valida regra configurável: S-Sim, N-Não, A-Aviso';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_tipo_executor IS 'Valida tipo executor: SP-Sim-Próprio, ST-Sim-Terceiro, N-Não, AP-Aviso-Próprio, AT-Aviso-Terceiro';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_rec_equip IS 'Valida Recurso - Equipamento: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_rec_pessoa IS 'Obriga Recurso - Pessoa: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_itemserv_i IS 'Obriga Item: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_itemserv_s IS 'Obriga Serviço: S-Sim, N-Não, A-Aviso, B-Bloqueia';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_tipo_prop_rec_equip IS 'Valida tipo prop. Recurso - Equipamento: SP-Sim-Próprio, ST-Sim-Terceiro, N-Não, AP-Aviso-Próprio, AT-Aviso-Terceiro';
COMMENT ON COLUMN ope_centro2_ord_tipo.valida_tipo_prop_rec_pessoa IS 'Valida tipo prop. Recurso - Pessoa: SP-Sim-Próprio, ST-Sim-Terceiro, N-Não, AP-Aviso-Próprio, AT-Aviso-Terceiro';
ALTER TABLE ope_centro2_ord_tipo OWNER TO postgres;

CREATE TABLE ope_ocor_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_ocor_tipo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo varchar(1) NOT NULL,
obrig_ope_compart varchar(1) NOT NULL,
CONSTRAINT pk_ope_ocor_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_tipo IS 'Operação-Tipo de Ocorrência';
COMMENT ON COLUMN ope_ocor_tipo.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ope_ocor_tipo.id IS 'ID do Tipo de Ocorrência';
COMMENT ON COLUMN ope_ocor_tipo.nome IS 'Nome';
COMMENT ON COLUMN ope_ocor_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_ocor_tipo.sigla_ocor_tipo IS 'Sigla de Tipo de Ocorrência';
COMMENT ON COLUMN ope_ocor_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_tipo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_ocor_tipo.tipo IS 'Tipo: A-Área, E-Equipamento';
COMMENT ON COLUMN ope_ocor_tipo.obrig_ope_compart IS 'Obriga Compartimento: N-Não, S-Sim, O-Opcional';
ALTER TABLE ope_ocor_tipo OWNER TO postgres;

CREATE TABLE ind_rel_relac_prm (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ind_prm_id varchar(36) NOT NULL,
ind_rel_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
ordem_exib int4 NOT NULL,
valor_padrao json,
CONSTRAINT pk_ind_rel_relac_prm PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_rel_relac_prm IS 'Indicador-Relatório x Parâmetros Ind/Rel';
COMMENT ON COLUMN ind_rel_relac_prm.id IS 'ID do Fonte de Dados x Parâmetros Ind/Rel';
COMMENT ON COLUMN ind_rel_relac_prm.ind_prm_id IS 'ID do Parâmetro Ind/Rel';
COMMENT ON COLUMN ind_rel_relac_prm.ind_rel_id IS 'ID do Relatório';
COMMENT ON COLUMN ind_rel_relac_prm.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_rel_relac_prm.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_rel_relac_prm.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_rel_relac_prm.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ind_rel_relac_prm.ordem_exib IS 'Ordem Exibição';
COMMENT ON COLUMN ind_rel_relac_prm.valor_padrao IS 'Valor Padrão';
ALTER TABLE ind_rel_relac_prm OWNER TO postgres;

CREATE TABLE ind_rel_var (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ind_rel_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp,
var_nome_tecnico varchar(50) NOT NULL,
var_nome_descritivo varchar(50) NOT NULL,
var_agrupavel varchar(1) NOT NULL,
ordem_padrao int4 NOT NULL DEFAULT 0,
largura numeric(18,2),
visivel varchar(1),
var_nome_tecnico_prefixo varchar(50),
CONSTRAINT pk_ind_rel_var PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ind_rel_var IS 'Indicador-Relatório x Variáveis';
COMMENT ON COLUMN ind_rel_var.id IS 'ID do Fonte de Dados x Parâmetros Ind/Rel';
COMMENT ON COLUMN ind_rel_var.ind_rel_id IS 'ID do Relatório';
COMMENT ON COLUMN ind_rel_var.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ind_rel_var.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ind_rel_var.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ind_rel_var.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ind_rel_var.var_nome_tecnico IS 'Nome da Variável - Técnico';
COMMENT ON COLUMN ind_rel_var.var_nome_descritivo IS 'Nome da Variável - Descritivo';
COMMENT ON COLUMN ind_rel_var.var_agrupavel IS 'Agrupável';
COMMENT ON COLUMN ind_rel_var.ordem_padrao IS 'Ordem Padrão';
COMMENT ON COLUMN ind_rel_var.largura IS 'Largura';
COMMENT ON COLUMN ind_rel_var.visivel IS 'Visível: S-Sim,N-Não';
COMMENT ON COLUMN ind_rel_var.var_nome_tecnico_prefixo IS 'Prefixo do Nome Técnico';
ALTER TABLE ind_rel_var OWNER TO postgres;

CREATE TABLE ope_centro2_param_per (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL,
dt_valid_ini date NOT NULL DEFAULT now(),
ope_centro2_id varchar(36) NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
ger_empresa_id varchar(36),
ope_frente_trabalho_id varchar(36),
CONSTRAINT pk_ope_centro2_param_per PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro2_param_per IS 'Operação-Parâmetros por Período do Centro Nível 2 de Entrada/Saída';
COMMENT ON COLUMN ope_centro2_param_per.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro2_param_per.id IS 'ID do Centro Nível 2 - Parametros por Período';
COMMENT ON COLUMN ope_centro2_param_per.dt_valid_ini IS 'Data validade inicial';
COMMENT ON COLUMN ope_centro2_param_per.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro2_param_per.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro2_param_per.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro2_param_per.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro2_param_per.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro2_param_per.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_centro2_param_per.ope_frente_trabalho_id IS 'ID da Frente de Trabalho';
ALTER TABLE ope_centro2_param_per OWNER TO postgres;

CREATE TABLE bor_tel (
id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
id_tipo varchar(50)  NOT NULL,
numero_serie varchar(50)  NOT NULL,
dthr_msg varchar(50) ,
dthr_fim varchar(50) ,
dthr_inicio varchar(50) ,
acel_viagem_m_s2 varchar(50) ,
freadas_bruscas_acum varchar(50) ,
freadas_bruscas_viagem varchar(50) ,
gps_qual_acel_max_viagem varchar(50) ,
gps_qual_desacel_max_viagem varchar(50) ,
gps_qual_rot_motor_max_viagem varchar(50) ,
gps_qual_vel_max_viagem_tac varchar(50) ,
id_ibutton varchar(50) ,
lat_acel_max_viagem varchar(50) ,
lat_desacel_max_viagem varchar(50) ,
lat_max_tempo_marcha_lenta_viagem varchar(50) ,
lat_rot_motor_max_viagem varchar(50) ,
lat_vel_max_banguela varchar(50) ,
lat_vel_max_viagem_gps varchar(50) ,
lat_vel_max_viagem_tac varchar(50) ,
long_acel_max_viagem varchar(50) ,
long_desacel_max_viagem varchar(50) ,
long_max_tempo_marcha_lenta_viagem varchar(50) ,
long_rot_motor_max_viagem varchar(50) ,
long_vel_max_banguela varchar(50) ,
long_vel_max_viagem_gps varchar(50) ,
long_vel_max_viagem_tac varchar(50) ,
maior_tempo_banguela_viagem varchar(50) ,
maior_vel_banguela varchar(50) ,
media_acel_brusca_m_s2_acum varchar(50) ,
media_acel_brusca_viage_m_s2 varchar(50) ,
media_freadas_m_s2_acum varchar(50) ,
media_freadas_viagem_m_s2 varchar(50) ,
nm_marcha_lenta_acum varchar(50) ,
nm_marcha_lenta_viagem varchar(50) ,
num_arranc_bruscas_acum varchar(50) ,
num_arranc_bruscas_viagem varchar(50) ,
num_banguela_acum varchar(50) ,
num_banguela_viagem varchar(50) ,
num_freio_motor_acum varchar(50) ,
num_rpm_acima_acum varchar(50) ,
num_rpm_acima_parcial varchar(50) ,
num_vezes_banguela_viagem varchar(50) ,
num_vezes_vel_acima_acum varchar(50) ,
num_vezes_vel_acima_parcial varchar(50) ,
odo_acum_gps_dec_km varchar(50) ,
odo_acum_tac_dec_km varchar(50) ,
odo_viagem_gps_dec_km varchar(50) ,
odo_viagem_tac_dec_km varchar(50) ,
rot_motor_max_viagem varchar(50) ,
rot_motor_med_viagem varchar(50) ,
tensao_batt_bkp_med_dec_volts varchar(50) ,
tensao_batt_veic_med_dec_volts varchar(50) ,
dthr_acel_max_viagem varchar(50) ,
dthr_desacel_max_viagem varchar(50) ,
dthr_max_tempo_marcha_lenta_viagem varchar(50) ,
dthr_rot_motor_max_viagem varchar(50) ,
dthr_vel_max_banguela varchar(50) ,
dthr_vel_max_viagem_gps varchar(50) ,
dthr_vel_max_viagem_tac varchar(50) ,
tempo_faixa_amarela_acum varchar(50) ,
tempo_faixa_amarela_parcial varchar(50) ,
tempo_faixa_azul_acum varchar(50) ,
tempo_faixa_azul_parcial varchar(50) ,
tempo_faixa_verde_acum varchar(50) ,
tempo_faixa_verde_parcial varchar(50) ,
tempo_faixa_vermelha_acum varchar(50) ,
tempo_faixa_vermelha_parcial varchar(50) ,
tempo_freio_motor_acum varchar(50) ,
tempo_marcha_lenta_acum varchar(50) ,
tempo_marcha_lenta_viagem varchar(50) ,
tempo_max_marcha_lenta_viagem varchar(50) ,
tempo_medio_marcha_lenta_viagem varchar(50) ,
tempo_pedal_freio_acionado_viagem varchar(50) ,
tempo_perm_bang_acum_secs varchar(50) ,
tempo_perm_bang_viagem_secs varchar(50) ,
tempo_rpm_acima_acum varchar(50) ,
tempo_rpm_acima_parcial varchar(50) ,
tempo_uso_acum_em_movimento_secs varchar(50)  NOT NULL,
tempo_uso_acum_parado_secs varchar(50) ,
tempo_uso_acum_total_secs varchar(50) ,
tempo_uso_viagem_em_movto_secs varchar(50) ,
tempo_uso_viagem_parado_secs varchar(50) ,
tempo_uso_viagem_total_secs varchar(50) ,
tempo_veic_deslig_acum_secs varchar(50) ,
tempo_veic_desl_entre_viagens_secs varchar(50) ,
tempo_vel_acima_acum varchar(50) ,
tempo_vel_acima_parcial varchar(50) ,
vel_final_frenagem_brusca varchar(50) ,
vel_final_max_acel_brusca varchar(50) ,
vel_inicial_frenagem_brusca varchar(50) ,
vel_inicial_max_acel_brusca varchar(50) ,
vel_max_viagem_gps varchar(50) ,
vel_max_viagem_tac varchar(50) ,
vel_media_gps_acum varchar(50) ,
vel_media_tac_acum varchar(50) ,
vel_med_viagem_gps varchar(50) ,
vel_med_viagem_tac varchar(50) ,
id_reatime varchar(100) ,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
status_msg varchar(50) ,
dthr_status timestamp(0),
ger_empresa_id varchar(36) ,
ope_centro2_pessoa_id varchar(36) ,
ope_centro2_equip_id_1 varchar(50) ,
unit_id varchar(36)  NOT NULL,
CONSTRAINT pk_bor_tel PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE bor_tel IS 'Bordo-Telemetria';
COMMENT ON COLUMN bor_tel.id IS 'ID Interno do Movimento';
COMMENT ON COLUMN bor_tel.id_tipo IS 'ID do Tipo da Movimento';
COMMENT ON COLUMN bor_tel.numero_serie IS 'Numero Serie Dispositivo';
COMMENT ON COLUMN bor_tel.dthr_msg IS 'Data e Hora de geração da mensagem pelo rastreador';
COMMENT ON COLUMN bor_tel.dthr_fim IS 'Data Final de Trabalho';
COMMENT ON COLUMN bor_tel.dthr_inicio IS 'Data Inicio de Trabalho';
COMMENT ON COLUMN bor_tel.acel_viagem_m_s2 IS 'Aceleração da Viagem Em Metro Por Segundo Ao Quadrado';
COMMENT ON COLUMN bor_tel.freadas_bruscas_acum IS 'Freadas Bruscas Acumuladas';
COMMENT ON COLUMN bor_tel.freadas_bruscas_viagem IS 'Freadas Bruscas  Na Viagem';
COMMENT ON COLUMN bor_tel.gps_qual_acel_max_viagem IS 'Qualidade da Aceleração Maxima na Viagem';
COMMENT ON COLUMN bor_tel.gps_qual_desacel_max_viagem IS 'Qualidade da Desaceleração Maxima na Viagem';
COMMENT ON COLUMN bor_tel.gps_qual_rot_motor_max_viagem IS 'Qualidade da Maxima da Rotação do Motor Na Viagem';
COMMENT ON COLUMN bor_tel.gps_qual_vel_max_viagem_tac IS 'Qualidade da Velocidade Maxima do Motor Na Viagem Tacografo ';
COMMENT ON COLUMN bor_tel.id_ibutton IS 'Numero IButton';
COMMENT ON COLUMN bor_tel.lat_acel_max_viagem IS 'Latitude de Aceleração Maxima de Viagem';
COMMENT ON COLUMN bor_tel.lat_desacel_max_viagem IS 'Latitude de Desaceleração Maxima de Viagem';
COMMENT ON COLUMN bor_tel.lat_max_tempo_marcha_lenta_viagem IS 'Latitude Tempo Maximo Em Marcha Lenta Na Viagem';
COMMENT ON COLUMN bor_tel.lat_rot_motor_max_viagem IS 'Latitude Rotação Maxima do Motor Na Viagem';
COMMENT ON COLUMN bor_tel.lat_vel_max_banguela IS 'Latitude Velocidade Maxima Na Banguela';
COMMENT ON COLUMN bor_tel.lat_vel_max_viagem_gps IS 'Latitude Velocidade Maxima De Viagem Gps';
COMMENT ON COLUMN bor_tel.lat_vel_max_viagem_tac IS 'Latitude da Velocidade Maxima de Viagem Tacografo';
COMMENT ON COLUMN bor_tel.long_acel_max_viagem IS 'Longitude da Aceleração Maxima na Viagem ';
COMMENT ON COLUMN bor_tel.long_desacel_max_viagem IS 'Longitude da Desaceleração Maxima de Viagem';
COMMENT ON COLUMN bor_tel.long_max_tempo_marcha_lenta_viagem IS 'Longitude Maxima Tempo Marcha Lenta Na Viagem';
COMMENT ON COLUMN bor_tel.long_rot_motor_max_viagem IS 'Longitude da Rotação Maxima do Motor Na Viagem';
COMMENT ON COLUMN bor_tel.long_vel_max_banguela IS 'Longitude da Velocidade Maxima Banguela';
COMMENT ON COLUMN bor_tel.long_vel_max_viagem_gps IS 'Longitude da Velocidade Maxima Na Viagem GPS';
COMMENT ON COLUMN bor_tel.long_vel_max_viagem_tac IS 'Longitude da Velocidade Maxima de Viagem Tacografo';
COMMENT ON COLUMN bor_tel.maior_tempo_banguela_viagem IS 'Maior Tempo de Banguela Na Viagem';
COMMENT ON COLUMN bor_tel.maior_vel_banguela IS 'Maior Velocidade de Banguela';
COMMENT ON COLUMN bor_tel.media_acel_brusca_m_s2_acum IS 'Media de Aceleração Brusca Em Metro Por Segundo ao Quadrado Acumuladas';
COMMENT ON COLUMN bor_tel.media_acel_brusca_viage_m_s2 IS 'Media de Aceleração Brusca Em Metro Por Segundo ao Quadrado';
COMMENT ON COLUMN bor_tel.media_freadas_m_s2_acum IS 'Media de Freadas Em Metro Por Segundo ao Quadrado Acumulada';
COMMENT ON COLUMN bor_tel.media_freadas_viagem_m_s2 IS 'Media de Freadas na Viagem Em Metro Por Segundo Ao Quadrado';
COMMENT ON COLUMN bor_tel.nm_marcha_lenta_acum IS 'Numero de Marcha Lenta Acumuladas';
COMMENT ON COLUMN bor_tel.nm_marcha_lenta_viagem IS 'Numero de Marcha Lenta Acumuladas Na Viagem';
COMMENT ON COLUMN bor_tel.num_arranc_bruscas_acum IS 'Numero de Arrancadas Bruscas Acumuladas';
COMMENT ON COLUMN bor_tel.num_arranc_bruscas_viagem IS 'Numero de Arrancadas Bruscas Na Viagem';
COMMENT ON COLUMN bor_tel.num_banguela_acum IS 'Numero de Banguelas Acumuladas';
COMMENT ON COLUMN bor_tel.num_banguela_viagem IS 'Numero de Banguelas na Viagem';
COMMENT ON COLUMN bor_tel.num_freio_motor_acum IS 'Numero de freio Motor Acumulado';
COMMENT ON COLUMN bor_tel.num_rpm_acima_acum IS 'Numero de Rpm Acima Acumulados';
COMMENT ON COLUMN bor_tel.num_rpm_acima_parcial IS 'Numero de Rpm Acima Parcial';
COMMENT ON COLUMN bor_tel.num_vezes_banguela_viagem IS 'Numero de Vezes Banguela Viagem ';
COMMENT ON COLUMN bor_tel.num_vezes_vel_acima_acum IS 'Numero de Vezes Velocidade Acima Esta Acumulado';
COMMENT ON COLUMN bor_tel.num_vezes_vel_acima_parcial IS 'Numero de Vezes Velocidade Acima Parcial';
COMMENT ON COLUMN bor_tel.odo_acum_gps_dec_km IS 'Odometro Acumulado GPS (decimos de Km) ';
COMMENT ON COLUMN bor_tel.odo_acum_tac_dec_km IS 'Odometro acumulado Tacografo (decimos de Km) ';
COMMENT ON COLUMN bor_tel.odo_viagem_gps_dec_km IS 'Odometro de Viagem GPS(decimos de Km) ';
COMMENT ON COLUMN bor_tel.odo_viagem_tac_dec_km IS 'Odometro de Viagem Tacografo (decimos de Km) ';
COMMENT ON COLUMN bor_tel.rot_motor_max_viagem IS 'Rotação Maxima Motor Na Viagem';
COMMENT ON COLUMN bor_tel.rot_motor_med_viagem IS 'Rotação Media do Motor Na Viagem';
COMMENT ON COLUMN bor_tel.tensao_batt_bkp_med_dec_volts IS 'Tensão da Bateria de Backup na Viagem (media(decimos de Volt 5 = 0,5V)';
COMMENT ON COLUMN bor_tel.tensao_batt_veic_med_dec_volts IS 'Tensão da Bateria do Veiculo na Viagem (decimos de Volt 5 = 0,5V)';
COMMENT ON COLUMN bor_tel.dthr_acel_max_viagem IS 'TimeStamp da Aceleração Maxima Na Viagem';
COMMENT ON COLUMN bor_tel.dthr_desacel_max_viagem IS 'TimeStamp da Desaceleração Maxima Na Viagem';
COMMENT ON COLUMN bor_tel.dthr_max_tempo_marcha_lenta_viagem IS 'TimeStamp do Tempo Maximo de Marchar Lenta Na Viagem';
COMMENT ON COLUMN bor_tel.dthr_rot_motor_max_viagem IS 'TimeStamp da Rotação Maxima Do Motor Na Viagem';
COMMENT ON COLUMN bor_tel.dthr_vel_max_banguela IS 'TimeStamp da Velocidade Maxima Banguela';
COMMENT ON COLUMN bor_tel.dthr_vel_max_viagem_gps IS 'TimeStamp da Velocidade Maxima Viagem Gps';
COMMENT ON COLUMN bor_tel.dthr_vel_max_viagem_tac IS 'TimeStamp da Velocidade Maxima Viagem Tacografo';
COMMENT ON COLUMN bor_tel.tempo_faixa_amarela_acum IS 'Tempo de faixa Amarela Acumulada';
COMMENT ON COLUMN bor_tel.tempo_faixa_amarela_parcial IS 'Tempo de Faixa Amarela Parcial';
COMMENT ON COLUMN bor_tel.tempo_faixa_azul_acum IS 'Tempo de Faixa Azul Acumulada';
COMMENT ON COLUMN bor_tel.tempo_faixa_azul_parcial IS 'Tempo de Faixa Azul Parcial';
COMMENT ON COLUMN bor_tel.tempo_faixa_verde_acum IS 'Tempo de Faixa Verde Acumulada';
COMMENT ON COLUMN bor_tel.tempo_faixa_verde_parcial IS 'Tempo de Faixa Verde Parcial';
COMMENT ON COLUMN bor_tel.tempo_faixa_vermelha_acum IS 'Tempo de Faixa Vermelha Acumulada';
COMMENT ON COLUMN bor_tel.tempo_faixa_vermelha_parcial IS 'Tempo de Faixa Vermelha Parcial';
COMMENT ON COLUMN bor_tel.tempo_freio_motor_acum IS 'Tempo de Freio Motor Acumulado';
COMMENT ON COLUMN bor_tel.tempo_marcha_lenta_acum IS 'Tempo de Marcha Lenta Acumulado';
COMMENT ON COLUMN bor_tel.tempo_marcha_lenta_viagem IS 'Tempo de Marcha Lenta Acumulado Na Viagem';
COMMENT ON COLUMN bor_tel.tempo_max_marcha_lenta_viagem IS 'Tempo Maximo de Marcha Lenta Na Viagem';
COMMENT ON COLUMN bor_tel.tempo_medio_marcha_lenta_viagem IS 'Tempo Medio de Marcha Lenta Na Viagem';
COMMENT ON COLUMN bor_tel.tempo_pedal_freio_acionado_viagem IS 'Tempo em Que O Pedal de Freio Foi Acionado Na Viagem';
COMMENT ON COLUMN bor_tel.tempo_perm_bang_acum_secs IS 'Tempo de Permanência em Banguela Acumulado (segundos)';
COMMENT ON COLUMN bor_tel.tempo_perm_bang_viagem_secs IS 'Tempo de Permanência em Banguela na Viagem (segundos)';
COMMENT ON COLUMN bor_tel.tempo_rpm_acima_acum IS 'Tempo Acumulado de Rpm Acima';
COMMENT ON COLUMN bor_tel.tempo_rpm_acima_parcial IS 'Tempo Parcial de Rpm Acima';
COMMENT ON COLUMN bor_tel.tempo_uso_acum_em_movimento_secs IS 'Tempo Acumulado de Uso em Movimento';
COMMENT ON COLUMN bor_tel.tempo_uso_acum_parado_secs IS 'Tempo de Uso Parado Acumulado em(segundos)';
COMMENT ON COLUMN bor_tel.tempo_uso_acum_total_secs IS 'Tempo de Uso Total Acumulado (segundos)';
COMMENT ON COLUMN bor_tel.tempo_uso_viagem_em_movto_secs IS 'Tempo de Uso Na Viagem Em Movimento(segundos)';
COMMENT ON COLUMN bor_tel.tempo_uso_viagem_parado_secs IS 'Tempo de Uso Na Viagem Parado(segundos)';
COMMENT ON COLUMN bor_tel.tempo_uso_viagem_total_secs IS 'Tempo de Uso Total Na Viagem (segundos)';
COMMENT ON COLUMN bor_tel.tempo_veic_deslig_acum_secs IS 'Tempo Acumulado Veiculo Desligado(segundos)';
COMMENT ON COLUMN bor_tel.tempo_veic_desl_entre_viagens_secs IS 'Tempo Veiculo Foi Desligado Entre Viagens(segundos)';
COMMENT ON COLUMN bor_tel.tempo_vel_acima_acum IS 'Tempo Velocidade Acima Acumulado';
COMMENT ON COLUMN bor_tel.tempo_vel_acima_parcial IS 'Tempo Velocidade Acima Parcial';
COMMENT ON COLUMN bor_tel.vel_final_frenagem_brusca IS 'Velocidade Final de Frenagem Bruscas';
COMMENT ON COLUMN bor_tel.vel_final_max_acel_brusca IS 'Velocidade Maxima Final de Aceleração Bruscas';
COMMENT ON COLUMN bor_tel.vel_inicial_frenagem_brusca IS 'Velocidade Inicial de Frenagem Bruscas';
COMMENT ON COLUMN bor_tel.vel_inicial_max_acel_brusca IS 'Velocidade Maxima Inicial de Aceleração Brusca';
COMMENT ON COLUMN bor_tel.vel_max_viagem_gps IS 'Velocidade Maxima de Viagem GPS';
COMMENT ON COLUMN bor_tel.vel_max_viagem_tac IS 'Velocidade Max Viagem Tacografo';
COMMENT ON COLUMN bor_tel.vel_media_gps_acum IS 'Velocidade Media GPS Acumulado';
COMMENT ON COLUMN bor_tel.vel_media_tac_acum IS 'Velocidade Media Tacografo Acumulado';
COMMENT ON COLUMN bor_tel.vel_med_viagem_gps IS 'Velocidade Media na Viagem GPS';
COMMENT ON COLUMN bor_tel.vel_med_viagem_tac IS 'Velocidade Media Viagem Com Tacografo';
COMMENT ON COLUMN bor_tel.id_reatime IS 'ID RealTime - Redis';
COMMENT ON COLUMN bor_tel.log_user_ins IS 'Log - Usuário de Inserçã£o';
COMMENT ON COLUMN bor_tel.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN bor_tel.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN bor_tel.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN bor_tel.status_msg IS 'Status Msg';
COMMENT ON COLUMN bor_tel.dthr_status IS 'Data de Status';
COMMENT ON COLUMN bor_tel.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN bor_tel.ope_centro2_pessoa_id IS 'ID do Centro Nível 2 - Pessoa';
COMMENT ON COLUMN bor_tel.ope_centro2_equip_id_1 IS 'ID do Centro Nível 2 - Equipamento 1';
COMMENT ON COLUMN bor_tel.unit_id IS 'ID da Unidade';
ALTER TABLE bor_tel OWNER TO postgres;

CREATE TABLE system_token (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
dt_validade timestamp(0) NOT NULL,
dt_token timestamp(0) NOT NULL,
token text NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_token PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE UNIQUE INDEX idx_system_token ON system_token USING btree (token pg_catalog.text_ops ASC NULLS LAST) WITH (fillfactor = 90);
COMMENT ON TABLE system_token IS 'System-Token';
COMMENT ON COLUMN system_token.id IS 'ID da Unidade';
COMMENT ON COLUMN system_token.dt_validade IS 'Data de validade do Token';
COMMENT ON COLUMN system_token.dt_token IS 'Data do Token';
COMMENT ON COLUMN system_token.token IS 'Token';
COMMENT ON COLUMN system_token.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_token.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_token.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_token.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_token OWNER TO postgres;

CREATE TABLE system_type_description (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
table_name varchar(100)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
field_name varchar(100) NOT NULL,
value_type varchar(50) NOT NULL,
description_type varchar(100) NOT NULL,
CONSTRAINT pk_system_type_description PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE UNIQUE INDEX idx_system_type_description ON system_type_description USING btree (table_name ASC NULLS LAST, field_name ASC NULLS LAST, value_type ASC NULLS LAST) WITH (fillfactor = 90);
COMMENT ON TABLE system_type_description IS 'System-Descrição de Tipos';
COMMENT ON COLUMN system_type_description.id IS 'ID da Descrição de Tipos';
COMMENT ON COLUMN system_type_description.table_name IS 'Nome da Tabela';
COMMENT ON COLUMN system_type_description.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_type_description.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_type_description.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_type_description.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_type_description.field_name IS 'Nome Campo';
COMMENT ON COLUMN system_type_description.value_type IS 'Valor do Tipo';
COMMENT ON COLUMN system_type_description.description_type IS 'Descrição do Valor';
ALTER TABLE system_type_description OWNER TO postgres;

CREATE TABLE ctb_conta_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_conta_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
estrutura varchar(50) NOT NULL,
ctb_conta_versao_id varchar(36) NOT NULL,
CONSTRAINT pk_ctb_conta_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_conta_grupo IS 'Contábil-Grupo de Contas';
COMMENT ON COLUMN ctb_conta_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_conta_grupo.id IS 'ID do Grupo de Conta';
COMMENT ON COLUMN ctb_conta_grupo.nome IS 'Nome';
COMMENT ON COLUMN ctb_conta_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_conta_grupo.sigla_conta_grupo IS 'Sigla do Grupo de Conta';
COMMENT ON COLUMN ctb_conta_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_conta_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_conta_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_conta_grupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_conta_grupo.estrutura IS 'Estrutura';
COMMENT ON COLUMN ctb_conta_grupo.ctb_conta_versao_id IS 'ID do Versao Conta Contábil';
ALTER TABLE ctb_conta_grupo OWNER TO postgres;

CREATE TABLE ctb_conta (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_conta varchar(50) NOT NULL,
ctb_conta_grupo_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_variacao varchar(1) NOT NULL,
tipo_dc varchar(1) NOT NULL,
tipo_conta varchar(2) NOT NULL,
ctb_conta_versao_id varchar(36) NOT NULL,
CONSTRAINT pk_ctb_conta PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_conta IS 'Contábil-Conta';
COMMENT ON COLUMN ctb_conta.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_conta.id IS 'ID da Conta Contábil';
COMMENT ON COLUMN ctb_conta.nome IS 'Nome';
COMMENT ON COLUMN ctb_conta.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_conta.sigla_conta IS 'Sigla Conta';
COMMENT ON COLUMN ctb_conta.ctb_conta_grupo_id IS 'ID do Grupo do Conta Contábil';
COMMENT ON COLUMN ctb_conta.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_conta.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_conta.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_conta.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_conta.tipo_variacao IS 'Tipo: F-Fixo, V-Variável, I-Investimento';
COMMENT ON COLUMN ctb_conta.tipo_dc IS 'Tipo: D-Débito, C-Crédito';
COMMENT ON COLUMN ctb_conta.tipo_conta IS 'Tipo Conta: 01-Ativo, 02-Passivo, 03-P.Liquido, 04-Resultado, 05-Compensação';
COMMENT ON COLUMN ctb_conta.ctb_conta_versao_id IS 'ID do Versao Conta Contábil';
ALTER TABLE ctb_conta OWNER TO postgres;

CREATE TABLE ctb_lote (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_lote varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ctb_lote PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_lote IS 'Contábil-Lote';
COMMENT ON COLUMN ctb_lote.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_lote.id IS 'ID do Lote Contábil';
COMMENT ON COLUMN ctb_lote.nome IS 'Nome';
COMMENT ON COLUMN ctb_lote.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_lote.sigla_lote IS 'Sigla do Lote Contábil';
COMMENT ON COLUMN ctb_lote.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_lote.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_lote.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_lote.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ctb_lote OWNER TO postgres;

CREATE TABLE ctb_historico (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_historico varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ctb_historico PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_historico IS 'Contábil-Histórico';
COMMENT ON COLUMN ctb_historico.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_historico.id IS 'ID do Histórico Contábil';
COMMENT ON COLUMN ctb_historico.nome IS 'Nome';
COMMENT ON COLUMN ctb_historico.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_historico.sigla_historico IS 'Sigla do Histórico Contábil';
COMMENT ON COLUMN ctb_historico.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_historico.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_historico.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_historico.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ctb_historico OWNER TO postgres;

CREATE TABLE ctb_conta_versao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_versao varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
versao_atual varchar NOT NULL DEFAULT 'N',
data_valid_ini date NOT NULL,
CONSTRAINT pk_ctb_conta_versao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_conta_versao IS 'Contábil-Versão de Conta';
COMMENT ON COLUMN ctb_conta_versao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_conta_versao.id IS 'ID do Versao Conta Contábil';
COMMENT ON COLUMN ctb_conta_versao.nome IS 'Nome';
COMMENT ON COLUMN ctb_conta_versao.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_conta_versao.sigla_versao IS 'Sigla do Versão Conta Contábil';
COMMENT ON COLUMN ctb_conta_versao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_conta_versao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_conta_versao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_conta_versao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_conta_versao.versao_atual IS 'Versão Atual';
COMMENT ON COLUMN ctb_conta_versao.data_valid_ini IS 'Data Validade Inicial';
ALTER TABLE ctb_conta_versao OWNER TO postgres;

CREATE TABLE ctb_lanc (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_empresa_id varchar(36) NOT NULL,
numero_lanc varchar(50) NOT NULL,
data_lanc date NOT NULL,
ctb_lote_id varchar(36) NOT NULL,
ctb_historico_id varchar(36) NOT NULL,
historico varchar(250) NOT NULL,
log_user_ins varchar(100) NOT NULL,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
status varchar(2) NOT NULL DEFAULT 'PD',
status_observacao varchar(250),
ctb_versao_id varchar(36),
CONSTRAINT pk_ctb_lanc PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_lanc IS 'Contábil-Lançamentos';
COMMENT ON COLUMN ctb_lanc.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_lanc.id IS 'ID do Lançamento Contábil';
COMMENT ON COLUMN ctb_lanc.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ctb_lanc.numero_lanc IS 'Ativo';
COMMENT ON COLUMN ctb_lanc.data_lanc IS 'Data Lançamento';
COMMENT ON COLUMN ctb_lanc.ctb_lote_id IS 'ID do Lote Contábil';
COMMENT ON COLUMN ctb_lanc.ctb_historico_id IS 'ID do Histórico Contábil';
COMMENT ON COLUMN ctb_lanc.historico IS 'Histórico';
COMMENT ON COLUMN ctb_lanc.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_lanc.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_lanc.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_lanc.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_lanc.status IS 'Satus: PD-Pendente, EA-Em analise, CD-Consciliado';
COMMENT ON COLUMN ctb_lanc.status_observacao IS 'Observação do Status';
COMMENT ON COLUMN ctb_lanc.ctb_versao_id IS 'ID da Versão Contábil / Previsão';
ALTER TABLE ctb_lanc OWNER TO postgres;

CREATE TABLE ctb_lanc_det (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ctb_lanc_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ctb_conta_id varchar(36) NOT NULL,
tipo_dc varchar(1) NOT NULL,
ope_centro2_id varchar(36),
ope_atividade_id varchar(36),
ctb_comp_id varchar(36),
valor numeric(18,2) NOT NULL DEFAULT 0,
process_id varchar(36),
origem_tipo varchar(50) NOT NULL,
origem_id varchar(36) NOT NULL,
observacao varchar(250),
qnt numeric(18,6) NOT NULL DEFAULT 0,
CONSTRAINT pk_ctb_lanc_det PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_lanc_det IS 'Contábil-Laçamento Detalhe';
COMMENT ON COLUMN ctb_lanc_det.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_lanc_det.id IS 'ID do Detalhe do Lançamento';
COMMENT ON COLUMN ctb_lanc_det.ctb_lanc_id IS 'ID do Lançamento Contábil';
COMMENT ON COLUMN ctb_lanc_det.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_lanc_det.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_lanc_det.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_lanc_det.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_lanc_det.ctb_conta_id IS 'ID da Conta Contábil';
COMMENT ON COLUMN ctb_lanc_det.tipo_dc IS 'Tipo: D-Débito, C-Crédito';
COMMENT ON COLUMN ctb_lanc_det.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ctb_lanc_det.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN ctb_lanc_det.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ctb_lanc_det.valor IS 'Valor Contábil';
COMMENT ON COLUMN ctb_lanc_det.process_id IS 'ID do Processo';
COMMENT ON COLUMN ctb_lanc_det.origem_tipo IS 'Tipo: MANUAL, Etc';
COMMENT ON COLUMN ctb_lanc_det.origem_id IS 'ID da Origem';
COMMENT ON COLUMN ctb_lanc_det.observacao IS 'Observação';
COMMENT ON COLUMN ctb_lanc_det.qnt IS 'Quantidade';
ALTER TABLE ctb_lanc_det OWNER TO postgres;

CREATE TABLE ope_centro_versao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_versao varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
versao_atual varchar(1) NOT NULL,
data_per_ini date NOT NULL,
data_per_fin date NOT NULL,
tipo_per varchar(1) NOT NULL,
CONSTRAINT pk_ope_centro_versao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_versao IS 'Operação-Versão da Operação';
COMMENT ON COLUMN ope_centro_versao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_versao.id IS 'ID da Versão da Operação';
COMMENT ON COLUMN ope_centro_versao.nome IS 'Nome';
COMMENT ON COLUMN ope_centro_versao.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro_versao.sigla_versao IS 'Sigla da Versão da Operação';
COMMENT ON COLUMN ope_centro_versao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_versao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_versao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_versao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_versao.versao_atual IS 'Versão Atual';
COMMENT ON COLUMN ope_centro_versao.data_per_ini IS 'Data Período Inicial';
COMMENT ON COLUMN ope_centro_versao.data_per_fin IS 'Data Período Final';
COMMENT ON COLUMN ope_centro_versao.tipo_per IS 'Tipo Período: D-Diário, M-Mensal, A-Anual';
ALTER TABLE ope_centro_versao OWNER TO postgres;

CREATE TABLE ctb_tipo_saldo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_tipo_saldo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
mes_ini_fechamento int2 NOT NULL DEFAULT 0,
mes_fin_fechamento int2 NOT NULL DEFAULT 12,
CONSTRAINT pk_ctb_tipo_saldo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_tipo_saldo IS 'Contábil-Tipo Saldo';
COMMENT ON COLUMN ctb_tipo_saldo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_tipo_saldo.id IS 'ID do Tipo Saldo';
COMMENT ON COLUMN ctb_tipo_saldo.nome IS 'Nome';
COMMENT ON COLUMN ctb_tipo_saldo.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_tipo_saldo.sigla_tipo_saldo IS 'Sigla do Tipo Saldo';
COMMENT ON COLUMN ctb_tipo_saldo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_tipo_saldo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_tipo_saldo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_tipo_saldo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_tipo_saldo.mes_ini_fechamento IS 'Mês Inicial de Fechamento';
COMMENT ON COLUMN ctb_tipo_saldo.mes_fin_fechamento IS 'Mês Final de Fechamento';
ALTER TABLE ctb_tipo_saldo OWNER TO postgres;

CREATE TABLE fin_pagrec_versao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_versao varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
data_per_ini date NOT NULL,
data_per_fin date NOT NULL,
versao_atual varchar(1) NOT NULL DEFAULT 'N',
tipo_per varchar(1) NOT NULL DEFAULT 'M',
CONSTRAINT pk_fin_pagrec_versao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_versao IS 'Financeiro-Pag/Rec Versão';
COMMENT ON COLUMN fin_pagrec_versao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_versao.id IS 'ID da Versão Pag/Rec';
COMMENT ON COLUMN fin_pagrec_versao.nome IS 'Nome';
COMMENT ON COLUMN fin_pagrec_versao.ativo IS 'Ativo';
COMMENT ON COLUMN fin_pagrec_versao.sigla_versao IS 'Sigla Versão Pag/Rec';
COMMENT ON COLUMN fin_pagrec_versao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_versao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_versao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_versao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_versao.data_per_ini IS 'Data Período Inicial';
COMMENT ON COLUMN fin_pagrec_versao.data_per_fin IS 'Data Período Final';
COMMENT ON COLUMN fin_pagrec_versao.versao_atual IS 'Versão Atual';
COMMENT ON COLUMN fin_pagrec_versao.tipo_per IS 'Tipo Período: D-Diário, M-Mensal, A-Anual';
ALTER TABLE fin_pagrec_versao OWNER TO postgres;

CREATE TABLE fin_pagrec_prev (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
data_per date NOT NULL,
ger_empresa_id varchar(36) NOT NULL,
fin_class_id varchar(36) NOT NULL,
ger_pessoa_id varchar(36) NOT NULL,
fin_pagrec_versao_id varchar(36) NOT NULL,
valor01 numeric(18,2) NOT NULL DEFAULT 0,
valor02 numeric(18,2) NOT NULL DEFAULT 0,
valor03 numeric(18,2) NOT NULL DEFAULT 0,
valor04 numeric(18,2) NOT NULL DEFAULT 0,
valor05 numeric(18,2) NOT NULL DEFAULT 0,
valor06 numeric(18,2) NOT NULL DEFAULT 0,
valor07 numeric(18,2) NOT NULL DEFAULT 0,
valor08 numeric(18,2) NOT NULL DEFAULT 0,
valor09 numeric(18,2) NOT NULL DEFAULT 0,
valor10 numeric(18,2) NOT NULL DEFAULT 0,
valor11 numeric(18,2) NOT NULL DEFAULT 0,
valor12 numeric(18,2) NOT NULL DEFAULT 0,
valor13 numeric(18,2) NOT NULL DEFAULT 0,
valor14 numeric(18,2) NOT NULL DEFAULT 0,
valor15 numeric(18,2) NOT NULL DEFAULT 0,
valor16 numeric(18,2) NOT NULL DEFAULT 0,
valor17 numeric(18,2) NOT NULL DEFAULT 0,
valor18 numeric(18,2) NOT NULL DEFAULT 0,
valor19 numeric(18,2) NOT NULL DEFAULT 0,
valor20 numeric(18,2) NOT NULL DEFAULT 0,
valor21 numeric(18,2) NOT NULL DEFAULT 0,
valor22 numeric(18,2) NOT NULL DEFAULT 0,
valor23 numeric(18,2) NOT NULL DEFAULT 0,
valor24 numeric(18,2) NOT NULL DEFAULT 0,
valor25 numeric(18,2) NOT NULL DEFAULT 0,
valor26 numeric(18,2) NOT NULL DEFAULT 0,
valor27 numeric(18,2) NOT NULL DEFAULT 0,
valor28 numeric(18,2) NOT NULL DEFAULT 0,
valor29 numeric(18,2) NOT NULL DEFAULT 0,
valor30 numeric(18,2) NOT NULL DEFAULT 0,
valor31 numeric(18,2) NOT NULL DEFAULT 0,
tipo_es varchar(1),
process_id varchar(36),
data_valid date,
CONSTRAINT pk_fin_pagrec_prev PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_prev IS 'Financeiro-Pag/Rec Previsto';
COMMENT ON COLUMN fin_pagrec_prev.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_prev.id IS 'ID da Previsão Pag/Rec';
COMMENT ON COLUMN fin_pagrec_prev.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_prev.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_prev.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_prev.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_prev.data_per IS 'Data do Período';
COMMENT ON COLUMN fin_pagrec_prev.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN fin_pagrec_prev.fin_class_id IS 'ID do Classificação';
COMMENT ON COLUMN fin_pagrec_prev.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN fin_pagrec_prev.fin_pagrec_versao_id IS 'ID da Versão Pag/Rec';
COMMENT ON COLUMN fin_pagrec_prev.valor01 IS 'Valor 01';
COMMENT ON COLUMN fin_pagrec_prev.valor02 IS 'Valor 02';
COMMENT ON COLUMN fin_pagrec_prev.valor03 IS 'Valor 03';
COMMENT ON COLUMN fin_pagrec_prev.valor04 IS 'Valor 04';
COMMENT ON COLUMN fin_pagrec_prev.valor05 IS 'Valor 05';
COMMENT ON COLUMN fin_pagrec_prev.valor06 IS 'Valor 06';
COMMENT ON COLUMN fin_pagrec_prev.valor07 IS 'Valor 07';
COMMENT ON COLUMN fin_pagrec_prev.valor08 IS 'Valor 08';
COMMENT ON COLUMN fin_pagrec_prev.valor09 IS 'Valor 09';
COMMENT ON COLUMN fin_pagrec_prev.valor10 IS 'Valor 10';
COMMENT ON COLUMN fin_pagrec_prev.valor11 IS 'Valor 11';
COMMENT ON COLUMN fin_pagrec_prev.valor12 IS 'Valor 12';
COMMENT ON COLUMN fin_pagrec_prev.valor13 IS 'Valor 13';
COMMENT ON COLUMN fin_pagrec_prev.valor14 IS 'Valor 14';
COMMENT ON COLUMN fin_pagrec_prev.valor15 IS 'Valor 15';
COMMENT ON COLUMN fin_pagrec_prev.valor16 IS 'Valor 16';
COMMENT ON COLUMN fin_pagrec_prev.valor17 IS 'Valor 17';
COMMENT ON COLUMN fin_pagrec_prev.valor18 IS 'Valor 18';
COMMENT ON COLUMN fin_pagrec_prev.valor19 IS 'Valor 19';
COMMENT ON COLUMN fin_pagrec_prev.valor20 IS 'Valor 20';
COMMENT ON COLUMN fin_pagrec_prev.valor21 IS 'Valor 21';
COMMENT ON COLUMN fin_pagrec_prev.valor22 IS 'Valor 22';
COMMENT ON COLUMN fin_pagrec_prev.valor23 IS 'Valor 23';
COMMENT ON COLUMN fin_pagrec_prev.valor24 IS 'Valor 24';
COMMENT ON COLUMN fin_pagrec_prev.valor25 IS 'Valor 25';
COMMENT ON COLUMN fin_pagrec_prev.valor26 IS 'Valor 26';
COMMENT ON COLUMN fin_pagrec_prev.valor27 IS 'Valor 27';
COMMENT ON COLUMN fin_pagrec_prev.valor28 IS 'Valor 28';
COMMENT ON COLUMN fin_pagrec_prev.valor29 IS 'Valor 29';
COMMENT ON COLUMN fin_pagrec_prev.valor30 IS 'Valor 30';
COMMENT ON COLUMN fin_pagrec_prev.valor31 IS 'Valor 31';
COMMENT ON COLUMN fin_pagrec_prev.tipo_es IS 'Tipo: E-Entrada; S-Saída';
COMMENT ON COLUMN fin_pagrec_prev.process_id IS 'ID do Processo';
COMMENT ON COLUMN fin_pagrec_prev.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_prev OWNER TO postgres;

CREATE TABLE ope_centro_rend_fator (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ope_centro2_id varchar(36),
ger_itemserv_id varchar(36),
ctb_comp_id varchar(36) NOT NULL,
fator_rend numeric(18,4) NOT NULL DEFAULT 0,
fator_util numeric(18,4) NOT NULL DEFAULT 100,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro_rend_id varchar(36) NOT NULL,
CONSTRAINT pk_ope_centro_rend_fator PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_rend_fator IS 'Operacional-Fator de rendimentos por Atividade';
COMMENT ON COLUMN ope_centro_rend_fator.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_rend_fator.id IS 'ID do Rendimento por Atividade';
COMMENT ON COLUMN ope_centro_rend_fator.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro_rend_fator.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ope_centro_rend_fator.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ope_centro_rend_fator.fator_rend IS 'Fator de Rendimento';
COMMENT ON COLUMN ope_centro_rend_fator.fator_util IS 'Fator de Utilização';
COMMENT ON COLUMN ope_centro_rend_fator.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_rend_fator.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_rend_fator.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_rend_fator.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_rend_fator.ope_centro_rend_id IS 'ID do Rendimento de Componente';
ALTER TABLE ope_centro_rend_fator OWNER TO postgres;

CREATE TABLE fin_pagrec_prev_var (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
fin_pagrec_prev_id varchar(36) NOT NULL,
fin_tipo_variacao_id varchar(36) NOT NULL,
valor01 numeric(18,2) NOT NULL DEFAULT 0,
valor02 numeric(18,2) NOT NULL DEFAULT 0,
valor03 numeric(18,2) NOT NULL DEFAULT 0,
valor04 numeric(18,2) NOT NULL DEFAULT 0,
valor05 numeric(18,2) NOT NULL DEFAULT 0,
valor06 numeric(18,2) NOT NULL DEFAULT 0,
valor07 numeric(18,2) NOT NULL DEFAULT 0,
valor08 numeric(18,2) NOT NULL DEFAULT 0,
valor09 numeric(18,2) NOT NULL DEFAULT 0,
valor10 numeric(18,2) NOT NULL DEFAULT 0,
valor11 numeric(18,2) NOT NULL DEFAULT 0,
valor12 numeric(18,2) NOT NULL DEFAULT 0,
valor13 numeric(18,2) NOT NULL DEFAULT 0,
valor14 numeric(18,2) NOT NULL DEFAULT 0,
valor15 numeric(18,2) NOT NULL DEFAULT 0,
valor16 numeric(18,2) NOT NULL DEFAULT 0,
valor17 numeric(18,2) NOT NULL DEFAULT 0,
valor18 numeric(18,2) NOT NULL DEFAULT 0,
valor19 numeric(18,2) NOT NULL DEFAULT 0,
valor20 numeric(18,2) NOT NULL DEFAULT 0,
valor21 numeric(18,2) NOT NULL DEFAULT 0,
valor22 numeric(18,2) NOT NULL DEFAULT 0,
valor23 numeric(18,2) NOT NULL DEFAULT 0,
valor24 numeric(18,2) NOT NULL DEFAULT 0,
valor25 numeric(18,2) NOT NULL DEFAULT 0,
valor26 numeric(18,2) NOT NULL DEFAULT 0,
valor27 numeric(18,2) NOT NULL DEFAULT 0,
valor28 numeric(18,2) NOT NULL DEFAULT 0,
valor29 numeric(18,2) NOT NULL DEFAULT 0,
valor30 numeric(18,2) NOT NULL DEFAULT 0,
valor31 numeric(18,2) NOT NULL DEFAULT 0,
data_valid date,
CONSTRAINT pk_fin_pagrec_prev_var PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_prev_var IS 'Financeiro-Pag/Rec Previsto - Variação';
COMMENT ON COLUMN fin_pagrec_prev_var.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_prev_var.id IS 'ID da Previsão Pag/Rec - Variação';
COMMENT ON COLUMN fin_pagrec_prev_var.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_prev_var.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_prev_var.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_prev_var.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_prev_var.fin_pagrec_prev_id IS 'ID da Previsão Pag/Rec';
COMMENT ON COLUMN fin_pagrec_prev_var.fin_tipo_variacao_id IS 'ID do Tipo de Variação';
COMMENT ON COLUMN fin_pagrec_prev_var.valor01 IS 'Valor 01';
COMMENT ON COLUMN fin_pagrec_prev_var.valor02 IS 'Valor 02';
COMMENT ON COLUMN fin_pagrec_prev_var.valor03 IS 'Valor 03';
COMMENT ON COLUMN fin_pagrec_prev_var.valor04 IS 'Valor 04';
COMMENT ON COLUMN fin_pagrec_prev_var.valor05 IS 'Valor 05';
COMMENT ON COLUMN fin_pagrec_prev_var.valor06 IS 'Valor 06';
COMMENT ON COLUMN fin_pagrec_prev_var.valor07 IS 'Valor 07';
COMMENT ON COLUMN fin_pagrec_prev_var.valor08 IS 'Valor 08';
COMMENT ON COLUMN fin_pagrec_prev_var.valor09 IS 'Valor 09';
COMMENT ON COLUMN fin_pagrec_prev_var.valor10 IS 'Valor 10';
COMMENT ON COLUMN fin_pagrec_prev_var.valor11 IS 'Valor 11';
COMMENT ON COLUMN fin_pagrec_prev_var.valor12 IS 'Valor 12';
COMMENT ON COLUMN fin_pagrec_prev_var.valor13 IS 'Valor 13';
COMMENT ON COLUMN fin_pagrec_prev_var.valor14 IS 'Valor 14';
COMMENT ON COLUMN fin_pagrec_prev_var.valor15 IS 'Valor 15';
COMMENT ON COLUMN fin_pagrec_prev_var.valor16 IS 'Valor 16';
COMMENT ON COLUMN fin_pagrec_prev_var.valor17 IS 'Valor 17';
COMMENT ON COLUMN fin_pagrec_prev_var.valor18 IS 'Valor 18';
COMMENT ON COLUMN fin_pagrec_prev_var.valor19 IS 'Valor 19';
COMMENT ON COLUMN fin_pagrec_prev_var.valor20 IS 'Valor 20';
COMMENT ON COLUMN fin_pagrec_prev_var.valor21 IS 'Valor 21';
COMMENT ON COLUMN fin_pagrec_prev_var.valor22 IS 'Valor 22';
COMMENT ON COLUMN fin_pagrec_prev_var.valor23 IS 'Valor 23';
COMMENT ON COLUMN fin_pagrec_prev_var.valor24 IS 'Valor 24';
COMMENT ON COLUMN fin_pagrec_prev_var.valor25 IS 'Valor 25';
COMMENT ON COLUMN fin_pagrec_prev_var.valor26 IS 'Valor 26';
COMMENT ON COLUMN fin_pagrec_prev_var.valor27 IS 'Valor 27';
COMMENT ON COLUMN fin_pagrec_prev_var.valor28 IS 'Valor 28';
COMMENT ON COLUMN fin_pagrec_prev_var.valor29 IS 'Valor 29';
COMMENT ON COLUMN fin_pagrec_prev_var.valor30 IS 'Valor 30';
COMMENT ON COLUMN fin_pagrec_prev_var.valor31 IS 'Valor 31';
COMMENT ON COLUMN fin_pagrec_prev_var.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_prev_var OWNER TO postgres;

CREATE TABLE fin_pagrec_prev_dest (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
fin_pagrec_prev_id varchar(36) NOT NULL,
ope_centro1_id_dest_pri varchar(36) NOT NULL,
ope_centro2_id_dest_pri varchar(36),
ope_centro1_id_dest_sec varchar(36),
ope_centro2_id_dest_sec varchar(36),
valor01 numeric(18,2) NOT NULL DEFAULT 0,
valor02 numeric(18,2) NOT NULL DEFAULT 0,
valor03 numeric(18,2) NOT NULL DEFAULT 0,
valor04 numeric(18,2) NOT NULL DEFAULT 0,
valor05 numeric(18,2) NOT NULL DEFAULT 0,
valor06 numeric(18,2) NOT NULL DEFAULT 0,
valor07 numeric(18,2) NOT NULL DEFAULT 0,
valor08 numeric(18,2) NOT NULL DEFAULT 0,
valor09 numeric(18,2) NOT NULL DEFAULT 0,
valor10 numeric(18,2) NOT NULL DEFAULT 0,
valor11 numeric(18,2) NOT NULL DEFAULT 0,
valor12 numeric(18,2) NOT NULL DEFAULT 0,
valor13 numeric(18,2) NOT NULL DEFAULT 0,
valor14 numeric(18,2) NOT NULL DEFAULT 0,
valor15 numeric(18,2) NOT NULL DEFAULT 0,
valor16 numeric(18,2) NOT NULL DEFAULT 0,
valor17 numeric(18,2) NOT NULL DEFAULT 0,
valor18 numeric(18,2) NOT NULL DEFAULT 0,
valor19 numeric(18,2) NOT NULL DEFAULT 0,
valor20 numeric(18,2) NOT NULL DEFAULT 0,
valor21 numeric(18,2) NOT NULL DEFAULT 0,
valor22 numeric(18,2) NOT NULL DEFAULT 0,
valor23 numeric(18,2) NOT NULL DEFAULT 0,
valor24 numeric(18,2) NOT NULL DEFAULT 0,
valor25 numeric(18,2) NOT NULL DEFAULT 0,
valor26 numeric(18,2) NOT NULL DEFAULT 0,
valor27 numeric(18,2) NOT NULL DEFAULT 0,
valor28 numeric(18,2) NOT NULL DEFAULT 0,
valor29 numeric(18,2) NOT NULL DEFAULT 0,
valor30 numeric(18,2) NOT NULL DEFAULT 0,
valor31 numeric(18,2) NOT NULL DEFAULT 0,
ope_atividade_id varchar(36) NOT NULL,
data_valid date,
CONSTRAINT pk_fin_pagrec_prev_dest PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE fin_pagrec_prev_dest IS 'Financeiro-Pag/Rec Previsto - Destinação';
COMMENT ON COLUMN fin_pagrec_prev_dest.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN fin_pagrec_prev_dest.id IS 'ID da Previsão Pag/Rec - Destinação';
COMMENT ON COLUMN fin_pagrec_prev_dest.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN fin_pagrec_prev_dest.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN fin_pagrec_prev_dest.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN fin_pagrec_prev_dest.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN fin_pagrec_prev_dest.fin_pagrec_prev_id IS 'ID da Previsão Pag/Rec';
COMMENT ON COLUMN fin_pagrec_prev_dest.ope_centro1_id_dest_pri IS 'ID do Centro Nível 1 Entrada/Saída - Destino Primário';
COMMENT ON COLUMN fin_pagrec_prev_dest.ope_centro2_id_dest_pri IS 'ID do Centro Nível 2 Entrada/Saída - Destino Primário';
COMMENT ON COLUMN fin_pagrec_prev_dest.ope_centro1_id_dest_sec IS 'ID do Centro Nível 1 Entrada/Saída - Destino Secundário';
COMMENT ON COLUMN fin_pagrec_prev_dest.ope_centro2_id_dest_sec IS 'ID do Centro Nível 2 Entrada/Saída - Destino Secundário';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor01 IS 'Valor 01';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor02 IS 'Valor 02';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor03 IS 'Valor 03';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor04 IS 'Valor 04';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor05 IS 'Valor 05';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor06 IS 'Valor 06';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor07 IS 'Valor 07';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor08 IS 'Valor 08';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor09 IS 'Valor 09';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor10 IS 'Valor 10';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor11 IS 'Valor 11';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor12 IS 'Valor 12';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor13 IS 'Valor 13';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor14 IS 'Valor 14';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor15 IS 'Valor 15';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor16 IS 'Valor 16';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor17 IS 'Valor 17';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor18 IS 'Valor 18';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor19 IS 'Valor 19';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor20 IS 'Valor 20';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor21 IS 'Valor 21';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor22 IS 'Valor 22';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor23 IS 'Valor 23';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor24 IS 'Valor 24';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor25 IS 'Valor 25';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor26 IS 'Valor 26';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor27 IS 'Valor 27';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor28 IS 'Valor 28';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor29 IS 'Valor 29';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor30 IS 'Valor 30';
COMMENT ON COLUMN fin_pagrec_prev_dest.valor31 IS 'Valor 31';
COMMENT ON COLUMN fin_pagrec_prev_dest.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN fin_pagrec_prev_dest.data_valid IS 'Data de Validação';
ALTER TABLE fin_pagrec_prev_dest OWNER TO postgres;

CREATE TABLE ope_centro_prev (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro_versao_id varchar(36) NOT NULL,
data_per date NOT NULL,
ger_empresa_id varchar(36) NOT NULL,
ope_atividade_id varchar(36) NOT NULL,
ope_periodo_id varchar(36) NOT NULL,
qnt01 numeric(18,2) NOT NULL DEFAULT 0,
qnt02 numeric(18,2) NOT NULL DEFAULT 0,
qnt03 numeric(18,2) NOT NULL DEFAULT 0,
qnt04 numeric(18,2) NOT NULL DEFAULT 0,
qnt05 numeric(18,2) NOT NULL DEFAULT 0,
qnt06 numeric(18,2) NOT NULL DEFAULT 0,
qnt07 numeric(18,2) NOT NULL DEFAULT 0,
qnt08 numeric(18,2) NOT NULL DEFAULT 0,
qnt09 numeric(18,2) NOT NULL DEFAULT 0,
qnt10 numeric(18,2) NOT NULL DEFAULT 0,
qnt11 numeric(18,2) NOT NULL DEFAULT 0,
qnt12 numeric(18,2) NOT NULL DEFAULT 0,
qnt13 numeric(18,2) NOT NULL DEFAULT 0,
qnt14 numeric(18,2) NOT NULL DEFAULT 0,
qnt15 numeric(18,2) NOT NULL DEFAULT 0,
qnt16 numeric(18,2) NOT NULL DEFAULT 0,
qnt17 numeric(18,2) NOT NULL DEFAULT 0,
qnt18 numeric(18,2) NOT NULL DEFAULT 0,
qnt19 numeric(18,2) NOT NULL DEFAULT 0,
qnt20 numeric(18,2) NOT NULL DEFAULT 0,
qnt21 numeric(18,2) NOT NULL DEFAULT 0,
qnt22 numeric(18,2) NOT NULL DEFAULT 0,
qnt23 numeric(18,2) NOT NULL DEFAULT 0,
qnt24 numeric(18,2) NOT NULL DEFAULT 0,
qnt25 numeric(18,2) NOT NULL DEFAULT 0,
qnt26 numeric(18,2) NOT NULL DEFAULT 0,
qnt27 numeric(18,2) NOT NULL DEFAULT 0,
qnt28 numeric(18,2) NOT NULL DEFAULT 0,
qnt29 numeric(18,2) NOT NULL DEFAULT 0,
qnt30 numeric(18,2) NOT NULL DEFAULT 0,
qnt31 numeric(18,2) NOT NULL DEFAULT 0,
process_id varchar(36),
ope_centro2_id varchar(36),
ope_centro2_ord_tipo_id varchar(36),
ordem_exec varchar(3),
tipo_executor varchar(1),
CONSTRAINT pk_ope_centro_prev PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_prev IS 'Operacional-Previsão por Atividade';
COMMENT ON COLUMN ope_centro_prev.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_prev.id IS 'ID da Previsão por Atividade';
COMMENT ON COLUMN ope_centro_prev.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_prev.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_prev.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_prev.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_prev.ope_centro_versao_id IS 'ID da Versão da Operação';
COMMENT ON COLUMN ope_centro_prev.data_per IS 'Data do Período';
COMMENT ON COLUMN ope_centro_prev.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_centro_prev.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN ope_centro_prev.ope_periodo_id IS 'ID do Período da Operação';
COMMENT ON COLUMN ope_centro_prev.qnt01 IS 'Quantidade 01';
COMMENT ON COLUMN ope_centro_prev.qnt02 IS 'Quantidade 02';
COMMENT ON COLUMN ope_centro_prev.qnt03 IS 'Quantidade 03';
COMMENT ON COLUMN ope_centro_prev.qnt04 IS 'Quantidade 04';
COMMENT ON COLUMN ope_centro_prev.qnt05 IS 'Quantidade 05';
COMMENT ON COLUMN ope_centro_prev.qnt06 IS 'Quantidade 06';
COMMENT ON COLUMN ope_centro_prev.qnt07 IS 'Quantidade 07';
COMMENT ON COLUMN ope_centro_prev.qnt08 IS 'Quantidade 08';
COMMENT ON COLUMN ope_centro_prev.qnt09 IS 'Quantidade 09';
COMMENT ON COLUMN ope_centro_prev.qnt10 IS 'Quantidade 10';
COMMENT ON COLUMN ope_centro_prev.qnt11 IS 'Quantidade 11';
COMMENT ON COLUMN ope_centro_prev.qnt12 IS 'Quantidade 12';
COMMENT ON COLUMN ope_centro_prev.qnt13 IS 'Quantidade 13';
COMMENT ON COLUMN ope_centro_prev.qnt14 IS 'Quantidade 14';
COMMENT ON COLUMN ope_centro_prev.qnt15 IS 'Quantidade 15';
COMMENT ON COLUMN ope_centro_prev.qnt16 IS 'Quantidade 16';
COMMENT ON COLUMN ope_centro_prev.qnt17 IS 'Quantidade 17';
COMMENT ON COLUMN ope_centro_prev.qnt18 IS 'Quantidade 18';
COMMENT ON COLUMN ope_centro_prev.qnt19 IS 'Quantidade 19';
COMMENT ON COLUMN ope_centro_prev.qnt20 IS 'Quantidade 20';
COMMENT ON COLUMN ope_centro_prev.qnt21 IS 'Quantidade 21';
COMMENT ON COLUMN ope_centro_prev.qnt22 IS 'Quantidade 22';
COMMENT ON COLUMN ope_centro_prev.qnt23 IS 'Quantidade 23';
COMMENT ON COLUMN ope_centro_prev.qnt24 IS 'Quantidade 24';
COMMENT ON COLUMN ope_centro_prev.qnt25 IS 'Quantidade 25';
COMMENT ON COLUMN ope_centro_prev.qnt26 IS 'Quantidade 26';
COMMENT ON COLUMN ope_centro_prev.qnt27 IS 'Quantidade 27';
COMMENT ON COLUMN ope_centro_prev.qnt28 IS 'Quantidade 28';
COMMENT ON COLUMN ope_centro_prev.qnt29 IS 'Quantidade 29';
COMMENT ON COLUMN ope_centro_prev.qnt30 IS 'Quantidade 30';
COMMENT ON COLUMN ope_centro_prev.qnt31 IS 'Quantidade 31';
COMMENT ON COLUMN ope_centro_prev.process_id IS 'ID do Processo';
COMMENT ON COLUMN ope_centro_prev.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro_prev.ope_centro2_ord_tipo_id IS 'ID do Tipo da Ordem';
COMMENT ON COLUMN ope_centro_prev.ordem_exec IS 'Ordem Execução';
COMMENT ON COLUMN ope_centro_prev.tipo_executor IS 'Tipo Executor: P-Próprio / T-Terceiro';
ALTER TABLE ope_centro_prev OWNER TO postgres;

CREATE TABLE ope_centro_prev_dest (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_centro_prev_id varchar(36) NOT NULL,
tipo_prev varchar(1) NOT NULL,
ope_centro1_id varchar(36) NOT NULL,
ope_centro2_id varchar(36),
ger_itemserv_id varchar(36),
ctb_comp_id varchar(36) NOT NULL,
qnt01 numeric(18,2) NOT NULL DEFAULT 0,
qnt02 numeric(18,2) NOT NULL DEFAULT 0,
qnt03 numeric(18,2) NOT NULL DEFAULT 0,
qnt04 numeric(18,2) NOT NULL DEFAULT 0,
qnt05 numeric(18,2) NOT NULL DEFAULT 0,
qnt06 numeric(18,2) NOT NULL DEFAULT 0,
qnt07 numeric(18,2) NOT NULL DEFAULT 0,
qnt08 numeric(18,2) NOT NULL DEFAULT 0,
qnt09 numeric(18,2) NOT NULL DEFAULT 0,
qnt10 numeric(18,2) NOT NULL DEFAULT 0,
qnt11 numeric(18,2) NOT NULL DEFAULT 0,
qnt12 numeric(18,2) NOT NULL DEFAULT 0,
qnt13 numeric(18,2) NOT NULL DEFAULT 0,
qnt14 numeric(18,2) NOT NULL DEFAULT 0,
qnt15 numeric(18,2) NOT NULL DEFAULT 0,
qnt16 numeric(18,2) NOT NULL DEFAULT 0,
qnt17 numeric(18,2) NOT NULL DEFAULT 0,
qnt18 numeric(18,2) NOT NULL DEFAULT 0,
qnt19 numeric(18,2) NOT NULL DEFAULT 0,
qnt20 numeric(18,2) NOT NULL DEFAULT 0,
qnt21 numeric(18,2) NOT NULL DEFAULT 0,
qnt22 numeric(18,2) NOT NULL DEFAULT 0,
qnt23 numeric(18,2) NOT NULL DEFAULT 0,
qnt24 numeric(18,2) NOT NULL DEFAULT 0,
qnt25 numeric(18,2) NOT NULL DEFAULT 0,
qnt26 numeric(18,2) NOT NULL DEFAULT 0,
qnt27 numeric(18,2) NOT NULL DEFAULT 0,
qnt28 numeric(18,2) NOT NULL DEFAULT 0,
qnt29 numeric(18,2) NOT NULL DEFAULT 0,
qnt30 numeric(18,2) NOT NULL DEFAULT 0,
qnt31 numeric(18,2) NOT NULL DEFAULT 0,
process_id varchar(36),
CONSTRAINT pk_ope_centro_prev_dest PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_prev_dest IS 'Operacional-Previsão por Atividade - Destinação';
COMMENT ON COLUMN ope_centro_prev_dest.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_prev_dest.id IS 'ID da Previsão por Atividade - Destinação';
COMMENT ON COLUMN ope_centro_prev_dest.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_prev_dest.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_prev_dest.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_prev_dest.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_prev_dest.ope_centro_prev_id IS 'ID da Previsão por Atividade';
COMMENT ON COLUMN ope_centro_prev_dest.tipo_prev IS 'Tipo Previsão: 1-Produção, 2-Equipamentos, 3-Pessoa, 4-Item/Serviço';
COMMENT ON COLUMN ope_centro_prev_dest.ope_centro1_id IS 'ID do Centro Nível 1 Entrada/Saída';
COMMENT ON COLUMN ope_centro_prev_dest.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro_prev_dest.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ope_centro_prev_dest.ctb_comp_id IS 'ID do Componente Contábil';
COMMENT ON COLUMN ope_centro_prev_dest.qnt01 IS 'Quantidade 01';
COMMENT ON COLUMN ope_centro_prev_dest.qnt02 IS 'Quantidade 02';
COMMENT ON COLUMN ope_centro_prev_dest.qnt03 IS 'Quantidade 03';
COMMENT ON COLUMN ope_centro_prev_dest.qnt04 IS 'Quantidade 04';
COMMENT ON COLUMN ope_centro_prev_dest.qnt05 IS 'Quantidade 05';
COMMENT ON COLUMN ope_centro_prev_dest.qnt06 IS 'Quantidade 06';
COMMENT ON COLUMN ope_centro_prev_dest.qnt07 IS 'Quantidade 07';
COMMENT ON COLUMN ope_centro_prev_dest.qnt08 IS 'Quantidade 08';
COMMENT ON COLUMN ope_centro_prev_dest.qnt09 IS 'Quantidade 09';
COMMENT ON COLUMN ope_centro_prev_dest.qnt10 IS 'Quantidade 10';
COMMENT ON COLUMN ope_centro_prev_dest.qnt11 IS 'Quantidade 11';
COMMENT ON COLUMN ope_centro_prev_dest.qnt12 IS 'Quantidade 12';
COMMENT ON COLUMN ope_centro_prev_dest.qnt13 IS 'Quantidade 13';
COMMENT ON COLUMN ope_centro_prev_dest.qnt14 IS 'Quantidade 14';
COMMENT ON COLUMN ope_centro_prev_dest.qnt15 IS 'Quantidade 15';
COMMENT ON COLUMN ope_centro_prev_dest.qnt16 IS 'Quantidade 16';
COMMENT ON COLUMN ope_centro_prev_dest.qnt17 IS 'Quantidade 17';
COMMENT ON COLUMN ope_centro_prev_dest.qnt18 IS 'Quantidade 18';
COMMENT ON COLUMN ope_centro_prev_dest.qnt19 IS 'Quantidade 19';
COMMENT ON COLUMN ope_centro_prev_dest.qnt20 IS 'Quantidade 20';
COMMENT ON COLUMN ope_centro_prev_dest.qnt21 IS 'Quantidade 21';
COMMENT ON COLUMN ope_centro_prev_dest.qnt22 IS 'Quantidade 22';
COMMENT ON COLUMN ope_centro_prev_dest.qnt23 IS 'Quantidade 23';
COMMENT ON COLUMN ope_centro_prev_dest.qnt24 IS 'Quantidade 24';
COMMENT ON COLUMN ope_centro_prev_dest.qnt25 IS 'Quantidade 25';
COMMENT ON COLUMN ope_centro_prev_dest.qnt26 IS 'Quantidade 26';
COMMENT ON COLUMN ope_centro_prev_dest.qnt27 IS 'Quantidade 27';
COMMENT ON COLUMN ope_centro_prev_dest.qnt28 IS 'Quantidade 28';
COMMENT ON COLUMN ope_centro_prev_dest.qnt29 IS 'Quantidade 29';
COMMENT ON COLUMN ope_centro_prev_dest.qnt30 IS 'Quantidade 30';
COMMENT ON COLUMN ope_centro_prev_dest.qnt31 IS 'Quantidade 31';
COMMENT ON COLUMN ope_centro_prev_dest.process_id IS 'ID do Processo';
ALTER TABLE ope_centro_prev_dest OWNER TO postgres;

CREATE TABLE ope_atividade_relac_prod (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ope_atividade_id varchar(36) NOT NULL,
ope_atividade_id_prod varchar(36) NOT NULL,
ordem_visual varchar(1) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_atividade_prod PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_atividade_relac_prod IS 'Operação-Relacionamento de Atividade Produtivas';
COMMENT ON COLUMN ope_atividade_relac_prod.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_atividade_relac_prod.id IS 'ID do Relac. de Atividade Produtivas';
COMMENT ON COLUMN ope_atividade_relac_prod.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN ope_atividade_relac_prod.ope_atividade_id_prod IS 'ID da Atividade de Produção';
COMMENT ON COLUMN ope_atividade_relac_prod.ordem_visual IS 'Ordem Visualização: 1,2,3';
COMMENT ON COLUMN ope_atividade_relac_prod.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_atividade_relac_prod.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_atividade_relac_prod.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_atividade_relac_prod.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_atividade_relac_prod OWNER TO postgres;

CREATE TABLE ctb_versao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_versao varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_rp varchar(1) NOT NULL,
versao_atual varchar NOT NULL DEFAULT 'N',
data_per_ini date NOT NULL,
data_per_fin date NOT NULL,
CONSTRAINT pk_ctb_versao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ctb_versao IS 'Contábil-Versão Contábil / Previsão';
COMMENT ON COLUMN ctb_versao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ctb_versao.id IS 'ID da Versão Contábil / Previsão';
COMMENT ON COLUMN ctb_versao.nome IS 'Nome';
COMMENT ON COLUMN ctb_versao.ativo IS 'Ativo';
COMMENT ON COLUMN ctb_versao.sigla_versao IS 'Sigla do Versão Conta Contábil';
COMMENT ON COLUMN ctb_versao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ctb_versao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ctb_versao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ctb_versao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ctb_versao.tipo_rp IS 'Tipo: R-Real, P-Previsto';
COMMENT ON COLUMN ctb_versao.versao_atual IS 'Versão Atual';
COMMENT ON COLUMN ctb_versao.data_per_ini IS 'Data Período Inicial';
COMMENT ON COLUMN ctb_versao.data_per_fin IS 'Data Período Final';
ALTER TABLE ctb_versao OWNER TO postgres;

CREATE TABLE crm_class_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_class_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_crm_class_gupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_class_grupo IS 'Atendimento-Grupo de Classificação';
COMMENT ON COLUMN crm_class_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_class_grupo.id IS 'ID do Grupo de Classificação';
COMMENT ON COLUMN crm_class_grupo.nome IS 'Nome';
COMMENT ON COLUMN crm_class_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN crm_class_grupo.sigla_class_grupo IS 'Sigla do Grupo de Classificação';
COMMENT ON COLUMN crm_class_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_class_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_class_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_class_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE crm_class_grupo OWNER TO postgres;

CREATE TABLE crm_class_subgrupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_class_subgrupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_class_grupo_id varchar(36) NOT NULL,
CONSTRAINT pk_crm_class_subgupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_class_subgrupo IS 'Atendimento-Sub-Grupo de Classificação';
COMMENT ON COLUMN crm_class_subgrupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_class_subgrupo.id IS 'ID do Sub-Grupo de Classificação';
COMMENT ON COLUMN crm_class_subgrupo.nome IS 'Nome';
COMMENT ON COLUMN crm_class_subgrupo.ativo IS 'Ativo';
COMMENT ON COLUMN crm_class_subgrupo.sigla_class_subgrupo IS 'Sigla do Sub-Grupo de Classificação';
COMMENT ON COLUMN crm_class_subgrupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_class_subgrupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_class_subgrupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_class_subgrupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_class_subgrupo.crm_class_grupo_id IS 'ID do Grupo de Classificação';
ALTER TABLE crm_class_subgrupo OWNER TO postgres;

CREATE TABLE crm_class (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_class varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_class_subgrupo_id varchar(36) NOT NULL,
CONSTRAINT pk_crm_class PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_class IS 'Atendimento-Classificação';
COMMENT ON COLUMN crm_class.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_class.id IS 'ID da Classificação';
COMMENT ON COLUMN crm_class.nome IS 'Nome';
COMMENT ON COLUMN crm_class.ativo IS 'Ativo';
COMMENT ON COLUMN crm_class.sigla_class IS 'Sigla da Classificação';
COMMENT ON COLUMN crm_class.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_class.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_class.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_class.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_class.crm_class_subgrupo_id IS 'ID do Sub-Grupo de Classificação';
ALTER TABLE crm_class OWNER TO postgres;

CREATE TABLE crm_org (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_org varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ger_visual_user varchar(1) NOT NULL DEFAULT 'S',
user_visual_user varchar(1) NOT NULL DEFAULT 'N',
CONSTRAINT pk_crm_org PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_org IS 'Atendimento-Organização';
COMMENT ON COLUMN crm_org.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_org.id IS 'ID da Organização';
COMMENT ON COLUMN crm_org.nome IS 'Nome';
COMMENT ON COLUMN crm_org.ativo IS 'Ativo';
COMMENT ON COLUMN crm_org.sigla_org IS 'Sigla da Organização';
COMMENT ON COLUMN crm_org.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_org.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_org.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_org.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_org.ger_visual_user IS 'Gerente visualiza atendimento de outros usuários';
COMMENT ON COLUMN crm_org.user_visual_user IS 'Usuário visualiza atendimento de outros usuários';
ALTER TABLE crm_org OWNER TO postgres;

CREATE TABLE crm_resposta (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
descritivo text NOT NULL,
ativo varchar(1) NOT NULL,
sigla_resposta varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_crm_resposta PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_resposta IS 'Atendimento-Resposta';
COMMENT ON COLUMN crm_resposta.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_resposta.id IS 'ID da Resposta';
COMMENT ON COLUMN crm_resposta.descritivo IS 'descritivo';
COMMENT ON COLUMN crm_resposta.ativo IS 'Ativo';
COMMENT ON COLUMN crm_resposta.sigla_resposta IS 'Sigla da Resposta';
COMMENT ON COLUMN crm_resposta.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_resposta.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_resposta.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_resposta.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE crm_resposta OWNER TO postgres;

CREATE TABLE crm_status (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_status varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_status varchar(2) NOT NULL,
obrig_motivo varchar(1) NOT NULL,
CONSTRAINT pk_crm_status PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_status IS 'Atendimento-Status';
COMMENT ON COLUMN crm_status.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_status.id IS 'ID do Status';
COMMENT ON COLUMN crm_status.nome IS 'Nome';
COMMENT ON COLUMN crm_status.ativo IS 'Ativo';
COMMENT ON COLUMN crm_status.sigla_status IS 'Sigla do Status';
COMMENT ON COLUMN crm_status.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_status.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_status.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_status.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_status.tipo_status IS 'Tipo Status: AB-Aberto, PE-Pendente, AI-Andamento, AT-Andamento Transf., FN-Finalizado, CA-Cancelado';
COMMENT ON COLUMN crm_status.obrig_motivo IS 'Obriga Motivo: S-Sim, N-Não';
ALTER TABLE crm_status OWNER TO postgres;

CREATE TABLE crm_prioridade (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_prioridade varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_crm_prioridade PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_prioridade IS 'Atendimento-Prioridade';
COMMENT ON COLUMN crm_prioridade.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_prioridade.id IS 'ID da Prioridade';
COMMENT ON COLUMN crm_prioridade.nome IS 'Nome';
COMMENT ON COLUMN crm_prioridade.ativo IS 'Ativo';
COMMENT ON COLUMN crm_prioridade.sigla_prioridade IS 'Sigla do Grupo de Classificação';
COMMENT ON COLUMN crm_prioridade.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_prioridade.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_prioridade.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_prioridade.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE crm_prioridade OWNER TO postgres;

CREATE TABLE crm_aviso (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
descritivo text NOT NULL,
ativo varchar(1) NOT NULL,
sigla_aviso varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_crm_aviso PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_aviso IS 'Atendimento-Avisos';
COMMENT ON COLUMN crm_aviso.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_aviso.id IS 'ID do Aviso';
COMMENT ON COLUMN crm_aviso.descritivo IS 'descritivo';
COMMENT ON COLUMN crm_aviso.ativo IS 'Ativo';
COMMENT ON COLUMN crm_aviso.sigla_aviso IS 'Sigla do Aviso';
COMMENT ON COLUMN crm_aviso.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_aviso.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_aviso.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_aviso.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE crm_aviso OWNER TO postgres;

CREATE TABLE crm_etapa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_etapa varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_crm_etapa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_etapa IS 'Atendimento-Etapa';
COMMENT ON COLUMN crm_etapa.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_etapa.id IS 'ID da Etapa';
COMMENT ON COLUMN crm_etapa.nome IS 'Nome';
COMMENT ON COLUMN crm_etapa.ativo IS 'Ativo';
COMMENT ON COLUMN crm_etapa.sigla_etapa IS 'Sigla da Etapa';
COMMENT ON COLUMN crm_etapa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_etapa.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_etapa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_etapa.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE crm_etapa OWNER TO postgres;

CREATE TABLE crm_aviso_org (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_aviso_id varchar(36) NOT NULL,
crm_org_id varchar(36) NOT NULL,
CONSTRAINT pk_crm_aviso_org PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_aviso_org IS 'Atendimento-Avisos x Organização';
COMMENT ON COLUMN crm_aviso_org.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_aviso_org.id IS 'ID do Aviso x Organização';
COMMENT ON COLUMN crm_aviso_org.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_aviso_org.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_aviso_org.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_aviso_org.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_aviso_org.crm_aviso_id IS 'ID do Aviso';
COMMENT ON COLUMN crm_aviso_org.crm_org_id IS 'ID da Organização';
ALTER TABLE crm_aviso_org OWNER TO postgres;

CREATE TABLE crm_status_prox (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_status_id varchar(36) NOT NULL,
crm_status_id_prox varchar(36) NOT NULL,
ordem int2 NOT NULL DEFAULT 0,
tipo_status_ant varchar(2),
CONSTRAINT pk_crm_status_prox PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_status_prox IS 'Atendimento-Próximo Status';
COMMENT ON COLUMN crm_status_prox.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_status_prox.id IS 'ID do Próximo Status';
COMMENT ON COLUMN crm_status_prox.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_status_prox.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_status_prox.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_status_prox.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_status_prox.crm_status_id IS 'ID do Status';
COMMENT ON COLUMN crm_status_prox.crm_status_id_prox IS 'ID do Status - Próximo';
COMMENT ON COLUMN crm_status_prox.ordem IS 'Ordem';
COMMENT ON COLUMN crm_status_prox.tipo_status_ant IS 'Tipo Status Anterior';
ALTER TABLE crm_status_prox OWNER TO postgres;

CREATE TABLE crm_etapa_prox (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_etapa_id varchar(36) NOT NULL,
crm_etapa_id_prox varchar(36) NOT NULL,
ordem int2 NOT NULL DEFAULT 0,
CONSTRAINT pk_crm_etapa_prox PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_etapa_prox IS 'Atendimento-Próximo Etapa';
COMMENT ON COLUMN crm_etapa_prox.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_etapa_prox.id IS 'ID do Próximo Etapa';
COMMENT ON COLUMN crm_etapa_prox.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_etapa_prox.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_etapa_prox.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_etapa_prox.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_etapa_prox.crm_etapa_id IS 'ID da Etapa';
COMMENT ON COLUMN crm_etapa_prox.crm_etapa_id_prox IS 'ID da Etapa - Próximo';
COMMENT ON COLUMN crm_etapa_prox.ordem IS 'Ordem';
ALTER TABLE crm_etapa_prox OWNER TO postgres;

CREATE TABLE crm_mov (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_etapa_id varchar(36) NOT NULL,
numero varchar(10) NOT NULL,
data_mov date NOT NULL DEFAULT now(),
envia_email_ext varchar(1) NOT NULL DEFAULT 'S',
descritivo_ext text NOT NULL,
descritivo_int text,
crm_status_id varchar(36) NOT NULL,
data_status date NOT NULL DEFAULT now(),
crm_prioridade_id varchar(36) NOT NULL,
system_user_id_solic varchar(36) NOT NULL,
system_user_id_atend_atu varchar(36),
system_user_id_atend_ant varchar(36),
CONSTRAINT pk_crm_mov PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_mov IS 'Atendimento-Movimento';
COMMENT ON COLUMN crm_mov.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_mov.id IS 'ID do Movimento';
COMMENT ON COLUMN crm_mov.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_mov.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_mov.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_mov.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_mov.crm_etapa_id IS 'ID da Etapa';
COMMENT ON COLUMN crm_mov.numero IS 'Número';
COMMENT ON COLUMN crm_mov.data_mov IS 'Data do Movimento';
COMMENT ON COLUMN crm_mov.envia_email_ext IS 'Envia Email Externo';
COMMENT ON COLUMN crm_mov.descritivo_ext IS 'Descritivo Externo';
COMMENT ON COLUMN crm_mov.descritivo_int IS 'Descritivo Interno';
COMMENT ON COLUMN crm_mov.crm_status_id IS 'ID do Status';
COMMENT ON COLUMN crm_mov.data_status IS 'Data do Status';
COMMENT ON COLUMN crm_mov.crm_prioridade_id IS 'ID da Prioridade';
COMMENT ON COLUMN crm_mov.system_user_id_solic IS 'ID do Usuário Solicitante';
COMMENT ON COLUMN crm_mov.system_user_id_atend_atu IS 'ID do Usuário Atendente Atual';
COMMENT ON COLUMN crm_mov.system_user_id_atend_ant IS 'ID do Usuário Atendente Anterior';
ALTER TABLE crm_mov OWNER TO postgres;

CREATE TABLE crm_mov_hist (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_mov_id varchar(36) NOT NULL,
data_hist date NOT NULL,
descritivo text NOT NULL,
visual_ext varchar(1) NOT NULL DEFAULT 'N',
envia_email_ext varchar(1) NOT NULL,
system_user_id_hist varchar(36) NOT NULL,
CONSTRAINT pk_crm_mov_hist PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_mov_hist IS 'Atendimento-Histórico do Movimento';
COMMENT ON COLUMN crm_mov_hist.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_mov_hist.id IS 'ID do Histórico do Movimento';
COMMENT ON COLUMN crm_mov_hist.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_mov_hist.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_mov_hist.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_mov_hist.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_mov_hist.crm_mov_id IS 'ID da Movimento';
COMMENT ON COLUMN crm_mov_hist.data_hist IS 'Data do Histórico';
COMMENT ON COLUMN crm_mov_hist.descritivo IS 'Descritivo';
COMMENT ON COLUMN crm_mov_hist.visual_ext IS 'Visualização Externa';
COMMENT ON COLUMN crm_mov_hist.envia_email_ext IS 'Envia Email Externo';
COMMENT ON COLUMN crm_mov_hist.system_user_id_hist IS 'ID do Usuário do Histórico';
ALTER TABLE crm_mov_hist OWNER TO postgres;

CREATE TABLE crm_mov_anexo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
crm_mov_id varchar(36) NOT NULL,
data_anexo date NOT NULL,
descritivo text NOT NULL,
visual_ext varchar(1) NOT NULL DEFAULT 'N',
envia_email_ext varchar(1) NOT NULL,
system_user_id_anexo varchar(36) NOT NULL,
nome_arq_anexo varchar(100) NOT NULL,
CONSTRAINT pk_crm_mov_anexo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_mov_anexo IS 'Atendimento-Anexos do Movimento';
COMMENT ON COLUMN crm_mov_anexo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_mov_anexo.id IS 'ID do Anexo do Movimento';
COMMENT ON COLUMN crm_mov_anexo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_mov_anexo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_mov_anexo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_mov_anexo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_mov_anexo.crm_mov_id IS 'ID da Movimento';
COMMENT ON COLUMN crm_mov_anexo.data_anexo IS 'Data do Anexo';
COMMENT ON COLUMN crm_mov_anexo.descritivo IS 'Descritivo';
COMMENT ON COLUMN crm_mov_anexo.visual_ext IS 'Visualização Externa';
COMMENT ON COLUMN crm_mov_anexo.envia_email_ext IS 'Envia Email Externo';
COMMENT ON COLUMN crm_mov_anexo.system_user_id_anexo IS 'ID do Usuário do Anexo';
COMMENT ON COLUMN crm_mov_anexo.nome_arq_anexo IS 'Nome Arquivo Anexo';
ALTER TABLE crm_mov_anexo OWNER TO postgres;

CREATE TABLE system_access_log (
id varchar(36) NOT NULL,
sessionid text ,
login text ,
login_time timestamp(6),
login_year varchar(4) ,
login_month varchar(2) ,
login_day varchar(2) ,
logout_time timestamp(6),
impersonated char(1) ,
access_ip varchar(45) ,
CONSTRAINT pk_system_access_log PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_access_log IS 'System-Log de Acesso';
COMMENT ON COLUMN system_access_log.id IS 'ID do Log da Sessão';
COMMENT ON COLUMN system_access_log.sessionid IS 'ID da Sessão';
COMMENT ON COLUMN system_access_log.login IS 'Login';
COMMENT ON COLUMN system_access_log.login_time IS 'Hora de Login';
COMMENT ON COLUMN system_access_log.login_year IS 'Ano de Login';
COMMENT ON COLUMN system_access_log.login_month IS 'Mês de Login';
COMMENT ON COLUMN system_access_log.login_day IS 'Dia de Login';
COMMENT ON COLUMN system_access_log.logout_time IS 'Hora Logout';
COMMENT ON COLUMN system_access_log.impersonated IS 'Personificado';
COMMENT ON COLUMN system_access_log.access_ip IS 'IP de Acesso';
ALTER TABLE system_access_log OWNER TO postgres;

CREATE TABLE system_change_log (
id varchar(36) NOT NULL,
logdate timestamp(6),
login text ,
tablename text ,
primarykey text ,
pkvalue text ,
operation text ,
columnname text ,
oldvalue text ,
newvalue text ,
access_ip text ,
transaction_id text ,
log_trace text ,
session_id text ,
class_name text ,
php_sapi text ,
log_year varchar(4) ,
log_month varchar(2) ,
log_day varchar(2) ,
CONSTRAINT pk_system_change_log PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_change_log IS 'System-Log de Alterações';
COMMENT ON COLUMN system_change_log.id IS 'ID do Log de Alterações';
COMMENT ON COLUMN system_change_log.logdate IS 'Data do Log';
COMMENT ON COLUMN system_change_log.login IS 'Login';
COMMENT ON COLUMN system_change_log.tablename IS 'Nome da Tabela';
COMMENT ON COLUMN system_change_log.primarykey IS 'Chave Primária';
COMMENT ON COLUMN system_change_log.pkvalue IS 'Valor da Chave';
COMMENT ON COLUMN system_change_log.operation IS 'Operação';
COMMENT ON COLUMN system_change_log.columnname IS 'Nome da Coluna';
COMMENT ON COLUMN system_change_log.oldvalue IS 'Valor Antigo';
COMMENT ON COLUMN system_change_log.newvalue IS 'Valor Novo';
COMMENT ON COLUMN system_change_log.access_ip IS 'IP do Acesso';
COMMENT ON COLUMN system_change_log.transaction_id IS 'ID da Transação';
COMMENT ON COLUMN system_change_log.log_trace IS 'Log do Trace';
COMMENT ON COLUMN system_change_log.session_id IS 'ID da Sessão';
COMMENT ON COLUMN system_change_log.class_name IS 'Nome da Classe';
COMMENT ON COLUMN system_change_log.php_sapi IS 'PHP Sapi';
COMMENT ON COLUMN system_change_log.log_year IS 'Ano do Log';
COMMENT ON COLUMN system_change_log.log_month IS 'Mês do Log';
COMMENT ON COLUMN system_change_log.log_day IS 'Dia do Log';
ALTER TABLE system_change_log OWNER TO postgres;

CREATE TABLE system_document (
id varchar(36) NOT NULL,
system_user_id varchar(36),
title text ,
description text ,
category_id varchar(36),
submission_date date,
archive_date date,
filename text ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_document PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_document IS 'System-Documento';
COMMENT ON COLUMN system_document.id IS 'ID do Documento';
COMMENT ON COLUMN system_document.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_document.title IS 'Titulo';
COMMENT ON COLUMN system_document.description IS 'Descrição';
COMMENT ON COLUMN system_document.category_id IS 'ID da Categoria';
COMMENT ON COLUMN system_document.submission_date IS 'Data de Submissão';
COMMENT ON COLUMN system_document.archive_date IS 'Data de Arquivo';
COMMENT ON COLUMN system_document.filename IS 'Nome do Arquivo';
COMMENT ON COLUMN system_document.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_document.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_document.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_document.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_document OWNER TO postgres;

CREATE TABLE system_document_category (
id varchar(36) NOT NULL,
name text ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_document_category PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_document_category IS 'System-Categoria Documento';
COMMENT ON COLUMN system_document_category.id IS 'ID da Categoria Documento';
COMMENT ON COLUMN system_document_category.name IS 'Nome';
COMMENT ON COLUMN system_document_category.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_document_category.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_document_category.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_document_category.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_document_category OWNER TO postgres;

CREATE TABLE system_document_group (
id varchar(36) NOT NULL,
document_id varchar(36),
system_group_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_document_group PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_document_group IS 'System-Documento  x Grupo';
COMMENT ON COLUMN system_document_group.id IS 'ID do Documento  x Grupo';
COMMENT ON COLUMN system_document_group.document_id IS 'ID do Documento';
COMMENT ON COLUMN system_document_group.system_group_id IS 'ID do Grupo de Acesso';
COMMENT ON COLUMN system_document_group.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_document_group.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_document_group.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_document_group.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_document_group OWNER TO postgres;

CREATE TABLE system_document_user (
id varchar(36) NOT NULL,
document_id varchar(36),
system_user_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_document_user PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_document_user IS 'System-Documento x Usuário';
COMMENT ON COLUMN system_document_user.id IS 'ID do Documento x Usuário';
COMMENT ON COLUMN system_document_user.document_id IS 'ID do Documento';
COMMENT ON COLUMN system_document_user.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_document_user.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_document_user.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_document_user.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_document_user.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_document_user OWNER TO postgres;

CREATE TABLE system_group (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
name varchar(100) ,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_group PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_group IS 'System-Grupo de Acesso';
COMMENT ON COLUMN system_group.id IS 'ID do Grupo';
COMMENT ON COLUMN system_group.name IS 'Nome';
COMMENT ON COLUMN system_group.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_group.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_group.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_group.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_group OWNER TO postgres;

CREATE TABLE system_group_program (
id varchar(36) NOT NULL,
system_group_id varchar(36),
system_program_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT system_group_program_pkey PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_system_group_program_group ON system_group_program USING btree (system_group_id ASC NULLS LAST);
CREATE INDEX idx_system_group_program_program ON system_group_program USING btree (system_program_id ASC NULLS LAST);
COMMENT ON TABLE system_group_program IS 'System-Grupo de Acesso x Programa';
COMMENT ON COLUMN system_group_program.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_group_program.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_group_program.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_group_program.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_group_program OWNER TO postgres;

CREATE TABLE system_message (
id varchar(36) NOT NULL,
system_user_id varchar(36),
system_user_to_id varchar(36),
subject text ,
message text ,
dt_message text ,
checked char(1) ,
CONSTRAINT pk_system_message PRIMARY KEY (id) 
)
WITHOUT OIDS;
ALTER TABLE system_message OWNER TO postgres;

CREATE TABLE system_preference (
id varchar(100)  NOT NULL,
value text ,
CONSTRAINT pk_system_preference PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_preference IS 'System-Preferências Globais';
COMMENT ON COLUMN system_preference.id IS 'ID da Preferencia';
COMMENT ON COLUMN system_preference.value IS 'Valor';
ALTER TABLE system_preference OWNER TO postgres;

CREATE TABLE system_program (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
name varchar(100)  NOT NULL,
controller varchar(100)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
menu varchar(1) NOT NULL,
type_program varchar(1) NOT NULL,
module_id varchar(36) NOT NULL,
icon varchar(50),
admin varchar(1) NOT NULL,
CONSTRAINT pk_system_program PRIMARY KEY (id) ,
CONSTRAINT unq_system_param UNIQUE (controller)
)
WITHOUT OIDS;
COMMENT ON TABLE system_program IS 'System-Programa';
COMMENT ON COLUMN system_program.id IS 'ID do Programa';
COMMENT ON COLUMN system_program.name IS 'Nome';
COMMENT ON COLUMN system_program.controller IS 'Controller';
COMMENT ON COLUMN system_program.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_program.log_date_ins IS 'Data de Inserção';
COMMENT ON COLUMN system_program.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_program.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_program.menu IS 'Exbir no Menu: S-Sim, N-Não';
COMMENT ON COLUMN system_program.type_program IS 'Tipo: T-Tabelas, L-Lançamento, P-Processamento, U-Utilitário';
COMMENT ON COLUMN system_program.module_id IS 'ID do Modulo';
COMMENT ON COLUMN system_program.icon IS 'Icone do Programa';
COMMENT ON COLUMN system_program.admin IS 'Acesso Administrador: S-Sim,N-Não';
ALTER TABLE system_program OWNER TO postgres;

CREATE TABLE system_request_log (
id varchar(36) NOT NULL,
endpoint text ,
logdate text ,
log_year varchar(4) ,
log_month varchar(2) ,
log_day varchar(2) ,
session_id text ,
login text ,
access_ip text ,
class_name text ,
http_host text ,
server_port text ,
request_uri text ,
request_method text ,
query_string text ,
request_headers text ,
request_body text ,
request_duration int4,
CONSTRAINT pk_system_request_log PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_request_log IS 'System-Log de Request';
COMMENT ON COLUMN system_request_log.id IS 'ID do Log de Request';
COMMENT ON COLUMN system_request_log.endpoint IS 'EndPoint';
COMMENT ON COLUMN system_request_log.logdate IS 'Data do Log';
COMMENT ON COLUMN system_request_log.log_year IS 'Ano do Log';
COMMENT ON COLUMN system_request_log.log_month IS 'Mês do Log';
COMMENT ON COLUMN system_request_log.log_day IS 'Dia do Log';
COMMENT ON COLUMN system_request_log.session_id IS 'ID da Sessão';
COMMENT ON COLUMN system_request_log.login IS 'Login';
COMMENT ON COLUMN system_request_log.access_ip IS 'IP de Acesso';
COMMENT ON COLUMN system_request_log.class_name IS 'Nome da Classa';
COMMENT ON COLUMN system_request_log.http_host IS 'Http Host';
COMMENT ON COLUMN system_request_log.server_port IS 'Porta do Servidor';
COMMENT ON COLUMN system_request_log.request_uri IS 'URI da Request';
COMMENT ON COLUMN system_request_log.request_method IS 'Metodo da Request';
COMMENT ON COLUMN system_request_log.query_string IS 'Query';
COMMENT ON COLUMN system_request_log.request_headers IS 'Cabeçalho da Request';
COMMENT ON COLUMN system_request_log.request_body IS 'Corpo da Request';
COMMENT ON COLUMN system_request_log.request_duration IS 'Tempo da Request';
ALTER TABLE system_request_log OWNER TO postgres;

CREATE TABLE system_sql_log (
id varchar(36) NOT NULL,
logdate timestamp(6),
login text ,
database_name text ,
sql_command text ,
statement_type text ,
access_ip varchar(45) ,
transaction_id text ,
log_trace text ,
session_id text ,
class_name text ,
php_sapi text ,
request_id text ,
log_year varchar(4) ,
log_month varchar(2) ,
log_day varchar(2) ,
CONSTRAINT pk_system_sql_log PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_sql_log IS 'System-Log de SQL';
COMMENT ON COLUMN system_sql_log.id IS 'ID do Log de SQL';
COMMENT ON COLUMN system_sql_log.logdate IS 'Data do Log';
COMMENT ON COLUMN system_sql_log.login IS 'Login';
COMMENT ON COLUMN system_sql_log.database_name IS 'Nome do Banco de Dados';
COMMENT ON COLUMN system_sql_log.sql_command IS 'Comando SQL';
COMMENT ON COLUMN system_sql_log.statement_type IS 'Comando Tipo';
COMMENT ON COLUMN system_sql_log.access_ip IS 'IP de Acesso';
COMMENT ON COLUMN system_sql_log.transaction_id IS 'ID da Transação';
COMMENT ON COLUMN system_sql_log.log_trace IS 'Log do Trace';
COMMENT ON COLUMN system_sql_log.session_id IS 'ID da Sessão';
COMMENT ON COLUMN system_sql_log.class_name IS 'Nome da Classe';
COMMENT ON COLUMN system_sql_log.php_sapi IS 'PHP Sapi';
COMMENT ON COLUMN system_sql_log.request_id IS 'ID da Request';
COMMENT ON COLUMN system_sql_log.log_year IS 'Ano do Log';
COMMENT ON COLUMN system_sql_log.log_month IS 'Mês do Log';
COMMENT ON COLUMN system_sql_log.log_day IS 'Dia do Log';
ALTER TABLE system_sql_log OWNER TO postgres;

CREATE TABLE system_user_group (
id varchar(36) NOT NULL,
system_user_id varchar(36),
system_group_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_user_group PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_system_user_group_group ON system_user_group USING btree (system_group_id ASC NULLS LAST);
CREATE INDEX idx_system_user_group_user ON system_user_group USING btree (system_user_id ASC NULLS LAST);
COMMENT ON TABLE system_user_group IS 'System-Usuário x Grupo de Acesso';
COMMENT ON COLUMN system_user_group.id IS 'ID do Usuário x Grupo';
COMMENT ON COLUMN system_user_group.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_user_group.system_group_id IS 'ID do Grupo de Acesso';
COMMENT ON COLUMN system_user_group.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_user_group.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_user_group.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_user_group.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_user_group OWNER TO postgres;

CREATE TABLE system_user_program (
id varchar(36) NOT NULL,
system_user_id varchar(36),
system_program_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_user_program PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_sys_user_program_program ON system_user_program USING btree (system_program_id pg_catalog.text_ops ASC NULLS LAST);
CREATE INDEX idx_sys_user_program_user ON system_user_program USING btree (system_user_id ASC NULLS LAST);
COMMENT ON TABLE system_user_program IS 'System-Usuário x Programa';
COMMENT ON COLUMN system_user_program.id IS 'ID do Usuário x Programa';
COMMENT ON COLUMN system_user_program.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_user_program.system_program_id IS 'ID do Programa';
COMMENT ON COLUMN system_user_program.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_user_program.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_user_program.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_user_program.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_user_program OWNER TO postgres;

CREATE TABLE system_notification (
id varchar(36) NOT NULL,
system_user_id varchar(36) NOT NULL,
system_user_to_id varchar(36),
subject text  NOT NULL,
message text  NOT NULL,
dt_message text  NOT NULL,
action_url1 text ,
action_label1 text ,
icon text ,
checked char(1)  DEFAULT 'N',
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
email_to varchar(100),
action_url2 text,
action_label2 text,
action_url3 text,
action_label3 text,
type_notification varchar(50),
CONSTRAINT pk_system_notification PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_notification IS 'Systtem-Notificações';
COMMENT ON COLUMN system_notification.id IS 'ID da Notificação de Sistema';
COMMENT ON COLUMN system_notification.system_user_id IS 'ID do Usuário - Emitente';
COMMENT ON COLUMN system_notification.system_user_to_id IS 'ID do Usuário - Destinatário';
COMMENT ON COLUMN system_notification.subject IS 'Assunto';
COMMENT ON COLUMN system_notification.message IS 'Mensagem';
COMMENT ON COLUMN system_notification.dt_message IS 'Data da Mensagem';
COMMENT ON COLUMN system_notification.action_url1 IS 'URL da Ação - 1';
COMMENT ON COLUMN system_notification.action_label1 IS 'Label da Ação - 1';
COMMENT ON COLUMN system_notification.icon IS 'Icone';
COMMENT ON COLUMN system_notification.checked IS 'Checado: S-Sim,N-Não';
COMMENT ON COLUMN system_notification.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_notification.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_notification.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_notification.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_notification.email_to IS 'Email - Destinatário';
COMMENT ON COLUMN system_notification.action_url2 IS 'URL da Ação - 2';
COMMENT ON COLUMN system_notification.action_label2 IS 'Label da Ação - 2';
COMMENT ON COLUMN system_notification.action_url3 IS 'URL da Ação - 3';
COMMENT ON COLUMN system_notification.action_label3 IS 'Label da Ação - 3';
COMMENT ON COLUMN system_notification.type_notification IS 'Tipo de Notificação: INVITE, OUTHER';
ALTER TABLE system_notification OWNER TO postgres;

CREATE TABLE system_process_log (
id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
type_process varchar(50)  NOT NULL,
unit_id varchar(36) ,
date_ini_process timestamp(6) NOT NULL DEFAULT now(),
date_fin_process timestamp(6),
param_process text  NOT NULL,
system_user_id varchar(36)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
reversed varchar(1) NOT NULL DEFAULT 'N',
CONSTRAINT pk_system_process_log PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_process_log IS 'System-Log de Processo';
COMMENT ON COLUMN system_process_log.id IS 'ID do Processo';
COMMENT ON COLUMN system_process_log.type_process IS 'Tipo do Processo';
COMMENT ON COLUMN system_process_log.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN system_process_log.date_ini_process IS 'Data Inicial do Processo';
COMMENT ON COLUMN system_process_log.date_fin_process IS 'Data Final do Processo';
COMMENT ON COLUMN system_process_log.param_process IS 'Parametros do Processo';
COMMENT ON COLUMN system_process_log.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_process_log.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_process_log.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_process_log.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_process_log.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_process_log.reversed IS 'Estornado';
ALTER TABLE system_process_log OWNER TO postgres;

CREATE TABLE system_notification_log(
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
system_user_id varchar(36) NOT NULL,
system_user_to_id varchar(36) NOT NULL,
email_to varchar(100),
subject text NOT NULL,
message text NOT NULL,
dt_message text  NOT NULL,
type_notification varchar(50),
icon text,
checked char(1)  DEFAULT 'N',
action_url1 text,
action_label1 text,
action_body1 text,
action_header1 text,
action_type1 text,
action_url2 text,
action_label2 text,
action_body2 text,
action_header2 text,
action_type2 text,
action_url3 text,
action_label3 text,
action_body3 text,
action_header3 text,
action_type3 text,
CONSTRAINT pk_system_notification_log PRIMARY KEY (id)
)
WITHOUT OIDS;
COMMENT ON TABLE system_notification_log IS 'Systtem-Notificações-Log';
COMMENT ON COLUMN system_notification_log.id IS 'ID da Notificação de Sistema';
COMMENT ON COLUMN system_notification_log.system_user_id IS 'ID do Usuário - Emitente';
COMMENT ON COLUMN system_notification_log.system_user_to_id IS 'ID do Usuário - Destinatário';
COMMENT ON COLUMN system_notification_log.subject IS 'Assunto';
COMMENT ON COLUMN system_notification_log.message IS 'Mensagem';
COMMENT ON COLUMN system_notification_log.checked IS 'Checado: S-Sim,N-Não';
COMMENT ON COLUMN system_notification_log.email_to IS 'Email - Destinatário';
COMMENT ON COLUMN system_notification_log.icon IS 'Icone';
COMMENT ON COLUMN system_notification_log.type_notification IS 'Tipo de Notificação: INVITE, OUTHER';
COMMENT ON COLUMN system_notification_log.dt_message IS 'Data da Mensagem';
COMMENT ON COLUMN system_notification_log.action_url1 IS 'URL da Ação - 1';
COMMENT ON COLUMN system_notification_log.action_label1 IS 'Label da Ação - 1';
COMMENT ON COLUMN system_notification_log.action_body1 IS 'Corpo da request - 1';
COMMENT ON COLUMN system_notification_log.action_header1 IS 'Header da request - 1';
COMMENT ON COLUMN system_notification_log.action_type1 IS 'Tipo da request - 1';
COMMENT ON COLUMN system_notification_log.action_url2 IS 'URL da Ação - 2';
COMMENT ON COLUMN system_notification_log.action_label2 IS 'Label da Ação - 2';
COMMENT ON COLUMN system_notification_log.action_body2 IS 'Corpo da request - 2';
COMMENT ON COLUMN system_notification_log.action_header2 IS 'Header da request - 2';
COMMENT ON COLUMN system_notification_log.action_type2 IS 'Tipo da request - 2';
COMMENT ON COLUMN system_notification_log.action_url3 IS 'URL da Ação - 3';
COMMENT ON COLUMN system_notification_log.action_label3 IS 'Label da Ação - 3';
COMMENT ON COLUMN system_notification_log.action_body3 IS 'Corpo da request - 3';
COMMENT ON COLUMN system_notification_log.action_header3 IS 'Header da request - 3';
COMMENT ON COLUMN system_notification_log.action_type3 IS 'Tipo da request - 3';
ALTER TABLE system_notification_log OWNER TO postgres;

CREATE TABLE ope_centro_rend (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
ope_atividade_id varchar(36) NOT NULL DEFAULT 'P',
ope_centro_versao_id varchar(36) NOT NULL,
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_centro_rend PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_rend IS 'Operação-Rendimentos por Atividade';
COMMENT ON COLUMN ope_centro_rend.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_rend.id IS 'ID do Rendimento de Componente';
COMMENT ON COLUMN ope_centro_rend.nome IS 'Nome';
COMMENT ON COLUMN ope_centro_rend.ativo IS 'Ativo';
COMMENT ON COLUMN ope_centro_rend.ope_atividade_id IS 'Tipo (P-Primario,S-Secundario)';
COMMENT ON COLUMN ope_centro_rend.ope_centro_versao_id IS 'ID da Versão da Operação';
COMMENT ON COLUMN ope_centro_rend.observacao IS 'Observação';
COMMENT ON COLUMN ope_centro_rend.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_rend.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_rend.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_rend.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_centro_rend OWNER TO postgres;

CREATE TABLE ope_regiao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
sigla_regiao varchar(50),
CONSTRAINT pk_ope_regiao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_regiao IS 'Operação-Região';
COMMENT ON COLUMN ope_regiao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_regiao.id IS 'ID do Região';
COMMENT ON COLUMN ope_regiao.nome IS 'Nome';
COMMENT ON COLUMN ope_regiao.ativo IS 'Ativo';
COMMENT ON COLUMN ope_regiao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_regiao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_regiao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_regiao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_regiao.sigla_regiao IS 'Sigla do Espacamento';
ALTER TABLE ope_regiao OWNER TO postgres;

CREATE TABLE ope_ocor_status (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_ocor_status varchar(50)  NOT NULL,
tipo_status varchar(1)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_ocor_status PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_status IS 'Operação-Status da Ocorrência';
COMMENT ON COLUMN ope_ocor_status.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor_status.id IS 'ID do Status da Ocorrência';
COMMENT ON COLUMN ope_ocor_status.nome IS 'Nome';
COMMENT ON COLUMN ope_ocor_status.ativo IS 'Ativo';
COMMENT ON COLUMN ope_ocor_status.sigla_ocor_status IS 'Sigla do Status da Ocorrência';
COMMENT ON COLUMN ope_ocor_status.tipo_status IS 'Tipo do Status: A-Aberta, N-Andamento,F-Solucionada,C-Cancelada';
COMMENT ON COLUMN ope_ocor_status.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_status.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_status.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_status.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_ocor_status OWNER TO postgres;

CREATE TABLE ope_ocor_prev (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_ocor_id varchar(36) NOT NULL,
ope_centro2_id varchar(36) NOT NULL,
ope_compart_id varchar(36),
observacao varchar(250),
data_ult_solucao date,
qnt_limite int4 NOT NULL DEFAULT 0,
qnt_aviso int4 NOT NULL DEFAULT 0,
qnt_dia_limite int4 NOT NULL DEFAULT 0,
qnt_dia_aviso int4 NOT NULL DEFAULT 0,
data_valid_ini date NOT NULL,
CONSTRAINT pk_ope_ocor_prev PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_prev IS 'Operação-Previsão de Ocorrência';
COMMENT ON COLUMN ope_ocor_prev.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor_prev.id IS 'ID da Previsão da Ocorrência';
COMMENT ON COLUMN ope_ocor_prev.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_prev.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_prev.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_prev.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_ocor_prev.ope_ocor_id IS 'ID da Ocorrência';
COMMENT ON COLUMN ope_ocor_prev.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_ocor_prev.ope_compart_id IS 'ID do Compartimento';
COMMENT ON COLUMN ope_ocor_prev.observacao IS 'Observação';
COMMENT ON COLUMN ope_ocor_prev.data_ult_solucao IS 'Data Última Solução';
COMMENT ON COLUMN ope_ocor_prev.qnt_limite IS 'Quantidade Limite';
COMMENT ON COLUMN ope_ocor_prev.qnt_aviso IS 'Quantidade Aviso';
COMMENT ON COLUMN ope_ocor_prev.qnt_dia_limite IS 'Quantidade Dias Limite';
COMMENT ON COLUMN ope_ocor_prev.qnt_dia_aviso IS 'Quantidade Dias Aviso';
COMMENT ON COLUMN ope_ocor_prev.data_valid_ini IS 'Data de Validade Inicial';
ALTER TABLE ope_ocor_prev OWNER TO postgres;

CREATE TABLE ope_ocor_mov (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
observacao varchar(250),
data_mov date NOT NULL,
numero varchar(50) NOT NULL,
ger_empresa_id varchar(36) NOT NULL,
ger_pessoa_endereco_id_exec varchar(36) NOT NULL,
ope_ocor_tipo_id varchar(36) NOT NULL,
CONSTRAINT pk_ope_ocor_mov PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_mov IS 'Operação-Movimentação de Ocorrência';
COMMENT ON COLUMN ope_ocor_mov.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor_mov.id IS 'ID da Movimentação da Ocorrência';
COMMENT ON COLUMN ope_ocor_mov.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_mov.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_mov.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_mov.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_ocor_mov.observacao IS 'Observação';
COMMENT ON COLUMN ope_ocor_mov.data_mov IS 'Data do Movimento';
COMMENT ON COLUMN ope_ocor_mov.numero IS 'Número do Movimento';
COMMENT ON COLUMN ope_ocor_mov.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_ocor_mov.ger_pessoa_endereco_id_exec IS 'ID do Endereço da Pessoa';
COMMENT ON COLUMN ope_ocor_mov.ope_ocor_tipo_id IS 'ID do Tipo de Ocorrência';
ALTER TABLE ope_ocor_mov OWNER TO postgres;

CREATE TABLE ope_ocor_mov_det (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ope_ocor_mov_id varchar(36) NOT NULL,
ope_ocor_id varchar(36) NOT NULL,
observacao varchar(250),
qnt_ocor numeric(18,6) NOT NULL DEFAULT 0,
qnt_ocor_calc numeric(18,6) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_ocor_status_id varchar(36) NOT NULL DEFAULT 0,
data_status date NOT NULL,
lat_x varchar(50),
long_y varchar(50),
ponto varchar(50),
ope_ocor_mov_dest_id varchar(36),
CONSTRAINT pk_ope_ocor_mov_det PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_mov_det IS 'Operação-Detalhe da Movimentação de Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_det.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor_mov_det.id IS 'ID do Detalhe da Movimentação da Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_det.ope_ocor_mov_id IS 'ID do Movimento de Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_det.ope_ocor_id IS 'ID da Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_det.observacao IS 'Observação';
COMMENT ON COLUMN ope_ocor_mov_det.qnt_ocor IS 'Quantidade da Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_det.qnt_ocor_calc IS 'Quantidade Cálculada da Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_det.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_mov_det.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_mov_det.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_mov_det.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_ocor_mov_det.ope_ocor_status_id IS 'ID do Status da Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_det.data_status IS 'Data do Status';
COMMENT ON COLUMN ope_ocor_mov_det.lat_x IS 'Latitude X';
COMMENT ON COLUMN ope_ocor_mov_det.long_y IS 'Longitude Y';
COMMENT ON COLUMN ope_ocor_mov_det.ponto IS 'Descrição do Ponto';
COMMENT ON COLUMN ope_ocor_mov_det.ope_ocor_mov_dest_id IS 'ID da Destinação da Movimentação da Ocorrência';
ALTER TABLE ope_ocor_mov_det OWNER TO postgres;

CREATE TABLE ope_ocor_mov_dest (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ope_ocor_mov_id varchar(36) NOT NULL,
ope_centro2_id varchar(36) NOT NULL,
ope_compart_id varchar(36),
observacao varchar(250),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_ocor_mov_dest PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_mov_dest IS 'Operação-Destinação da Movimentação de Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_dest.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor_mov_dest.id IS 'ID da Destinação da Movimentação da Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_dest.ope_ocor_mov_id IS 'ID do Movimento de Ocorrência';
COMMENT ON COLUMN ope_ocor_mov_dest.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_ocor_mov_dest.ope_compart_id IS 'ID do Compartimento';
COMMENT ON COLUMN ope_ocor_mov_dest.observacao IS 'Observação';
COMMENT ON COLUMN ope_ocor_mov_dest.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_mov_dest.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_mov_dest.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_mov_dest.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_ocor_mov_dest OWNER TO postgres;

CREATE TABLE ope_compart_status (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_compart_status varchar(50)  NOT NULL,
tipo_status varchar(1)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_compart_status PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_status IS 'Operação-Status do Compartimento';
COMMENT ON COLUMN ope_compart_status.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_compart_status.id IS 'ID do Status do Compartimento';
COMMENT ON COLUMN ope_compart_status.nome IS 'Nome';
COMMENT ON COLUMN ope_compart_status.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_status.sigla_compart_status IS 'Sigla do Status do Compartimento';
COMMENT ON COLUMN ope_compart_status.tipo_status IS 'Tipo do Status: M-Montado/Utilizando, D-Desmontado/Parado, C-Cancelado/Eliminado';
COMMENT ON COLUMN ope_compart_status.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_status.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_status.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_status.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_compart_status OWNER TO postgres;

CREATE TABLE ope_compart_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_compart_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_compart_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_grupo IS 'Operação-Grupo do Compartimento';
COMMENT ON COLUMN ope_compart_grupo.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ope_compart_grupo.id IS 'ID de Grupo do Compartimento';
COMMENT ON COLUMN ope_compart_grupo.nome IS 'Nome';
COMMENT ON COLUMN ope_compart_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_grupo.sigla_compart_grupo IS 'Sigla de Grupo do Compartimento';
COMMENT ON COLUMN ope_compart_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_grupo.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_compart_grupo OWNER TO postgres;

CREATE TABLE ope_compart_subgrupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_compart_subgrupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_compart_grupo_id varchar(36) NOT NULL,
CONSTRAINT pk_ope_compart_subgrupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_subgrupo IS 'Operação-Sub-Grupo do Compartimento';
COMMENT ON COLUMN ope_compart_subgrupo.unit_id IS 'ID de Unidade';
COMMENT ON COLUMN ope_compart_subgrupo.id IS 'ID de Sub-Grupo do Compartimento';
COMMENT ON COLUMN ope_compart_subgrupo.nome IS 'Nome';
COMMENT ON COLUMN ope_compart_subgrupo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_subgrupo.sigla_compart_subgrupo IS 'Sigla de Grupo do Compartimento';
COMMENT ON COLUMN ope_compart_subgrupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_subgrupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_subgrupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_subgrupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_compart_subgrupo.ope_compart_grupo_id IS 'ID do Grupo de Compartimento';
ALTER TABLE ope_compart_subgrupo OWNER TO postgres;

CREATE TABLE ope_compart_ocor (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_compart_ocor varchar(50)  NOT NULL,
tipo_ocor varchar(1)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ope_compart_status_id varchar(36) NOT NULL,
CONSTRAINT pk_ope_compart_ocor PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_ocor IS 'Operação-Ocorrência do Compartimento';
COMMENT ON COLUMN ope_compart_ocor.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_compart_ocor.id IS 'ID da Ocorrência do Compartimento';
COMMENT ON COLUMN ope_compart_ocor.nome IS 'Nome';
COMMENT ON COLUMN ope_compart_ocor.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_ocor.sigla_compart_ocor IS 'Sigla da Ocorrência de Compartimento';
COMMENT ON COLUMN ope_compart_ocor.tipo_ocor IS 'Tipo da Ocorrência: M-Movimentação, D-Medidação';
COMMENT ON COLUMN ope_compart_ocor.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_ocor.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_ocor.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_ocor.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_compart_ocor.ope_compart_status_id IS 'ID do Status do Compartimento';
ALTER TABLE ope_compart_ocor OWNER TO postgres;

CREATE TABLE ope_compart_medida (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_compart_medida varchar(50)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_compart_medida PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_medida IS 'Operação-Medida do Compartimento';
COMMENT ON COLUMN ope_compart_medida.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_compart_medida.id IS 'ID da Medida do Compartimento';
COMMENT ON COLUMN ope_compart_medida.nome IS 'Nome';
COMMENT ON COLUMN ope_compart_medida.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_medida.sigla_compart_medida IS 'Sigla da Medida do Compartimento';
COMMENT ON COLUMN ope_compart_medida.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_medida.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_medida.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_medida.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_compart_medida OWNER TO postgres;

CREATE TABLE ope_compart_tipo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_compart_tipo varchar(50)  NOT NULL,
tipo_compart varchar(1)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
qnt_lonas numeric(18,3) NOT NULL DEFAULT 1,
qnt_sulco_min numeric(18,3) NOT NULL DEFAULT 0,
qnt_sulco_max numeric(18,3) DEFAULT 0,
ope_compart_medida_id varchar(36) NOT NULL,
CONSTRAINT pk_ope_compart_tipo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_tipo IS 'Operação-Tipo do Compartimento';
COMMENT ON COLUMN ope_compart_tipo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_compart_tipo.id IS 'ID da Tipo do Compartimento';
COMMENT ON COLUMN ope_compart_tipo.nome IS 'Nome';
COMMENT ON COLUMN ope_compart_tipo.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_tipo.sigla_compart_tipo IS 'Sigla da Ocorrência de Compartimento';
COMMENT ON COLUMN ope_compart_tipo.tipo_compart IS 'Tipo do Compartimento: P-Pneu, O-Outro';
COMMENT ON COLUMN ope_compart_tipo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_tipo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_tipo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_tipo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_compart_tipo.qnt_lonas IS 'Quantidade Lonas';
COMMENT ON COLUMN ope_compart_tipo.qnt_sulco_min IS 'Quantidade Sulco Mínimo';
COMMENT ON COLUMN ope_compart_tipo.qnt_sulco_max IS 'Quantidade Sulco Máximo';
COMMENT ON COLUMN ope_compart_tipo.ope_compart_medida_id IS 'ID da Medida do Compartimento';
ALTER TABLE ope_compart_tipo OWNER TO postgres;

CREATE TABLE ope_compart_posicao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
sigla_compart_posicao varchar(50)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
numero_eixo int2 NOT NULL DEFAULT 0,
posicao varchar(1) NOT NULL,
banda_montagem varchar(1) NOT NULL,
lado_montagem varchar(1) NOT NULL,
CONSTRAINT pk_ope_compart_posicao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_compart_posicao IS 'Operação-Posição do Compartimento';
COMMENT ON COLUMN ope_compart_posicao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_compart_posicao.id IS 'ID da Posição do Compartimento';
COMMENT ON COLUMN ope_compart_posicao.nome IS 'Nome';
COMMENT ON COLUMN ope_compart_posicao.ativo IS 'Ativo';
COMMENT ON COLUMN ope_compart_posicao.sigla_compart_posicao IS 'Sigla da Posição do Compartimento';
COMMENT ON COLUMN ope_compart_posicao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_compart_posicao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_compart_posicao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_compart_posicao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_compart_posicao.numero_eixo IS 'Numero Eixo';
COMMENT ON COLUMN ope_compart_posicao.posicao IS 'Posição: D-Dianteiro, T-Traseiro';
COMMENT ON COLUMN ope_compart_posicao.banda_montagem IS 'Banda Montagem: I-Interna, E-Externa';
COMMENT ON COLUMN ope_compart_posicao.lado_montagem IS 'Lado Montagem: D-Direito, E-Esquerdo, C-Central';
ALTER TABLE ope_compart_posicao OWNER TO postgres;

CREATE TABLE ope_estagio (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100)  NOT NULL,
ativo varchar(1)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
sigla_estagio varchar(50) NOT NULL,
CONSTRAINT pk_ope_estagio PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_estagio IS 'Operação-Estágio';
COMMENT ON COLUMN ope_estagio.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_estagio.id IS 'ID do Estágio';
COMMENT ON COLUMN ope_estagio.nome IS 'Nome';
COMMENT ON COLUMN ope_estagio.ativo IS 'Ativo';
COMMENT ON COLUMN ope_estagio.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_estagio.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_estagio.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_estagio.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_estagio.sigla_estagio IS 'Sigla do Estágio';
ALTER TABLE ope_estagio OWNER TO postgres;

CREATE TABLE ope_ocor_compart_mov (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
observacao varchar(250),
data_mov date,
numero varchar(50),
ger_empresa_id varchar(36),
ger_pessoa_endereco_id_exec varchar(36),
CONSTRAINT pk_ope_compart_mov PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_compart_mov IS 'Operação-Movimentação de Compartimento';
COMMENT ON COLUMN ope_ocor_compart_mov.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor_compart_mov.id IS 'ID da Movimentação da Compartimento';
COMMENT ON COLUMN ope_ocor_compart_mov.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_compart_mov.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_compart_mov.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_compart_mov.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_ocor_compart_mov.observacao IS 'Observação';
COMMENT ON COLUMN ope_ocor_compart_mov.data_mov IS 'Data do Movimento';
COMMENT ON COLUMN ope_ocor_compart_mov.numero IS 'Número do Movimento';
COMMENT ON COLUMN ope_ocor_compart_mov.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_ocor_compart_mov.ger_pessoa_endereco_id_exec IS 'ID do Endereço da Pessoa';
ALTER TABLE ope_ocor_compart_mov OWNER TO postgres;

CREATE TABLE ope_ocor_compart_mov_det (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ope_compart_mov_id varchar(36) NOT NULL,
ope_compart_ocor_id varchar(36) NOT NULL,
ope_compart_id varchar(36) NOT NULL,
observacao varchar(250),
qnt_medicao numeric(18,6) NOT NULL DEFAULT 0,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_ope_compart_mov_det PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_ocor_compart_mov_det IS 'Operação-Detalhe da Movimentação de Compartimento';
COMMENT ON COLUMN ope_ocor_compart_mov_det.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_ocor_compart_mov_det.id IS 'ID do Detalhe da Movimentação da Compartimento';
COMMENT ON COLUMN ope_ocor_compart_mov_det.ope_compart_mov_id IS 'ID da Movimentação do Compartimento';
COMMENT ON COLUMN ope_ocor_compart_mov_det.ope_compart_ocor_id IS 'ID da Ocorrência do Compartimento';
COMMENT ON COLUMN ope_ocor_compart_mov_det.ope_compart_id IS 'ID do Compartimento';
COMMENT ON COLUMN ope_ocor_compart_mov_det.observacao IS 'Observação';
COMMENT ON COLUMN ope_ocor_compart_mov_det.qnt_medicao IS 'Quantidade da Medição';
COMMENT ON COLUMN ope_ocor_compart_mov_det.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_ocor_compart_mov_det.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_ocor_compart_mov_det.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_ocor_compart_mov_det.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE ope_ocor_compart_mov_det OWNER TO postgres;

CREATE TABLE ope_centro_config (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
tipo_regra varchar(1) NOT NULL,
ope_centro2_ord_tipo_id varchar(36),
mov_operacao_id varchar(36),
ger_empresa_id varchar(36),
ope_centro1_id varchar(36),
ope_centro2_id varchar(36),
ope_atividade_id varchar(36),
ger_itemserv_grupo_id varchar(36),
ger_itemserv_subgrupo_id varchar(36),
ger_itemserv_id varchar(36),
ope_compart_grupo_id varchar(36),
ope_compart_subgrupo_id varchar(36),
ope_compart_id varchar(36),
ope_centro_tipo_id varchar(36),
ope_centro_subtipo_id varchar(36),
ope_centro_grupo_id varchar(36),
ope_centro_subgrupo_id varchar(36),
ope_estagio_id varchar(36),
observacao varchar(250),
ativo varchar(1) NOT NULL,
CONSTRAINT pk_ope_centro_regra_config PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ope_centro_config IS 'Operação-Regra de Configuração';
COMMENT ON COLUMN ope_centro_config.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ope_centro_config.id IS 'ID da Regra da Configuração';
COMMENT ON COLUMN ope_centro_config.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ope_centro_config.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ope_centro_config.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ope_centro_config.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ope_centro_config.tipo_regra IS 'Tipo Regra: E-Exclusão, I-Inclusão';
COMMENT ON COLUMN ope_centro_config.ope_centro2_ord_tipo_id IS 'ID do Tipo da Ordem';
COMMENT ON COLUMN ope_centro_config.mov_operacao_id IS 'ID da Operação do Movimento';
COMMENT ON COLUMN ope_centro_config.ger_empresa_id IS 'ID da Empresa';
COMMENT ON COLUMN ope_centro_config.ope_centro1_id IS 'ID do Centro Nível 1 Entrada/Saída';
COMMENT ON COLUMN ope_centro_config.ope_centro2_id IS 'ID do Centro Nível 2 Entrada/Saída';
COMMENT ON COLUMN ope_centro_config.ope_atividade_id IS 'ID da Atividade';
COMMENT ON COLUMN ope_centro_config.ger_itemserv_grupo_id IS 'ID do Grupo do Item/Serviço';
COMMENT ON COLUMN ope_centro_config.ger_itemserv_subgrupo_id IS 'ID do Sub-Grupo de Item/Serviço';
COMMENT ON COLUMN ope_centro_config.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN ope_centro_config.ope_compart_grupo_id IS 'ID de Grupo do Compartimento';
COMMENT ON COLUMN ope_centro_config.ope_compart_subgrupo_id IS 'ID de Sub-Grupo do Compartimento';
COMMENT ON COLUMN ope_centro_config.ope_compart_id IS 'ID do Compartimento';
COMMENT ON COLUMN ope_centro_config.ope_centro_tipo_id IS 'ID do Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_config.ope_centro_subtipo_id IS 'ID do Sub-Tipo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_config.ope_centro_grupo_id IS 'ID do Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_config.ope_centro_subgrupo_id IS 'ID do Sub-Grupo de Centro Entrada/Saída';
COMMENT ON COLUMN ope_centro_config.ope_estagio_id IS 'ID do Estágio';
COMMENT ON COLUMN ope_centro_config.observacao IS 'Observação';
COMMENT ON COLUMN ope_centro_config.ativo IS 'Ativo: S-Sim, N-Não';
ALTER TABLE ope_centro_config OWNER TO postgres;

CREATE TABLE ger_marca_pessoa (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
ger_marca_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ger_pessoa_id varchar(36),
observacao varchar(250),
CONSTRAINT pk_ger_marca_pessoa PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE ger_marca_pessoa IS 'Geral-Marca x Pessoa';
COMMENT ON COLUMN ger_marca_pessoa.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN ger_marca_pessoa.id IS 'ID do Marca x Pessoa';
COMMENT ON COLUMN ger_marca_pessoa.ger_marca_id IS 'ID da Marca';
COMMENT ON COLUMN ger_marca_pessoa.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN ger_marca_pessoa.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN ger_marca_pessoa.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN ger_marca_pessoa.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN ger_marca_pessoa.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN ger_marca_pessoa.observacao IS 'Observação';
ALTER TABLE ger_marca_pessoa OWNER TO postgres;

CREATE TABLE system_user_preference (
id varchar(100)  NOT NULL,
value text ,
system_user_id varchar(36) NOT NULL,
object_type varchar(36) NOT NULL,
object_id varchar(36) NOT NULL,
preference_description varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
defaultd varchar(1),
CONSTRAINT pk_system_user_preference PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_user_preference IS 'System-Preferência do Usuário';
COMMENT ON COLUMN system_user_preference.id IS 'ID da Preferencia do Usuário';
COMMENT ON COLUMN system_user_preference.value IS 'Valor';
COMMENT ON COLUMN system_user_preference.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_user_preference.object_type IS 'Tipo do Objeto';
COMMENT ON COLUMN system_user_preference.object_id IS 'ID do Objeto';
COMMENT ON COLUMN system_user_preference.preference_description IS 'Descrição da Preferência';
COMMENT ON COLUMN system_user_preference.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_user_preference.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_user_preference.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_user_preference.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_user_preference.defaultd IS 'Padrão: S-Sim, N-Não';
ALTER TABLE system_user_preference OWNER TO postgres;

CREATE TABLE mov_cotacao (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
ger_pessoa_id varchar(36) NOT NULL,
ger_pessoa_endereco_id varchar(36),
ger_itemserv_id varchar(36) NOT NULL,
observacao1 varchar(250),
observacao2 varchar(250),
qnt_cot numeric(18,6) NOT NULL DEFAULT 0,
valor_unit_cot numeric(18,6) NOT NULL DEFAULT 0,
valor_total_cot numeric(18,6) NOT NULL DEFAULT 0,
valor_desc_cot numeric(18,6) NOT NULL DEFAULT 0,
valor_frete_cot numeric(18,6) NOT NULL DEFAULT 0,
valor_outro_cot numeric(18,6) NOT NULL,
valor_total_trib_cot numeric(18,6) NOT NULL DEFAULT 0,
status varchar(1) NOT NULL DEFAULT 'P',
data_status timestamp,
system_user_id_aprov varchar(36),
fin_cond_pagrec_id varchar(36) NOT NULL,
CONSTRAINT pk_mov_cotacao PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_cotacao IS 'Movimentação-Cotação do Movimento';
COMMENT ON COLUMN mov_cotacao.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_cotacao.id IS 'ID do Cotação do Movimento';
COMMENT ON COLUMN mov_cotacao.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_cotacao.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_cotacao.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_cotacao.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_cotacao.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN mov_cotacao.ger_pessoa_id IS 'ID da Pessoa';
COMMENT ON COLUMN mov_cotacao.ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa';
COMMENT ON COLUMN mov_cotacao.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN mov_cotacao.observacao1 IS 'Observação 1';
COMMENT ON COLUMN mov_cotacao.observacao2 IS 'Observação 2';
COMMENT ON COLUMN mov_cotacao.qnt_cot IS 'Quantidade';
COMMENT ON COLUMN mov_cotacao.valor_unit_cot IS 'Valor Unitário';
COMMENT ON COLUMN mov_cotacao.valor_total_cot IS 'Valor Total';
COMMENT ON COLUMN mov_cotacao.valor_desc_cot IS 'Valor Desconto';
COMMENT ON COLUMN mov_cotacao.valor_frete_cot IS 'Valor Frete';
COMMENT ON COLUMN mov_cotacao.valor_outro_cot IS 'Valor Outros';
COMMENT ON COLUMN mov_cotacao.valor_total_trib_cot IS 'Valor Total de Tributos';
COMMENT ON COLUMN mov_cotacao.status IS 'Status: P-Pendente, A-Aprovado, C-Cancelado';
COMMENT ON COLUMN mov_cotacao.data_status IS 'Data do Status';
COMMENT ON COLUMN mov_cotacao.system_user_id_aprov IS 'ID do Usuário Aprovador';
COMMENT ON COLUMN mov_cotacao.fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec';
ALTER TABLE mov_cotacao OWNER TO postgres;

CREATE TABLE mov_cotacao_anal (
unit_id varchar(36)  NOT NULL,
id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
mov_id varchar(36)  NOT NULL,
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
c01_ger_pessoa_id varchar(36) ,
c01_ger_pessoa_endereco_id varchar(36) ,
c01_observacao1 varchar(250) ,
c01_observacao2 varchar(250) ,
c01_qnt_cot numeric(18,6) DEFAULT 0,
c01_valor_unit_cot numeric(18,6) DEFAULT 0,
c01_valor_total_cot numeric(18,6) DEFAULT 0,
c01_valor_desc_cot numeric(18,6) DEFAULT 0,
c01_valor_frete_cot numeric(18,6) DEFAULT 0,
c01_valor_outro_cot numeric(18,6),
c01_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c01_status varchar(1)  DEFAULT 'P'::character varying,
c01_data_status timestamp(6),
c01_system_user_id_aprov varchar(36) ,
c02_ger_pessoa_id varchar(36) ,
c02_ger_pessoa_endereco_id varchar(36) ,
c02_observacao1 varchar(250) ,
c02_observacao2 varchar(250) ,
c02_qnt_cot numeric(18,6) DEFAULT 0,
c02_valor_unit_cot numeric(18,6) DEFAULT 0,
c02_valor_total_cot numeric(18,6) DEFAULT 0,
c02_valor_desc_cot numeric(18,6) DEFAULT 0,
c02_valor_frete_cot numeric(18,6) DEFAULT 0,
c02_valor_outro_cot numeric(18,6),
c02_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c02_status varchar(1)  DEFAULT 'P'::character varying,
c02_data_status timestamp(6),
c02_system_user_id_aprov varchar(36) ,
c03_ger_pessoa_id varchar(36) ,
c03_ger_pessoa_endereco_id varchar(36) ,
c03_observacao1 varchar(250) ,
c03_observacao2 varchar(250) ,
c03_qnt_cot numeric(18,6) DEFAULT 0,
c03_valor_unit_cot numeric(18,6) DEFAULT 0,
c03_valor_total_cot numeric(18,6) DEFAULT 0,
c03_valor_desc_cot numeric(18,6) DEFAULT 0,
c03_valor_frete_cot numeric(18,6) DEFAULT 0,
c03_valor_outro_cot numeric(18,6),
c03_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c03_status varchar(1)  DEFAULT 'P'::character varying,
c03_data_status timestamp(6),
c03_system_user_id_aprov varchar(36) ,
c04_ger_pessoa_id varchar(36) ,
c04_ger_pessoa_endereco_id varchar(36) ,
c04_observacao1 varchar(250) ,
c04_observacao2 varchar(250) ,
c04_qnt_cot numeric(18,6) DEFAULT 0,
c04_valor_unit_cot numeric(18,6) DEFAULT 0,
c04_valor_total_cot numeric(18,6) DEFAULT 0,
c04_valor_desc_cot numeric(18,6) DEFAULT 0,
c04_valor_frete_cot numeric(18,6) DEFAULT 0,
c04_valor_outro_cot numeric(18,6),
c04_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c04_status varchar(1)  DEFAULT 'P'::character varying,
c04_data_status timestamp(6),
c04_system_user_id_aprov varchar(36) ,
c05_ger_pessoa_id varchar(36) ,
c05_ger_pessoa_endereco_id varchar(36) ,
c05_observacao1 varchar(250) ,
c05_observacao2 varchar(250) ,
c05_qnt_cot numeric(18,6) DEFAULT 0,
c05_valor_unit_cot numeric(18,6) DEFAULT 0,
c05_valor_total_cot numeric(18,6) DEFAULT 0,
c05_valor_desc_cot numeric(18,6) DEFAULT 0,
c05_valor_frete_cot numeric(18,6) DEFAULT 0,
c05_valor_outro_cot numeric(18,6),
c05_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c05_status varchar(1)  DEFAULT 'P'::character varying,
c05_data_status timestamp(6),
c05_system_user_id_aprov varchar(36) ,
c06_ger_pessoa_id varchar(36) ,
c06_ger_pessoa_endereco_id varchar(36) ,
c06_observacao1 varchar(250) ,
c06_observacao2 varchar(250) ,
c06_qnt_cot numeric(18,6) DEFAULT 0,
c06_valor_unit_cot numeric(18,6) DEFAULT 0,
c06_valor_total_cot numeric(18,6) DEFAULT 0,
c06_valor_desc_cot numeric(18,6) DEFAULT 0,
c06_valor_frete_cot numeric(18,6) DEFAULT 0,
c06_valor_outro_cot numeric(18,6),
c06_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c06_status varchar(1)  DEFAULT 'P'::character varying,
c06_data_status timestamp(6),
c06_system_user_id_aprov varchar(36) ,
c07_ger_pessoa_id varchar(36) ,
c07_ger_pessoa_endereco_id varchar(36) ,
c07_observacao1 varchar(250) ,
c07_observacao2 varchar(250) ,
c07_qnt_cot numeric(18,6) DEFAULT 0,
c07_valor_unit_cot numeric(18,6) DEFAULT 0,
c07_valor_total_cot numeric(18,6) DEFAULT 0,
c07_valor_desc_cot numeric(18,6) DEFAULT 0,
c07_valor_frete_cot numeric(18,6) DEFAULT 0,
c07_valor_outro_cot numeric(18,6),
c07_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c07_status varchar(1)  DEFAULT 'P'::character varying,
c07_data_status timestamp(6),
c07_system_user_id_aprov varchar(36) ,
c08_ger_pessoa_id varchar(36) ,
c08_ger_pessoa_endereco_id varchar(36) ,
c08_observacao1 varchar(250) ,
c08_observacao2 varchar(250) ,
c08_qnt_cot numeric(18,6) DEFAULT 0,
c08_valor_unit_cot numeric(18,6) DEFAULT 0,
c08_valor_total_cot numeric(18,6) DEFAULT 0,
c08_valor_desc_cot numeric(18,6) DEFAULT 0,
c08_valor_frete_cot numeric(18,6) DEFAULT 0,
c08_valor_outro_cot numeric(18,6),
c08_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c08_status varchar(1)  DEFAULT 'P'::character varying,
c08_data_status timestamp(6),
c08_system_user_id_aprov varchar(36) ,
c09_ger_pessoa_id varchar(36) ,
c09_ger_pessoa_endereco_id varchar(36) ,
c09_observacao1 varchar(250) ,
c09_observacao2 varchar(250) ,
c09_qnt_cot numeric(18,6) DEFAULT 0,
c09_valor_unit_cot numeric(18,6) DEFAULT 0,
c09_valor_total_cot numeric(18,6) DEFAULT 0,
c09_valor_desc_cot numeric(18,6) DEFAULT 0,
c09_valor_frete_cot numeric(18,6) DEFAULT 0,
c09_valor_outro_cot numeric(18,6),
c09_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c09_status varchar(1)  DEFAULT 'P'::character varying,
c09_data_status timestamp(6),
c09_system_user_id_aprov varchar(36) ,
c10_ger_pessoa_id varchar(36) ,
c10_ger_pessoa_endereco_id varchar(36) ,
c10_observacao1 varchar(250) ,
c10_observacao2 varchar(250) ,
c10_qnt_cot numeric(18,6) DEFAULT 0,
c10_valor_unit_cot numeric(18,6) DEFAULT 0,
c10_valor_total_cot numeric(18,6) DEFAULT 0,
c10_valor_desc_cot numeric(18,6) DEFAULT 0,
c10_valor_frete_cot numeric(18,6) DEFAULT 0,
c10_valor_outro_cot numeric(18,6),
c10_valor_total_trib_cot numeric(18,6) DEFAULT 0,
c10_status varchar(1)  DEFAULT 'P'::character varying,
c10_data_status timestamp(6),
c10_system_user_id_aprov varchar(36) ,
ger_itemserv_id varchar(36) NOT NULL,
c01_fin_cond_pagrec_id varchar(36),
c02_fin_cond_pagrec_id varchar(36),
c03_fin_cond_pagrec_id varchar(36),
c04_fin_cond_pagrec_id varchar(36),
c05_fin_cond_pagrec_id varchar(36),
c06_fin_cond_pagrec_id varchar(36),
c07_fin_cond_pagrec_id varchar(36),
c08_fin_cond_pagrec_id varchar(36),
c09_fin_cond_pagrec_id varchar(36),
c10_fin_cond_pagrec_id varchar(36),
CONSTRAINT pk_mov_cotacao_anal PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE mov_cotacao_anal IS 'MOV-Analise de Cotação do Movimento';
COMMENT ON COLUMN mov_cotacao_anal.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN mov_cotacao_anal.id IS 'ID da Analise de Cotação do Movimento';
COMMENT ON COLUMN mov_cotacao_anal.mov_id IS 'ID do Movimento';
COMMENT ON COLUMN mov_cotacao_anal.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN mov_cotacao_anal.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN mov_cotacao_anal.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN mov_cotacao_anal.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN mov_cotacao_anal.c01_ger_pessoa_id IS 'ID da Pessoa - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_observacao1 IS 'Observação 1 - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_observacao2 IS 'Observação 2 - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_qnt_cot IS 'Quantidade - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_valor_unit_cot IS 'Valor Unitário - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_valor_total_cot IS 'Valor Total - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_valor_desc_cot IS 'Valor Desconto - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_valor_frete_cot IS 'Valor Frete - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_valor_outro_cot IS 'Valor Outros - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_valor_total_trib_cot IS 'Valor Total de Tributos - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_status IS 'Status - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_data_status IS 'Data do Status - C01';
COMMENT ON COLUMN mov_cotacao_anal.c01_system_user_id_aprov IS 'ID do Usuário Aprovador - C01';
COMMENT ON COLUMN mov_cotacao_anal.c02_ger_pessoa_id IS 'ID da Pessoa - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_observacao1 IS 'Observação 1 - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_observacao2 IS 'Observação 2 - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_qnt_cot IS 'Quantidade - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_valor_unit_cot IS 'Valor Unitário - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_valor_total_cot IS 'Valor Total - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_valor_desc_cot IS 'Valor Desconto - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_valor_frete_cot IS 'Valor Frete - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_valor_outro_cot IS 'Valor Outros - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_valor_total_trib_cot IS 'Valor Total de Tributos - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_status IS 'Status - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_data_status IS 'Data do Status - C02';
COMMENT ON COLUMN mov_cotacao_anal.c02_system_user_id_aprov IS 'ID do Usuário Aprovador - C02';
COMMENT ON COLUMN mov_cotacao_anal.c03_ger_pessoa_id IS 'ID da Pessoa - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_observacao1 IS 'Observação 1 - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_observacao2 IS 'Observação 2 - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_qnt_cot IS 'Quantidade - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_valor_unit_cot IS 'Valor Unitário - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_valor_total_cot IS 'Valor Total - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_valor_desc_cot IS 'Valor Desconto - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_valor_frete_cot IS 'Valor Frete - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_valor_outro_cot IS 'Valor Outros - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_valor_total_trib_cot IS 'Valor Total de Tributos - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_status IS 'Status - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_data_status IS 'Data do Status - C03';
COMMENT ON COLUMN mov_cotacao_anal.c03_system_user_id_aprov IS 'ID do Usuário Aprovador - C03';
COMMENT ON COLUMN mov_cotacao_anal.c04_ger_pessoa_id IS 'ID da Pessoa - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_observacao1 IS 'Observação 1 - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_observacao2 IS 'Observação 2 - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_qnt_cot IS 'Quantidade - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_valor_unit_cot IS 'Valor Unitário - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_valor_total_cot IS 'Valor Total - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_valor_desc_cot IS 'Valor Desconto - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_valor_frete_cot IS 'Valor Frete - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_valor_outro_cot IS 'Valor Outros - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_valor_total_trib_cot IS 'Valor Total de Tributos - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_status IS 'Status - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_data_status IS 'Data do Status - C04';
COMMENT ON COLUMN mov_cotacao_anal.c04_system_user_id_aprov IS 'ID do Usuário Aprovador - C04';
COMMENT ON COLUMN mov_cotacao_anal.c05_ger_pessoa_id IS 'ID da Pessoa - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_observacao1 IS 'Observação 1 - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_observacao2 IS 'Observação 2 - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_qnt_cot IS 'Quantidade - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_valor_unit_cot IS 'Valor Unitário - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_valor_total_cot IS 'Valor Total - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_valor_desc_cot IS 'Valor Desconto - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_valor_frete_cot IS 'Valor Frete - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_valor_outro_cot IS 'Valor Outros - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_valor_total_trib_cot IS 'Valor Total de Tributos - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_status IS 'Status - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_data_status IS 'Data do Status - C05';
COMMENT ON COLUMN mov_cotacao_anal.c05_system_user_id_aprov IS 'ID do Usuário Aprovador - C05';
COMMENT ON COLUMN mov_cotacao_anal.c06_ger_pessoa_id IS 'ID da Pessoa - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_observacao1 IS 'Observação 1 - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_observacao2 IS 'Observação 2 - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_qnt_cot IS 'Quantidade - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_valor_unit_cot IS 'Valor Unitário - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_valor_total_cot IS 'Valor Total - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_valor_desc_cot IS 'Valor Desconto - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_valor_frete_cot IS 'Valor Frete - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_valor_outro_cot IS 'Valor Outros - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_valor_total_trib_cot IS 'Valor Total de Tributos - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_status IS 'Status - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_data_status IS 'Data do Status - C06';
COMMENT ON COLUMN mov_cotacao_anal.c06_system_user_id_aprov IS 'ID do Usuário Aprovador - C06';
COMMENT ON COLUMN mov_cotacao_anal.c07_ger_pessoa_id IS 'ID da Pessoa - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_observacao1 IS 'Observação 1 - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_observacao2 IS 'Observação 2 - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_qnt_cot IS 'Quantidade - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_valor_unit_cot IS 'Valor Unitário - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_valor_total_cot IS 'Valor Total - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_valor_desc_cot IS 'Valor Desconto - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_valor_frete_cot IS 'Valor Frete - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_valor_outro_cot IS 'Valor Outros - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_valor_total_trib_cot IS 'Valor Total de Tributos - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_status IS 'Status - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_data_status IS 'Data do Status - C07';
COMMENT ON COLUMN mov_cotacao_anal.c07_system_user_id_aprov IS 'ID do Usuário Aprovador - C07';
COMMENT ON COLUMN mov_cotacao_anal.c08_ger_pessoa_id IS 'ID da Pessoa - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_observacao1 IS 'Observação 1 - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_observacao2 IS 'Observação 2 - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_qnt_cot IS 'Quantidade - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_valor_unit_cot IS 'Valor Unitário - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_valor_total_cot IS 'Valor Total - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_valor_desc_cot IS 'Valor Desconto - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_valor_frete_cot IS 'Valor Frete - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_valor_outro_cot IS 'Valor Outros - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_valor_total_trib_cot IS 'Valor Total de Tributos - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_status IS 'Status - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_data_status IS 'Data do Status - C08';
COMMENT ON COLUMN mov_cotacao_anal.c08_system_user_id_aprov IS 'ID do Usuário Aprovador - C08';
COMMENT ON COLUMN mov_cotacao_anal.c09_ger_pessoa_id IS 'ID da Pessoa - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_observacao1 IS 'Observação 1 - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_observacao2 IS 'Observação 2 - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_qnt_cot IS 'Quantidade - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_valor_unit_cot IS 'Valor Unitário - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_valor_total_cot IS 'Valor Total - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_valor_desc_cot IS 'Valor Desconto - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_valor_frete_cot IS 'Valor Frete - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_valor_outro_cot IS 'Valor Outros - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_valor_total_trib_cot IS 'Valor Total de Tributos - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_status IS 'Status - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_data_status IS 'Data do Status - C09';
COMMENT ON COLUMN mov_cotacao_anal.c09_system_user_id_aprov IS 'ID do Usuário Aprovador - C09';
COMMENT ON COLUMN mov_cotacao_anal.c10_ger_pessoa_id IS 'ID da Pessoa - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_ger_pessoa_endereco_id IS 'ID do Endereço da Pessoa - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_observacao1 IS 'Observação 1 - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_observacao2 IS 'Observação 2 - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_qnt_cot IS 'Quantidade - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_valor_unit_cot IS 'Valor Unitário - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_valor_total_cot IS 'Valor Total - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_valor_desc_cot IS 'Valor Desconto - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_valor_frete_cot IS 'Valor Frete - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_valor_outro_cot IS 'Valor Outros - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_valor_total_trib_cot IS 'Valor Total de Tributos - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_status IS 'Status - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_data_status IS 'Data do Status - C10';
COMMENT ON COLUMN mov_cotacao_anal.c10_system_user_id_aprov IS 'ID do Usuário Aprovador - C10';
COMMENT ON COLUMN mov_cotacao_anal.ger_itemserv_id IS 'ID do Item/Serviço';
COMMENT ON COLUMN mov_cotacao_anal.c01_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C01';
COMMENT ON COLUMN mov_cotacao_anal.c02_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C02';
COMMENT ON COLUMN mov_cotacao_anal.c03_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C03';
COMMENT ON COLUMN mov_cotacao_anal.c04_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C04';
COMMENT ON COLUMN mov_cotacao_anal.c05_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C05';
COMMENT ON COLUMN mov_cotacao_anal.c06_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C06';
COMMENT ON COLUMN mov_cotacao_anal.c07_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C07';
COMMENT ON COLUMN mov_cotacao_anal.c08_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C08';
COMMENT ON COLUMN mov_cotacao_anal.c09_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C09';
COMMENT ON COLUMN mov_cotacao_anal.c10_fin_cond_pagrec_id IS 'ID da Condiçao de Pag/Rec - C10';
            
ALTER TABLE mov_cotacao_anal OWNER TO postgres;

CREATE TABLE system_module (
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
name varchar(100)  NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
sigla_module varchar(50) NOT NULL,
system_id varchar(36) NOT NULL,
icon varchar(50) NOT NULL,
color varchar(50) NOT NULL,
CONSTRAINT pk_system_module PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE system_module IS 'System-Modulos';
COMMENT ON COLUMN system_module.id IS 'ID do Modulo';
COMMENT ON COLUMN system_module.name IS 'Nome';
COMMENT ON COLUMN system_module.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_module.log_date_ins IS 'Data de Inserção';
COMMENT ON COLUMN system_module.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_module.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_module.sigla_module IS 'Sigla do Modulo';
COMMENT ON COLUMN system_module.system_id IS 'ID do Sistema';
COMMENT ON COLUMN system_module.icon IS 'Icone do Modulo';
COMMENT ON COLUMN system_module.color IS 'Cor do Modulo';
ALTER TABLE system_module OWNER TO postgres;

CREATE TABLE system_param (
id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
log_user_ins varchar(100) ,
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100) ,
log_date_upd timestamp(0),
type varchar(250)  NOT NULL,
system_id varchar(36)  NOT NULL,
paramkey varchar(255)  NOT NULL,
paramvalue text  NOT NULL,
CONSTRAINT pk_system_param PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_system_param ON system_param USING btree (paramkey pg_catalog.text_ops ASC NULLS LAST, system_id pg_catalog.text_ops ASC NULLS LAST);
COMMENT ON TABLE system_param IS 'System-Parâmetro do Sistema';
COMMENT ON COLUMN system_param.id IS 'ID da Preferência';
COMMENT ON COLUMN system_param.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_param.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_param.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_param.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN system_param.type IS 'Tipo: TX-Texto,DT-Data,VR-Valor';
COMMENT ON COLUMN system_param.system_id IS 'ID do Sistema';
COMMENT ON COLUMN system_param.paramkey IS 'Chave do Parametro';
COMMENT ON COLUMN system_param.paramvalue IS 'Valor da Parâmetro';
ALTER TABLE system_param OWNER TO postgres;

CREATE TABLE system_program_favorite (
id varchar(36) NOT NULL,
system_user_id varchar(36),
system_program_id varchar(36),
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_system_program_favorite PRIMARY KEY (id) 
)
WITHOUT OIDS;
CREATE INDEX idx_sys_program_favorite_program ON system_program_favorite USING btree (system_program_id pg_catalog.text_ops ASC NULLS LAST);
CREATE INDEX idx_sys_program_favorite_user ON system_program_favorite USING btree (system_user_id ASC NULLS LAST);
COMMENT ON TABLE system_program_favorite IS 'System-Programa Favorito';
COMMENT ON COLUMN system_program_favorite.id IS 'ID do Programa Favorito';
COMMENT ON COLUMN system_program_favorite.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN system_program_favorite.system_program_id IS 'ID do Programa';
COMMENT ON COLUMN system_program_favorite.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN system_program_favorite.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN system_program_favorite.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN system_program_favorite.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE system_program_favorite OWNER TO postgres;

CREATE TABLE crm_tag (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
descritivo text NOT NULL,
ativo varchar(1) NOT NULL,
sigla_tag varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_crm_tag PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_tag IS 'Atendimento-Tag';
COMMENT ON COLUMN crm_tag.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_tag.id IS 'ID da Tag';
COMMENT ON COLUMN crm_tag.descritivo IS 'descritivo';
COMMENT ON COLUMN crm_tag.ativo IS 'Ativo';
COMMENT ON COLUMN crm_tag.sigla_tag IS 'Sigla do Tag';
COMMENT ON COLUMN crm_tag.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_tag.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_tag.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_tag.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE crm_tag OWNER TO postgres;

CREATE TABLE crm_mov_tag (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
crm_mov_id varchar(36) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
CONSTRAINT pk_crm_mov_tag PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_mov_tag IS 'Atendimento-Tag do Movimento';
COMMENT ON COLUMN crm_mov_tag.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_mov_tag.id IS 'ID da Tag do Movimento';
COMMENT ON COLUMN crm_mov_tag.crm_mov_id IS 'ID da Movimento';
COMMENT ON COLUMN crm_mov_tag.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_mov_tag.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_mov_tag.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_mov_tag.log_date_upd IS 'Log - Data de Alteração';
ALTER TABLE crm_mov_tag OWNER TO postgres;

CREATE TABLE crm_chat_grupo (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
nome varchar(100) NOT NULL,
ativo varchar(1) NOT NULL,
sigla_chat_grupo varchar(50) NOT NULL,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
log_user_upd varchar(100),
log_date_upd timestamp(0),
system_user_id_orig varchar(36) NOT NULL,
system_user_id_dest varchar(36),
tipo varchar(1) NOT NULL DEFAULT 'G',
senha varchar(100),
acesso_privado varchar(1) NOT NULL DEFAULT 'N',
CONSTRAINT pk_crm_chat_grupo PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_chat_grupo IS 'Atendimento-Grupo de Chat';
COMMENT ON COLUMN crm_chat_grupo.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_chat_grupo.id IS 'ID da Grupo do Chat';
COMMENT ON COLUMN crm_chat_grupo.nome IS 'Nome';
COMMENT ON COLUMN crm_chat_grupo.ativo IS 'Ativo';
COMMENT ON COLUMN crm_chat_grupo.sigla_chat_grupo IS 'Sigla da Classificação';
COMMENT ON COLUMN crm_chat_grupo.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_chat_grupo.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_chat_grupo.log_user_upd IS 'Log - Usuário de Alteração';
COMMENT ON COLUMN crm_chat_grupo.log_date_upd IS 'Log - Data de Alteração';
COMMENT ON COLUMN crm_chat_grupo.system_user_id_orig IS 'ID do Usuário - Origem';
COMMENT ON COLUMN crm_chat_grupo.system_user_id_dest IS 'ID do Usuário - Destino';
COMMENT ON COLUMN crm_chat_grupo.tipo IS 'Tipo: G-Grupo, U-Usuário';
COMMENT ON COLUMN crm_chat_grupo.senha IS 'Senha';
COMMENT ON COLUMN crm_chat_grupo.acesso_privado IS 'Acesso Privado';
ALTER TABLE crm_chat_grupo OWNER TO postgres;

CREATE TABLE crm_chat_msg (
unit_id varchar(36) NOT NULL,
id varchar(36) NOT NULL DEFAULT uuid_generate_v4(),
corpo text,
system_user_id_orig varchar(36) NOT NULL,
data_msg date,
log_user_ins varchar(100),
log_date_ins timestamp(0) DEFAULT now(),
ativo varchar(1),
crm_chat_grupo_id varchar(36) NOT NULL,
CONSTRAINT pk_crm_chat_msg PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_chat_msg IS 'Atendimento-Mensagens do Chat';
COMMENT ON COLUMN crm_chat_msg.unit_id IS 'ID da Unidade';
COMMENT ON COLUMN crm_chat_msg.id IS 'ID da Grupo do Chat';
COMMENT ON COLUMN crm_chat_msg.corpo IS 'Nome';
COMMENT ON COLUMN crm_chat_msg.system_user_id_orig IS 'ID do Usuário - Admin';
COMMENT ON COLUMN crm_chat_msg.data_msg IS 'Data da Mensagem';
COMMENT ON COLUMN crm_chat_msg.log_user_ins IS 'Log - Usuário de Inserção';
COMMENT ON COLUMN crm_chat_msg.log_date_ins IS 'Log - Data de Inserção';
COMMENT ON COLUMN crm_chat_msg.ativo IS 'Ativo';
COMMENT ON COLUMN crm_chat_msg.crm_chat_grupo_id IS 'ID do Grupo de Chat';
ALTER TABLE crm_chat_msg OWNER TO postgres;

CREATE TABLE crm_chat_grupo_usuario (
id varchar(36)  NOT NULL DEFAULT uuid_generate_v4(),
system_user_id varchar(36)  NOT NULL,
crm_chat_grupo_id varchar(36)  NOT NULL,
CONSTRAINT pk_crm_chat_grupo_usuario PRIMARY KEY (id) 
)
WITHOUT OIDS;
COMMENT ON TABLE crm_chat_grupo_usuario IS 'Atendimento-Grupo do Chat x Usuário';
COMMENT ON COLUMN crm_chat_grupo_usuario.id IS 'ID da Grupo do Chat x Usuário';
COMMENT ON COLUMN crm_chat_grupo_usuario.system_user_id IS 'ID do Usuário';
COMMENT ON COLUMN crm_chat_grupo_usuario.crm_chat_grupo_id IS 'ID da Grupo do Chat';
ALTER TABLE crm_chat_grupo_usuario OWNER TO postgres;

   
               """)
 

def downgrade():
    pass