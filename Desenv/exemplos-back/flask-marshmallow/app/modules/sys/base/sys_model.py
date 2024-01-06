import uuid

from sqlalchemy import TIMESTAMP, Index, Integer, Text, text

from app.utils.generic_model import generic_model
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()

#==========================================================

class SysUnit(generic_model,db.Model):
    __tablename__ = 'sys_unit'
    __table_args__ = {'comment': 'System-Unidade (Base de Clientes)'}

    name = db.Column(db.String(100), comment='Nome')
    sigla_unit = db.Column(db.String(100), comment='Sigla da (Dono Unidade/Tenancy)')
    active = db.Column(db.String(1))
    
#==========================================================

class SysUser(generic_model,db.Model): 
    __tablename__ = 'sys_user'
    __table_args__ = {'comment': 'System-Usuário'}

    name = db.Column(db.String(100), comment='Nome')
    login = db.Column(db.String(100), unique=True, comment='Login')
    email = db.Column(db.String(100), unique=True, comment='Email')
    password = db.Column(db.String(100), comment='Password')
    active = db.Column(db.String(1), default='S',  comment='Ativo')
    active_message = db.Column(db.Text, default='N', comment='Mensagem de Ativação')
    phone = db.Column(db.String(50), comment='Telefone')
    document = db.Column(db.String(50), comment='Documento CPF / RG')
    admin = db.Column(db.String(1),  comment='Administrador')
    login_ext = db.Column(db.String(100), comment='Login externo')
    frontpage_id = db.Column(db.String(36), comment='ID do Programa - Inicial')
    origem = db.Column(db.String(1),  comment='Origem: 1-Local, 2-Chat')
    chat = db.Column(db.String(1), comment='Utiliza Chat')
    image_url = db.Column(db.String(1000), comment='Url da imagem do usuario')
    email_verified = db.Column(db.String(1), comment='Codigo do provider autenticado')
    provider = db.Column(db.String(50))
    provider_code = db.Column(db.String(50))

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)

#==========================================================

class SysDocumentCategory (generic_model, db.Model):
    __tablename__ = 'sys_document_category'
    __table_args__ = {'comment': 'System-Categoria Documento'}

    name = db.Column(db.String(100), comment='nome')
    active = db.Column(db.String(1), comment='active') 
 
#==========================================================

class SysGroup(generic_model, db.Model):
    __tablename__ = 'sys_group'
    __table_args__ = {'comment': 'System-Grupo de Acesso'} 

    name = db.Column(db.String(100), comment='Nome')
 
#==========================================================

class SysDocumentGroup(generic_model, db.Model):
    __tablename__ = 'sys_document_group'
    __table_args__ = {'comment': 'System-Documento  x Grupo'}

    document_id = db.Column(db.ForeignKey('sys_document.id'), comment='ID do Documento')
    document_id_obj = db.relationship('SysDocument')

    sys_group_id = db.Column(db.ForeignKey('sys_group.id'), comment='ID do Grupo de Acesso')
    sys_group_id_obj = db.relationship('SysGroup')

#==========================================================

class SysDocument(generic_model, db.Model):
    __tablename__ = 'sys_document'
    __table_args__ = {'comment': 'System-Documento'}

    
    title = db.Column(db.Text, comment='Titulo')
    description = db.Column(db.Text, comment='Descrição')
    submission_date = db.Column(db.Date, comment='Data de Submissão')
    
    filename = db.Column(db.Text, comment='Nome do Arquivo')
    content_type = db.Column(db.String(50), comment='Tipo de Conteudo')
    active = db.Column(db.Text, comment='active')
    archive_date = db.Column(db.Date, comment='Data de Arquivo', nullable=False)

    sys_user_id = db.Column(db.ForeignKey('sys_user.id'), comment='ID do Usuário')
    sys_user_id_obj = db.relationship('SysUser')
   
    sys_category_id = db.Column(db.ForeignKey('sys_document_category.id'), comment='ID da Categoria')
    sys_category_id_obj = db.relationship('SysDocumentCategory')

