import { ValidationError } from 'class-validator';
import { Global } from '@nestjs/common';
import { validate } from 'class-validator';

@Global()
export class UtilsService {
  static formatErrors(validationErrors: ValidationError[]): string {
    const errorsArray: string[] = [];

    for (const error of validationErrors) {
      let errorsString = `\n\`${error.property}\` errors:\n`;

      for (const constraint in error.constraints) {
        if (!error.constraints.hasOwnProperty(constraint)) {
          continue;
        }

        errorsString += `    - ${error.constraints[constraint]}\n`;
      }

      errorsArray.push(errorsString);
    }

    return errorsArray.join('\n');
  }

  static async validateErrors(input): Promise<void> {
    const valid = await validate(input);
    if (valid.length > 0) {
      throw new Error(UtilsService.formatErrors(valid));
    }
  }
}
