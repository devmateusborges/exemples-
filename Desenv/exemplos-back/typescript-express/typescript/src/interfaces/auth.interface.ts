import { SysUserDto } from '@/dtos/sysUser.dto';
import { Request } from 'express';

export interface TokenDataStore {
  id: string;
}

export interface TokenData {
  token: string;
  expiresIn: number;
}

export interface RequestUser extends Request {
  user: SysUserDto;
}
