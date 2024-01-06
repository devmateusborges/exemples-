import { Injectable } from '@nestjs/common';
import { SystemAccessLog } from '../../../entities/SystemAccessLog.entity';
import { BaseService } from '../../../shared/bases/base.service';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';

@Injectable()
export class SystemAccessLogService extends BaseService<SystemAccessLog> {
  constructor(
    @InjectRepository(SystemAccessLog)
    private systemAccessLog: Repository<SystemAccessLog>,
  ) {
    super(systemAccessLog);
  }
}
