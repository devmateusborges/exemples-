import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemAccessLogCreateDto {
  constructor(
    sessionid?: string,
    login?: string,
    login_year?: string,
    login_month?: string,
    login_day?: string,
    impersonated?: string,
    login_time?: number,
  ) {
    this.sessionid = sessionid;
    this.login = login;
    this.login_time = login_time;
    this.login_year = login_year;
    this.login_month = login_month;
    this.login_day = login_day;
    this.impersonated = impersonated;
  }

  @IsNotEmpty()
  @IsOptional()
  sessionid: string;
  @IsNotEmpty()
  @IsOptional()
  login: string;
  @IsNotEmpty()
  @IsOptional()
  login_time: number;
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
}
