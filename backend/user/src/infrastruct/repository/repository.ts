import { Injectable } from "@nestjs/common";
import { AlreadyExistsException, CreateUserModel, FailedLoginException, getClearObjectFields, IUserRepository, LoginUserModel, PaginationHandler, UpdateUserModel, UserModel, UserNotFoundException } from "src/domain";
import { PrismaService } from "../database";
import { PasswordUtils } from "src/package";
import { Prisma } from "../database/generated/prisma/client";

@Injectable()
export class UserRepository implements IUserRepository {

  constructor(private readonly prisma: PrismaService) { }

  async login(loginData: LoginUserModel): Promise<UserModel> {

    const passwordUtils = new PasswordUtils();

    const existedUser = await this.prisma.user.findUnique({
      where: {
        email: loginData.email,
      },
    });

    if (!existedUser) {
      throw new UserNotFoundException();
    }

    const isValidPassword = await passwordUtils.comparePassword({
      hashedPassowrd: existedUser.password,
      normal_password: loginData.password,
    });

    if (!isValidPassword) {
      throw new FailedLoginException();
    }

    return existedUser;
  }

  async create(createModel: CreateUserModel): Promise<boolean> {
    const existedUser = await this.prisma.user.findUnique({
      where: {
        email: createModel.email,
      },
    });

    if (existedUser) {
      throw new AlreadyExistsException();
    }

    const passwordUtils = new PasswordUtils();

    const hashedPassword = await passwordUtils.hashPassword(createModel.password);

    await this.prisma.user.create({
      data: {
        createdAt: new Date(),
        updatedAt: new Date(),
        email: createModel.email,
        name: createModel.name,
        password: hashedPassword,
      }
    });

    return true;
  }

  getMany: PaginationHandler<UserModel[]> = async (params) => {

    const where: Prisma.UserWhereInput = {}
    const cursor: Prisma.UserWhereUniqueInput | undefined = undefined;

    if (params.cursor) {
      cursor!.id = params.cursor;
    }

    if (params.search) {
      where.name = { contains: params.search, mode: "insensitive" };
    }

    const users = await this.prisma.user.findMany({
      where,
      cursor,
      take: params.limit + 1,
      skip: params.cursor ? 1 : 0,
      orderBy: {
        createdAt: 'asc',
      },
    })

    const hasNextPage = users.length > params.limit;
    const nextCursor = hasNextPage ? users[users.length - 1].id : null;

    return {
      data: users,
      pagination: {
        hasNextPage,
        cursor: nextCursor,
      }
    }
  };

  async getOne(id: string): Promise<UserModel> {
    const user = await this.prisma.user.findUnique({
      where: {
        id: id
      },
    });

    if (!user) {
      throw new UserNotFoundException();
    }

    return user;
  }

  async update(updateModel: UpdateUserModel): Promise<boolean> {
    const passwordUtils = new PasswordUtils();
    const dataForUpdate = getClearObjectFields(updateModel);

    if (dataForUpdate.hasOwnProperty('password')) {
      dataForUpdate['password'] = await passwordUtils.hashPassword(dataForUpdate['password']);
    }

    await this.prisma.user.update({
      where: {
        id: updateModel.id,
      },
      data: {
        ...dataForUpdate,
      },
    });

    return true;
  }

  async delete(id: string): Promise<boolean> {
    await this.prisma.user.delete({
      where: {
        id,
      },
    });

    return true;
  }

}