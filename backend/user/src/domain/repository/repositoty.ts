import { CreateUserModel, LoginUserModel, UpdateUserModel, UserModel } from "../models";
import { PaginationHandler } from "../types";

export abstract class IUserRepository {
  abstract create(createModel: CreateUserModel): Promise<boolean>;
  abstract getMany: PaginationHandler<UserModel[]>;
  abstract getOne(id: string): Promise<UserModel>;
  abstract update(updateModel: UpdateUserModel): Promise<boolean>;
  abstract delete(id: string): Promise<boolean>;
  abstract login(login: LoginUserModel): Promise<UserModel>;
}