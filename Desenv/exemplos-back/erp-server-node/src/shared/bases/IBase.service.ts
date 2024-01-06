import { FindConditions, FindOneOptions } from 'typeorm';

export interface IBaseService<T> {
  getAll(conditions?: FindConditions<T>): Promise<T[]>;
  get(id: string): Promise<T>;
  create(entity: T): Promise<T>;
  update(id: string, entity: T): Promise<T>;
  delete(id: string);
}
