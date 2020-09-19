from register import reg
from login import log
from encript_generator import Message
from encript_breaker import unique_id

result_stat = False
reg_stat = False
count = 0
print("\t\t\t Welcome User ")
print("\t\t\t NOTE: To exit, enter invaild input!!")
lg = ['login', 'Login']
res = ['register', 'Register']
while (not result_stat):
    final_input = input("Please write \nRegister (if new User) \nLogin (if existing user)\n")
    if (final_input in lg and count < 3):
        result_stat = log()
        count += 1
        continue

    elif (final_input in res):
        reg_stat = reg()
        if (reg_stat):
            result_stat = log()
        else:
            reg_stat = False
            result_stat = False
    else:
        print("Invalid Option :(")
        result_stat = False
        reg_stat = False
        stat = input("If you like to quit please write quit else press enter: ")
        if (stat == 'quit' or stat == 'Quit'):
            print("Thank you :)")
            quit()
        elif (stat=='No' or stat=='no'):
            continue
while (result_stat):
    inpt = input("what you like to do \nEncript \nDecript \n")
    if (inpt == 'Encript' or inpt == 'encript'):
        mesg = input("Enter your Message: ")
        Message(mesg)
        print('\n')
    elif (inpt == 'Decript' or inpt == 'decript'):
        cde = input("Enter your code: ")
        print("Your Message is: ")
        print(unique_id(cde),'\n')
        #raise Exception(unique_id(cde))
    else:
        print('Invalid Input :( \n')
        qt = input("Do you want to continue: ")
        if (qt == 'no' or qt == 'NO'):
            print("Thank you :) \n")
            result_stat = False
            quit()
        elif(qt=='yes' or qt=='Yes'):
            result_stat = True
            print('\n')
            continue



