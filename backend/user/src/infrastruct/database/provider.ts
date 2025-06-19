import { Provider } from "@nestjs/common";
import { PrismaService } from "./prisma.service";

export const DB_PROVIDER: Provider[] = [
  PrismaService,
];