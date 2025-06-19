import * as bcrypt from 'bcrypt';

export class PasswordUtils {
  public async generateAndHashPassword() {
    const generatedPassword = this.generateRandomString(12);
    const hashedPassword = await bcrypt.hash(
      generatedPassword,
      await bcrypt.genSalt(10),
    );
    return hashedPassword;
  }

  public async hashPassword(password: string) {
    return bcrypt.hash(password, await bcrypt.genSalt(10));
  }

  public async comparePassword({
    hashedPassowrd,
    normal_password,
  }: {
    normal_password: string;
    hashedPassowrd: string;
  }) {
    return bcrypt.compare(normal_password, hashedPassowrd);
  }

  private generateRandomString(length: number) {
    const characters =
      'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }
}
