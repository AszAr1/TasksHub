import { ServiceResponse } from "./service-response.type";

export abstract class IUseCase<R, P = undefined> {
  abstract invoke(params: P): Promise<ServiceResponse<R>>;
}