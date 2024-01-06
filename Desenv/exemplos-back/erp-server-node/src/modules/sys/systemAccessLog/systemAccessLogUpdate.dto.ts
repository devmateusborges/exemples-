import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemAccessLogUpdate {
  @IsNotEmpty()
  @IsOptional()
  sessionid: string;
  @IsNotEmpty()
  @IsOptional()
  login: string;
  @IsNotEmpty()
  @IsOptional()
  login_time: Date;
  @IsNotEmpty()
  @IsOptional()
  login_year: string;
  @IsNotEmpty()
  @IsOptional()
  login_month: string;
  @IsNotEmpty()
  @IsOptional()
  login_day: string;
  @IsNotEmpty()
  @IsOptional()
  impersonated: string;
  @IsNotEmpty()
  @IsOptional()
  access_ip: string;
}
