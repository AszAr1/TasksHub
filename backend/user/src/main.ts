import { NestFactory } from '@nestjs/core';
import { CoreModule } from './core/core.module';
import { AppConfigService } from './infrastruct/config';

async function bootstrap() {
  const app = await NestFactory.create(CoreModule);
  const cfg = app.get(AppConfigService);

  app.enableCors({
    credentials: cfg.AppServerCorsConfig.allowCookies,
    methods: cfg.AppServerCorsConfig.allowedMethods,
    origin: cfg.AppServerCorsConfig.frontendLink,
  });

  await app.listen(cfg.AppServerConfig.port, () => {
    console.log('Server is running on port:' + '' + cfg.AppServerConfig.port);
  });
}
bootstrap();
