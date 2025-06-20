export interface PaginationParams {
  cursor?: string | null;
  limit: number;
  search?: string;
}

export interface PaginationResult<D> {
  data: D;
  pagination: {
    cursor?: string | null;
    hasNextPage: boolean;
  };
}

export type PaginationHandler<R, P extends PaginationParams = PaginationParams> = (params: P) => Promise<PaginationResult<R>>;