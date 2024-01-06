import {
  HttpStatus,
  ExceptionFilter,
  Catch,
  ArgumentsHost,
} from '@nestjs/common';
import { Response as ExpressResponse } from 'express';
import { ExceptionResponse } from '../interfaces/exception-response.interface';
import { HttpArgumentsHost } from '@nestjs/common/interfaces';

@Catch()
export default class AllExceptionsFilter implements ExceptionFilter {
  catch(exception: any, host: ArgumentsHost) {
    const ctx: HttpArgumentsHost = host.switchToHttp();
    const res = ctx.getResponse<ExpressResponse>();
    const exceptionMessage: string | null = exception.message || null;
    const exceptionResponse: null | ExceptionResponse = exception.getResponse
      ? (exception.getResponse() as ExceptionResponse)
      : null;
    const status: number = exception.getStatus ? exception.getStatus() : 500;

    const pgCodes = {
      duplicateError: '23505',
    };
    if (exception.code == pgCodes.duplicateError) {
      return res.status(HttpStatus.CONFLICT).json({
        statusCode: HttpStatus.CONFLICT,
        message: exceptionMessage + 'zzz',
        error: exceptionResponse,
      });
    }

    return res.status(status).json({
      message: exceptionMessage,
      error: exceptionResponse,
    });
  }
}
