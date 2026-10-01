# 1. Shape Polymorphism

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [
    Circle(7),
    Rectangle(10, 5),
    Triangle(10, 8)
]

for shape in shapes:
    print("Area:", shape.area())


# 2. Employee Salary Polymorphism

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 15000


class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 10000


class Tester(Employee):
    def calculate_salary(self):
        return 35000 + 7000


employees = [
    Manager(),
    Developer(),
    Tester()
]

for employee in employees:
    print("Salary:", employee.calculate_salary())


# 3. Vehicle Start Polymorphism

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with a diesel engine")


vehicles = [
    Car(),
    Bike(),
    Bus()
]

for vehicle in vehicles:
    vehicle.start()


# 4. Animal Sound Polymorphism

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog says Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow")


class Cow(Animal):
    def sound(self):
        print("Cow says Moo")


class Lion(Animal):
    def sound(self):
        print("Lion says Roar")


animals = [
    Dog(),
    Cat(),
    Cow(),
    Lion()
]

for animal in animals:
    animal.sound()


# 5. Notification Polymorphism

class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")


class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()


# 6. Student Grade Polymorphism

class Student:
    def calculate_grade(self):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self):
        marks = 85

        if marks >= 80:
            return "A"
        elif marks >= 60:
            return "B"
        else:
            return "C"


class MedicalStudent(Student):
    def calculate_grade(self):
        marks = 90

        if marks >= 85:
            return "A+"
        elif marks >= 70:
            return "A"
        else:
            return "B"


class ManagementStudent(Student):
    def calculate_grade(self):
        marks = 75

        if marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        else:
            return "C"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print("Grade:", student.calculate_grade())


# 7. Bank Account Interest Polymorphism

class BankAccount:
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self):
        balance = 100000
        rate = 7
        return balance * rate / 100


class CurrentAccount(BankAccount):
    def calculate_interest(self):
        balance = 100000
        rate = 4
        return balance * rate / 100


class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        balance = 100000
        rate = 8
        return balance * rate / 100


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest:", account.calculate_interest())


# 8. Report Polymorphism

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())


# 9. Distance Operator Overloading

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet

        total_feet = total_feet + total_inches // 12
        total_inches = total_inches % 12

        return Distance(total_feet, total_inches)

    def display(self):
        print("Distance:", self.feet, "feet", self.inches, "inches")


distance1 = Distance(5, 8)
distance2 = Distance(4, 7)

distance3 = distance1 + distance2

distance3.display()


# 10. Student Operator Overloading

class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks


student1 = Student("Yash", 450)
student2 = Student("Rahul", 420)

if student1 > student2:
    print(student1.name, "has higher marks")
elif student1 < student2:
    print(student2.name, "has higher marks")
else:
    print("Both students have equal marks")


# 11. Product Operator Overloading

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


product1 = Product("Laptop", 60000)
product2 = Product("Mobile", 40000)

if product1 == product2:
    print("Both products have the same price")
else:
    print("Products have different prices")

if product1 > product2:
    print(product1.name, "is more expensive")
else:
    print(product2.name, "is more expensive")


# 12. Online Shopping Payment Polymorphism

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI Payment:", amount)


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card Payment:", amount)


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet Payment:", amount)


def process_payment(payment, amount):
    payment.make_payment(amount)


process_payment(UPIPayment(), 1000)
process_payment(CardPayment(), 2000)
process_payment(WalletPayment(), 1500)


# 13. Person Role Polymorphism

class Person:
    def display_role(self):
        pass


class Student(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student(),
    Faculty(),
    Administrator()
]

for person in people:
    person.display_role()


# 14. Media Polymorphism

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing Audio")


class Video(Media):
    def play(self):
        print("Playing Video")


class Podcast(Media):
    def play(self):
        print("Playing Podcast")


media_list = [
    Audio(),
    Video(),
    Podcast()
]

for media in media_list:
    media.play()


# 15. SmartDevice Polymorphism

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light turned ON")

    def turn_off(self):
        print("Light turned OFF")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan turned ON")

    def turn_off(self):
        print("Fan turned OFF")


class AC(SmartDevice):
    def turn_on(self):
        print("AC turned ON")

    def turn_off(self):
        print("AC turned OFF")


class TV(SmartDevice):
    def turn_on(self):
        print("TV turned ON")

    def turn_off(self):
        print("TV turned OFF")


devices = [
    Light(),
    Fan(),
    AC(),
    TV()
]

for device in devices:
    device.turn_on()
    device.turn_off()

