from alembic import op


revision = "202301060942001"
down_revision = "202211301615006"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
alter table sys_document add column fis_certificado_id varchar(36);
alter table sys_document add constraint fk_sys_document_fis_certificado_id foreign key (fis_certificado_id) references fis_certificado;
update sys_type_description set value_type = description_type, description_type = value_type where table_name = 'sys_document';
"""
    )


def downgrade():
    pass