#==========================================================

class SysDocumentUser(generic_model, db.Model):
    __tablename__ = 'sys_document_user'
    __table_args__ = {'comment': 'System-Documento x Usuário'}

    sys_document_id = db.Column(db.ForeignKey('sys_document.id'), comment='ID do Documento')
    sys_document_id_obj = db.relationship('SysDocument')

    sys_user_id = db.Column(db.ForeignKey('sys_user.id'), comment='ID do Usuário')
    sys_user_id_obj = db.relationship('SysUser')

#==========================================================
#error sql 
class SysGroupProgram(generic_model, db.Model):
    __tablename__ = 'sys_group_program'
    __table_args__ = {'comment': 'System-Grupo de Acesso x Programa'}
  
    sys_group_id = db.Column(db.ForeignKey('sys_group.id'),index=True, comment='ID do Documento')

    sys_group_id_obj = db.relationship('SysGroup')
    
    sys_program_id = db.Column(db.ForeignKey('sys_program.id'), index=True,comment='ID do ProgamGrupo de Acesso')
    sys_program_id_obj = db.relationship('SysProgram')

#==========================================================

class SysUserGroup(generic_model, db.Model):
    __tablename__ = 'sys_user_group'
    __table_args__ = {'comment': 'System-Usuário x Grupo de Acesso'}

    sys_user_id = db.Column(db.ForeignKey('sys_user.id'), index=True, comment='ID do Usuário')
    sys_user_id_obj = db.relationship('SysUser')

    sys_group_id = db.Column(db.ForeignKey('sys_group.id'), index=True, comment='ID do Grupo de Acesso')
    sys_group_id_obj = db.relationship('SysGroup')

#==========================================================

class SysRestriction(generic_model, db.Model):
    __tablename__ = 'sys_restriction'
    __table_args__ = {'comment': 'System-Restrição de Sistema'}

    name = db.Column(db.String(100), comment='Nome')

#==========================================================

class Sys(generic_model, db.Model):
    __tablename__ = 'sys'
    __table_args__ = {'comment': 'System-Sistema'}

    name = db.Column(db.String(100), comment='Nome')

#==========================================================

class SysModule(generic_model, db.Model):
    __tablename__ = 'sys_module'
    __table_args__ = {'comment': 'System-Modulos'}

    name = db.Column(db.String(100),  comment='Nome')
    sigla_module = db.Column(db.String(50),  comment='Sigla do Modulo')

    sys_id = db.Column(db.ForeignKey('sys.id'),  comment='ID do Sistema')
    sys_id_obj = db.relationship('Sys')
    
    icon = db.Column(db.String(50),  comment='Icone do Modulo')
    color = db.Column(db.String(50),  comment='Cor do Modulo')

#==========================================================

class SysLicence(generic_model, db.Model):
    __tablename__ = 'sys_licence'
    __table_args__ = {'comment': 'System-Licenças'}

    tipo_doc = db.Column(db.String(100),  comment='Tipo Documento')
    nome_solicitante = db.Column(db.String(100),  comment='Nome da Solicitante')
    doc = db.Column(db.String(100), comment='Documento')
    end_logradouro = db.Column(db.String(100), comment='Endereço - Logradouro')
    end_bairro = db.Column(db.String(100), comment='Endereço - Bairro')
    end_numero = db.Column(db.String(100), comment='Endereço - Número')
    end_cidade = db.Column(db.String(100), comment='Endereço - Cidade')
    end_uf = db.Column(db.String(100), comment='Endereço - Unidade Federação')
    end_pais = db.Column(db.String(100), comment='Endereço - País')
    log_date_ins = db.Column(db.TIMESTAMP(),  server_default=text("now()"), comment='Log - Data de Inserção')
    status = db.Column(db.String(2),  comment='Status: AT-Ativo, PA-Pend. Ativação, PF-Pend. Financeira, IN-Inativa')
    status_data = db.Column(db.TIMESTAMP(),  server_default=text("now()"), comment='Data do Status')
    status_observacao = db.Column(db.String(250),  comment='Status Observação')
    sys_version = db.Column(db.String(50), comment='Versão do Cliente')
    chamado_id = db.Column(db.String(100), comment='Versão do Cliente')

    sys_plan_id = db.Column(db.ForeignKey('sys_plan.id'),  comment='ID do Plano de Utilização do Sistema')
    sys_plan_id_obj = db.relationship('SysPlan')

    sys_id = db.Column(db.ForeignKey('sys.id'),  comment='ID do Sistema')
    sys_id_obj = db.relationship('Sys')
    
    sys_user_id = db.Column(db.ForeignKey('sys_user.id', ondelete='CASCADE'), comment='ID do Usuário')
    sys_user_id_obj = db.relationship('SysUser')

