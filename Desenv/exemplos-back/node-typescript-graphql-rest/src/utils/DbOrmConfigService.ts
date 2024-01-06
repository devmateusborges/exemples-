import * as dotenv from 'dotenv'
import * as fs from 'fs'
import { resolve } from 'path'
import { injectable } from 'tsyringe'

@injectable()
class DbOrmConfigService {
  private ormconfig: any
  private ormconfigEnv: any

  getOrmConfig(name: string): any {
    this.ormconfig = fs.readFileSync(resolve(__dirname, '../../ormconfig.json'))
    if (process.env.NODE_ENV == 'test') {
      this.ormconfigEnv = JSON.parse(this.ormconfig)[0]
    } else if (process.env.NODE_ENV == 'development') {
      this.ormconfigEnv = JSON.parse(this.ormconfig)[1]
    } else if (process.env.NODE_ENV == 'production') {
      this.ormconfigEnv = JSON.parse(this.ormconfig)[2]
    }
    return this.ormconfigEnv[name]
  }
}
export { DbOrmConfigService }
