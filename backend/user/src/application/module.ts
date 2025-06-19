import { Module } from "@nestjs/common";
import { APPLICATION_USER_PROVIDER } from "./user";
import { InfrastructModule } from "src/infrastruct";

@Module({
  imports: [InfrastructModule],
  providers: [
    ...APPLICATION_USER_PROVIDER,
  ],
  exports: [
    ...APPLICATION_USER_PROVIDER,
  ]
})
export class ApplicationModule { }