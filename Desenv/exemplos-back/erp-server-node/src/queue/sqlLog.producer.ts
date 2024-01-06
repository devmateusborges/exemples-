import { HttpException, Injectable } from '@nestjs/common';
import { Queue } from 'bull';
import { InjectQueue } from '@nestjs/bull';
import LogService from '../log/log.service';
import { SystemSqlLogCreateDto } from '../modules/sys/systemSqlLog/systemSqlLogCreate.dto';

@Injectable()
export class SqlLogProducer {
  constructor(
    @InjectQueue('sqlLog-queue') private sqlLogQueue: Queue,
    private logService: LogService,
  ) {}

  async sqlLogJob(sqlLog: SystemSqlLogCreateDto) {
    try {
      const res = await this.sqlLogQueue.add('sqlLog-job', sqlLog, {
        delay: 10000,
      });

      this.logService.createSqlLog(
        __filename,
        'SqlLogProducer.accessLogJob',
        sqlLog,
      );

      return res;
    } catch (error) {
      throw new HttpException('Error add sqlLog-job', 500);
    }
  }
}
