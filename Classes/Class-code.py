__author__='Akash'
import datetime
class Person:
    def __init__(self, name, birth, number, email):
        self.name=name #instance attribute
        self.birth=birth
        self.number=number
        self.email=email
    def age(self): #instance method
	# instance object accesible through self only
        today=datetime.date.today()
        age= today.year - self.birth.year
        if today < datetime.date(today.year, self.birth.month, self.birth.day):
            age -= 1
        return age

def ()main():
    per = Person(
        'Jae',
        datetime.date(1992, 10, 9),
        '7387793377',
        'akashals721@gmail.com'
    )
    print 'Code For Age::'
    print(per.name, per.birth, per.number, per.email)
    print 'Age is ',per.age()
#    print isinstance(per, Person)

if __name__=='__main__':
    main()
