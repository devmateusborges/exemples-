import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemEmailLogUpdate {
  @IsNotEmpty()
  typeInOut: string;
  @IsNotEmpty()
  dateLog: Date;
  @IsNotEmpty()
  emailFrom: string;
  @IsNotEmpty()
  subject: string;
  @IsOptional()
  body: string;
  @IsNotEmpty()
  @IsOptional()
  errorMessage: string;
  @IsNotEmpty()
  emailTo: string;
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
