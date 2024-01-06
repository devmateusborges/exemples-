import { BadGatewayException, Injectable } from '@nestjs/common';
import { FindConditions, FindOneOptions, ObjectID, Repository } from 'typeorm';
import { IBaseService } from './IBase.service';
import { BaseEntity } from './base.entity';

export class BaseService<T extends BaseEntity> implements IBaseService<T> {
  constructor(private readonly genericRepository: Repository<T>) {}

  async create(entity: any): Promise<T> {
    try {
      const entityCreated = await this.genericRepository.save(entity);
      return entityCreated;
    } catch (error) {
      throw new BadGatewayException(error);
    }
  }

  async getAll(conditions?: FindConditions<T>): Promise<T[]> {
    try {
      return <Promise<T[]>>this.genericRepository.find(conditions);
    } catch (error) {
      throw new BadGatewayException(error);
    }
  }

  async get(id: string): Promise<T> {
    try {
      return <Promise<T>>this.genericRepository.findOneOrFail(id);
    } catch (error) {
      throw new BadGatewayException(error);
    }
  }

  async delete(id: string) {
    try {
      const entityDeleted = await this.get(id);
      if (entityDeleted) this.genericRepository.delete([id]);
    } catch (error) {
      throw new BadGatewayException(error);
    }
  }

  async update(id: string, entity: any): Promise<any> {
    let entityUpdated: any = null;
    try {
      const entityFind = await this.get(id);
      if (entityFind) {
        entity.id = id;
        entityUpdated = await this.genericRepository.save(entity);
      }

      return entityUpdated;
    } catch (error) {
      throw new BadGatewayException(error);
    }
  }
}
