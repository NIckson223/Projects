from collections import UserDict




class Field():
    def __init__(self,value) -> None:
        self.value = value
    def __str__(self):
        return self.value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    pass


class AddresBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value]=record

    def del_record(self,record):
        self.data.pop(record.name.value, None)

    def show_records(self):
        return self.data


class Record():
    def __init__(self,name,phone=None):
        self.name = name
        self.phones=[]
        if phone:
            self.phones.append(phone)

    def delete_phones(self):
        self.phones=[]
    def add_phone(self,phone):
        self.phones.append(phone)

    def change_phone(self, phone):
        self.delete_phones()
        self.phones.append(phone)

    def show_contacts(self):
        return f'Name: {self.name}\nPhone: {self.phones}'

    
        
    




