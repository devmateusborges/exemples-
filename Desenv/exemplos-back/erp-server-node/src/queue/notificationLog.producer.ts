import { HttpException, Injectable } from '@nestjs/common';
import { Queue } from 'bull';
import { InjectQueue } from '@nestjs/bull';
import LogService from '../log/log.service';
import { SystemNotificationLogCreateDto } from '../modules/sys/systemNotificationLog/systemNotificationLogCreate.dto';

@Injectable()
export class NotificationLogProducer {
  constructor(
    @InjectQueue('notificationLog-queue') private notificationLogQueue: Queue,
    private logService: LogService,
  ) {}

  async notificationLogJob(notificationLog: SystemNotificationLogCreateDto) {
    try {
      const res = await this.notificationLogQueue.add(
        'notificationLog-job',
        notificationLog,
        {
          delay: 10000,
        },
      );

      this.logService.createNotificationLog(
        __filename,
        'NotificationLogProducer.accessLogJob',
        notificationLog,
      );

      return res;
    } catch (error) {
      throw new HttpException('Error add notificationLog-job', 500);
    }
  }
}
