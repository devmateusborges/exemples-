import { HttpException, Injectable } from '@nestjs/common';
import { Queue } from 'bull';
import { InjectQueue } from '@nestjs/bull';
import { MailDto } from '../mail/mail.dto';
import LogService from '../log/log.service';

@Injectable()
export class MailProducer {
  constructor(
    @InjectQueue('sendMail-queue') private sendMailQueue: Queue,
    private logService: LogService,
  ) {}

  async sendMailJob(mailDto: MailDto) {
    try {
      const res = await this.sendMailQueue.add('sendMail-job', mailDto, {
        delay: 10000,
      });

      this.logService.createMailLog(
        __filename,
        'MailProducer.sendMailJob',
        mailDto,
      );
      return res;
    } catch (error) {
      throw new HttpException('Error add sendMail-job', 500);
    }
  }
}
