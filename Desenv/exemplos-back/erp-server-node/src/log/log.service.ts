import { SystemEmailLog } from './../entities/SystemEmailLog.entity';
import { Injectable } from '@nestjs/common';
import { getManager, Timestamp } from 'typeorm';
import { SystemEmailLogCreateDto } from '../modules/sys/systemEmailLog/systemEmailLogCreate.dto';
import { SystemAccessLog } from '../entities/SystemAccessLog.entity';
import { SystemChangeLog } from '../entities/SystemChangeLog.entity';
import { SystemNotificationLogCreateDto } from '../modules/sys/systemNotificationLog/systemNotificationLogCreate.dto';
import { SystemAccessLogCreateDto } from '../modules/sys/systemAccessLog/systemAccessLogCreate.dto';
import { SystemChangeLogCreateDto } from '../modules/sys/systemChangeLog/systemChangeLogCreate.dto';
import { SystemNotificationLog } from '../entities/SystemNotificationLog.entity';
import { SystemSqlLog } from '../entities/SystemSqlLog.entity';
import { SystemSqlLogCreateDto } from '../modules/sys/systemSqlLog/systemSqlLogCreate.dto';

@Injectable()
export default class LogService {
  async createLog(
    log: any,
    //log: CreateLogDto
  ) {
    console.log('>>>createLog');
    //TODO ajustar para gravar onde quiser, pg mongo etc
    /*const newLog = await this.logsRepository.create(log);
    await this.logsRepository.save(newLog, {
      data: {
        isCreatingLogs: true
      }
    })
    */

    return null; //newLog;
  }
  async createMailLog(filename: string, metodoname: string, obj: any) {
    console.log('>>>createMailLog > ' + filename + ' > ' + metodoname);

    //TODO EJ - verificar possibilidade de passar para service, mais estava dando erros nos teste devido injecao de depencia
    //TODO LF - aqui poderia chamar controller inves de instanciar o service
    const repo = await getManager('local').getRepository(SystemEmailLog);
    await repo.save(
      new SystemEmailLogCreateDto(
        'OU',
        new Date(),
        '.',
        obj.data.tos[0],
        obj.data.subject,
        obj.data.textbody,
        null,
        null,
        null,
        'HTML',
      ),
    );
  }

  async createAccessLog(filename: string, metodoname: string, obj: any) {
    console.log('>>>createAccessLog > ' + filename + ' > ' + metodoname);
    const repo = await getManager('local').getRepository(SystemAccessLog);
    const date = new Date();

    await repo.save(
      new SystemAccessLogCreateDto(
        'teste',
        obj.login,
        date.getFullYear().toString(),
        date.getMonth().toString(),
        date.getDate().toString(),
        '1',
        date.getTime(),
      ),
    );
  }

  async createChangeLog(filename: string, metodoname: string, obj: any) {
    console.log('>>>createChangeLog > ' + filename + ' > ' + metodoname);
    const repo = await getManager('local').getRepository(SystemChangeLog);
    await repo.save(
      new SystemChangeLogCreateDto(
        new Date(),
        obj.data.login,
        obj.data.tablename,
        obj.data.primarykey,
        obj.data.pkvalue,
        obj.data.operation,
        obj.data.columnname,
        obj.data.oldvalue,
        obj.data.newvalue,
        obj.data.access_ip,
        obj.data.transaction_id,
        obj.data.log_trace,
        obj.data.session_id,
        obj.data.class_name,
        obj.data.php_sapi,
        obj.data.log_year,
        obj.data.log_month,
        obj.data.log_day,
      ),
    );
  }

  async createNotificationLog(filename: string, metodoname: string, obj: any) {
    console.log('>>>createNotificationLog > ' + filename + ' > ' + metodoname);
    const repo = await getManager('local').getRepository(SystemNotificationLog);
    await repo.save(
      new SystemNotificationLogCreateDto(
        obj.data.system_user_id,
        obj.data.system_user_to_id,
        obj.data.subject,
        obj.data.message,
        obj.data.email_to,
        obj.data.dt_message,
        obj.data.type_notification,
        obj.data.icon,
        obj.data.checked,
        obj.data.action_url1,
        obj.data.action_label1,
        obj.data.action_body1,
        obj.data.action_header1,
        obj.data.action_type1,
        obj.data.action_url2,
        obj.data.action_label2,
        obj.data.action_body2,
        obj.data.action_header2,
        obj.data.action_type2,
        obj.data.action_url3,
        obj.data.action_label3,
        obj.data.action_body3,
        obj.data.action_header3,
        obj.data.action_type3,
      ),
    );
  }

  async createSqlLog(filename: string, metodoname: string, obj: any) {
    console.log('>>>createSqlLog > ' + filename + ' > ' + metodoname);
    const repo = await getManager('local').getRepository(SystemSqlLog);
    await repo.save(
      new SystemSqlLogCreateDto(
        new Date(),
        obj.data.login,
        obj.data.database_name,
        obj.data.sql_command,
        obj.data.statement_type,
        obj.data.access_ip,
        obj.data.transaction_id,
        obj.data.log_trace,
        obj.data.session_id,
        obj.data.class_name,
        obj.data.php_sapi,
        obj.data.request_id,
        obj.data.log_year,
        obj.data.log_month,
        obj.data.log_day,
      ),
    );
  }
}
