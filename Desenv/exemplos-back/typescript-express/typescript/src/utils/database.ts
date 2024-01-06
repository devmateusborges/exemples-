import { join } from 'path';
import { Connection, ConnectionOptions, createConnection, getConnection } from 'typeorm';
import getOrmConfig from '@utils/config';
import { logger } from '@utils/logger';

let DB_HOST = null;
let DB_PORT = null;
let DB_USER = null;
let DB_PASSWORD = null;
let DB_DATABASE = null;

const ormConfig = async () => {
  DB_HOST = (await getOrmConfig(process.env.NODE_ENV))['host'];
  DB_PORT = (await getOrmConfig(process.env.NODE_ENV))['port'];
  DB_USER = (await getOrmConfig(process.env.NODE_ENV))['username'];
  DB_PASSWORD = (await getOrmConfig(process.env.NODE_ENV))['password'];
  DB_DATABASE = (await getOrmConfig(process.env.NODE_ENV))['database'];

  const dbConnection: ConnectionOptions = {
    type: 'postgres',
    name: 'default',
    host: DB_HOST,
    port: +DB_PORT,
    username: DB_USER,
    password: DB_PASSWORD,
    database: DB_DATABASE,
    synchronize: false,
    logging: true,
    entities: [join(__dirname, '../**/*.entity{.ts,.js}')],
    migrations: [join(__dirname, '../**/*.migration{.ts,.js}')],
    subscribers: [join(__dirname, '../**/*.subscriber{.ts,.js}')],
    cli: {
      entitiesDir: 'src/entities',
      migrationsDir: 'src/migration',
      subscribersDir: 'src/subscriber',
    },
  };

  return dbConnection;
};

const connectDb = async (): Promise<Connection> => {
  const dboptions = await ormConfig();
  logger.info('Init conecting Database');
  let conn = null;
  try {
    conn = await getConnection();
  } catch (error) {
    conn = await createConnection(dboptions);
  }
  logger.info('Finish conecting Database');
  return conn;
};

export default { ormConfig, connectDb };
