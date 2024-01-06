import { GenericDto } from '@/utils/genericDto';
import { IsEmail, IsString } from 'class-validator';

export class SysUserDto extends GenericDto {
  @IsEmail()
  public email: string;
  @IsString()
  public name: string;
  @IsString()
  public login: string;
  @IsString()
  public password: string;
}
