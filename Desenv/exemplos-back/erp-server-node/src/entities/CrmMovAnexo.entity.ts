import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUser } from './SystemUser.entity';
import { SystemUnit } from './SystemUnit.entity';
import { CrmMov } from './CrmMov.entity';
import { BaseEntity } from '../shared/bases/base.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';

@Index('pk_crm_mov_anexo', ['id'], { unique: true })
@Entity('crm_mov_anexo', { schema: 'public' })
export class CrmMovAnexo extends BaseEntity {
  @Column('timestamp without time zone', { name: 'data_anexo' })
  dataAnexo: Date;

  @Column('text', { name: 'descritivo' })
  descritivo: string;

  @Column('varchar', {
    name: 'visual_ext',
    length: 1,
    default: () => "'N'",
  })
  visualExt: string;

  @Column('varchar', { name: 'envia_email_ext', length: 1 })
  enviaEmailExt: string;

  @Column('varchar', { name: 'nome_arq_anexo', length: 100 })
  nomeArqAnexo: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUser)
  @JoinColumn([{ name: 'system_user_id_anexo', referencedColumnName: 'id' }])
  systemUserIdAnexo: SystemUser;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => CrmMov, (crmMov) => crmMov.crmMovAnexos)
  @JoinColumn([{ name: 'crm_mov_id', referencedColumnName: 'id' }])
  crmMov: CrmMov;
}
