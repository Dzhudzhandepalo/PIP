import random


class Employee() :
    def __init__(self , name , age ):
        self.name = name
        self.age = age
        self.unemployed = False


class QA(Employee):
    def __init__(self , name , age ):
        super().__init__(name , age)

qa1 = QA("Bob" , 28)
qa2 = QA("Tax" , 20)


class Developer(Employee):
    def __init__(self , name , age ):
        super().__init__(name , age)

dev1 = Developer("Joko" , 25)
dev2 = Developer("Barbara" , 23)



def random_quit(employees) :
    Employee = random.choice(employees)
    Employee.unemployed = True
    print(f"{Employee.name} was fired!")


employees = [qa1, qa2, dev1, dev2]
random_quit(employees)
