import { Request, Response } from 'express'
import { container } from 'tsyringe'
import { UserService } from './UserService'

class UserController {
  async store(request: Request, response: Response) {
    const { firstname, lastname, email, username, password } = request.body
    const userService = container.resolve(UserService)
    const store = await userService.store({
      firstname,
      lastname,
      email,
      username,
      password
    })

    return response.json(store)
  }

  async getAll(request: Request, response: Response) {
    const userService = container.resolve(UserService)
    const all = await userService.getAll()
    return response.json(all)
  }
}

export { UserController }
