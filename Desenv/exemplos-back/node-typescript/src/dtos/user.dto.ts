import { IsNotEmpty, IsString } from 'class-validator';
 
class CreateUsertDto {
  @IsString()
  @IsNotEmpty()
  public xxx: string;
 
}
 
export default CreateUsertDto;