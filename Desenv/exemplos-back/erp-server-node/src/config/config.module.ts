import { Module, Global } from '@nestjs/common';
import { ConfigService } from './config.service';
import { TypeOrmConfigService } from './typeOrmConfig.service';

@Global()
@Module({
  providers: [
    {
      provide: ConfigService,
      useValue: new ConfigService(process.env.NODE_ENV),
    },
    TypeOrmConfigService,
  ],
  exports: [ConfigService, TypeOrmConfigService],
})
export class ConfigModule {}
