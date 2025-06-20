import { Provider } from "@nestjs/common";
import { IUserRepository } from "src/domain";
import { UserRepository } from "./repository";

export const REPOSITORY_PROVIDER: Provider[] = [
  {
    provide: IUserRepository,
    useClass: UserRepository,
  }
]