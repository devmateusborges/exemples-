import { Entity, Column, PrimaryGeneratedColumn, OneToMany, JoinColumn, ManyToOne } from 'typeorm';
import { BaseEntity } from '@shared/base.entity';
import { LogColumn } from './log-column';
import { UserRoleEnum } from './user-role.enum';
import { Exclude } from 'class-transformer';
import { Tenant } from './tenant.entity';

@Entity({ name: 'user' })
export class User extends BaseEntity {
  @PrimaryGeneratedColumn('uuid', { name: 'id', comment: 'ID Users' })
  id: string;

  @Column('varchar', { name: 'firstname', length: 50, comment: 'Firt Name' })
  firstname: string;

  @Column('varchar', { name: 'lastname', length: 50, comment: 'Last Name' })
  lastname: string;

  @Column('varchar', { name: 'username', length: 255, unique: true, comment: 'User Name' })
  username: string;

  @Column('text', { name: 'email', unique: true, comment: 'Email' })
  email: string;

  @Exclude()
  @Column('text', { name: 'password', select: false })
  password: string;

  @Column('varchar',{ name: 'role', length: 50, default: UserRoleEnum.user, comment: 'Role' })
  role: string;

  @Column(type => LogColumn)
  log: LogColumn;

  @Column('varchar', { name: 'tenant_id', nullable: true, comment: 'ID Tenant' })
  @ManyToOne(type => Tenant, { cascade: false, eager: true })
  @JoinColumn({ name: 'tenant_id', referencedColumnName: 'id' })
  tenant: Tenant;
}
