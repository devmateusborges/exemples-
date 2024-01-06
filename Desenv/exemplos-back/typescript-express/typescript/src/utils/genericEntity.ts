import { BaseEntity, Column } from 'typeorm';

export class GenericEntity extends BaseEntity {
  @Column('varchar', {
    primary: true,
    name: 'id',
    default: () => 'uuid_generate_v4()',
  })
  public id: string;
}
