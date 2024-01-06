import { memo, useLayoutEffect, useRef, useState } from "react";
import { t } from "i18next";
import AppContainerFields from "../../../components/toolkit-react/AppContainerFields";
import AppFieldCheck from "../../../components/toolkit-react/AppFieldCheck";
import AppFieldDropdownFk from "../../../components/toolkit-react/AppFieldDropdownFk";
import AppFieldText from "../../../components/toolkit-react/AppFieldText";
import useFormControl, {
  IFieldControl,
} from "../../../components/toolkit-react/hooks/useFormControl";
import IAppDet from "../../../components/toolkit-react/interface/IAppDet";
import FinBancoService from "../../../services/modules/fin/FinBancoService";
import GerCidadeService from "../../../services/modules/ger/GerCidadeService";
import { ConstProgramUtil } from "../../../utils/ConstProgramUtil";
import { capitalize, formatDateTimeColumn } from "../../../utils/FuncUtil";
import GenericFormDet from "../../generics/GenericFormDet";
import { IAppDataTableColumns } from "../../../components/toolkit-react/AppDataTable";
import AppFieldRadioButton from "../../../components/toolkit-react/AppFieldRadioButton";
import SysTypeDescriptionService from "../../../services/modules/sys/SysTypeDescriptionService";
import AppFieldDropdown from "../../../components/toolkit-react/AppFieldDropdown";

const gerCidadeService = new GerCidadeService();

