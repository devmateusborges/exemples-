export interface IgenericService<T> {
  findAllObjs(): Promise<T[]>;

  findByIdObj(id: string): Promise<T>;

  createObj(dataObj: T): Promise<T>;

  updateObj(id: string, dataObj: T): Promise<T>;

  deleteObj(id: string): Promise<T>;
}
