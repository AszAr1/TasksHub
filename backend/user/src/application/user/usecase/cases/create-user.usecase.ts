import { HttpException, HttpStatus, Injectable } from "@nestjs/common";
import { IUserRepository, ServiceResponse } from "src/domain";
import { CreateUserRequestDto } from "../../dto";
import { UserApplicationMapper } from "../../mapper";
import { ICreateUserUseCase } from "../type";

@Injectable()
export class CreateUserUseCase implements ICreateUserUseCase {

  constructor(
    private readonly rep: IUserRepository,
    private readonly mapper: UserApplicationMapper,
  ) { }

  async invoke(params: CreateUserRequestDto): Promise<ServiceResponse<boolean>> {
    try {
      const model = this.mapper.mapFromCreateRequestToModel(params);
      const request = await this.rep.create(model);

      return ServiceResponse.success(request);

    } catch (error) {

      if (error instanceof HttpException) {
        return ServiceResponse.fail(error.message, error.getStatus());
      }

      return ServiceResponse.fail('Internal server error', HttpStatus.INTERNAL_SERVER_ERROR);

    }
  }

}