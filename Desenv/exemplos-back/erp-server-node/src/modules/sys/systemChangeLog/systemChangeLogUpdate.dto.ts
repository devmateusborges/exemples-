import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemChangeLogUpdate {
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
