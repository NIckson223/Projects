from collections import UserDict
from datetime import datetime,date


class Field():
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return self.value
   
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)

    def valid_phone(self,phone):
        new_phone = str(phone).strip().replace("+", "").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        try:
            new_phone = [str(int(i)) for i in new_phone]
        except ValueError:
            print("Phone number is wrong!")

        else:
            new_phone=''.join(new_phone)
            if len(new_phone)==12:
                return f'+{new_phone}'
            elif len(new_phone):
                return f'+38{new_phone}'
            else:
                return f"Wrong lenght of number"

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_phone):
        if self.valid_phone(new_phone):
            self.__value = self.valid_phone(new_phone)


class AddresBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value]=record

    def del_record(self,record):
        self.data.pop(record.name.value, None)

    def show_records(self):
        return self.data
    
    def iterator(self, n=1):
        rec = list(self.data.keys())
        rec_num = len(rec)
        if n > rec_num:
            n = rec_num
        for i in range(0, rec_num, n):
            yield [self.data[rec[i+j]].show_contact() for j in range(n) if i + j < rec_num]
    


class Record():
    def __init__(self,name,phone=None,birthday=None):
        self.name = name
        self.phones=[]
        if phone:
            self.phones.append(phone)
        if isinstance(birthday,Birthday):
            self.birthday = birthday
        else:
            self.birthday = None
    def __str__(self):
        return str([i.value for i in self.phones])
    def __repr__(self):
        return str([i.value for i in self.phones])


    def delete_phones(self):
        self.phones=[]

    def add_phone(self,phone):
        self.phones.append(phone)

    def add_birthday(self, birthday):
        if isinstance(birthday,Birthday):
            self.birthday = birthday
        else:
            self.birthday = None

    def change_phone(self, phone):
        self.delete_phones()
        self.phones.append(phone)

    def show_contact(self):
        return {"name": self.name.value,
                "phone": [phone.value for phone in self.phones] if self.phones else [],
                "birthday": self.birthday.value if self.birthday else self.birthday}

    def days_to_birthday(self):
        birthday = datetime(year=int(datetime.now().year),month=int(self.birthday.value[3:5]), day=int(self.birthday.value[:2])).date()
        time_now = datetime.now().date()
        delta = birthday - time_now
        if int(delta.days) >= 0:
            return f"{delta.days} left to the birthaday"
        else:
            birthday = datetime(year=int(datetime.now().year)+1,month=int(self.birthday.value[3:5]), day=int(self.birthday.value[:2])).date()
            delta = birthday - time_now
            return f"{delta.days} left to the birthaday"

    



class Birthday(Field):

    def __init__(self, birthday):
        self.__value = None
        self.value = birthday

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_birthday):
        if self.check_birthday(new_birthday):
            self.__value = self.check_birthday(new_birthday)

    def check_birthday(self, birthday):
        try:
            year = int(birthday[6:])
            month = int(birthday[3:5])
            day = int(birthday[:2])
        except ValueError:
            print(f"EROR: Try - dd.mm.yyyy, only numbers")
        else:
            return birthday







if __name__=='__main__':
    name = Name("Bill")
    phone = Phone("380-504324231")
    rec = Record(name, phone)
    rec.add_birthday("20.05.2002")
    ab = AddresBook()
    ab.add_record(rec)
    name1 = Name("Nick")
    phone1 = Phone("21321313")
    rec1 = Record(name1, phone1)
    ab.add_record(rec1)
    name2 = Name("Taras")
    phone2 = Phone("0909090909")
    rec2 = Record(name2, phone2)
    ab.add_record(rec2)
    name3 = Name("Kolya")
    phone3 = Phone("1144411221")
    birthday3 = Birthday("01.02.2001")
    print(birthday3)
    rec3 = Record(name3, phone3, birthday3)
    print(rec3.birthday.value)
    print(rec3.days_to_birthday())
    ab.add_record(rec3)
    print(ab.show_records())
    a = ab.iterator(3)
    print(next(a))
    print(next(a))