import { LoginDto } from '@/dtos/login.dto';
import { Router } from 'express';
import AuthController from '@controllers/auth.controller';
import { SysUserDto } from '@dtos/sysUser.dto';
import { Routes } from '@interfaces/routes.interface';
import authMiddleware from '@middlewares/auth.middleware';
import validationMiddleware from '@middlewares/validation.middleware';

class AuthRoute implements Routes {
  public path = '/';
  public router = Router();
  public controller = new AuthController();

  constructor() {
    this.initializeRoutes();
  }

  private initializeRoutes() {
    this.router.post(`${this.path}signup`, validationMiddleware(SysUserDto, 'body'), this.controller.signUp);
    this.router.post(`${this.path}login`, validationMiddleware(LoginDto, 'body'), this.controller.logIn);
    this.router.post(`${this.path}logout`, authMiddleware, this.controller.logOut);
  }
}

export default AuthRoute;