#==========================================================
 
class SysPlan(generic_model, db.Model):
    __tablename__ = 'sys_plan'
    __table_args__ = {'comment': 'System-Plano de Utilização do Sistema'}

    name = db.Column(db.String(100), comment='Nome')
    type_plan = db.Column(db.String(2),  comment='Tipo: FR-Free, TR-Trial, PG-Pago')
    description = db.Column(Text,  comment='Descrição do Plano')
    
    sys_id = db.Column(db.ForeignKey('sys.id'),  comment='ID do Sistema')
    sys_id_obj = db.relationship('Sys')

#==========================================================

class SysPlanRestriction(generic_model, db.Model):
    __tablename__ = 'sys_plan_restriction'
    __table_args__ = {'comment': 'System-Plano de Utilização x Restrição'}

    sys_plan_id = db.Column(db.ForeignKey('sys_plan.id'),  comment='ID do Plano de Utilização do Sistema')
    sys_plan_id_obj = db.relationship('SysPlan')
    sys_restriction_id = db.Column(db.ForeignKey('sys_restriction.id'),  comment='ID da Restrição do Sistema')
    sys_restriction_id_obj = db.relationship('SysRestriction')
    
    value_restriction = db.Column(Integer,  server_default=text("1"), comment='Valor da Restrição') 

#==========================================================

class SysRestrictionLicence(generic_model, db.Model):
    __tablename__ = 'sys_restriction_licence'
    __table_args__ = {'comment': 'System-Restrição do Sistema x Licença'}

    sys_restriction_id = db.Column(db.ForeignKey('sys_restriction.id'),  comment='ID de Restrição do Sistema')
    sys_restriction_id_obj = db.relationship('SysRestriction')
    
    sys_licence_id = db.Column(db.ForeignKey('sys_licence.id', ondelete='CASCADE'),  comment='ID de Licença')
    sys_licence_id_obj = db.relationship('SysLicence')

    value_restriction = db.Column(Integer,  comment='Valor de Restrição')
  
#==========================================================

class SysProgram(generic_model, db.Model):
    __tablename__ = 'sys_program'
    __table_args__ = {'comment': 'System-Grupo de Acesso x Programa'}
    
    name = db.Column(db.String(100), comment='Nome')
    controller = db.Column(db.String(100),  comment='tipo : Controller')
    menu = db.Column(db.String(1),  comment='tipo: menu')
    type_program = db.Column(db.String(1),  comment='tipo ')
    icon = db.Column(db.String(50),  comment='tipo ')
    admin = db.Column(db.String(1),  comment='admin ')

    sys_module_id= db.Column(db.ForeignKey('sys_module.id'), index=True)
    sys_module_id_obj = db.relationship('SysModule')
 
#==========================================================>>>>>>>>

class SysGroupProgramFeature(generic_model, db.Model):
    __tablename__ = 'sys_group_program_feature'
    __table_args__ = {'comment': 'Sistema - Grupo - Features do Programa'}

    identity_feature = db.Column(db.String(200),  comment='Identificador da feature')

    sys_group_id = db.Column(db.ForeignKey('sys_group.id'),  comment='ID do Grupo')
    sys_group_id_obj = db.relationship('SysGroup')

    sys_program_id = db.Column(db.ForeignKey('sys_program.id'),  comment='ID do Programa')
    sys_program_id_obj = db.relationship('SysProgram')

