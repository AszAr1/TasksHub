import { Body, Controller, Get, Param, Post, Res } from "@nestjs/common";
import { ROUTES } from "./routes";
import { CreateUserRequestDto, ICreateUserUseCase, IGetUsersUseCase, IGetUserUsecase } from "src/application/user";
import { Response } from "express";

@Controller([ROUTES.KEY])
export class UserController {
  constructor(
    private readonly createUsecUseCase: ICreateUserUseCase,
    private readonly getUsersUsecUseCase: IGetUsersUseCase,
    private readonly getUserUseCase: IGetUserUsecase,
  ) { }

  @Post(ROUTES.CREATE)
  async createUser(
    @Body() createData: CreateUserRequestDto,
    @Res() response: Response
  ) {
    const request = await this.createUsecUseCase.invoke(createData);

    if (request.isFailure()) {
      return response.status(request.Code).json(request.Error);
    }

    return response.status(request.Code).json(request.Data);
  }

  @Get(ROUTES.GET_MANY)
  async getMany(@Res() response: Response) {
    const request = await this.getUsersUsecUseCase.invoke({
      limit: 10,
    });

    if (request.isFailure()) {
      return response.status(request.Code).json(request.Error);
    }

    return response.status(request.Code).json(request.Data);
  }

  @Get(ROUTES.GET_BY_ID)
  async getUserById(
    @Param('id') id: string,
    @Res() response: Response,
  ) {
    const request = await this.getUserUseCase.invoke({ id: id });

    if (request.isFailure()) {
      return response.status(request.Code).json(request.Error);
    }

    return response.status(request.Code).json(request.Data);
  }

}