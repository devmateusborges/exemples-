import { Processor, Process } from '@nestjs/bull';
import { Job } from 'bull';
import LogService from '../log/log.service';
import { HttpException } from '@nestjs/common';
import { SystemSqlLogCreateDto } from '../modules/sys/systemSqlLog/systemSqlLogCreate.dto';

@Processor('sqlLog-queue')
export class SqlLogConsumer {
  constructor(private logService: LogService) {}

  @Process('sqlLog-job')
  async sqlLogJob(job: Job<SystemSqlLogCreateDto>) {
    try {
      this.logService.createSqlLog(__filename, 'sqlLogConsumer.sqlLogJob', job);
    } catch (error) {
      throw new HttpException('Error add sqlLog-job', 500);
    }
  }
}
