import { HttpException, Injectable } from '@nestjs/common';
import { Queue } from 'bull';
import { InjectQueue } from '@nestjs/bull';
import LogService from '../log/log.service';
import { SystemChangeLogCreateDto } from '../modules/sys/systemChangeLog/systemChangeLogCreate.dto';

@Injectable()
export class ChangeLogProducer {
  constructor(
    @InjectQueue('changeLog-queue') private accessLogQueue: Queue,
    private logService: LogService,
  ) {}

  async changeLogJob(changeLog: SystemChangeLogCreateDto) {
    try {
      const res = await this.accessLogQueue.add('changeLog-job', changeLog, {
        delay: 10000,
      });

      this.logService.createChangeLog(
        __filename,
        'ChangeLogProducer.accessLogJob',
        changeLog,
      );
      return res;
    } catch (error) {
      throw new HttpException('Error add changeLog-job', 500);
    }
  }
}
