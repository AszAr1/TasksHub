import { IUseCase } from "src/domain";
import { UserResponseDto } from "../../dto";

type Params = {
  id: string
}

export abstract class IGetUserUsecase extends IUseCase<UserResponseDto, Params> { }