import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
  OneToMany,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CrmClass } from './CrmClass.entity';
import { CrmEtapa } from './CrmEtapa.entity';
import { CrmOrg } from './CrmOrg.entity';
import { CrmPrioridade } from './CrmPrioridade.entity';
import { CrmStatus } from './CrmStatus.entity';
import { CrmMovAnexo } from './CrmMovAnexo.entity';
import { CrmMovHist } from './CrmMovHist.entity';
import { CrmMovTag } from './CrmMovTag.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_mov', ['id'], { unique: true })
@Entity('crm_mov', { schema: 'public' })
export class CrmMov extends BaseEntity {
  @Column('varchar', { name: 'numero', length: 10 })
  numero: string;

  @Column('timestamp without time zone', {
    name: 'data_mov',
    default: () => 'now()',
  })
  dataMov: Date;

  @Column('varchar', {
    name: 'envia_email_ext',
    length: 1,
    default: () => "'S'",
  })
  enviaEmailExt: string;

  @Column('text', { name: 'descritivo_ext' })
  descritivoExt: string;

  @Column('text', { name: 'descritivo_int', nullable: true })
  descritivoInt: string;

  @Column('timestamp without time zone', {
    name: 'data_status',
    default: () => 'now()',
  })
  dataStatus: Date;

  @Column('varchar', { name: 'titulo', nullable: true, length: 200 })
  titulo: string;

  @Column('varchar', {
    name: 'contato_email',
    nullable: true,
    length: 200,
  })
  contatoEmail: string;

  @Column('varchar', {
    name: 'contato_telefone',
    nullable: true,
    length: 50,
  })
  contatoTelefone: string;

  @Column('varchar', { name: 'anonimo', nullable: true, length: 1 })
  anonimo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'system_user_id_atend_ant', referencedColumnName: 'id' },
  ])
  systemUserIdAtendAnt: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([
    { name: 'system_user_id_atend_atu', referencedColumnName: 'id' },
  ])
  systemUserIdAtendAtu: SystemUser;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_solic', referencedColumnName: 'id' }])
  systemUserIdSolic: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmClass, (crmClass) => crmClass.crmMovs)
  @JoinColumn([{ name: 'crm_class_id', referencedColumnName: 'id' }])
  crmClass: CrmClass;

  @ManyToOne(() => CrmEtapa, (crmEtapa) => crmEtapa.crmMovs)
  @JoinColumn([{ name: 'crm_etapa_id', referencedColumnName: 'id' }])
  crmEtapa: CrmEtapa;

  @ManyToOne(() => CrmOrg, (crmOrg) => crmOrg.crmMovs)
  @JoinColumn([{ name: 'crm_org_id', referencedColumnName: 'id' }])
  crmOrg: CrmOrg;

  @ManyToOne(() => CrmPrioridade, (crmPrioridade) => crmPrioridade.crmMovs)
  @JoinColumn([{ name: 'crm_prioridade_id', referencedColumnName: 'id' }])
  crmPrioridade: CrmPrioridade;

  @ManyToOne(() => CrmStatus, (crmStatus) => crmStatus.crmMovs)
  @JoinColumn([{ name: 'crm_status_id', referencedColumnName: 'id' }])
  crmStatus: CrmStatus;

  @OneToMany(() => CrmMovAnexo, (crmMovAnexo) => crmMovAnexo.crmMov)
  crmMovAnexos: CrmMovAnexo[];

  @OneToMany(() => CrmMovHist, (crmMovHist) => crmMovHist.crmMov)
  crmMovHists: CrmMovHist[];

  @OneToMany(() => CrmMovTag, (crmMovTag) => crmMovTag.crmMov)
  crmMovTags: CrmMovTag[];
}
