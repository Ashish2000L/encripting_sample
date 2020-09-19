def find_message(code):
    file_break = open('messages.txt', 'r')
    file_append = open('messages.txt', 'a')
    final_location=file_append.tell()
    fi_loc=file_break.tell()
    while(fi_loc<final_location):
        line=file_break.readline()
        line=line.replace(',',' ')
        line=line.split(' ')
        if line[0]==code:
            file_break.close()
            file_append.close()
            return line[1], line[2]
    print("No Such Message exist, please check your code again :$ \n")
    file_append.close()
    file_break.close()
    return 0,0

def encrepting_message(text):
    text=text.replace('-',' ')
    text=text.replace('\n','')
    text=text.rstrip(" ")
    message_list=text.split(' ')
    decimal=[int(x,16) for x in message_list]
    return decimal

def sp_cd_extract(sp_code):
    sp_code=sp_code.replace('-',' ')
    sp_code=sp_code.rstrip(' ')
    code_lst=sp_code.split(' ')
    return code_lst
def unique_id(Unique_Id):
    uniq_id=str(Unique_Id)
    if(len(uniq_id)!=8):
        print("\t\t\t Invalid code, Please check again \n")
    else:
        safe_code,message=find_message(uniq_id)
        if safe_code!=0 and message!=0:
            message_decimal=encrepting_message(message)
            sp_code_lst=sp_cd_extract(safe_code)
            actual_decimal=[x - int(y) for x,y in zip(message_decimal,sp_code_lst)]
            string=''
            for i in actual_decimal:
                string=string+chr(i)
                
            return string
