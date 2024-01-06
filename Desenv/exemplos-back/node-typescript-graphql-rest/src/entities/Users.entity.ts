import {
  Entity,
  Column,
  PrimaryGeneratedColumn,
  OneToMany,
  JoinColumn,
  ManyToOne,
  BeforeInsert,
  BeforeUpdate
} from 'typeorm'
import { BaseLogColumn } from './BaseLogColumn'
import { Exclude } from 'class-transformer'
import { BaseEntity } from './BaseEntity'
import bcrypt from 'bcryptjs'

@Entity({ name: 'users' })
export class Users extends BaseEntity {
  @PrimaryGeneratedColumn('uuid', { name: 'id', comment: 'ID Users' })
  id: string

  @Column('varchar', { name: 'firstname', length: 50, comment: 'Firt Name' })
  firstname: string

  @Column('varchar', { name: 'lastname', length: 50, comment: 'Last Name' })
  lastname: string

  @Column('varchar', {
    name: 'username',
    length: 255,
    unique: true,
    comment: 'User Name'
  })
  username: string

  @Column('text', { name: 'email', unique: true, comment: 'Email' })
  email: string

  @Exclude()
  @Column('text', { name: 'password', select: false })
  password: string

  @BeforeInsert()
  @BeforeUpdate()
  hasPassword() {
    this.password = bcrypt.hashSync(this.password, 8)
  }

  @Column(() => BaseLogColumn)
  log: BaseLogColumn
}
