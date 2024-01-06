import { LogLevel } from '@nestjs/common/services/logger.service';

function LogLevels(isProduction: boolean): LogLevel[] {
  if (isProduction) {
    return ['log', 'warn', 'error'];
  }
  return ['error', 'warn', 'log', 'verbose', 'debug'];
}

export default LogLevels;
