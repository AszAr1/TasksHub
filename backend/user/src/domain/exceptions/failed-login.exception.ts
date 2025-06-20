import { HttpException, HttpStatus } from "@nestjs/common";

export class FailedLoginException extends HttpException {
  constructor() {
    super('Login failed. Uncorrect password or email', HttpStatus.BAD_REQUEST);
  }
}