import json
import os
import re
import uuid
from app.env import (
    DB_DATABASE,
    DB_HOST,
    DB_PASSWORD,
    DB_PORT,
    DB_USERNAME,
    REPORT_FOLDER,
    STORAGE_UPLOAD_FOLDER,
)
from app.exceptions.ApiException import ApiException
from app.generics.generic_service import generic_service
from app.modules.ind.base.ind_model import IndPrm, IndRel, IndRelPrm
from app.modules.ind.base.ind_type import TypeIndReportFormat
from app.modules.sys.base.sys_model import SysDocument
from app.modules.sys.sys_document_service import sys_document_service
from app.utils.funcs_util import funcs_util
from pyreportjasper import PyReportJasper


class ind_rel_service(generic_service):

    # ==============================
    def generate_report(self, session, body):
        paramsFinal = {}
        paramsFinalTypeL = []
        # ================
        internals = body.get("internals")
        if internals is None:
            raise ApiException(
                message=f"Param is required",
                name="VALIDATION_ERROR",
                status_code=400,
            )
        # ================
        params = body.get("params")
        if params is None:
            raise ApiException(
                message=f"Param is required",
                name="VALIDATION_ERROR",
                status_code=400,
            )
        # ================
        queue = body.get("queue")
        if queue is None:
            raise ApiException(
                message=f"Param [queue] is required",
                name="VALIDATION_ERROR",
                status_code=400,
            )
        # ================
        internalsRequireds = [
            "reportFormat",
            "pParTitleReport",
            "pParUnitId",
            "pParIndRelId",
            "pParUser",
        ]

        # Valida parametros envidados existem
        # ================
        for d in internals:
            vparNomeTec = d["parNomeTec"]
            try:
                internalsRequireds.index(vparNomeTec)
            except ValueError:
                raise ApiException(
                    message=f"Param [{vparNomeTec}] internal is not exists",
                    name="VALIDATION_ERROR",
                    status_code=400,
                )

            paramsFinal[d["parNomeTec"]] = d["parValor"]

        # Valida parametros envidados estao faltando
        # ================
        for d in internalsRequireds:
            internalsUrlExists = funcs_util.findListDict(
                ListDict=internals, searchField="parNomeTec", searchValue=d
            )
            if internalsUrlExists is None:
                raise ApiException(
                    message=f"Param [{d}] internal is required",
                    name="VALIDATION_ERROR",
                    status_code=400,
                )

        # Busca todos parametros do rel
        # ================
        ind_rel_id = paramsFinal["pParIndRelId"]
        reportFormat = paramsFinal["reportFormat"]

        ind_rel_prms = (
            session.query(IndPrm, IndRelPrm, IndRel)
            .filter(IndPrm.id == IndRelPrm.ind_prm_id)
            .filter(IndRel.id == IndRelPrm.ind_rel_id)
            .filter(IndRelPrm.ind_rel_id == ind_rel_id)
            .filter(IndPrm.ativo == "S")
            .filter(IndRel.ativo == "S")
            .all()
        )
        # ================
        if ind_rel_prms is None or ind_rel_prms == []:
            raise ApiException(
                message=f"Report ID [{ind_rel_id}] not exists",
                name="VALIDATION_ERROR",
                status_code=400,
            )
        # Valida parametros envidados existem
        # ================
        for p in params:
            vparNomeTec = p["parNomeTec"]
            irpExists = False
            for irp in ind_rel_prms:
                if irp[0].nome_tecnico == vparNomeTec:
                    irpExists = True

            if not irpExists:
                raise ApiException(
                    message=f"Param [{vparNomeTec}] specific is not exists",
                    name="VALIDATION_ERROR",
                    status_code=400,
                )
        # Valida parametros envidados estao faltando
        # ================

        for irp in ind_rel_prms:
            tipo_rel = irp[2].tipo

            # Diferente de Internal
            if irp[0].internal != "S":
                # ================
                vparNomeTec = irp[0].nome_tecnico
                paramsUrlExists = funcs_util.findListDict(
                    ListDict=params, searchField="parNomeTec", searchValue=vparNomeTec
                )
                # ================
                if paramsUrlExists is None:
                    raise ApiException(
                        message=f"Param [{vparNomeTec}] specific is required",
                        name="VALIDATION_ERROR",
                        status_code=400,
                    )
                # ================
                valorParam = str(paramsUrlExists["parValor"])
                if irp[0].obrigatorio == "S" and (
                    irp[0].valor_padrao is None or irp[0].valor_padrao == ""
                ):
                    # ================
                    if valorParam is None or valorParam == "":
                        raise ApiException(
                            message=f"Param [{vparNomeTec}] specific value is required",
                            name="VALIDATION_ERROR",
                            status_code=400,
                        )
                # ================
                if valorParam is None or valorParam == "":
                    if irp[0].valor_padrao is not None and irp[0].valor_padrao != "":
                        valorParam = str(irp[0].valor_padrao)
                # ================
                if irp[0].valor_prefixo is not None and irp[0].valor_prefixo != "":
                    valorParam = str(irp[0].valor_prefixo) + str(valorParam)
                # ================
                if irp[0].valor_sufixo is not None and irp[0].valor_sufixo != "":
                    valorParam = str(valorParam) + str(irp[0].valor_sufixo)
                # ================
                if tipo_rel in ("R", "C"):
                    nome_tecnico_rel = irp[2].nome_tecnico
                    paramsFinal[vparNomeTec] = valorParam
                elif tipo_rel in ("L"):
                    nome_tecnico_rel = "reportlist"
                    paramsFinalTypeL.append(
                        {"parNomeTec": vparNomeTec, "parValor": valorParam}
                    )
                else:
                    raise ApiException(
                        message=f"Type report not implemented",
                        name="VALIDATION_ERROR",
                        status_code=400,
                    )

        # ================
        if tipo_rel == "L":
            # ================
            cols = body.get("cols")
            if cols is None:
                raise ApiException(
                    message=f"Cols is required",
                    name="VALIDATION_ERROR",
                    status_code=400,
                )
            # ================

            paramsFinalTypeLText = json.dumps(
                {"params": paramsFinalTypeL, "cols": cols}
            )
            paramsFinalTypeLTextAux = re.sub('"', "%22", paramsFinalTypeLText)

            paramsFinal["pParParams"] = paramsFinalTypeLTextAux

        # ================
        result = None
        if queue == "S":
            raise ApiException(
                message=f"Generated queue not implemented",
                name="VALIDATION_ERROR",
                status_code=400,
            )
            result = {
                "generated": "S",
                "sys_process_log": "xx",
                "queue_id": "",
                "params": paramsFinal,
            }
        else:
            result_process_report = self.process_report(
                report_name=nome_tecnico_rel, params=paramsFinal, format=reportFormat
            )

            result = {
                "generated": result_process_report.get("generated"),
                "sys_process_log": "xx",
                "queue_id": "",
                "params": paramsFinal,
                "report_name_generated": result_process_report.get(
                    "report_name_generated"
                ),
            }

        return result

    def process_report(self, report_name, params, open=False, format="pdf"):
        srvDoc = sys_document_service(model=SysDocument)
        # ================
        name_file = report_name
        # ================
        input_base_file = "app" + os.sep + REPORT_FOLDER
        input_file = os.path.join(input_base_file, name_file + ".jasper")
        # ================
        output_base_file = "app" + os.sep + STORAGE_UPLOAD_FOLDER
        if not os.path.isdir(output_base_file):
            os.mkdir(output_base_file)
        # ================
        output_file_name = name_file + "-" + str(uuid.uuid4())
        output_file = os.path.join(output_base_file, output_file_name)
        # ================
        conn = {
            "driver": "postgres",
            "username": DB_USERNAME,
            "password": DB_PASSWORD,
            "host": DB_HOST,
            "database": DB_DATABASE,
            "schema": "public",
            "port": DB_PORT,
            "jdbc_driver": "org.postgresql.Driver",
            "jdbc_dir": "libs" + os.sep + "jdbc" + os.sep + "postgresql.jar",
        }
        # ================
        path_sub_report = os.path.abspath(__file__)
        path_sub_report = path_sub_report.split(os.sep)
        for i in range(3):
            path_sub_report.pop(len(path_sub_report) - 1)
        path_sub_report = os.sep.join(path_sub_report) + os.sep + REPORT_FOLDER + os.sep
        # ================
        pyreportjasper = PyReportJasper()

        paramsAux = params
        paramsAux["pSubReportsPath"] = path_sub_report
        pyreportjasper.config(
            input_file=input_file,
            output_file=output_file,
            output_formats=[format],
            parameters=paramsAux,
            db_connection=conn,
        )
        # ================
        pyreportjasper.process_report()

        # ================
        if format == TypeIndReportFormat.TYPE_PDF:
            output_file_name = output_file_name + ".pdf"

        if open and format == TypeIndReportFormat.TYPE_PDF:
            return srvDoc.download_open(output_file_name, False)
        else:
            return {"generated": "S", "report_name_generated": output_file_name}
