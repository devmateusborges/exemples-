import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { System } from '../../entities/System.entity';
import { SystemGroup } from '../../entities/SystemGroup.entity';
import { SystemGroupProgram } from '../../entities/SystemGroupProgram.entity';
import { SystemGroupProgramFeature } from '../../entities/SystemGroupProgramFeature.entity';
import { SystemLicence } from '../../entities/SystemLicence.entity';
import { SystemLicenceDevice } from '../../entities/SystemLicenceDevice.entity';
import { SystemMigrations } from '../../entities/SystemMigrations.entity';
import { SystemParam } from '../../entities/SystemParam.entity';
import { SystemPlan } from '../../entities/SystemPlan.entity';
import { SystemPlanRestriction } from '../../entities/SystemPlanRestriction.entity';
import { SystemPreference } from '../../entities/SystemPreference.entity';
import { SystemProgram } from '../../entities/SystemProgram.entity';
import { SystemProgramFavorite } from '../../entities/SystemProgramFavorite.entity';
import { SystemProgramFeature } from '../../entities/SystemProgramFeature.entity';
import { SystemPsqlResult } from '../../entities/SystemPsqlResult.entity';
import { SystemRestriction } from '../../entities/SystemRestriction.entity';
import { SystemRestrictionLicence } from '../../entities/SystemRestrictionLicence.entity';
import { SystemSession } from '../../entities/SystemSession.entity';
import { SystemUnit } from '../../entities/SystemUnit.entity';
import { SystemTypeDescription } from '../../entities/SystemTypeDescription.entity';
import { SystemUnitPreference } from '../../entities/SystemUnitPreference.entity';
import { SystemUserCrmChatGrupo } from '../../entities/SystemUserCrmChatGrupo.entity';
import { SystemUserCrmClass } from '../../entities/SystemUserCrmClass.entity';
import { SystemUserCrmOrg } from '../../entities/SystemUserCrmOrg.entity';
import { SystemUserGroup } from '../../entities/SystemUserGroup.entity';
import { SystemUserIndPnl } from '../../entities/SystemUserIndPnl.entity';
import { SystemUserPreference } from '../../entities/SystemUserPreference.entity';
import { SystemUserProgram } from '../../entities/SystemUserProgram.entity';
import { SystemUserProgramFeature } from '../../entities/SystemUserProgramFeature.entity';
import { SystemUserUnit } from '../../entities/SystemUserUnit.entity';
import { SystemUser } from '../../entities/SystemUser.entity';
import { SystemSqlLog } from '../../entities/SystemSqlLog.entity';
import { SystemNotificationLog } from '../../entities/SystemNotificationLog.entity';
import { SystemEmailLog } from '../../entities/SystemEmailLog.entity';
import { SystemChangeLog } from '../../entities/SystemChangeLog.entity';
import { SystemAccessLog } from '../../entities/SystemAccessLog.entity';
import { SystemUserService } from './systemuser/systemuser.service';
import { SystemUserController } from './systemuser/systemuser.controller';
import { SystemAccessLogService } from './systemAccessLog/systemAccessLog.service';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      SystemUser,
      System,
      SystemGroup,
      SystemGroupProgram,
      SystemGroupProgramFeature,
      SystemLicence,
      SystemLicenceDevice,
      SystemMigrations,
      SystemParam,
      SystemPlan,
      SystemPlanRestriction,
      SystemPreference,
      SystemProgram,
      SystemProgramFavorite,
      SystemProgramFeature,
      SystemPsqlResult,
      SystemRestriction,
      SystemRestrictionLicence,
      SystemSession,
      SystemUnit,
      SystemTypeDescription,
      SystemUnitPreference,
      SystemUserCrmChatGrupo,
      SystemUserCrmClass,
      SystemUserCrmOrg,
      SystemUserGroup,
      SystemUserIndPnl,
      SystemUserPreference,
      SystemUserProgram,
      SystemUserProgramFeature,
      SystemUserUnit,
      SystemSqlLog,
      SystemNotificationLog,
      SystemEmailLog,
      SystemChangeLog,
      SystemAccessLog,
      SystemEmailLog,
    ]),
  ],
  providers: [SystemUserService, SystemAccessLogService],
  controllers: [SystemUserController],
  exports: [SystemUserService, SystemAccessLogService],
})
export class SystemModule {}
