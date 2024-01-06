import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Ind } from '../../entities/Ind.entity';
import { IndCjd } from '../../entities/IndCjd.entity';
import { IndCjdRelacFtd } from '../../entities/IndCjdRelacFtd.entity';
import { IndCnd } from '../../entities/IndCnd.entity';
import { IndFtd } from '../../entities/IndFtd.entity';
import { IndFtdRelacPrm } from '../../entities/IndFtdRelacPrm.entity';
import { IndRelVar } from '../../entities/IndRelVar.entity';
import { IndSubgrupo } from '../../entities/IndSubgrupo.entity';
import { IndUnitParam } from '../../entities/IndUnitParam.entity';
import { IndVrAno } from '../../entities/IndVrAno.entity';
import { IndVrBimestre } from '../../entities/IndVrBimestre.entity';
import { IndVrDia } from '../../entities/IndVrDia.entity';
import { IndVrMes } from '../../entities/IndVrMes.entity';
import { IndVrMeta } from '../../entities/IndVrMeta.entity';
import { IndVrQuadrimestre } from '../../entities/IndVrQuadrimestre.entity';
import { IndVrQuinzena } from '../../entities/IndVrQuinzena.entity';
import { IndVrSemana } from '../../entities/IndVrSemana.entity';
import { IndVrSemestre } from '../../entities/IndVrSemestre.entity';
import { IndVrTrimestre } from '../../entities/IndVrTrimestre.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      Ind,
      IndCjd,
      IndCjdRelacFtd,
      IndCnd,
      IndFtd,
      IndFtdRelacPrm,
      IndRelVar,
      IndSubgrupo,
      IndUnitParam,
      IndVrAno,
      IndVrBimestre,
      IndVrDia,
      IndVrMes,
      IndVrMeta,
      IndVrQuadrimestre,
      IndVrQuinzena,
      IndVrSemana,
      IndVrSemestre,
      IndVrTrimestre,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class IndModule {}
