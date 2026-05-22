flag = 0
while 1:
    password_input = int(input("Mời bạn nhập mật khẩu: "))
    if password_input != 123456:
        flag += 1
        if flag == 3:
            print("Tài khoản đã bị khóa!")
            break
        print("Mật khẩu sai, vui lòng nhập lại!")
    else:
        print("Đăng nhập thành công!")
        break

    