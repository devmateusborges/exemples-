import { User } from '@models/user.entity'
import { conn } from '@config/db'

export class UserService {
  async find (props) {
    const repo = (await conn).getRepository(User);
    return await repo.find(props);
  }
}
