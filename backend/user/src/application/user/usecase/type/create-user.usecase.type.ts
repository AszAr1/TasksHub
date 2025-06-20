import { IUseCase } from "src/domain";
import { CreateUserRequestDto } from "../../dto";

export abstract class ICreateUserUseCase extends IUseCase<boolean, CreateUserRequestDto> { }