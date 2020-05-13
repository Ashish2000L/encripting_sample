def logins():
    User = input("Enter Username: ").encode()
    pasd = input("Enter password: ").encode()
    U_lst = list(User)
    P_lst = list(pasd)
    U_hexa = [hex(i)[2:] for i in U_lst]
    P_hexa = [hex(i)[2:] for i in P_lst]

    return U_hexa, P_hexa

def status():
    stat = False
    user_nm, pass_word = logins()
    file_files = open('init.txt', 'r')
    apps = open('init.txt', 'a')
    eof = apps.tell()
    loc_file = file_files.tell()
    while ((loc_file < eof)):
        details = file_files.readline()
        details = details.replace(',', ' ')
        details = details.split(' ')
        loc_file = file_files.tell()
        for i in range(2):
            details[i] = details[i].replace('-', ' ')
            details[i] = details[i].replace('\n', '')
            details[i] = details[i].rstrip(' ')
        username = details[0].split(' ')
        password = details[1].split(' ')
        if username == user_nm:
            if password == pass_word:
                print("you are successfully logged in :) \n")
                apps.close()
                file_files.close()
                return True
            else:
                print("password dosen't matches with username :( \n")
                apps.close()
                file_files.close()
                return False
    print("No such use exist :3 \n")
    apps.close()
    file_files.close()
    return False



def log():
    return status()



