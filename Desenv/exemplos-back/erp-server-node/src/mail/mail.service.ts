import { MailerService } from '@nestjs-modules/mailer';
import { Injectable } from '@nestjs/common';
import { MailDto } from './mail.dto';
import { UtilsService } from '../shared/bases/utils.service';
import { MailProducer } from '../queue/mail.producer';
import LogService from '../log/log.service';

@Injectable()
export class MailService {
  constructor(
    private mailerService: MailerService,
    private mailerProducer: MailProducer,
    private logService: LogService,
  ) {}

  async addEmailQueue(input: MailDto) {
    await UtilsService.validateErrors(input);
    const res = await this.mailerProducer.sendMailJob(input);
    return res;
  }

  async sendEmail(input: MailDto) {
    await UtilsService.validateErrors(input);

    const auxAttachments: Array<any> = [];

    if (input.attachments) {
      let file: object;

      for (file of input.attachments) {
        auxAttachments.push(file);
      }
    }

    let auxTemplate = './email_empty';
    let auxContext = {};

    if (input.template) {
      auxTemplate = './' + input.template;

      //TODO as variaveis de marca e site devem ser buscadas do banco de dados, pensar como fazer isso, usar systemparamservice.
      auxContext = {
        link: input.link,
        textlink: input.textlink,
        textcall: input.textcall,
        textbody: input.textbody,
        website: '{{website}}',
        websitemarca: '{{websitemarca}}',
      };

      if (input.contextextra) {
        const arrayContext = Object.entries(input.contextextra);
        arrayContext.forEach((contx) => {
          auxContext[contx[0]] = contx[1];
        });
      }
    }

    await this.mailerService.sendMail({
      to: input.tos,
      subject: input.subject,
      template: auxTemplate,
      context: auxContext,
      attachments: auxAttachments,
    });
  }
}
