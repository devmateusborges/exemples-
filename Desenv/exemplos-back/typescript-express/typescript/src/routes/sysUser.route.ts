import { Router } from 'express';
import UsersController from '@controllers/users.controller';
import { SysUserDto } from '@dtos/sysUser.dto';
import { Routes } from '@interfaces/routes.interface';
import validationMiddleware from '@middlewares/validation.middleware';
import authMiddleware from '@/middlewares/auth.middleware';

class SysUsersRoute implements Routes {
  public path = '/sys/sysuser';
  public router = Router();
  public controller = new UsersController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
    this.router.get(`${this.path}`, authMiddleware, this.controller.findAll);
    this.router.get(`${this.path}/:id`, this.controller.findById);
    this.router.post(`${this.path}`, authMiddleware, validationMiddleware(SysUserDto, 'body'), this.controller.create);
    this.router.put(`${this.path}/:id`, authMiddleware, validationMiddleware(SysUserDto, 'body', true), this.controller.update);
    this.router.delete(`${this.path}/:id`, authMiddleware, this.controller.delete);
  }
}

export default SysUsersRoute;
