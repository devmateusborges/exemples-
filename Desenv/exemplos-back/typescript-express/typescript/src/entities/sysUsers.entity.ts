import { GenericEntity } from '@/utils/genericEntity';
import { Column, Entity } from 'typeorm';
import { GenericLogsCols } from './../utils/genericLogCols';

@Entity('sys_user')
export class SysUserEntity extends GenericEntity {
  @Column({ name: 'name' })
  name: string;
  @Column({ name: 'login' })
  login: string;
  @Column({ name: 'password' })
  password: string;
  @Column({ name: 'email' })
  email: string;
  @Column({ name: 'active' })
  active: string;
  @Column({ name: 'active_message' })
  active_message: string;
  @Column({ name: 'phone' })
  phone: string;
  @Column({ name: 'document' })
  document: string;
  @Column({ name: 'admin' })
  admin: string;
  @Column({ name: 'login_ext' })
  login_ext: string;
  @Column({ name: 'frontpage_id' })
  frontpage_id: string;
  @Column({ name: 'origem' })
  origem: string;
  @Column({ name: 'chat' })
  chat: string;

  @Column(() => GenericLogsCols)
  log: GenericLogsCols;
}
