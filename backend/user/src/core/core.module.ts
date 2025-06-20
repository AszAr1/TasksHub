import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { ApplicationModule } from 'src/application';
import { InfrastructModule } from 'src/infrastruct';
import loadAppConfig from 'src/infrastruct/config/config.setup';
import { PresentationModule } from 'src/presentation';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      load: [loadAppConfig],
    }),
    InfrastructModule,
    ApplicationModule,
    PresentationModule,
  ],
})
export class CoreModule { }
