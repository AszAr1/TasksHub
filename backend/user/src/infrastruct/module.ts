import { Module } from "@nestjs/common";
import { CONFIG_PROVIDER } from "./config";
import { DB_PROVIDER } from "./database";
import { REPOSITORY_PROVIDER } from "./repository";

@Module({
  providers: [
    ...CONFIG_PROVIDER,
    ...DB_PROVIDER,
    ...REPOSITORY_PROVIDER,
  ],
  exports: [
    ...CONFIG_PROVIDER,
    ...DB_PROVIDER,
    ...REPOSITORY_PROVIDER,
  ],
})
export class InfrastructModule { }