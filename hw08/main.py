from datetime import datetime,date,timedelta

day_i ='0123456'
str_days=['Monday','Tuesday','Wendsday','Thursday','Friday','Saturnday','Sunday']
dict_days={}
for k,v in zip(day_i,str_days):
    dict_days[ord(k)]=v

print()



users=[
    {
    'name':'Nick',
    'birthday':datetime(year=2002, month=12,day=21).date()
    },
    {
    'name':'Sam',
    'birthday':datetime(year=2001, month=11,day=14).date()
    },
    {
    'name':'Andrew',
    'birthday':datetime(year=1997, month=11,day=8).date()

    },
    {
    'name':'Tina',
    'birthday':datetime(year=2001, month=11,day=14).date()
    },
    {
    'name':'Kate',
    'birthday':datetime(year=2001, month=11,day=9).date()
    },
    {
    'name':'Taras',
    'birthday':datetime(year=2001, month=11,day=6).date()
    },
    {
    'name':'Yaroslav',
    'birthday':datetime(year=2001, month=11,day=6).date()
    },
]

mn=[]
tues=[]
wedn=[]
thur=[]
fri=[]
sat=[]
sun=[]
days=[mn,tues,wedn,thur,fri,sat,sun]

def get_birthdays_per_week(users):
    global mn,tues,wedn,thur,fri,sat,sun
    
    
    current_date = datetime.today().date()

    for person in users:
        date_birthday=person.get('birthday')
        name_person=person.get('name')
        difference = current_date-date_birthday
        if current_date.month == date_birthday.month:
            difference =date_birthday.day-current_date.day
            if difference<7:
                if difference==0 or difference==-1 or difference==-2:
                    mn.append(name_person)
                elif difference==1:
                    tues.append(name_person)
                elif difference==2:
                    wedn.append(name_person)
                elif difference==3:
                    thur.append(name_person)
                elif difference==4:
                    fri.append(name_person)
                elif difference==5:
                    sat.append(name_person)
                elif difference==6:
                    sun.append(name_person)
                

def days_of_week(days):
    for d in range(7):
        if len(days[d])!=0:
            str_names=''
            for n in days[d]:
                str_names+=n + (''if n==(days[d][-1]) else ', ')
            print(str(d).translate(dict_days),':', str_names)

    
    
def main():
    get_birthdays_per_week(users)
    days_of_week(days)


main()