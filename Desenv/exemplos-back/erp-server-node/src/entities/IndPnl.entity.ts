import { Column, Entity, Index, OneToMany } from 'typeorm';
import { IndPnlRelacRel } from './IndPnlRelacRel.entity';
import { SystemUserIndPnl } from './SystemUserIndPnl.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_ind_pnl', ['id'], { unique: true })
@Entity('ind_pnl', { schema: 'public' })
export class IndPnl extends BaseEntity {
  @Column('varchar', { name: 'nome', nullable: true, length: 250 })
  nome: string;

  @Column('varchar', { name: 'tipo', nullable: true, length: 1 })
  tipo: string;

  @Column('varchar', { name: 'icon', nullable: true, length: 50 })
  icon: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToMany(() => IndPnlRelacRel, (indPnlRelacRel) => indPnlRelacRel.indPnl)
  indPnlRelacRels: IndPnlRelacRel[];

  @OneToMany(
    () => SystemUserIndPnl,
    (systemUserIndPnl) => systemUserIndPnl.indPnl,
  )
  systemUserIndPnls: SystemUserIndPnl[];
}
