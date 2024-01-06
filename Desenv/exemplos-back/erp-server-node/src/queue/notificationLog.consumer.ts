import { Processor, Process } from '@nestjs/bull';
import { Job } from 'bull';
import LogService from '../log/log.service';
import { HttpException } from '@nestjs/common';
import { SystemNotificationLogCreateDto } from '../modules/sys/systemNotificationLog/systemNotificationLogCreate.dto';

@Processor('notificationLog-queue')
export class NotificationLogConsumer {
  constructor(private logService: LogService) {}

  @Process('notificationLog-job')
  async notificationLogJob(job: Job<SystemNotificationLogCreateDto>) {
    try {
      this.logService.createNotificationLog(
        __filename,
        'notificationLogConsumer.notificationLogJob',
        job,
      );
    } catch (error) {
      throw new HttpException('Error add notificationLog-job', 500);
    }
  }
}
