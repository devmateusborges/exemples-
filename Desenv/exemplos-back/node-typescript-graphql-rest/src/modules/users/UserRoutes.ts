import { UserController } from '@modules/users/UserController'
import { Router } from 'express'

const UserRoutes = Router()

const userController = new UserController()

UserRoutes.post('/users', userController.store)
UserRoutes.get('/users', userController.getAll)

export { UserRoutes }
