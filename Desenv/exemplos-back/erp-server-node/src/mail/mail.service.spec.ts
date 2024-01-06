import { Test, TestingModule } from '@nestjs/testing';
import { MailService } from './mail.service';
import { MailModule } from './mail.module';
import { MailDto } from './mail.dto';
import { INestApplication } from '@nestjs/common';
import { LogModule } from '../log/log.module';

jest.setTimeout(10000);

//TODO LF - fechar conexao com redis ao finalizar teste para nao ter vazamento
describe('MailService', () => {
  let app: INestApplication;
  let mailService: MailService;

  beforeAll(async () => {
    const moduleRef: TestingModule = await Test.createTestingModule({
      imports: [LogModule, MailModule],
    }).compile();

    app = await moduleRef.createNestApplication();
    await app.init();

    mailService = moduleRef.get<MailService>(MailService);
  });

  // afterAll(async () => {
  //   await app.close();
  // });

  describe('sedEmail', () => {
    it('send email test', async () => {
      jest.spyOn(mailService, 'sendEmail');

      const input = new MailDto(
        ['admin@gmail.com', 'lucas.ferreira.arantes@gmail.com'],
        'dev.resultfacil.com.br?token=xxxx',
        'Testing SendEmail',
        'seu usuário foi criado com sucesso, por favor complete seu registro clicando no botão abaixo',
        'Caso tenha dúvidas, por favor entre contato com nosso SUPORTE pelo(s) telefones {{websitetelefones}}',
        'token',
        'teste',
        null,
        null,
        null,
      );

      const res = await mailService.addEmailQueue(input);

      expect(res).toBeDefined();
    }, 20000);
  });
});
