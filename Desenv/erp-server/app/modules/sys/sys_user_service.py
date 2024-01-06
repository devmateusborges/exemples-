from app.env import APP_SERVER_URL, MAIL_SMTP_FROM, WEBSITE_BRAND_RESUME, APP_ERP_URL
from app.generics.generic_service import generic_service
from app.modules.sys.base.sys_model import SysUser
from app.modules.sys.sys_token_service import sys_token_service
from app.utils.email_util import email_util
from passlib.hash import pbkdf2_sha256
from flask import current_app
import random
from app.modules.sys.base.sys_serealizer import SysUserSchema
import json
from app.exceptions.ApiException import ApiException


class SysUser_service(generic_service):
    # ==============================

    def sendActivationEmail(self, obj: SysUser):
        srvEmail = email_util()
        srvToken = sys_token_service()
        data_token = {"login": obj.login}
        token = srvToken.generate_token(
            session=current_app.db.session, hours=36, data_token=data_token
        )
        # ================

        template_data = {
            "text_to": obj.name,
            "text_body": "Your login has been created, please check your email for validation and continue accessing",
            "text_button": "Validate my login",
            "url_button": str(APP_SERVER_URL)
            + "/api/auth/registervalidate?token="
            + token,
        }
        # ================

        srvEmail.send_mail_template(
            to_email=obj.email,
            from_email=MAIL_SMTP_FROM,
            subject=str(WEBSITE_BRAND_RESUME) + " - Validation of your login",
            template_name="generic_email",
            template_data=template_data,
        )

    # ==============================
    def redefinePassword(self, user_instance, body):
        new_password_sha256 = pbkdf2_sha256.hash(body["newpassword"])
        user_instance["password"] = new_password_sha256

        current_app.db.session.add(SysUserSchema().load(user_instance))

    # ==============================
    def resetPassword(self, user_instance):
        new_password = ""

        for i in range(0, 14):
            x = random.randint(1, 100)
            new_password += str(x)

        new_password_sha256 = pbkdf2_sha256.hash(new_password)
        user_instance["password"] = new_password_sha256
        # ================

        srvEmail = email_util()
        template_data = {
            "text_to": user_instance["name"] + " Your password has been reseted",
            "text_body": new_password,
            "text_button": "Return to login",
            "url_button": str(APP_ERP_URL) + "/web/signin",
        }
        # ================

        srvEmail.send_mail_template(
            to_email=user_instance["email"],
            from_email=MAIL_SMTP_FROM,
            subject=str(WEBSITE_BRAND_RESUME) + " - Password reseted",
            template_name="generic_email",
            template_data=template_data,
        )

        current_app.db.session.add(SysUserSchema().load(user_instance))

    # ==============================
    def sendRedefinePasswordEmail(self, obj: SysUser, body):
        srvEmail = email_util()
        srvToken = sys_token_service()
        bodyAux = json.dumps(body, separators=(",", ":"))
        data_token = {"login": obj["login"], "body": bodyAux}
        token = srvToken.generate_token(
            session=current_app.db.session, hours=36, data_token=data_token
        )
        # ================

        template_data = {
            "text_to": obj["name"],
            "text_body": "Please check your email for validation and continue redefining password",
            "text_button": "Yes redefine password",
            "url_button": f"{str(APP_SERVER_URL)}/api/auth/passwordredefinevalidate?token={token}",
            "text_button_2": "If not you, deactivate this user",
            "url_button_2": f"{str(APP_SERVER_URL)}/api/auth/deactivateuser?token={token}",
        }
        # ================

        srvEmail.send_mail_template(
            to_email=obj["email"],
            from_email=MAIL_SMTP_FROM,
            subject=str(WEBSITE_BRAND_RESUME)
            + " - Validation of your password redefine",
            template_name="redefine_password_email",
            template_data=template_data,
        )

    # ==============================
    def sendResetPasswordEmail(self, obj: SysUser):
        srvEmail = email_util()
        srvToken = sys_token_service()
        data_token = {"login": obj.login}
        token = srvToken.generate_token(
            session=current_app.db.session, hours=36, data_token=data_token
        )
        # ================

        template_data = {
            "text_to": obj.name,
            "text_body": "Please check your email for validation and an email will be sent with the new password",
            "text_button": "Yes reset password",
            "url_button": f"{str(APP_SERVER_URL)}/api/auth/passwordresetvalidate?token={token}",
            "text_button_2": "If not you, deactivate this user",
            "url_button_2": f"{str(APP_SERVER_URL)}/api/auth/deactivateuser?token={token}",
        }
        # ================

        srvEmail.send_mail_template(
            to_email=obj.email,
            from_email=MAIL_SMTP_FROM,
            subject=str(WEBSITE_BRAND_RESUME) + " - Validation of your password reset",
            template_name="redefine_password_email",
            template_data=template_data,
        )

    def deactivateuser(self, obj: SysUser):
        obj["active"] = "N"
        obj["active_message"] = "INATIVO_POR_REDEF_SENHA"
        current_app.db.session.add(SysUserSchema().load(obj))