#==========================================================

class SysLicenceDevice(generic_model, db.Model):
    __tablename__ = 'sys_licence_device'
    __table_args__ = {'comment': 'System-Dispositivos da Licença'}

    sigla_device = db.Column(db.String(100),  comment='Identifcador do Dispositivo (Mac,UUid,Etc)')

    sys_licence_id = db.Column(db.ForeignKey('sys_licence.id'),  comment='ID da Licença')
    sys_licence_id_obj = db.relationship('SysLicence')
    
#==========================================================

class SysProgramFavorite(generic_model, db.Model):
    __tablename__ = 'sys_program_favorite'
    __table_args__ = {'comment': 'System-Programa Favorito'}

    sys_user_id = db.Column(db.ForeignKey('sys_user.id'), index=True, comment='ID do Usuário')
    sys_user_id_obj = db.relationship('SysUser')

    sys_program_id = db.Column(db.ForeignKey('sys_program.id'), index=True, comment='ID do Programa')
    sys_program_id_obj = db.relationship('SysProgram')

#===========================================================

class SysProgramFeature(generic_model, db.Model):
    __tablename__ = 'sys_program_feature'
    __table_args__ = {'comment': 'Sistema - Features do Programa'}

    
    identity = db.Column(db.String(200),  comment='Identificador da feature')
    descricao = db.Column(Text, comment='Descrição da feature')
    
    sys_program_id = db.Column(db.ForeignKey('sys_program.id'),  comment='ID do Programa')
    sys_program_id_obj = db.relationship('SysProgram')

#===========================================================
   
class SysUserProgramFeature(generic_model, db.Model):
    __tablename__ = 'sys_user_program_feature'
    __table_args__ = {'comment': 'Sistema - Usuário - Features do Programa'}


    identity_feature = db.Column(db.String(200),  comment='Identificador da feature')

    sys_program_id = db.Column(db.ForeignKey('sys_program.id'),  comment='ID do Programa')
    sys_program_id_obj = db.relationship('SysProgram')

    sys_user_id = db.Column(db.ForeignKey('sys_user.id'),  comment='ID do Usuário')
    sys_user_id_obj = db.relationship('SysUser')

#===========================================================

class SysChangeLog(generic_model, db.Model):
    __tablename__ = 'sys_change_log'
    __table_args__ = {'comment': 'System-Log de Alterações'}

    
    logdate = db.Column(db.TIMESTAMP(), comment='Data do Log')
    login = db.Column(Text, comment='Login')
    tablename = db.Column(Text, comment='Nome da Tabela')
    primarykey = db.Column(Text, comment='Chave Primária')
    pkvalue = db.Column(Text, comment='Valor da Chave')
    operation = db.Column(Text, comment='Operação')
    columnname = db.Column(Text, comment='Nome da Coluna')
    oldvalue = db.Column(Text, comment='Valor Antigo')
    newvalue = db.Column(Text, comment='Valor Novo')
    access_ip = db.Column(Text, comment='IP do Acesso')
    transaction_id = db.Column(Text, comment='ID da Transação')
    log_trace = db.Column(Text, comment='Log do Trace')
    session_id = db.Column(Text, comment='ID da Sessão')
    class_name = db.Column(Text, comment='Nome da Classe')
    php_sapi = db.Column(Text, comment='PHP Sapi')
    log_year = db.Column(db.String(4), comment='Ano do Log')
    log_month = db.Column(db.String(2), comment='Mês do Log')
    log_day = db.Column(db.String(2), comment='Dia do Log')    

#===========================================================

