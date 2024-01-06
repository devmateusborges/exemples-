import { container } from 'tsyringe'
import { UserService } from './UserService'

const usersResolvers = {
  Query: {
    getAllUsers() {
      const userService = container.resolve(UserService)
      const users = userService.getAll()
      return users
    }
  },
  Mutation: {
    createUser(_, { input }) {
      const userService = container.resolve(UserService)
      const user = userService.store(input)
      return user
    }
  }
}

export default usersResolvers
