import { Connection, createConnection, getConnectionManager } from 'typeorm'
import { injectable } from 'tsyringe'

@injectable()
class DbService {
  async conn() {
    let connection: Connection
    const hasConnection = getConnectionManager().has(process.env.NODE_ENV)
    if (hasConnection) {
      connection = await getConnectionManager().get(process.env.NODE_ENV)
      if (!connection.isConnected) {
        connection = await connection.connect()
      }
    } else {
      connection = await createConnection(process.env.NODE_ENV)
    }

    return connection
  }
}
export { DbService }
