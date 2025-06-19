import { Provider } from "@nestjs/common";
import { UserApplicationMapper } from "./mapper";
import { USER_USECASE_PROVIDER } from "./usecase";

export const APPLICATION_USER_PROVIDER: Provider[] = [
  UserApplicationMapper,
  ...USER_USECASE_PROVIDER,
];