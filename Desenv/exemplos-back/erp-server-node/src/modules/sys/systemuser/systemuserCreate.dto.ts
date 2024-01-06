import { IsEmail, IsNotEmpty, Matches } from 'class-validator';
import { MessagesHelper } from '../../../helpers/messages.helper';
import { RegExHelper } from '../../../helpers/regex.helper';
import { ApiProperty } from '@nestjs/swagger';

export class SystemUserCreateDto {
  @ApiProperty()
  @IsNotEmpty()
  name: string;
  @ApiProperty()
  @IsNotEmpty()
  login: string;
  @ApiProperty()
  @IsNotEmpty()
  @Matches(RegExHelper.password, { message: MessagesHelper.PASSWORD_INVALID })
  password: string;
  @ApiProperty()
  @IsNotEmpty()
  email: string;
  @ApiProperty()
  @IsNotEmpty()
  active: string;
  @ApiProperty()
  @IsNotEmpty()
  active_message: string;
  @ApiProperty()
  @IsNotEmpty()
  phone: string;
  @ApiProperty()
  @IsNotEmpty()
  document: string;
  @ApiProperty()
  @IsNotEmpty()
  admin: string;
  @ApiProperty()
  @IsNotEmpty()
  login_ext: string;
  @ApiProperty()
  frontpage_id: string;
  @ApiProperty()
  @IsNotEmpty()
  origem: string;
  @ApiProperty()
  @IsNotEmpty()
  chat: string;
}
