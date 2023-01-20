
contacts={
    'Nick': '380661090741',
}


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
    
    return wrap

@input_eror
def add(arg):
    contacts[arg.split()[1]]=arg.split()[2]
    return f'Contact {arg.split()[1]} has been added with number {arg.split()[2]} '


@input_eror
def change(arg):
    try:
        number=contacts.get(arg[1])
        print(f'Number: {number}\n')
        print('Write a new number to change exist:\n')
        new_number=input()
        contacts[arg[1]]=new_number
        print(f'\nNumber sucsessful changed to: {new_number}')
    except:
        print("Not exist contact")
    

@input_eror
def showphone(arg):
    print(f'{"*"*8:*^70}\n')
    if contacts.get(arg[1]):
        number=contacts.get(arg[1])
        print(f"Name: {arg[1]}")
        print(f'Number: {number}')
    else:
        print('Not exist contact')
    print(f'{"*"*8:*^70}\n')
    
@input_eror
def showcontacts():
    print(f'{"*"*8:*^70}\n')
    print('All contacts:\n')
    for k,v in contacts.items():
        print(f"Name: {k}")
        print(f'Number: {v}\n')

@input_eror
def hello():
    info()
    

def bye():
    print('Bye Bye!')


commands={
    'hello':hello,
    'add':add,
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
    main()