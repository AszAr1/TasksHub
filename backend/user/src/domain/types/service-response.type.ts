import { HttpStatus } from "@nestjs/common";

export class ServiceResponse<T> {
  private data?: T;
  private error?: string;
  private code: number;

  public get Data() {
    return {
      data: this.data,
      code: this.code,
    };
  }

  public get Error() {
    return {
      error: this.error,
      code: this.code,
    };
  }

  public get Code() {
    return this.code;
  }

  private constructor(props: {
    data?: T,
    error?: string,
    code: number;
  }) {
    this.data = props.data;
    this.error = props.error;
    this.code = props.code;
  }

  static success<T>(data: T): ServiceResponse<T> {
    return new ServiceResponse({
      data,
      code: HttpStatus.OK,
    });
  }

  static fail<T>(error: string, code: number): ServiceResponse<T> {
    return new ServiceResponse({
      error,
      code,
    });
  }

  public isFailure(): boolean {
    return !!this.error;
  }
}