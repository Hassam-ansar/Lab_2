
# Task_1: While loop
# no:1:
count = 0 

while(count < 3):
    print("Hello Geek")
    count = count + 1

# no:2
i = 1
while(i<6):
    print(i)
    i+=1

#  Single stement while block.
# count = 0
# while (count <=1): print("Hello Geek")


# Task_2: for loop...

# Iterate over list
list = [1,2,3,4,5]
for i in list:
    print(i)

# Iterate over a tuple
tuple = (20, 30, 40, 50, 60)

for i in tuple:
    print(i)

#Iterate over a string
str = "This is a string"

for i in str:
    print(i)


# Iterating by index of sequence..
list_1 = [1, 4, "apple", "mango", 3.9]
for index in range(len(list_1)):
    print(index)


# Task_3:  Break and continue statement..
# Break statement: 'break' is uesd to come out of loop when encountered.
# it instructs the program to exist the loop now:

for i in range(0,100):
    if(i == 34):
        break   # Exit the loop right now  
    print(i)

# continue statement:is used to stop the current iteration of loop continue with the next one.
# it instructs the program to skip this iteration.
for i in range(0,100):
    if(i == 34):
        continue   # skip this iteration   
    print(i)


# Task_4 : Functions
# Function with arguments.
def goodboy(name, ending):
    print("Good Day,",name)
    print(ending)
    return "ok"

# goodboy("Hassam", "Thank you")
a = goodboy("Hassam", "Thank you")
print(a)


# Default argument :
def goodDay(name , ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)

goodDay("Hassam", "Thanks")
goodDay("Mani")
goodDay("Shabii..", "Aura")


# passing list as paremeters
def func_list(list_3):
    for i in list_3:
        print(i)

fruits = ["Apple", "Mango", "Leechi", "Banana"]
func_list(fruits)


# Task_5: OOP

#Example_1
class Myclass:
    a = 10

    def Hello(self):
        print(f"Hello Hassam.")


st1 = Myclass()
print("a = ",st1.a)
st1.Hello()

# Example_2
class student:
    
    roll_no = 27  # This is class attributes

    marks = 100


s1 = student()
s1.name = "Hassam"   # This is an object(instant) attribute
print("Name =",s1.name , ", Roll no =",s1.roll_no , ", Marks =",s1.marks)

s2 = student()
s2.name = "Mani"   # This is a object attribute
print("Name =",s2.name , " ,Roll no =",s2.roll_no , ", Marks =",s2.marks)

# Example_3
class Employee:
    language = "Python"   #This is a class attributes 

    salary = 1200000

    # constructor:
    def __init__(self, Name, Salary, Language):    # Dunder method which is automatically called
        self.name = Name
        self.salary = Salary
        self.language = Language
        print("I am creating an object")
        
    def getinfo(self):
        print(f"The language is {self.language}. The salay is {self.salary}")
    
    @staticmethod
    def hay():
        print("Good morning")

hassam = Employee("Hassam", 1300000, "Javascript")

# hassam.name = "Hassam"

print(hassam.name, hassam.salary, hassam.language)