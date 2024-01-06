import { config } from 'dotenv';
config({ path: `.env.${process.env.NODE_ENV || 'development'}` });
import * as fs from 'fs';
import { BaseConnectionOptions } from 'typeorm/connection/BaseConnectionOptions';

const getOrmConfig = async (env: any): Promise<any> => {
  if (env === 'undefined') {
    env = 'development';
  }
  const ormconfig = await fs.readFileSync('ormconfig.json');
  const ormconfigJson = JSON.parse(ormconfig.toString());
  let ormconfigAux = null;
  ormconfigJson.forEach((obj: any) => {
    if (obj.name == env) {
      ormconfigAux = obj;
    }
  });

  return ormconfigAux;
};

export const CREDENTIALS = process.env.CREDENTIALS === 'true';
export const { NODE_ENV, PORT, SECRET_KEY, LOG_FORMAT, LOG_DIR, ORIGIN } = process.env;
export default getOrmConfig;
