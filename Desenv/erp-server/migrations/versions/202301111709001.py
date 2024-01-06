from alembic import op


revision = "202301111709001"
down_revision = "202301060942001"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
insert into sys_program (id, name, controller, menu, type_program, sys_module_id, icon, admin, active, code_program)
values ('77f9a7ee-d06e-45f9-b835-11b1e04e7517', 'Redefinir senha', '/private/sys/redefinepassword', 'S', 'T', 'ca29f487-243f-4c94-8a39-7c3faca63e90', 'mdi mdi-table', 'N', 'S', '1185');
  
insert into sys_group_program (id, sys_group_id, sys_program_id) values ('4eba28b7-5199-41a2-a2a7-739405994790', '0256e515-51a4-49a2-a8b8-adc36470cd51', '77f9a7ee-d06e-45f9-b835-11b1e04e7517');
insert into sys_group_program (id, sys_group_id, sys_program_id) values ('6935248c-55a0-4e57-aaaf-1c4287b14f5f', '4218d8f1-8595-4052-aace-ba36f772623e', '77f9a7ee-d06e-45f9-b835-11b1e04e7517');

insert into sys_type_description (id, table_name, field_name, value_type, description_type) 
values ('543205d6-978f-4f1b-ba69-3ec43826eb05', 'sys_user', 'active_message', 'REDEFINIR_SENHA', 'Redefinir senha');

insert into sys_type_description (id, table_name, field_name, value_type, description_type) 
values ('6ea0daaf-fe41-4e4d-907c-3a1d66fdd278', 'sys_user', 'active_message', 'NOVO_USUARIO', 'Novo usuário');

insert into sys_type_description (id, table_name, field_name, value_type, description_type) 
values ('8cc49815-836d-4e2c-a110-c7bfc0a345ff', 'sys_user', 'active_message', 'TEMPORARIO', 'Temporario');

insert into sys_type_description (id, table_name, field_name, value_type, description_type) 
values ('f8ffdc85-e35e-40a7-a7fb-078506a6cb23', 'sys_user', 'active_message', 'PADRAO', 'Padrão');

insert into sys_type_description (id, table_name, field_name, value_type, description_type) 
values ('842a6c5e-89eb-4c97-b182-742c41a8a39a', 'sys_user', 'active_message', 'INATIVO_POR_REDEF_SENHA', 'IN18INATIVOPORREDEFSENHA');
"""
    )


def downgrade():
    pass
