import { api } from "../../../utils/ApiUtil";
import BaseService from "../../GenericService";

export default class SysProgramActionService extends BaseService {
  constructor() {
    super("sys/sysprogramaction/");
  }

  // ==============================
  async getByUserLogin(params: any): Promise<any> {
    const result = await api.get<any>(`${this.resource}getbyuserlogin/`, {
      params,
    });

    return result;
  }
}
