import { Module } from '@nestjs/common';
import { MailerModule } from '@nestjs-modules/mailer';
import { HandlebarsAdapter } from '@nestjs-modules/mailer/dist/adapters/handlebars.adapter';
import { MailService } from './mail.service';
import { join } from 'path';
import { ConfigService } from '../config/config.service';
import { ConfigModule } from '../config/config.module';
import { MailProducer } from '../queue/mail.producer';
import { MailConsumer } from '../queue/mail.consumer';
import { QueueModule } from '../queue/queue.module';
import { LogModule } from '../log/log.module';
@Module({
  imports: [
    ConfigModule,
    LogModule,
    MailerModule.forRootAsync({
      useFactory: async (config: ConfigService) => ({
        transport: {
          host: config.get('MAIL_SMTP_HOST'),
          secure: false,
          auth: {
            user: config.get('MAIL_SMTP_USER'),
            pass: config.get('MAIL_SMTP_PASS'),
          },
        },
        defaults: {
          from: 'suporte@resultfacil.com.br',
        },
        template: {
          dir: join(__dirname, 'templates'),
          adapter: new HandlebarsAdapter(),
          options: {
            strict: true,
          },
        },
      }),
      inject: [ConfigService],
    }),
    QueueModule,
  ],
  providers: [MailService, MailProducer, MailConsumer],
  exports: [MailService, MailProducer],
})
export class MailModule {}
