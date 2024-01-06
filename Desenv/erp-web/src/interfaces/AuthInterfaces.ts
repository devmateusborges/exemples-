import { ISysUnit, ISysUser } from "./SysInterfaces";

export interface ILoginRequest {
  login: string;
  password: string;
  unit_id: string;
}

export interface ILoginSocialRequest {
  login: string;
}

export interface IRegisterRequest {
  name: string;
  login: string;
  email: string;
  username: string;
  password: string;
  document: string;
}

export interface IResetPasswordRequest {
  email: string;
}

export interface IRedefinePasswordRequest {
  password: string;
  new_password: string;
}
