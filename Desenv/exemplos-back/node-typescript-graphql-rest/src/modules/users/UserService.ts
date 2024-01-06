import { validate } from 'class-validator'
import { container, injectable } from 'tsyringe'
import { getConnection, getRepository } from 'typeorm'
import { UserDTO } from './UserDTO'
import { Users } from 'entities/Users.entity'
import { DbService } from '../../utils/DbService'

@injectable()
class UserService {
  private dbService: DbService
  constructor() {
    this.dbService = container.resolve(DbService)
  }
  async store(input: UserDTO) {
    const conn = await this.dbService.conn()
    const repo = await conn.getRepository(Users)

    const exists = await repo.findOne({ where: { username: input.username } })

    if (exists) {
      throw new Error('User already exists!')
    }

    const userDTO = new UserDTO()
    userDTO.firstname = input.firstname
    userDTO.lastname = input.lastname
    userDTO.email = input.email
    userDTO.username = input.username
    userDTO.password = input.password

    await validate(userDTO).then((errors) => {
      if (errors.length > 0) {
        throw new Error('Validate User ' + errors)
      }
    })

    const resultSave = await repo.save(userDTO)

    return resultSave
  }

  async getAll() {
    const conn = await this.dbService.conn()
    const repo = await conn.getRepository(Users)
    const resultAll = await repo.find()
    return resultAll
  }
}

export { UserService }
