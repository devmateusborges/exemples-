import { hash } from 'bcrypt';
import { EntityRepository, Repository } from 'typeorm';
import { SysUserDto } from '@dtos/sysUser.dto';
import { SysUserEntity } from '@entities/sysUsers.entity';
import { BusinessException } from '@exceptions/businessException';
import { isEmpty } from '@utils/util';

@EntityRepository()
class UserService extends Repository<SysUserEntity> {
  public async findAllObjs(): Promise<SysUserDto[]> {
    const dataObjs: SysUserDto[] = await SysUserEntity.find();
    return dataObjs;
  }

  public async findByIdObj(id: string): Promise<SysUserDto> {
    if (isEmpty(id)) throw new BusinessException(400, "You're not id");

    const dataObj: SysUserDto = await SysUserEntity.findOne({ where: { id: id } });
    if (!dataObj) throw new BusinessException(409, "You're not found");

    return dataObj;
  }

  public async createObj(dataObj: SysUserDto): Promise<SysUserDto> {
    if (isEmpty(dataObj)) throw new BusinessException(400, "You're not data");

    const dataObjFind: SysUserDto = await SysUserEntity.findOne({ where: { email: dataObj.email } });
    if (dataObjFind) throw new BusinessException(409, `You're email ${dataObj.email} already exists`);

    const hashedPassword = await hash(dataObj.password, 10);
    const dataObjCreate: SysUserDto = await SysUserEntity.create({ ...dataObj, password: hashedPassword }).save();

    return dataObjCreate;
  }

  public async updateObj(id: string, dataObj: SysUserDto): Promise<SysUserDto> {
    if (isEmpty(dataObj)) throw new BusinessException(400, "You're not data");

    const dataObjFind: SysUserDto = await SysUserEntity.findOne({ where: { id: id } });
    if (!dataObjFind) throw new BusinessException(409, "You're not found");

    const hashedPassword = await hash(dataObj.password, 10);
    await SysUserEntity.update(id, { ...dataObj, password: hashedPassword });

    const dataObjUpdate: SysUserDto = await SysUserEntity.findOne({ where: { id: id } });
    return dataObjUpdate;
  }

  public async deleteObj(id: string): Promise<SysUserDto> {
    if (isEmpty(id)) throw new BusinessException(400, "You're not id");

    const dataObjFind: SysUserDto = await SysUserEntity.findOne({ where: { id: id } });
    if (!dataObjFind) throw new BusinessException(409, "You're not found");

    await SysUserEntity.delete({ id: id });
    return dataObjFind;
  }
}

export default UserService;
