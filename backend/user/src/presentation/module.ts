import { Module } from "@nestjs/common";
import { UserController } from "./user/controller";
import { ApplicationModule } from "src/application";
import { InfrastructModule } from "src/infrastruct";

@Module({
  imports: [InfrastructModule, ApplicationModule],
  controllers: [UserController],
})
export class PresentationModule { }