import { IsNotEmpty, IsEmail, IsOptional } from 'class-validator';

export class MailDto {
  constructor(
    tos: Array<string>,
    link: string,
    textlink: string,
    textcall: string,
    textbody: string,
    token: string,
    subject?: string,
    template?: any,
    contextextra?: any,
    attachments?: Array<object>,
  ) {
    this.tos = tos;
    this.link = link;
    this.textlink = textlink;
    this.textcall = textcall;
    this.textbody = textbody;
    this.token = token;
    this.subject = subject;
    this.template = template;
    this.contextextra = contextextra;
    this.attachments = attachments;
  }
  @IsNotEmpty()
  //TODO ver esse array e validar com isEmail LF
  //@IsEmail()
  tos: Array<string>;
  @IsOptional()
  @IsNotEmpty()
  token: string;
  @IsNotEmpty()
  textcall: string;
  @IsNotEmpty()
  textbody: string;
  @IsNotEmpty()
  textlink: string;
  @IsNotEmpty()
  link: string;
  @IsOptional()
  attachments?: Array<object>;
  @IsNotEmpty()
  @IsOptional()
  subject: string;
  @IsNotEmpty()
  @IsOptional()
  template: any;
  @IsNotEmpty()
  @IsOptional()
  contextextra: any;
}
