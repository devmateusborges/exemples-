import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemEmailLogCreateDto {
  constructor(
    typeInOut: string,
    dateLog: Date,
    emailFrom: string,
    emailTo: string,
    subject: string,
    body?: string,
    errorMessage?: string,
    login?: string,
    dateSend?: Date,
    bodyType?: string,
    unitId?: string,
  ) {
    this.typeInOut = typeInOut;
    this.dateLog = dateLog;
    this.emailFrom = emailFrom;
    this.emailTo = emailTo;
    this.subject = subject;
    this.body = body;
    this.errorMessage = errorMessage;
    this.login = login;
    this.dateSend = dateSend;
    this.bodyType = bodyType;
    this.unitId = unitId;
  }
  @IsNotEmpty()
  typeInOut: string;
  @IsNotEmpty()
  dateLog: Date;
  @IsNotEmpty()
  emailFrom: string;
  @IsNotEmpty()
  subject: string;
  @IsNotEmpty()
  emailTo: string;
  @IsOptional()
  body: string;
  @IsNotEmpty()
  @IsOptional()
  errorMessage: string;
  @IsNotEmpty()
  @IsOptional()
  login: string;
  @IsNotEmpty()
  @IsOptional()
  dateSend: Date;
  @IsNotEmpty()
  bodyType: string;
  @IsNotEmpty()
  @IsOptional()
  unitId: string;
}
