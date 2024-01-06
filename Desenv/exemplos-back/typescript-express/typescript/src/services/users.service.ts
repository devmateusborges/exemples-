import database from '@/utils/database';
import { SysUserEntity } from '@entities/sysUsers.entity';

import { EntityRepository } from 'typeorm';
import { GenericService } from './../utils/genericService';

@EntityRepository()
class UserService extends GenericService<SysUserEntity> {
  constructor() {
    super();
    database.connectDb().then(conn => {
      this.repo = conn.getRepository(SysUserEntity);
    });
  }
}

export default UserService;
