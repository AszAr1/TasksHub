import { HttpException, HttpStatus, Injectable } from "@nestjs/common";
import { IGetUsersUseCase } from "../type";
import { IUserRepository, PaginationParams, PaginationResult, ServiceResponse } from "src/domain";
import { UserResponseDto } from "../../dto";
import { UserApplicationMapper } from "../../mapper";

@Injectable()
export class GetUsersUseCase implements IGetUsersUseCase {

  constructor(
    private readonly rep: IUserRepository,
    private readonly mapper: UserApplicationMapper,
  ) { }

  async invoke(params: PaginationParams): Promise<ServiceResponse<PaginationResult<UserResponseDto[]>>> {
    try {
      const req = await this.rep.getMany(params);
      return ServiceResponse.success({
        pagination: req.pagination,
        data: req.data.map(i => ({
          ...i,
        }))
      })
    } catch (error) {
      if (error instanceof HttpException) {
        return ServiceResponse.fail(error.message, error.getStatus());
      }

      return ServiceResponse.fail('Internal error', HttpStatus.INTERNAL_SERVER_ERROR);
    }
  }

}