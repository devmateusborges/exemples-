import datetime
import uuid
from flask import current_app, send_from_directory
from sqlalchemy import column


from app.env import STORAGE_UPLOAD_FOLDER
from app.exceptions.ApiException import ApiException
from app.generics.generic_service import generic_service

import base64
import os

from app.modules.sys.base.sys_model import SysDocument
from app.utils.funcs_util import funcs_util


class sys_document_service(generic_service):
    def delete_files(self, documents, orphans):
        for doc in documents:
            orphans = orphans.filter(SysDocument.id != doc["id"])
        # ==============================
        for doc in orphans.all():
            file_name_id_old = str(doc.id) + "-" + doc.filename
            file_path_old = "app/" + STORAGE_UPLOAD_FOLDER + "/" + file_name_id_old
            # ==============================
            if os.path.exists(file_path_old):
                os.remove(file_path_old)

    def handle_delete_files(
        self, docFieldName, parentPk, parentFieldName, body, childsFieldName=None
    ):
        parentId = funcs_util.getAttr(body, parentPk)
        documents = body[docFieldName]
        # ======================== Parent
        orphans = current_app.db.session.query(SysDocument).filter(
            column(parentFieldName) == parentId
        )
        self.delete_files(documents, orphans)
        # ======================== Chields
        if childsFieldName is not None:
            for docChield in childsFieldName:
                if len(body[docChield["fieldName"]]) > 0:
                    for docChieldObj in body[docChield["fieldName"]]:
                        chieldDocuments = docChieldObj[docChield["docFieldName"]]
                        chieldId = funcs_util.getAttr(docChieldObj, docChield["pk"])
                        chiedlOrphans = current_app.db.session.query(
                            SysDocument
                        ).filter(column(docChield["fieldNameId"]) == chieldId)

                        self.delete_files(chieldDocuments, chiedlOrphans)
                else:
                    chiedlOrphans = current_app.db.session.query(SysDocument).filter(
                        column(docChield["fieldNameId"]).like("%")
                    )

                    self.delete_files([], chiedlOrphans)

    def save_files(self, document):
        documentSrv = sys_document_service(SysDocument)

        contenttype = document.get("content_type")
        documentId = document.get("id")
        filename = document.get("filename")
        file64 = document.get("file64")
        # ========================
        if file64 is not None:
            documentSrv.uploadfile(
                sys_document_id=documentId,
                file_base64=file64,
                filename=filename,
                file_content_type=contenttype,
                storage_type=1,
            )

    def handle_save_files(self, docFieldName, body, docChildsFieldName=None):
        # ======================== Parent
        for document in body[docFieldName]:
            self.save_files(document)
        # ======================== Chields
        if docChildsFieldName is not None:
            for docChield in docChildsFieldName:
                for docChieldObj in body[docChield["fieldName"]]:
                    for document in docChieldObj[docChield["docFieldName"]]:
                        self.save_files(document)

    def uploadfile(
        self, sys_document_id, file_base64, filename, file_content_type, storage_type
    ):

        document = self.find_by_id(sys_document_id)

        if filename != document.filename:
            raise ApiException(
                message={"filename": "File name not equal file saved"},
                name="VALIDATION_ERROR",
            )

        if file_content_type != document.content_type:
            raise ApiException(
                message={"file_content_type": "Content Type not equal file saved"},
                name="VALIDATION_ERROR",
            )

        file_content = base64.b64decode(file_base64)
        file_name_id = str(sys_document_id) + "-" + filename

        file_path = "app/" + STORAGE_UPLOAD_FOLDER + "/" + file_name_id

        if storage_type == 1:

            if not os.path.isdir("app/" + STORAGE_UPLOAD_FOLDER):
                os.mkdir("app/" + STORAGE_UPLOAD_FOLDER)

            # Deleta se existir antigo
            if document.filename is not None:
                file_name_id_old = str(sys_document_id) + "-" + document.filename
                file_path_old = "app/" + STORAGE_UPLOAD_FOLDER + "/" + file_name_id_old
                if os.path.exists(file_path_old):
                    os.remove(file_path_old)

            with open(file_path, "wb") as file:
                file.write(file_content)

                self.save(document)

                file.close()

            return {"sys_document_id": sys_document_id, "upload": True}

        elif storage_type == 2:
            pass
            # TODO Implementar cloud DO

    # ==============================
    def download(self, sys_document_id, storage_type):

        if storage_type == 1:
            document = self.find_by_id(sys_document_id)
            filename = sys_document_id + "-" + str(document.filename)

            if document.id != sys_document_id:
                raise ApiException(
                    message={"id": "File id not equal exist"}, name="VALIDATION_ERROR"
                )

            if document.id == sys_document_id:

                return send_from_directory(
                    directory=STORAGE_UPLOAD_FOLDER, path=filename
                )
        elif storage_type == 2:
            pass
            # TODO Implementar cloud DO

    # ==============================
    def download_open(self, filename):
        return send_from_directory(
            directory=STORAGE_UPLOAD_FOLDER, path=filename, as_attachment=True
        )

    # ==============================
    def active(self, obj):

        if obj.active == "S":
            obj.archive_date
        elif obj.active == "N":
            obj.archive_date = None

        return self.save(obj)
