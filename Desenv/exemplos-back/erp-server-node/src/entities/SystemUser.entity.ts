import {
  BeforeInsert,
  Column,
  Entity,
  Index,
  OneToMany,
  PrimaryColumn,
} from 'typeorm';
import { hashSync } from 'bcrypt';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('idx_unq_system_user_email', ['email'], { unique: true })
@Index('pk_system_user', ['id'], { unique: true })
@Index('idx_unq_system_user_login', ['login'], { unique: true })
@Entity('system_user', { schema: 'public' })
export class SystemUser extends BaseEntity {
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

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @BeforeInsert()
  hashPassword() {
    this.password = hashSync(this.password, 10);
  }
}
