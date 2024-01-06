export interface ISysUser {
  id: string;
  name: string;
  login: string;
  email: string;
  password: string;
  active: string;
}

export interface ISysUnit {
  id: string;
  name: string;
  sigla_unit: string;
  active: string;
}
