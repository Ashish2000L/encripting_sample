def reg():
    file = open('init.txt', 'a')
    usrnm = input('Enter username: ').encode()
    paswrd = input('Enter password: ').encode()
    u_lst = list(usrnm)
    p_lst = list(paswrd)
    u_hexa = [hex(i)[2:] for i in u_lst]
    p_hexa = [hex(i)[2:] for i in p_lst]
    for i in u_hexa:
        file.write(str(i))
        file.write('-')
    file.write(',')
    for i in p_hexa:
        file.write(str(i))
        file.write('-')

    print("Registration successful !! \n")
    file.write('\n')
    file.close()
    return True
