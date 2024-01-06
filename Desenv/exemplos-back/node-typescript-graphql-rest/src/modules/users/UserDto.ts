import { IsEmail, IsString } from 'class-validator'

export class UserDTO {
  @IsString()
  firstname: string
  @IsString()
  lastname: string
  @IsEmail()
  email: string
  @IsString()
  username: string
  @IsString()
  password: string
}
