import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemSqlLogCreateDto {
  constructor(
    logdate?: Date,
    login?: string,
    database_name?: string,
    sql_command?: string,
    statement_type?: string,
    access_ip?: string,
    transaction_id?: string,
    log_trace?: string,
    session_id?: string,
    class_name?: string,
    php_sapi?: string,
    request_id?: string,
    log_year?: string,
    log_month?: string,
    log_day?: string,
  ) {
    this.logdate = logdate;
    this.login = login;
    this.database_name = database_name;
    this.sql_command = sql_command;
    this.statement_type = statement_type;
    this.access_ip = access_ip;
    this.transaction_id = transaction_id;
    this.log_trace = log_trace;
    this.session_id = session_id;
    this.class_name = class_name;
    this.php_sapi = php_sapi;
    this.request_id = request_id;
    this.log_year = log_year;
    this.log_month = log_month;
    this.log_day = log_day;
  }

  @IsNotEmpty()
  @IsOptional()
  logdate: Date;
  @IsNotEmpty()
  @IsOptional()
  login: string;
  @IsNotEmpty()
  @IsOptional()
  database_name: string;
  @IsNotEmpty()
  @IsOptional()
  sql_command: string;
  @IsNotEmpty()
  @IsOptional()
  statement_type: string;
  @IsNotEmpty()
  @IsOptional()
  access_ip: string;
  @IsNotEmpty()
  @IsOptional()
  transaction_id: string;
  @IsNotEmpty()
  @IsOptional()
  log_trace: string;
  @IsNotEmpty()
  @IsOptional()
  session_id: string;
  @IsNotEmpty()
  @IsOptional()
  class_name: string;
  @IsNotEmpty()
  @IsOptional()
  php_sapi: string;
  @IsNotEmpty()
  @IsOptional()
  request_id: string;
  @IsNotEmpty()
  @IsOptional()
  log_year: string;
  @IsNotEmpty()
  @IsOptional()
  log_month: string;
  @IsNotEmpty()
  @IsOptional()
  log_day: string;
}
