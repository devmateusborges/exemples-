import { NextFunction, Response } from 'express';
import { verify } from 'jsonwebtoken';
import { SECRET_KEY } from '@utils/config';
import { SysUserEntity } from '@entities/sysUsers.entity';
import { BusinessException } from '@exceptions/businessException';
import { TokenDataStore, RequestUser } from '@interfaces/auth.interface';

const authMiddleware = async (req: RequestUser, res: Response, next: NextFunction) => {
  try {
    const Authorization = req.cookies['Authorization'] || (req.header('Authorization') ? req.header('Authorization').split('Bearer ')[1] : null);

    if (Authorization) {
      const secretKey: string = SECRET_KEY;
      const { id } = (await verify(Authorization, secretKey)) as TokenDataStore;
      const findUser = await SysUserEntity.findOne(id, { select: ['id', 'email', 'password'] });

      if (findUser) {
        req.user = findUser;
        next();
      } else {
        next(new BusinessException(401, 'Wrong authentication token'));
      }
    } else {
      next(new BusinessException(404, 'Authentication token missing'));
    }
  } catch (error) {
    next(new BusinessException(401, 'Wrong authentication token'));
  }
};

export default authMiddleware;
