import { Column, CreateDateColumn, UpdateDateColumn } from 'typeorm';

export class GenericLogsCols {
  //TODO Verificar como podemos setar usuario logado nas colunas de user
  @Column({ name: '_user_ins' })
  userins: string;

  @CreateDateColumn({
    name: '_date_ins',
  })
  dateins: Date;

  @Column({ name: '_user_upd' })
  userupd: string;

  @UpdateDateColumn({
    name: '_date_upd',
  })
  dateupd: Date;
}
