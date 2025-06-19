export type ServerCorsConfigType = {
  frontendLink: string;
  allowedMethods: string;
  allowCookies: boolean;
}

export type ServerConfigType = {
  port: string;
  host: string;
  cors: ServerCorsConfigType;
}

export type AppConfigType = {
  server: ServerConfigType;
}