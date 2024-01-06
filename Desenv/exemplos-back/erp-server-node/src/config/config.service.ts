import { Logger, Injectable, Global } from '@nestjs/common';
import * as dotenv from 'dotenv';
import * as fs from 'fs';

@Global()
@Injectable()
export class ConfigService {
  private readonly envConfig: { [key: string]: string };
  private ormconfig: any;
  private ormconfigJson: any;
  private ormconfigEnv: any;

  constructor(env: string) {
    if (env === 'undefined') {
      env = 'local';
    }
    console.log('>>>Init ConfigService env[' + env + ']');

    this.envConfig = dotenv.parse(fs.readFileSync('.env.' + env));

    this.ormconfig = fs.readFileSync('ormconfig.json');
    this.ormconfigJson = JSON.parse(this.ormconfig);

    this.ormconfigJson.forEach((obj) => {
      if (obj.name == env) {
        this.ormconfigEnv = obj;
      }
    });
    console.log(
      '>>>Init ConfigService ormconfig[' + this.ormconfigEnv.name + ']',
    );
  }

  get(key: string): string {
    return this.envConfig[key];
  }

  getOrmConfig(): any {
    return this.ormconfigEnv;
  }
}
