import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { SystemDocument } from '../../entities/SystemDocument.entity';
import { SystemDocumentCategory } from '../../entities/SystemDocumentCategory.entity';
import { SystemDocumentGroup } from '../../entities/SystemDocumentGroup.entity';
import { SystemDocumentUser } from '../../entities/SystemDocumentUser.entity';

@Module({
  imports: [
    TypeOrmModule.forFeature([
      SystemDocument,
      SystemDocumentCategory,
      SystemDocumentGroup,
      SystemDocumentUser,
    ]),
  ],
  providers: [],
  controllers: [],
  exports: [],
})
export class DocModule {}
