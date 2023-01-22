from cont_f import*
AB = AddresBook()


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
            if f.__name__ == "delete":
                return "Please type command in a proper way: delete Name "
            if f.__name__ == "showphone":
                return "Please type command in a proper way: phone Name"
            if f.__name__=="showcontacts":
                return "Please type command in a proper way"
    
    return wrap

@input_eror
def add(arg):
    name=arg.split()[1]
    phone=arg.split()[2]
    if name not in AB:
        name=Name(name)
        phone=Phone(phone)
        rec=Record(name,phone)
        AB.add_record(rec)
    else:
        rec=AB.get(name)
        rec.add_phone(phone)
    
    return f'Contact {arg.split()[1]} has been added with number {arg.split()[2]} '


@input_eror
def change(arg):
    name = arg.split()[1]
    phone = arg.split()[2]
    if name in AB:
        rec=AB.get(name)
        rec.change_phone(phone)
    else:
        return f"Please add {name} to phonebook firstly"
    return f"Contact {name} changed successfully"
    

@input_eror
def showphone(arg):
    print(f'{"*"*8:*^70}\n')
    if AB[arg.split()[1]]:
        phone=AB[arg.split()[1]]
        return f'{arg.split()[1]} phone: '+str(phone)
    else:
        return 'Not exst'

    
@input_eror
def showcontacts():
    print(AB.show_records())
    return  AB.show_records()

@input_eror
def hello():
    info()

@input_eror
def delete(arg):
    name = arg.split()[1]
    if name in AB:
        rec=AB.get(name)
        rec.delete_phones()
        AB.del_record(rec)
    else:
        return f"Please add {name} to phonebook firstly"
    return f"Contact {name} numbers deleted successfully"

def bye():
    print('Bye Bye!')


commands={
    'hello':hello,
    'add':add,
    'delete':delete,
    'change':change,
    'phone':showphone,
    'showall': showcontacts,
    'end_work':bye

}

def parser(command):
    if command.split()[0].lower()=='hello':
        return 'hello'
    elif command.split()[0].lower()=='add':
        return 'add'
    elif command.lower() in ["good bye", "close", "exit"]:
        return "end_work"
    elif command.split()[0].lower()=='change':
        return 'change'
    elif command.split()[0].lower()=='phone':
        return 'phone'
    elif command.split()[0].lower()=='showall':
        return 'showall'
    elif command.split()[0].lower()=='delete':
        return 'delete'

    else:
        return 'wrong command'


def main():
    print(f'{"*"*8:*^70}')
    print(f'Welcome in contact-book!\n')
    while True:
        info()
        user_input = input("Enter a command (q to quit): ")
        if user_input == "q":
            break
        
        command = parser(user_input)
        if command == 'hello':
            commands['hello']()
            input('\nClick Enter to resume....')
            break
        if command == 'end_work':
            commands['end_work']()
            input('\nClick Enter to resume....')
            break
        if command =='showall':
            commands['showall']()
            input('\nClick Enter to resume....')
            
            continue
        if command =='wrong command':
            print('Wrong command!')
            input('\nClick Enter to resume....')
            continue
        print(commands[command](user_input))
        input('\nClick Enter to resume....')


if __name__=='__main__':
    
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    AB.add_record(rec)

    assert isinstance(AB['Bill'], Record)
    assert isinstance(AB['Bill'].name, Name)
    assert isinstance(AB['Bill'].phones, list)
    assert isinstance(AB['Bill'].phones[0], Phone)
    assert AB['Bill'].phones[0].value == '1234567890'
    main()