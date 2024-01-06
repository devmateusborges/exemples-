import { Module } from '@nestjs/common';
import LogCustom from './logCustom';
import LogService from './log.service';

@Module({
  imports: [],
  providers: [
    {
      provide: LogCustom,
      useValue: new LogCustom(),
    },
    LogService,
  ],
  exports: [LogService],
})
export class LogModule {}
