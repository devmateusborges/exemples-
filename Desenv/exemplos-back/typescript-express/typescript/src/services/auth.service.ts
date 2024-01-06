import { compare, hash } from 'bcrypt';
import { sign } from 'jsonwebtoken';
import { EntityRepository, Repository } from 'typeorm';
import { SECRET_KEY } from '@utils/config';
import { SysUserDto } from '@dtos/sysUser.dto';
import { SysUserEntity } from '@entities/sysUsers.entity';
import { BusinessException } from '@exceptions/businessException';
import { TokenDataStore, TokenData } from '@interfaces/auth.interface';
import { isEmpty } from '@utils/util';
import { LoginDto } from '@/dtos/login.dto';

@EntityRepository()
class AuthService extends Repository<SysUserEntity> {
  public async signup(userData: SysUserDto): Promise<SysUserDto> {
    if (isEmpty(userData)) throw new BusinessException(400, "You're not userData");

    const findUser: SysUserDto = await SysUserEntity.findOne({ where: { email: userData.email } });
    if (findUser) throw new BusinessException(409, `You're email ${userData.email} already exists`);

    const hashedPassword = await hash(userData.password, 10);
    const createUserData: SysUserDto = await SysUserEntity.create({ ...userData, password: hashedPassword }).save();
    return createUserData;
  }

  public async login(userData: LoginDto): Promise<{ cookie: string; findUser: SysUserDto }> {
    if (isEmpty(userData)) throw new BusinessException(400, "You're not userData");

    const findUser: SysUserDto = await SysUserEntity.findOne({ where: { email: userData.email } });
    if (!findUser) throw new BusinessException(409, `You're email ${userData.email} not found`);

    const isPasswordMatching: boolean = await compare(userData.password, findUser.password);
    if (!isPasswordMatching) throw new BusinessException(409, "You're password not matching");

    const tokenData = this.createToken(findUser);
    const cookie = this.createCookie(tokenData);

    return { cookie, findUser };
  }

  public async logout(userData: SysUserDto): Promise<SysUserDto> {
    if (isEmpty(userData)) throw new BusinessException(400, "You're not userData");

    const findUser: SysUserDto = await SysUserEntity.findOne({ where: { email: userData.email, password: userData.password } });
    if (!findUser) throw new BusinessException(409, "You're not user");

    return findUser;
  }

  public createToken(user: SysUserDto): TokenData {
    const tokenDataStore: TokenDataStore = { id: user.id };
    const secretKey: string = SECRET_KEY;
    const expiresIn: number = 60 * 60;

    return { expiresIn, token: sign(tokenDataStore, secretKey, { expiresIn }) };
  }

  public createCookie(tokenData: TokenData): string {
    return `Authorization=${tokenData.token}; HttpOnly; Max-Age=${tokenData.expiresIn};`;
  }
}

export default AuthService;
