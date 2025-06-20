import { Provider } from "@nestjs/common";
import { AppConfigService } from "./config.service";

export const CONFIG_PROVIDER: Provider[] = [AppConfigService];