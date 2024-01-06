import { IsNotEmpty, IsOptional } from 'class-validator';

export class SystemNotificationLogUpdate {
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
