import { Injectable } from "@nestjs/common";
import { ConfigService } from "@nestjs/config";
import { AppConfigType, ServerConfigType, ServerCorsConfigType } from "./config.type";

@Injectable()
export class AppConfigService {
  constructor(private readonly cfgService: ConfigService) { }

  get AppServerConfig(): ServerConfigType {
    return this.cfgService.getOrThrow<ServerConfigType>('server');
  }

  get AppServerCorsConfig(): ServerCorsConfigType {
    return this.cfgService.getOrThrow<ServerCorsConfigType>('server.cors');
  }
}