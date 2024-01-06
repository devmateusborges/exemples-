import { UserService } from '@services/user.service';
import HttpException from '@shared/http-exception';
import { Router, Request, Response, NextFunction } from 'express';

export class UserController {
    router: Router
    constructor() {
        this.router = Router();
       
        this.init();
    }
    public async get(req: Request, res: Response, next: NextFunction) {
        try {
            const service = new UserService();
            const result = await service.find(null);
            res.send(result);
            
        } catch (error) {
            next(new HttpException(404, error));
        }
    }
    init() {
        this.router.get('/', this.get);
    }
}


const userController = new UserController();
export default userController.router;