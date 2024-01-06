import {
  Body,
  Controller,
  Delete,
  Get,
  HttpCode,
  HttpStatus,
  Param,
  ParseUUIDPipe,
  Post,
  Put,
  UseGuards,
} from '@nestjs/common';
import { ApiBearerAuth, ApiResponse, ApiTags } from '@nestjs/swagger';
import { AuthGuard } from '@nestjs/passport';
import { SystemUserCreateDto } from './systemuserCreate.dto';
import { SystemUserUpdateDto } from './systemuserUpdate.dto';
import { SystemUserService } from './systemuser.service';

@ApiBearerAuth('jwt')
@ApiTags('sysUser')
@Controller('v1/sysUser')
@UseGuards(AuthGuard('jwt'))
export class SystemUserController {
  constructor(private readonly sysUserService: SystemUserService) {}

  @Get()
  @ApiResponse({ type: [SystemUserCreateDto], status: HttpStatus.OK })
  @HttpCode(HttpStatus.OK)
  async getAll() {
    return await this.sysUserService.getAll();
  }

  @Post()
  @ApiResponse({ type: SystemUserCreateDto, status: HttpStatus.CREATED })
  @HttpCode(HttpStatus.CREATED)
  async create(@Body() body: SystemUserCreateDto) {
    return await this.sysUserService.create(body);
  }

  @Get(':id')
  @ApiResponse({ type: SystemUserCreateDto, status: HttpStatus.OK })
  @HttpCode(HttpStatus.OK)
  async get(@Param('id', new ParseUUIDPipe()) id: string) {
    return await this.sysUserService.get(id);
  }

  @Put(':id')
  @ApiResponse({ type: SystemUserUpdateDto, status: HttpStatus.ACCEPTED })
  @HttpCode(HttpStatus.ACCEPTED)
  async update(
    @Param('id', new ParseUUIDPipe()) id: string,
    @Body() body: SystemUserUpdateDto,
  ) {
    return await this.sysUserService.update(id, body);
  }

  @Delete(':id')
  @ApiResponse({ type: SystemUserCreateDto, status: HttpStatus.NO_CONTENT })
  @HttpCode(HttpStatus.NO_CONTENT)
  async delete(@Param('id', new ParseUUIDPipe()) id: string) {
    await this.sysUserService.delete(id);
  }
}
