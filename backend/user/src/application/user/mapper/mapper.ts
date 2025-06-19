import { Injectable } from "@nestjs/common";
import { CreateUserModel, UserModel, LoginUserModel } from "src/domain";
import { CreateUserRequestDto, UserResponseDto, LoginUserRequestDto } from "../dto";

@Injectable()
export class UserApplicationMapper {

  public mapFromCreateRequestToModel(dto: CreateUserRequestDto): CreateUserModel {
    return {
      ...dto,
    }
  }

  public mapFromDomainToResponse(model: UserModel): UserResponseDto {
    return {
      ...model,
    }
  }

  public mapFromLoginRequestToDomain(dto: LoginUserRequestDto): LoginUserModel {
    return {
      ...dto,
    }
  }

}