interface IAGerEnderecoDet2Form extends IAppDet {}
export const dataTableColumnsDet2: IAppDataTableColumns = {
  columns: [
    {
      appField: "id",
      appHeader: "ID",
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "end_logradouro",
      appHeader: capitalize(t("IN18ENDERECOLOGRADOURODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "end_logradouro_nr",
      appHeader: capitalize(t("IN18NUMEROENDERECODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "end_bairro",
      appHeader: capitalize(t("IN18BAIRRODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "end_complemento",
      appHeader: capitalize(t("IN18ENDERECOCOMPLEMENTODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "end_cep",
      appHeader: capitalize(t("IN18ENDERECOCEPDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "fone",
      appHeader: capitalize(t("IN18TELEFONEDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "email",
      appHeader: capitalize(t("IN18EMAILDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "contato",
      appHeader: capitalize(t("IN18CONTATODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "tipo",
      appHeader: capitalize(t("IN18TIPODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "end_ger_cidade_id_obj.nome",
      appHeader: capitalize(t("IN18CIDADEDEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "padrao_obj.description",
      appHeader: capitalize(t("IN18PADRAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "ativo_obj.description",
      appHeader: capitalize(t("IN18ATIVODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: false,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "log_user_ins",
      appHeader: capitalize(t("IN18USUARIODEINSERCAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "text",
      appExport: true,
    },
    {
      appField: "log_date_ins",
      appHeader: capitalize(t("IN18DATADEINSERCAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "date",
      appExport: true,
    },
    {
      appField: "log_date_upd",
      appHeader: capitalize(t("IN18DATADEALTERACAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "date",
      appExport: true,
    },
    {
      appField: "log_user_upd",
      appHeader: capitalize(t("IN18USUARIODEALTERACAODEFAULT")),
      appSortable: true,
      appFilter: true,
      appFilterMatch: "contains",
      appFilterGlobal: true,
      appHidden: true,
      appDataType: "text",
      appExport: true,
    },
  ],
};

const sysTypeDescriptionService = new SysTypeDescriptionService();

const GerEnderecoDet2Form: React.FC<IAGerEnderecoDet2Form> = (
  props: IAGerEnderecoDet2Form
) => {
  // ==============================

  const [tipo_opt, setTipo_opt] = useState([]);
  // ==============================

  useLayoutEffect(() => {
    (async () => {
      const res = await sysTypeDescriptionService.getDescription(
        "ger_pessoa_endereco",
        "tipo"
      );
      setTipo_opt(res);
    })();
  }, []);
  // ==============================
  const fieldControls: Array<IFieldControl> = [
    {
      fieldName: "end_logradouro",
      required: [true, "Endereço Logradouro is required"],
      defaultValue: "",
      type: "text",
      maxValue: [100, "Maximum 100 characters for end Endereço Logradouro"],
    },
    {
      fieldName: "end_logradouro_nr",
      required: [true, "Numero Endereço is required"],
      defaultValue: "",
      type: "numeric",
      maxValue: [
        10,
        "Maximum 10 characters for end Endereço Logradouro Numero",
      ],
    },
    {
      fieldName: "end_bairro",
      required: [true, "Bairro is required"],
      defaultValue: "",
      type: "text",
    },
    {
      fieldName: "end_complemento",
      required: [true, "Endereço Complemento is required"],
      defaultValue: "",
      type: "text",
      maxValue: [
        100,
        "Maximum 100 characters for end Endereço Logradouro Endereço Complemento",
      ],
    },
    {
      fieldName: "end_cep",
      required: [true, "Endereço Cep is required"],
      defaultValue: "",
      type: "text",
      maxValue: [
        100,
        "Maximum 100 characters for end Endereço Logradouro Endereço Complemento",
      ],
    },
    {
      fieldName: "fone",
      required: [true, "Telefone is required"],
      defaultValue: "",
      type: "text",
      maxValue: [
        100,
        "Maximum 100 characters for end Endereço Logradouro Endereço Complemento",
      ],
    },
    {
      fieldName: "email",
      required: [true, "Email is required"],
      defaultValue: "",
      type: "text",
      maxValue: [
        100,
        "Maximum 100 characters for end Endereço Logradouro Endereço Complemento",
      ],
    },
    {
      fieldName: "contato",
      required: [true, "Contato is required"],
      defaultValue: "",
      type: "text",
      maxValue: [
        100,
        "Maximum 100 characters for end Endereço Logradouro Endereço Complemento",
      ],
    },
    {
      fieldName: "tipo",
      required: [true, "Tipo is required"],
      defaultValue: "",
      type: "radio",
    },
    {
      fieldName: "end_ger_cidade_id",
      required: [true, "Cidade is required"],
      defaultValue: "",
      type: "foreignkey",
    },
    {
      fieldName: "padrao",
      required: [false, ""],
      defaultValue: "N",
      type: "checkbox",
    },
    {
      fieldName: "ativo",
      required: [false, ""],
      defaultValue: "S",
      type: "checkbox",
    },
  ];
  // ==============================

  const formControl = useFormControl({
    fieldControls,
  });
  // ==============================

  return (
    <>
      <GenericFormDet
        ref={props.appRef}
        name="ger_pessoa_endereco_childs"
        appGenericListOptions={{
          id: "gerenderecodet2",
          appHelpText: "Endereço",
          appProgramId: ConstProgramUtil.cGerpessoaId,
          appDataTableColumns: dataTableColumnsDet2,
          appDataTableDataValue: props.appDataTableDataValue,
          appDataTablePaginateMode: "local",
          appShowTopBar: true,
          appRefreshVisible: true,
          appAddVisible: true,
          appDeleteVisible: true,
          appEditVisible: true,
          appButtonDeleteVisibleRow: true,
          appButtonEditVisibleRow: true,
          appPreferenceVisible: true,
          appAddActionCode: "ADD_DET1",
          appEditActionCode: "EDIT_DET1",
          appDeleteActionCode: "DELETE_DET1",
          appSaveActionCode: "SAVE_DET1",
        }}
        appGenericFormOptions={{
          appFormControl: formControl,
        }}
      >
        <div className="p-0 md:p-2">
          <AppContainerFields>
            <AppFieldText
              appFormControl={formControl}
              name="end_logradouro"
              appTitle={capitalize(t("IN18ENDERECOLOGRADOURODEFAULT"))}
              appHelpText="Endereço Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="end_logradouro_nr"
              appTitle={capitalize(t("IN18NUMEROENDERECODEFAULT"))}
              appHelpText="Numero Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="end_bairro"
              appTitle={capitalize(t("IN18BAIRRODEFAULT"))}
              appHelpText="Bairro Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="end_complemento"
              appTitle={capitalize(t("IN18ENDERECOCOMPLEMENTODEFAULT"))}
              appHelpText="Endereço Complemento Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="end_cep"
              appTitle={capitalize(t("IN18ENDERECOCEPDEFAULT"))}
              appHelpText="Endereço Cep Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="fone"
              appTitle={capitalize(t("IN18TELEFONEDEFAULT"))}
              appHelpText="Telefone Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="email"
              appTitle={capitalize(t("IN18EMAILDEFAULT"))}
              appHelpText="Email Help"
            />
            <AppFieldText
              appFormControl={formControl}
              name="contato"
              appTitle={capitalize(t("IN18CONTATODEFAULT"))}
              appHelpText="Contato Help"
            />
            <AppFieldDropdownFk
              appFormControl={formControl}
              name="end_ger_cidade_id"
              appTitle={capitalize(t("IN18CIDADEDEFAULT"))}
              appHelpText="Cidade Help"
              appOptionLabel="nome"
              appOptionValue="id"
              appDataKey="id"
              appServiceDefault={gerCidadeService}
              appServiceFilterId="id"
              appServiceFilterDescription="nome"
            />
            <AppFieldRadioButton
              appFormControl={formControl}
              name="tipo"
              appTitle="Tipo"
              appOptions={tipo_opt}
              appOptionsLabel="description_type"
              appOptionsValue="value_type"
            />
            <AppFieldCheck
              appFormControl={formControl}
              name="padrao"
              appTitle={capitalize(t("IN18PADRAODEFAULT"))}
              appHelpText="Padrao Help"
              appTrueValue="S"
              appTrueValueLabel="Sim"
              appFalseValue="N"
              appFalseValueLabel="Não"
            />
            <AppFieldCheck
              appFormControl={formControl}
              name="ativo"
              appTitle={capitalize(t("IN18ATIVODEFAULT"))}
              appHelpText="Ativo Help"
              appTrueValue="S"
              appTrueValueLabel="Sim"
              appFalseValue="N"
              appFalseValueLabel="Não"
            />
          </AppContainerFields>
        </div>
      </GenericFormDet>
    </>
  );
};

export default memo(GerEnderecoDet2Form);
