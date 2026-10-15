#1
f = open("student.txt", "w")
f.write("1 Rahul\n Vahid\n Yash")
f.close()

r = input("Enter roll number: ")

f = open("student.txt", "r")
for line in f:
    if line.startswith(r + " "):
        print(line)
        break
else:
    print("Student not found")
f.close()


#2

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(self.name, self.roll)

s = Student(input("Name: "), input("Roll: "))

with open("college.txt", "a") as f:
    f.write(s.name + " " + s.roll + "\n")

s.display()
print("Recored saved successfully")
s.display()





       
