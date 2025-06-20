export type UserModel = {
  id: string;
  email: string;
  password: string;
  name: string;
  createdAt: Date;
  updatedAt: Date;
}

export type LoginUserModel = {
  email: string;
  password: string;
}

export type UpdateUserModel = {
  id: string;
  email?: string;
  password?: string;
  name?: string;
  createdAt?: Date;
  updatedAt?: Date;
}

export type CreateUserModel = {
  email: string;
  password: string;
  name: string;
}