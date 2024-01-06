import { Injectable, Logger } from '@nestjs/common';
import { TypeOrmModuleOptions, TypeOrmOptionsFactory } from '@nestjs/typeorm';
import { ConfigService } from './config.service';

@Injectable()
export class TypeOrmConfigService implements TypeOrmOptionsFactory {
  constructor(private readonly configService: ConfigService) {
    console.log('>>>Init TypeOrmConfigService');
  }

  async createTypeOrmOptions(): Promise<TypeOrmModuleOptions> {
    const direntities = JSON.parse(
      JSON.stringify(await this.configService.getOrmConfig().entities),
    )[0];

    console.log('>>>Init createTypeOrmOptions entities [' + direntities + ']');
    return {
      name: await this.configService.getOrmConfig().name,
      type: await this.configService.getOrmConfig().type,
      host: await this.configService.getOrmConfig().host,
      port: Number(await this.configService.getOrmConfig().port),
      username: await this.configService.getOrmConfig().username,
      password: await this.configService.getOrmConfig().password,
      database: await this.configService.getOrmConfig().database,
      entities: [direntities],
      synchronize: false,
      logging: await this.configService.getOrmConfig().logging,
      migrationsTableName: await this.configService.getOrmConfig()
        .migrationsTableName,
      migrations: [
        JSON.parse(
          JSON.stringify(await this.configService.getOrmConfig().migrations),
        )[0],
      ],
      subscribers: [
        JSON.parse(
          JSON.stringify(this.configService.getOrmConfig().subscribers),
        )[0],
      ],
      logger: 'advanced-console' as const,
    };
    //   return {
    //     type: 'postgres',
    //     host: 'localhost',
    //     port: 5432,
    //     username: 'postgres',
    //     password: 'postgres',
    //     database: 'rfdadoslocal',
    //     entities: ["dist/entities/**/*.js"],
    //     synchronize: false,
    //     logging: true,
    //     migrationsTableName: 'system_migration',
    //     migrations: ["dist/migration/**/*.js"],
    //     subscribers: ["dist/subscriber/**/*.js"],
    //     logger: 'advanced-console' as 'advanced-console',
    // };
  }
}
