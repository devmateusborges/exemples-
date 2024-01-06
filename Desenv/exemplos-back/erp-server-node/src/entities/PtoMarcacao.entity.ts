import {
  Column,
  Entity,
  Index,
  JoinColumn,
  ManyToOne,
  OneToOne,
} from 'typeorm';
import { SystemUnit } from './SystemUnit.entity';
import { PtoMedidor } from './PtoMedidor.entity';
import { BaseLogColumn } from '../shared/bases/baseLogColumn';
import { BaseEntity } from '../shared/bases/base.entity';

@Index('pk_pto_marcacao', ['id'], { unique: true })
@Entity('pto_marcacao', { schema: 'public' })
export class PtoMarcacao extends BaseEntity {
  @Column('timestamp without time zone', { name: 'marc_data', nullable: true })
  marcData: Date | null;

  @Column('integer', { name: 'marc_dia', nullable: true })
  marcDia: number | null;

  @Column('integer', { name: 'marc_mes', nullable: true })
  marcMes: number | null;

  @Column('integer', { name: 'marc_ano', nullable: true })
  marcAno: number | null;

  @Column('integer', { name: 'marc_hora', nullable: true })
  marcHora: number | null;

  @Column('integer', { name: 'marc_minuto', nullable: true })
  marcMinuto: number | null;

  @Column('varchar', {
    name: 'process_id',
    nullable: true,
    length: 36,
  })
  processId: string;

  @Column((type) => BaseLogColumn)
  log: BaseLogColumn;

  @OneToOne(() => SystemUnit)
  @JoinColumn([{ name: 'unit_id', referencedColumnName: 'id' }])
  unit: SystemUnit;

  @ManyToOne(() => PtoMedidor, (ptoMedidor) => ptoMedidor.ptoMarcacaos)
  @JoinColumn([{ name: 'pto_medidor_id', referencedColumnName: 'id' }])
  ptoMedidor: PtoMedidor;
}
