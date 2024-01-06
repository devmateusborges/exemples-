import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { System } from './System.entity';
import { SystemPlan } from './SystemPlan.entity';
import { SystemUser } from './SystemUser.entity';
import { SystemLicenceDevice } from './SystemLicenceDevice.entity';
import { SystemRestrictionLicence } from './SystemRestrictionLicence.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_system_licence', ['id'], { unique: true })
@Entity('system_licence', { schema: 'public' })
export class SystemLicence extends BaseEntity {
  @Column('varchar', { name: 'tipo_doc', length: 100 })
  tipoDoc: string;

  @Column('varchar', { name: 'nome_solicitante', length: 100 })
  nomeSolicitante: string;

  @Column('varchar', { name: 'doc', nullable: true, length: 100 })
  doc: string;

  @Column('varchar', {
    name: 'end_logradouro',
    nullable: true,
    length: 100,
  })
  endLogradouro: string;

  @Column('varchar', {
    name: 'end_bairro',
    nullable: true,
    length: 100,
  })
  endBairro: string;

  @Column('varchar', {
    name: 'end_numero',
    nullable: true,
    length: 100,
  })
  endNumero: string;

  @Column('varchar', {
    name: 'end_cidade',
    nullable: true,
    length: 100,
  })
  endCidade: string;

  @Column('varchar', { name: 'end_uf', nullable: true, length: 100 })
  endUf: string;

  @Column('varchar', {
    name: 'end_pais',
    nullable: true,
    length: 100,
  })
  endPais: string;

  @Column('varchar', { name: 'chamado_id', length: 100 })
  chamadoId: string;

  @Column('varchar', { name: 'status', length: 2 })
  status: string;

  @Column('timestamp without time zone', {
    name: 'status_data',
    default: () => 'now()',
  })
  statusData: Date;

  @Column('varchar', { name: 'status_observacao', length: 250 })
  statusObservacao: string;

  @Column('varchar', {
    name: 'system_version',
    nullable: true,
    length: 50,
  })
  systemVersion: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @ManyToOne(() => System, (system) => system.systemLicences)
  @JoinColumn([{ name: 'system_id', referencedColumnName: 'id' }])
  system: System;

  @ManyToOne(() => SystemPlan, (systemPlan) => systemPlan.systemLicences)
  @JoinColumn([{ name: 'system_plan_id', referencedColumnName: 'id' }])
  systemPlan: SystemPlan;

  @OneToOne(() => SystemUser, {
    onDelete: 'CASCADE',
  })
  @JoinColumn([{ name: 'system_user_id', referencedColumnName: 'id' }])
  systemUser: SystemUser;

  @OneToMany(
    () => SystemLicenceDevice,
    (systemLicenceDevice) => systemLicenceDevice.systemLicence,
  )
  systemLicenceDevices: SystemLicenceDevice[];

  @OneToMany(
    () => SystemRestrictionLicence,
    (systemRestrictionLicence) => systemRestrictionLicence.systemLicence,
  )
  systemRestrictionLicences: SystemRestrictionLicence[];
}
