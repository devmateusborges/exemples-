import { Injectable, Logger, UnauthorizedException } from '@nestjs/common';
import { SystemUserService } from '../modules/sys/systemuser/systemuser.service';
import { compareSync, hashSync } from 'bcrypt';
import { JwtService } from '@nestjs/jwt';
import { AuthLoginDto } from './authLogin.dto';
import { SystemUser } from '../entities/SystemUser.entity';
import { SystemAccessLogService } from '../modules/sys/systemAccessLog/systemAccessLog.service';
import { SystemAccessLogCreateDto } from '../modules/sys/systemAccessLog/systemAccessLogCreate.dto';
import LogService from '../log/log.service';

@Injectable()
export class AuthService {
  private readonly logger = new Logger(AuthService.name);
  constructor(
    private readonly sysUserService: SystemUserService,
    private readonly jwtService: JwtService,
    private readonly logService: LogService,
  ) {
    this.logger.log('Init AuthService');
  }

  public async login(authLoginDTO: AuthLoginDto): Promise<any> {
    const user = await this.validateUser(authLoginDTO);

    const payload = { id: user.id, login: user.login, email: user.email };

    const token = this.jwtService.sign(payload);

    this.logService.createAccessLog(__filename, 'AuthService.login', user);

    return {
      token: token,
    };
  }

  async validateUser(authLoginDTO: AuthLoginDto): Promise<SystemUser> {
    let user;
    try {
      user = await this.sysUserService.getAll({ login: authLoginDTO.login });
    } catch (error) {
      throw new UnauthorizedException();
    }

    const isPasswordValid = compareSync(
      authLoginDTO.password,
      user[0].password,
    );
    if (!isPasswordValid) {
      throw new UnauthorizedException();
    }

    return user[0];
  }
}
