import { Processor, Process } from '@nestjs/bull';
import { Job } from 'bull';
import { MailService } from '../mail/mail.service';
import { MailDto } from '../mail/mail.dto';
import LogService from '../log/log.service';
import { HttpException } from '@nestjs/common';

@Processor('sendMail-queue')
export class MailConsumer {
  constructor(
    private mailerService: MailService,
    private logService: LogService,
  ) {}

  @Process('sendMail-job')
  async sendMailJob(job: Job<MailDto>) {
    try {
      //TODO testar erro ao processar fila para marcar ela como não processada
      const { data } = job;
      await this.mailerService.sendEmail(data);
      this.logService.createMailLog(
        __filename,
        'MailConsumer.sendMailJob',
        job,
      );
    } catch (error) {
      throw new HttpException('Error add sendMail-job', 500);
    }
  }
}
