import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemSqlLogUpdate {
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
