import { UserController } from './controllers/user.controller';
import * as dotenv from 'dotenv';
import express from 'express';
import morgan from 'morgan';
import userController from '@controllers/user.controller';
import errorMiddleware from './middleware/errorMiddleware';

class App {

  public express: express.Application;

  constructor() {
    dotenv.config({path: process.env.NODE_ENV+'.env'})
    this.express = express();
    this.middleware();
    this.routes();
  }

  private middleware(): void {
    this.express.use(morgan('dev'));
    this.express.use(errorMiddleware);
  }



  private routes(): void {   
    let router = express.Router();
  
    router.get('/', (req, res, next) => {
      res.json({
        message: 'Server is running'
      });
    });
    this.express.use('/', router);
    this.express.use('/api/v1/user', userController);
  }
}

export default new App().express;

