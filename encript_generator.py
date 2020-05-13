import random
import uuid

sample = False
def cofactor(num):
    for i in range(2, num):
        if int(num % i) == 0:
            return False
    return True


def uuid_check(ids):
    file_read = open('messages.txt', 'r')
    for i in file_read:
        i = i.replace(',', ' ')
        i = i.split(' ')
        if ids == i[0]:
            file_read.close()
            return False
    file_read.close()
    return True


def Message(text):
    global sample, id
    message = text.encode()
    p = list(message)
    k = []
    for i in range(len(p)):
        ask = True
        while (ask):
            m = random.randrange(100000)
            if (cofactor(m)):
                k.append(m)
                ask = False

    a = [x + y for x, y in zip(p, k)]
    file_gen = open('messages.txt', 'a')

    while (not sample):
        id=''
        unique_id = uuid.uuid4()
        unique_id = str(unique_id).replace('-', '')
        for i in unique_id:
            if str(i).isnumeric():
                id = id + i
        if uuid_check(id[:8]):
            sample = True

    sample=False
    unique_id = str(id[:8])
    file_gen.write(unique_id)

    file_gen.write(',')

    for i in k:
        file_gen.write(str(i))
        file_gen.write('-')

    hexadecimal = [hex(i)[2:] for i in a]
    encript = ''
    for i in hexadecimal:
        encript = encript + i + '-'
    file_gen.write(',')
    file_gen.write(encript)
    file_gen.write('\n')
    file_gen.close()
    print('\t\t\t Message encripting Successful :) \n')
    print("\t\t\t unique code is: ", unique_id)
    print('\n')