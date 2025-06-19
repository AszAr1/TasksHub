import { IUserRepository, ServiceResponse } from "src/domain";
import { UserResponseDto } from "../../dto";
import { IGetUserUsecase } from "../type";
import { HttpException, HttpStatus, Injectable } from "@nestjs/common";
import { UserApplicationMapper } from "../../mapper";

@Injectable()
export class GetUserUseCase implements IGetUserUsecase {

  constructor(
    private readonly rep: IUserRepository,
    private readonly mapper: UserApplicationMapper,
  ) { }

  async invoke(params: { id: string; }): Promise<ServiceResponse<UserResponseDto>> {
    try {

      const request = await this.rep.getOne(params.id);
      const response = this.mapper.mapFromDomainToResponse(request)

      return ServiceResponse.success(response);
    } catch (error) {

      if (error instanceof HttpException) {
        return ServiceResponse.fail(error.message, error.getStatus());
      }

      return ServiceResponse.fail('Internal error', HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }
}