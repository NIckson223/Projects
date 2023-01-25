
from pathlib import Path
from ab_classes import*
import os

workdir = os.getcwd()

FILE_NAME = os.path.join(workdir,"ab.bin")
SERIALIZATION_PATH = Path(FILE_NAME)



def info():
    
    print(f'''
    Commands to use:\n\n
    {'add *name* *number*':<30} {"add new contact":->50}\n
    {'change *name*':<30} {'change contact number':->50}\n
    {'phone *name*':<30} {'show number':->50}\n
    {'showall':<30} {'show all numbers':->50}    
    ''')



def input_eror(f):
    def wrap(*arg,**kwarg):
        try:
            res=f(*arg,**kwarg)
            return res
        except:
            if f.__name__=='add':
                return()
            if f.__name__ == "change":
                return "Please type command in a proper way: change Name Phone"
            if f.__name__ == "showphone":
                return "Please type command in a proper way: phone Phone"
            if f.__name__=="showcontacts":
                return "Please type command in a proper way"
            if f.__name__ == "find":
                return "Please type command in a proper way: find Phone/Name"
    
    return wrap

@input_eror
def add(arg):
    name =Name(arg.split(' ')[1])
    phone =Phone(arg.split(' ')[2])
    if arg.split(' ')[3]:
        birthday=Birthday(arg.split(' ')[3])
    contact = Record(name,phone)
    ab.add_record(contact)
    return f'Contact added with\n Name:{name} Phone:{phone}'

@input_eror
def change(arg):
    try:
        ab[arg.split(' ')[1]].change_phone(arg.split(' ')[2])
    except:
        print("Not exist contact")
    
    
@input_eror
def showcontacts(*_):
    return ab.show_records()

@input_eror
def hello(*_):
    info()

@input_eror
def find(request):
    request = input('Write request:\n>>>')
    try:
        if request.isnumeric():
            print(ab.find_for_phone(request))
        else:
            print(ab.find_by_name(request))
    except:
        return f'{request} not found in Address book'
    

def bye(*_):
    print('Bye Bye!')


commands={
    'hello':hello,
    'add':add,
    'change':change,
    'find':find,
    'showall': showcontacts,
    'end_work':bye

}   




if __name__=='__main__':
    find =True
    ab = AddresBook()
    
    if SERIALIZATION_PATH.exists():
        ab.deserialize(FILE_NAME)
        
    while find:
        command = input('Write an command\n>>>  ')
        for k,v in commands.items():
            if  (command not in ['bye','good bye',"close", "exit",'q']):
                if command==k:
                    print(v(command))
                    print(f'{v}')
            else:
                bye(command)
                find=False
        
    ab.serialize(FILE_NAME)

    