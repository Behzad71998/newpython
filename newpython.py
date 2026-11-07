class person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
   
    
    def printname(self):
        print(self.name)

    def printgender(self):
        print(self.gender)

    def printage(self):
        print(self.age)
            

class student(person):
    def __init__(self, name, gender, age, roll_num):
        super().__init__(name, gender, age)
        self.roll_num = roll_num
    def printroll_num(self):
        print(self.roll_num)

s = student("Ali","male",22,212)
print(s.printroll_num())
print(s.printname())
print(s.printgender)
print(s.printage)
print("hello")
