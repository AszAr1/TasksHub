import { IUseCase, PaginationParams, PaginationResult } from "src/domain";
import { UserResponseDto } from "../../dto";

export abstract class IGetUsersUseCase extends IUseCase<PaginationResult<UserResponseDto[]>, PaginationParams> { }