import { IsNotEmpty } from 'class-validator';
export class SystemUserUpdateDto {
  @IsNotEmpty()
  name: string;
  @IsNotEmpty()
  login: string;
  @IsNotEmpty()
  email: string;
  @IsNotEmpty()
  active: string;
  @IsNotEmpty()
  active_message: string;
  @IsNotEmpty()
  phone: string;
  @IsNotEmpty()
  document: string;
  @IsNotEmpty()
  admin: string;
  @IsNotEmpty()
  login_ext: string;
  frontpage_id: string;
  @IsNotEmpty()
  origem: string;
  @IsNotEmpty()
  chat: string;
}