class SysEmailLog(generic_model, db.Model):
    __tablename__ = 'sys_email_log'
    __table_args__ = {'comment': 'System-Log de envio de Email'}

    sys_unit_id = db.Column(db.ForeignKey('sys_unit.id'), index=True)
    sys_unit_id_obj = db.relationship('SysUnit')

    type_in_out = db.Column(db.String(2),  comment='Tipo Entrada ou Saída')
    date_log = db.Column(db.TIMESTAMP(),  server_default=text("now()"), comment='Data/Hora do Log')
    email_from = db.Column(Text,  comment='Email - De')
    subject = db.Column(Text,  comment='Assunto')
    body = db.Column(Text, comment='Corpo')
    error_message = db.Column(Text, comment='Mensagem de Erro')
    email_to = db.Column(Text,  comment='Email - Para')
    login = db.Column(db.String(50), comment='Login')
    date_send = db.Column(db.TIMESTAMP(), comment='Data/Hora de Envio')
    body_type = db.Column(db.String(50), comment='Tipo do Corpo: text;html')

#==========================================================

class SysMigration(generic_model, db.Model):
    __tablename__ = 'sys_migration'

    version_num = db.Column(db.String(32), primary_key=True)

#==========================================================

class SysNotificationLog(generic_model, db.Model):
    __tablename__ = 'sys_notification_log'
    __table_args__ = {'comment': 'Systtem-Notificações-Log'}

    sys_user_id = db.Column(db.ForeignKey('sys_user.id'), index=True)
    sys_user_id_obj = db.relationship('SysUser')

    sys_user_to_id = db.Column(db.String(36),  comment='ID do Usuário - Destinatário')
    email_to = db.Column(db.String(100), comment='Email - Destinatário')
    subject = db.Column(Text,  comment='Assunto')
    message = db.Column(Text,  comment='Mensagem')
    dt_message = db.Column(Text,  comment='Data da Mensagem')
    type_notification = db.Column(db.String(50), comment='Tipo de Notificação: INVITE, OUTHER')
    icon = db.Column(Text, comment='Icone')
    checked = db.Column(db.CHAR(1),  comment='Checado: S-Sim,N-Não')
    action_url1 = db.Column(Text, comment='URL da Ação - 1')
    action_label1 = db.Column(Text, comment='Label da Ação - 1')
    action_body1 = db.Column(Text, comment='Corpo da request - 1')
    action_header1 = db.Column(Text, comment='Header da request - 1')
    action_type1 = db.Column(Text, comment='Tipo da request - 1')
    action_url2 = db.Column(Text, comment='URL da Ação - 2')
    action_label2 = db.Column(Text, comment='Label da Ação - 2')
    action_body2 = db.Column(Text, comment='Corpo da request - 2')
    action_header2 = db.Column(Text, comment='Header da request - 2')
    action_type2 = db.Column(Text, comment='Tipo da request - 2')
    action_url3 = db.Column(Text, comment='URL da Ação - 3')
    action_label3 = db.Column(Text, comment='Label da Ação - 3')
    action_body3 = db.Column(Text, comment='Corpo da request - 3')
    action_header3 = db.Column(Text, comment='Header da request - 3')
    action_type3 = db.Column(Text, comment='Tipo da request - 3')

#==========================================================

class SysToken(generic_model, db.Model):
    __tablename__ = 'sys_token'
    __table_args__ = {'comment': 'System-Token'}

    dt_validade = db.Column(db.TIMESTAMP(),  comment='Data de validade do Token')
    dt_token = db.Column(db.TIMESTAMP(),  comment='Data do Token')
    token = db.Column(Text,  unique=True, comment='Token')

#==========================================================

class SysTypeDescription(generic_model, db.Model):
    __tablename__ = 'sys_type_description'
    __table_args__ = ( Index('idx_sys_type_description', 'table_name', 'field_name', 'value_type', unique=True),
        {'comment': 'System-Descrição de Tipos'}
    )

    table_name = db.Column(db.String(100),  comment='Nome da Tabela')
    field_name = db.Column(db.String(100),  comment='Nome Campo')
    value_type = db.Column(db.String(50),  comment='Valor do Tipo')
    description_type = db.Column(db.String(100),  comment='Descrição do Valor')
   