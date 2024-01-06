import { Global, Module } from '@nestjs/common';
import { LogModule } from './log/log.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { TypeOrmConfigService } from './config/typeOrmConfig.service';
import { AuthModule } from './auth/auth.module';
import { ConfigModule } from './config/config.module';
import { ConfigService } from './config/config.service';

//Module
import { BorModule } from './modules/bor/bor.module';
import { BovModule } from './modules/bov/bov.module';
import { CrmModule } from './modules/crm/crm.module';
import { CtbModule } from './modules/ctb/ctb.module';
import { DocModule } from './modules/doc/doc.module';
import { FinModule } from './modules/fin/fin.module';
import { FisModule } from './modules/fis/fis.module';
import { GerModule } from './modules/ger/ger.module';
import { IndModule } from './modules/ind/ind.module';
import { MobModule } from './modules/mob/mob.module';
import { MovModule } from './modules/mov/mov.module';
import { OpeModule } from './modules/ope/ope.module';
import { PtoModule } from './modules/pto/pto.module';
import { RhmModule } from './modules/rhm/rhm.module';
import { SystemModule } from './modules/sys/system.module';
import { TstModule } from './modules/tst/tst.module';
import { MailModule } from './mail/mail.module';
import { SystemUserController } from './modules/sys/systemuser/systemuser.controller';
import { SystemUserService } from './modules/sys/systemuser/systemuser.service';

@Global()
@Module({
  imports: [
    ConfigModule,
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService, TypeOrmConfigService],
      useClass: TypeOrmConfigService,
    }),
    LogModule,
    SystemModule,
    AuthModule,
    BorModule,
    BovModule,
    CrmModule,
    CtbModule,
    FinModule,
    DocModule,
    FisModule,
    GerModule,
    IndModule,
    MobModule,
    MovModule,
    OpeModule,
    PtoModule,
    RhmModule,
    TstModule,
    MailModule,
  ],
  controllers: [],
  providers: [],
  exports: [],
})
export class AppModule {}
