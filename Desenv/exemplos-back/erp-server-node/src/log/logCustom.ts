import { Injectable, ConsoleLogger, Global } from '@nestjs/common';

import LogLevels from './logLevels';
import LogService from './log.service';

@Global()
@Injectable()
class LogCustom extends ConsoleLogger {
  private readonly logService: LogService;
  constructor() {
    const environment = process.env.NODE_ENV;

    super('', {
      logLevels: LogLevels(environment === 'production'),
      timestamp: true,
    });

    this.logService = new LogService();
  }

  log(message: string, context?: string) {
    super.log.apply(this, [message, context]);

    this.logService.createLog({
      message,
      context,
      level: 'log',
    });
  }
  error(message: string, stack?: string, context?: string) {
    super.error.apply(this, [message, stack, context]);

    this.logService.createLog({
      message,
      context,
      level: 'error',
    });
  }
  warn(message: string, context?: string) {
    super.warn.apply(this, [message, context]);

    this.logService.createLog({
      message,
      context,
      level: 'error',
    });
  }
  debug(message: string, context?: string) {
    super.debug.apply(this, [message, context]);

    this.logService.createLog({
      message,
      context,
      level: 'error',
    });
  }
  verbose(message: string, context?: string) {
    super.debug.apply(this, [message, context]);

    this.logService.createLog({
      message,
      context,
      level: 'error',
    });
  }
}

export default LogCustom;
