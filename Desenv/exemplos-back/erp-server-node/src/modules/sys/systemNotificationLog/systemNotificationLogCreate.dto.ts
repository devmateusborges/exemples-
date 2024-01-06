import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemNotificationLogCreateDto {
  constructor(
    system_user_id: string,
    system_user_to_id: string,
    subject: string,
    message: string,
    email_to?: string,
    dt_message?: string,
    type_notification?: string,
    icon?: string,
    checked?: string,
    action_url1?: string,
    action_label1?: string,
    action_body1?: string,
    action_header1?: string,
    action_type1?: string,
    action_url2?: string,
    action_label2?: string,
    action_body2?: string,
    action_header2?: string,
    action_type2?: string,
    action_url3?: string,
    action_label3?: string,
    action_body3?: string,
    action_header3?: string,
    action_type3?: string,
  ) {
    this.system_user_id = system_user_id;
    this.system_user_to_id = system_user_to_id;
    this.subject = subject;
    this.message = message;
    this.email_to = email_to;
    this.dt_message = dt_message;
    this.type_notification = type_notification;
    this.icon = icon;
    this.checked = checked;
    this.action_url1 = action_url1;
    this.action_label1 = action_label1;
    this.action_body1 = action_body1;
    this.action_header1 = action_header1;
    this.action_type1 = action_type1;
    this.action_url2 = action_url2;
    this.action_label2 = action_label2;
    this.action_body2 = action_body2;
    this.action_header2 = action_header2;
    this.action_type2 = action_type2;
    this.action_url3 = action_url3;
    this.action_label3 = action_label3;
    this.action_body3 = action_body3;
    this.action_header3 = action_header3;
    this.action_type3 = action_type3;
  }

  @IsNotEmpty()
  system_user_id: string;
  @IsNotEmpty()
  subject: string;
  @IsNotEmpty()
  system_user_to_id: string;
  @IsNotEmpty()
  message: string;
  @IsNotEmpty()
  @IsOptional()
  email_to: string;
  @IsNotEmpty()
  @IsOptional()
  dt_message: string;
  @IsNotEmpty()
  @IsOptional()
  type_notification: string;
  @IsNotEmpty()
  @IsOptional()
  icon: string;
  @IsNotEmpty()
  @IsOptional()
  checked: string;
  @IsNotEmpty()
  @IsOptional()
  action_url1: string;
  @IsNotEmpty()
  @IsOptional()
  action_label1: string;
  @IsNotEmpty()
  @IsOptional()
  action_body1: string;
  @IsNotEmpty()
  @IsOptional()
  action_header1: string;
  @IsNotEmpty()
  @IsOptional()
  action_type1: string;
  @IsNotEmpty()
  @IsOptional()
  action_url2: string;
  @IsNotEmpty()
  @IsOptional()
  action_label2: string;
  @IsNotEmpty()
  @IsOptional()
  action_body2: string;
  @IsNotEmpty()
  @IsOptional()
  action_header2: string;
  @IsNotEmpty()
  @IsOptional()
  action_type2: string;
  @IsNotEmpty()
  @IsOptional()
  action_url3: string;
  @IsNotEmpty()
  @IsOptional()
  action_label3: string;
  @IsNotEmpty()
  @IsOptional()
  action_body3: string;
  @IsNotEmpty()
  @IsOptional()
  action_header3: string;
  @IsNotEmpty()
  @IsOptional()
  action_type3: string;
}
