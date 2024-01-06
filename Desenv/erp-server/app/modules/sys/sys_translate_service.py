import uuid
from flask import current_app
from app.env import GOOGLE_API_CLIENT
from app.exceptions.ApiException import ApiException
from app.generics.generic_service import generic_service
import gspread

from app.modules.sys.base.sys_model import SysTranslate, SysTranslateLang


class sys_translate_service(generic_service):

    # ==============================
    def update_from_google_sheet(self):
        # ==============================
        gc = gspread.service_account_from_dict(GOOGLE_API_CLIENT)
        sh = gc.open_by_key("1NMQPEUyXT4tbd7CyPaz3-hOMgvLwIzfs-WdsJiG4Bls")
        worksheet = sh.worksheet("Translate")
        vals = worksheet.get_all_values()
        rows = 0

        # ==============================
        current_app.db.session.query(SysTranslate).delete()

        langs = (
            current_app.db.session.query(SysTranslateLang)
            .filter(SysTranslateLang.code != "TST1")
            .all()
        )
        # ==============================
        valLang = 2
        for lang in langs:

            # ==============================
            for val in vals:
                if val[0] != "TERMO_CODE":
                    trans = SysTranslate()
                    trans.id = uuid.uuid4()
                    trans.sys_translate_lang_id = lang.id
                    trans.term_group = "DEFAULT"
                    trans.term_orig = val[0]
                    trans.term_translate = val[valLang]

                    rows = rows + 1
                    current_app.db.session.add(trans)

            valLang = valLang + 1

            current_app.db.session.commit()

        current_app.db.session.close()

        return {"code": "200", "msg": "Successfully update [" + str(rows) + "] rows"}

    # ==============================
    def get_term_translate(self, plang, pterm_group, pterm_orig):
        try:
            cache_key = f"TRANSLATE-{plang}-{pterm_group}-{pterm_orig}"
            cache_trans = current_app.cache.get(cache_key)
            if cache_trans is None:
                term_translate = (
                    current_app.db.session.query(SysTranslate, SysTranslateLang)
                    .filter(SysTranslate.sys_translate_lang_id == SysTranslateLang.id)
                    .filter(SysTranslateLang.code == plang)
                    .filter(SysTranslate.term_group == pterm_group)
                    .filter(SysTranslate.term_orig == pterm_orig)
                    .first()
                )

                if term_translate is None:
                    cache_trans = pterm_orig
                else:
                    cache_trans = term_translate[0].term_translate

                current_app.cache.set(cache_key, cache_trans)

            return cache_trans
        except Exception as e:
            raise ApiException(
                message={
                    "error": f"Error get_term_translate: plang [{plang}] pterm_group [{pterm_group}] pterm_orig [{pterm_orig}]"
                },
                name="VALIDATION_ERROR",
                status_code=400,
            )
