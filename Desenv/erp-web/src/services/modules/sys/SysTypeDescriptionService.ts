import { api } from "../../../utils/ApiUtil";
import BaseService from "../../GenericService";

export default class SysTypeDescriptionService extends BaseService {
  constructor() {
    super("sys/systypedescription/");
  }

  getDescription = async (table_name: string, field_name: string) => {
    const result = await api.get<any>(`${this.resource}`, {
      params: {
        pfilters: { filter: { and: { field_name, table_name } } },
      },
    });

    return result.data.items;
  };
}
