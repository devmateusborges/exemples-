import { Module } from '@nestjs/common';
import { BullModule } from '@nestjs/bull';

//TODO utilizar config do redis
@Module({
  imports: [
    BullModule.forRoot({
      redis: {
        host: '127.0.0.1',
        port: 6379,
      },
    }),
    BullModule.registerQueue(
      { name: 'accessLog-queue' },
      { name: 'changeLog-queue' },
      { name: 'sendMail-queue' },
      { name: 'notificationLog-queue' },
      { name: 'sqlLog-queue' },
    ),
  ],
  providers: [],
  exports: [BullModule],
})
export class QueueModule {}
