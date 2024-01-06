import { api } from "../../../utils/ApiUtil";
import BaseService from "../../GenericService";

export default class GerPerService extends BaseService {
  constructor() {
    super("ger/gerper/");
  }
  // ==============================
  async generatePer(params: any): Promise<any> {
    const result = await api.post<any>(`${this.resource}generateper`, params);

    return result;
  }
}
