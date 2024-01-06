import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { SystemUser } from '../../../entities/SystemUser.entity';
import { BaseService } from '../../../shared/bases/base.service';

@Injectable()
export class SystemUserService extends BaseService<SystemUser> {
  constructor(
    @InjectRepository(SystemUser)
    private readonly systemUser: Repository<SystemUser>,
  ) {
    super(systemUser);
  }
}
