import database from '@/utils/database';
import { BusinessException } from '@/exceptions/businessException';
import { IgenericService } from '@/interfaces/genericService.interface';
import { isEmpty } from 'class-validator';
import { Repository } from 'typeorm';
import { GenericEntity } from './genericEntity';
export class GenericService<T extends GenericEntity> implements IgenericService<T> {
  public repo: Repository<T>;

  public async findAllObjs(): Promise<T[]> {
    const dataObjs = await this.repo.find();
    return dataObjs;
  }

  public async findByIdObj(idFind: string): Promise<T> {
    if (isEmpty(idFind)) throw new BusinessException(400, "You're not id");

    const dataObj = await this.repo.findOne({ where: { id: idFind } });
    if (!dataObj) throw new BusinessException(409, "You're not found");

    return dataObj;
  }

  public async createObj(dataObj: any): Promise<T> {
    if (isEmpty(dataObj)) throw new BusinessException(400, "You're not data");

    const dataObjCreate = await this.repo.save({ ...dataObj });

    return dataObjCreate;
  }

  public async updateObj(idFind: string, dataObj: any): Promise<T> {
    if (isEmpty(dataObj)) throw new BusinessException(400, "You're not data");

    const dataObjFind = await this.repo.findOne({ where: { id: idFind } });
    if (!dataObjFind) throw new BusinessException(409, "You're not found");

    await this.repo.update(idFind, { ...dataObj });

    const dataObjUpdate = await this.repo.findOne({ where: { id: idFind } });
    return dataObjUpdate;
  }

  public async deleteObj(idFind: string): Promise<T> {
    if (isEmpty(idFind)) throw new BusinessException(400, "You're not id");

    const findUser: T = await this.repo.findOne({ where: { id: idFind } });
    if (!findUser) throw new BusinessException(409, "You're not found");

    await this.repo.delete([idFind]);
    return findUser;
  }
}
