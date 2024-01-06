import { SysUserDto } from '@dtos/sysUser.dto';
import userService from '@services/users.service';
import { NextFunction, Request, Response } from 'express';

class UsersController {
  public service = new userService();

  public findAll = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const findAllObjs: SysUserDto[] = await this.service.findAllObjs();

      res.status(200).json({ data: findAllObjs, message: 'findAll' });
    } catch (error) {
      next(error);
    }
  };

  public findById = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const idObj = req.params.id;
      const findAllObj: SysUserDto = await this.service.findByIdObj(idObj);

      res.status(200).json({ data: findAllObj, message: 'findOne' });
    } catch (error) {
      next(error);
    }
  };

  public create = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const dataObj: SysUserDto = req.body;
      const dataObjCreate: SysUserDto = await this.service.createObj(dataObj);

      res.status(201).json({ data: dataObjCreate, message: 'created' });
    } catch (error) {
      next(error);
    }
  };

  public update = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const id = req.params.id;
      const dataObj: SysUserDto = req.body;
      const dataObjUpdate: SysUserDto = await this.service.updateObj(id, dataObj);

      res.status(200).json({ data: dataObjUpdate, message: 'updated' });
    } catch (error) {
      next(error);
    }
  };

  public delete = async (req: Request, res: Response, next: NextFunction): Promise<void> => {
    try {
      const id = req.params.id;
      const dataObjDelete: SysUserDto = await this.service.deleteObj(id);

      res.status(200).json({ data: dataObjDelete, message: 'deleted' });
    } catch (error) {
      next(error);
    }
  };
}

export default UsersController;
