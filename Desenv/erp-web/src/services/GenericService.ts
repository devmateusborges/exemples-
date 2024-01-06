import { api } from "../utils/ApiUtil";

export default class BaseService {
  resource: string;
  // ==============================
  constructor(resource: string) {
    this.resource = resource;
  }
  // ==============================
  async list(params: any = undefined): Promise<any> {
    const result = await api.get<any>(this.resource, {
      params,
    });
    return result?.data;
  }
  // ==============================
  async findById(id: any): Promise<any> {
    const result = await api.get<any>(`${this.resource}${id}`);
    return result?.data;
  }
  // ==============================
  async save(data: any): Promise<any> {
    const result = await api.post<any>(this.resource, data);
    return result?.data;
  }
  // ==============================
  async delete(id: any): Promise<any> {
    const result = await api.delete<any>(`${this.resource}${id}`);
    // console.log("delete", result);
    return result?.data;
  }
}
