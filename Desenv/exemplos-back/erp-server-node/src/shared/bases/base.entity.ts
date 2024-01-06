import { Column } from 'typeorm';

export class BaseEntity {
  @Column('varchar', { primary: true, name: 'id', length: 36 })
  public id: string;
}
