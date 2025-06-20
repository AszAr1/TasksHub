export class UserResponseDto {
  id: string;
  email: string;
  name: string;
  createdAt: Date;
  updatedAt: Date;

  constructor(data: {
    id: string;
    email: string;
    name: string;
    createdAt: Date;
    updatedAt: Date;
  }) {
    this.id = data.id;
    this.email = data.email;
    this.name = data.name;
    this.createdAt = data.createdAt,
      this.updatedAt = data.updatedAt;
  }
}