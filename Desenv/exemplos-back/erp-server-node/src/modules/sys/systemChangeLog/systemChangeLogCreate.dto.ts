import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemChangeLogCreateDto {
  constructor(
    logdate?: Date,
    login?: string,
    tablename?: string,
    primarykey?: string,
    pkvalue?: string,
    operation?: string,
    columnname?: string,
    oldvalue?: string,
    newvalue?: string,
    access_ip?: string,
    transaction_id?: string,
    log_trace?: string,
    session_id?: string,
    class_name?: string,
    php_sapi?: string,
    log_year?: string,
    log_month?: string,
    log_day?: string,
  ) {
    this.logdate = logdate;
    this.login = login;
    this.tablename = tablename;
    this.primarykey = primarykey;
    this.pkvalue = pkvalue;
    this.operation = operation;
    this.columnname = columnname;
    this.oldvalue = oldvalue;
    this.newvalue = newvalue;
    this.access_ip = access_ip;
    this.transaction_id = transaction_id;
    this.log_trace = log_trace;
    this.session_id = session_id;
    this.class_name = class_name;
    this.php_sapi = php_sapi;
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
  tablename: string;
  @IsNotEmpty()
  @IsOptional()
  primarykey: string;
  @IsNotEmpty()
  @IsOptional()
  pkvalue: string;
  @IsNotEmpty()
  @IsOptional()
  operation: string;
  @IsNotEmpty()
  @IsOptional()
  columnname: string;
  @IsNotEmpty()
  @IsOptional()
  oldvalue: string;
  @IsNotEmpty()
  @IsOptional()
  newvalue: string;
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
  log_year: string;
  @IsNotEmpty()
  @IsOptional()
  log_month: string;
  @IsNotEmpty()
  @IsOptional()
  log_day: string;
}
