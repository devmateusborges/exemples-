from app import db
from app.modules.sys.base.sys_model import Sys, SysChangeLog, SysDocument, SysDocumentCategory, SysDocumentGroup, SysDocumentUser, SysEmailLog, SysGroup, SysGroupProgram, SysGroupProgramFeature, SysLicence, SysLicenceDevice, SysMigration, SysModule, SysNotificationLog, SysPlan, SysPlanRestriction, SysProgram, SysProgramFavorite, SysProgramFeature, SysRestriction, SysRestrictionLicence, SysToken, SysTypeDescription, SysUnit, SysUser, SysUserGroup, SysUserProgramFeature
from app.utils.generic_schema import generic_schema
from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, fields,validate, validates, validates_schema
from app.utils.types_utils import TypeSN

from app.modules.sys.base.sys_types import TypeSysDocumentContentType, TypeSysUserOrigem, TypeSysprogram, TypeSysLicenceStatus, TypeSysPlan

ma = Marshmallow()

#==========================================================

class LoginSchema(ma.Schema):

    login = fields.Str(required=True)
    password = fields.Str(required=True)
    unit_id = fields.Str(required=True)
    
#==========================================================

class SysUnitSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysUnit
        sqla_session = db.session
        load_instance = True
        
    name =  fields.Str(required=True)
    sigla_unit =  fields.Str(required=True)
    active = fields.Str(load_default='S',validate=validate.OneOf(TypeSN.array))
    
#==========================================================

class SysUserSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysUser
        sqla_session = db.session
        load_instance = True
        
    login = fields.Str(required=True)
    password = fields.Str(required=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    active = fields.Str(load_default='S', validate=validate.OneOf(TypeSN.array))
    active_message = fields.Str(required=True)
    phone = fields.Str(required=True)
    document = fields.Str(required=True)
    admin = fields.Str(required=True)
    login_ext = fields.Str(required=True)
    frontpage_id = fields.Str(required=True)
    origem = fields.Str(required=True , validate=validate.OneOf(TypeSysUserOrigem.array))
    chat = fields.Str(required=True)
    image_url = fields.Str(required=True)
    email_verified = fields.Str(required=True)
    provider = fields.Str(required=True)
    provider_code = fields.Str(required=True)

#==========================================================

class SysDocumentCategorySchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysDocumentCategory
        sqla_session = db.session
        load_instance = True
        
    name =  fields.Str(required=True)
    active = fields.Str(load_default='S', validate=validate.OneOf(TypeSN.array))

#==========================================================

class  SysGroupSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysGroup
        sqla_session = db.session
        load_instance = True
        
    name =  fields.Str(required=True)

#==========================================================

class SysDocumentGroupSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysDocumentGroup
        sqla_session = db.session
        load_instance = True
        include_fk = True

    document_fk_id = fields.Str(required=True)
    document_fk_id_obj = fields.Nested('SysDocumentSchema')
    sys_group_fk_id = fields.Str(required=True)
    sys_group_fk_id_obj = fields.Nested('SysGroupSchema')

#==========================================================

class SysDocumentSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysDocument
        sqla_session = db.session
        load_instance = True
        include_fk = True
    
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    submission_date = fields.Str(required=True)
    
    filename = fields.Str(required=True)
    content_type = fields.Str(required=True,validate=validate.OneOf(TypeSysDocumentContentType.array))
    active = fields.Str(load_default='S',validate=validate.OneOf(TypeSN.array))
    archive_date = fields.Str(required=False)

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested('SysUserSchema')
   
    sys_category_id = fields.Str(required=True)
    sys_category_id_obj = fields.Nested('SysDocumentCategorySchema')

#===========================================================

class SysDocumentUserSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysDocumentUser
        sqla_session = db.session
        load_instance = True
        include_fk = True

    sys_document_id = fields.Str(required=True)
    sys_document_id_obj = fields.Nested('SysDocumentSchema')

    sys_user_id  = fields.Str(required=True)
    sys_user_id_obj  = fields.Nested('SysUserSchema')

#==========================================================

class SysGroupProgramSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysGroupProgram
        sqla_session = db.session
        load_instance = True
        include_fk = True

    sys_group_id = fields.Str(required=True)
    sys_group_id_obj = fields.Nested('SysGroupSchema')
   

    sys_program_id  = fields.Str(required=True)
    sys_program_id_obj = fields.Nested('SysProgramSchema')

#==========================================================

class SysUserGroupSchema(generic_schema,ma.SQLAlchemySchema):

    class Meta:
        model = SysUserGroup
        sqla_session = db.session
        load_instance = True
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested('SysUserSchema')

    sys_group_id= fields.Str(required=True)
    sys_group_id_obj = fields.Nested('SysGroupSchema')

#==========================================================

class SysRestrictionSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysRestriction
        sqla_session = db.session
        load_instance = True
        include_fk = True

    name =  fields.Str(required=True)

#==========================================================

class SysSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = Sys
        sqla_session = db.session
        load_instance = True
        include_fk = True

    name =  fields.Str(required=True)

#==========================================================

class SysModuleSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysModule
        sqla_session = db.session
        load_instance = True
        include_fk = True

    name =  fields.Str(required=True)
    sigla_module = fields.Str(required=True)
    icon  = fields.Str(required=True)
    color = fields.Str(required=True)

    sys_id = fields.Str(required=True)
    sys_id_obj = fields.Nested('SysSchema')

#==========================================================

class SysLicenceSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysLicence
        sqla_session = db.session
        load_instance = True
        include_fk = True

    tipo_doc =  fields.Str(required=True)
    nome_solicitante = fields.Str(required=True)
    doc  = fields.Str(required=True)
    end_logradouro = fields.Str(required=True)
    end_bairro =  fields.Str(required=True)
    end_numero = fields.Str(required=True)
    end_cidade  = fields.Str(required=True)
    end_pais = fields.Str(required=True)
    end_uf = fields.Str(required=True)
    log_date_ins =  fields.Str(required=True)
    status = fields.Str(required=True,validate=validate.OneOf(TypeSysLicenceStatus.array))
    status_data  = fields.Str(required=True)
    status_observacao = fields.Str(required=True)
    sys_version = fields.Str(required=True)
    chamado_id = fields.Str(required=True)
    sys_plan_id = fields.Str(required=True)
    sys_plan_id_obj = fields.Nested('SysPlanSchema')

    sys_id = fields.Str(required=True)
    sys_id_obj = fields.Nested('SysSchema')


    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested('SysUserSchema')

#==========================================================

class SysPlanSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysPlan
        sqla_session = db.session
        load_instance = True
        include_fk = True

    name =  fields.Str(required=True)
    type_plan= fields.Str(required=True, validate=validate.OneOf(TypeSysPlan.array))
    description  = fields.Str(required=True)

    sys_id = fields.Str(required=True)
    sys_id_obj = fields.Nested('SysSchema')

#==========================================================

class SysPlanRestrictionSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysPlanRestriction
        sqla_session = db.session
        load_instance = True
        include_fk = True

    value_restriction =  fields.Str(required=True)
    
    sys_plan_id= fields.Str(required=True)
    sys_plan_id_obj = fields.Nested('SysPlanSchema')

    sys_restriction_id = fields.Str(required=True)
    sys_restriction_id_obj = fields.Nested('SysRestrictionSchema')

#==========================================================

class SysRestrictionLicenceSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysRestrictionLicence
        sqla_session = db.session
        load_instance = True
        include_fk = True

    value_restriction =  fields.Str(required=True)
    
    sys_restriction_id = fields.Str(required=True)
    sys_restriction_id_obj = fields.Nested('SysRestrictionSchema')

    sys_licence_id = fields.Str(required=True)
    sys_licence_id_obj = fields.Nested('SysLicenceSchema')

#==========================================================

class SysProgramSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysProgram
        sqla_session = db.session
        load_instance = True
        include_fk = True

    name =  fields.Str(required=True)
    controller = fields.Str(required=True)
    menu  = fields.Str(required=True, validate=validate.OneOf(TypeSN.array))
    type_program = fields.Str(required=True, validate=validate.OneOf(TypeSysprogram.array))
    icon  =  fields.Str(required=True)
    admin = fields.Str(required=True, validate=validate.OneOf(TypeSN.array))

    sys_module_id= fields.Str(required=True)
    sys_module_id_obj = fields.Nested('SysModuleSchema')

#===========================================================>>>>>>>>

class SysGroupProgramFeatureSchema(generic_schema,ma.SQLAlchemySchema):

    class Meta:
        model = SysGroupProgramFeature
        sqla_session = db.session
        load_instance = True
        include_fk = True

    identity_feature =  fields.Str(required=True)

    sys_group_id = fields.Str(required=True)
    sys_group_id_obj = fields.Nested('SysGroupSchema')

    sys_program_id = fields.Str(required=True)
    sys_program_id_obj = fields.Nested('SysProgramSchema')

#==========================================================

class SysLicenceDeviceSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysLicenceDevice
        sqla_session = db.session
        load_instance = True
        include_fk = True

    sigla_device =  fields.Str(required=True)

    sys_licence_id = fields.Str(required=True)
    sys_licence_id_obj = fields.Nested('SysLicenceSchema')

#==========================================================

class SysProgramFavoriteSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysProgramFavorite
        sqla_session = db.session
        load_instance = True
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested('SysUserSchema')

    sys_program_id = fields.Str(required=True)
    sys_program_id_obj = fields.Nested('SysProgramSchema')

#==========================================================

class SysProgramFeatureSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model =SysProgramFeature
        sqla_session = db.session
        load_instance = True
        include_fk = True

    identity =  fields.Str(required=True)
    descricao =  fields.Str(required=True)

    sys_program_id  = fields.Str(required=True)
    sys_program_id_obj = fields.Nested('SysProgramSchema')

#==========================================================

class SysUserProgramFeatureSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysUserProgramFeature
        sqla_session = db.session
        load_instance = True
        include_fk = True

    identity_feature =  fields.Str(required=True)

    sys_program_id = fields.Str(required=True)
    sys_program_id_obj = fields.Nested('SysProgramSchema')

    sys_user_id = fields.Str(required=True)
    sys_user_id_obj = fields.Nested('SysUserSchema')

#==========================================================

class SysChangeLogSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysChangeLog
        sqla_session = db.session
        load_instance = True
        include_fk = True

    logdate = fields.Str(required=True)
    login = fields.Str(required=True)
    tablename = fields.Str(required=True)
    primarykey = fields.Str(required=True)
    pkvalue = fields.Str(required=True)
    operation = fields.Str(required=True)
    columnname = fields.Str(required=True)
    oldvalue = fields.Str(required=True)
    newvalue = fields.Str(required=True)
    access_ip = fields.Str(required=True)
    transaction_id = fields.Str(required=True)
    log_trace = fields.Str(required=True)
    session_id = fields.Str(required=True)
    class_name = fields.Str(required=True)
    php_sapi = fields.Str(required=True)
    log_year = fields.Str(required=True)
    log_month = fields.Str(required=True)
    log_day = fields.Str(required=True) 
    
#==========================================================

class SysEmailLogSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysEmailLog
        sqla_session = db.session
        load_instance = True
        include_fk = True

    sys_unit_id = fields.Str(required=True)
    sys_unit_id_obj = fields.Nested('SysUnitSchema')

    type_in_out= fields.Str(required=True)
    date_log  = fields.Str(required=True)
    email_from = fields.Str(required=True)
    subject  = fields.Str(required=True)
    body = fields.Str(required=True)
    error_message = fields.Str(required=True)
    email_to = fields.Str(required=True)
    login  = fields.Str(required=True)
    date_send = fields.Str(required=True)
    body_type = fields.Str(required=True)

#========================================================== 

class SysMigrationSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysMigration
        sqla_session = db.session
        load_instance = True
        include_fk = True

    version_num = fields.Str(required=True)


#========================================================== 

class SysNotificationLogSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysNotificationLog
        sqla_session = db.session
        load_instance = True
        include_fk = True

    sys_user_id = fields.Str(required=True)
    sys_user_to_id = fields.Str(required=True)

    email_to = fields.Str(required=True)
    subject = fields.Str(required=True)
    message = fields.Str(required=True)
    dt_message = fields.Str(required=True)
    type_notification = fields.Str(required=True)
    icon = fields.Str(required=True)
    checked = fields.Str(load_default='S', validate=validate.OneOf(TypeSN.array))
    action_url1 = fields.Str(required=True)
    action_label1 = fields.Str(required=True)
    action_body1 = fields.Str(required=True)
    action_header1 = fields.Str(required=True)
    action_type1 = fields.Str(required=True)
    action_url2 = fields.Str(required=True)
    action_label2 = fields.Str(required=True)
    action_body2 = fields.Str(required=True)
    action_header2 = fields.Str(required=True)
    action_type2 = fields.Str(required=True)
    action_url3 = fields.Str(required=True)
    action_label3 = fields.Str(required=True)
    action_body3 = fields.Str(required=True)
    action_header3 = fields.Str(required=True)
    action_type3 = fields.Str(required=True)

#==========================================================

class SysTokenSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysToken
        sqla_session = db.session
        load_instance = True
        include_fk = True

    dt_validade = fields.Str(required=True)
    dt_token = fields.Str(required=True) 
    token = fields.Str(required=True)
   
#==========================================================

class SysTypeDescriptionSchema(generic_schema,ma.SQLAlchemySchema):
    class Meta:
        model = SysTypeDescription
        sqla_session = db.session
        load_instance = True
        include_fk = True

    table_name = fields.Str(required=True)
    field_name = fields.Str(required=True) 
    value_type = fields.Str(required=True)
    description_type = fields.Str(required=True)