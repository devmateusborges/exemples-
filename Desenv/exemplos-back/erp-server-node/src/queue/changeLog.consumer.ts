import { Processor, Process } from '@nestjs/bull';
import { Job } from 'bull';
import LogService from '../log/log.service';
import { HttpException } from '@nestjs/common';
import { SystemChangeLogCreateDto } from '../modules/sys/systemChangeLog/systemChangeLogCreate.dto';

@Processor('changeLog-queue')
export class ChangeLogConsumer {
  constructor(private logService: LogService) {}

  @Process('changeLog-job')
  async changeLogJob(job: Job<SystemChangeLogCreateDto>) {
    try {
      this.logService.createChangeLog(
        __filename,
        'changeLogConsumer.changeLogJob',
        job,
      );
    } catch (error) {
      throw new HttpException('Error add changeLog-job', 500);
    }
  }
}
