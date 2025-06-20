import { Provider } from "@nestjs/common";
import { ICreateUserUseCase, IGetUsersUseCase, IGetUserUsecase } from "../type";
import { CreateUserUseCase } from "./create-user.usecase";
import { GetUsersUseCase } from "./get-users.usecase";
import { GetUserUseCase } from "./get-user.usecase";


export const USER_USECASE_PROVIDER: Provider[] = [
  {
    provide: ICreateUserUseCase,
    useClass: CreateUserUseCase,
  },
  {
    provide: IGetUsersUseCase,
    useClass: GetUsersUseCase,
  },
  {
    provide: IGetUserUsecase,
    useClass: GetUserUseCase,
  }
]