class Person:
    def __init__(self):
        print("Person.__init__ call")
        self.hello = '안녕하세요'

class Student(Person):
    def __init__(self):
        print('Student.__init__ call')
        super().__init__()
        self.school='학교'

james = Student()
print(james.school)
print(james.hello)