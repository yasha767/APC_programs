# 1. Abstract Shape Class

class Shape(ABC):
    @abstractmethod
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


circle = Circle(7)
rectangle = Rectangle(10, 5)
triangle = Triangle(10, 8)

print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())
print("Triangle Area:", triangle.area())


# 2. Abstract Vehicle Class

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class Bus(Vehicle):
    def start(self):
        print("Bus started")

    def stop(self):
        print("Bus stopped")


vehicles = [
    Car(),
    Bike(),
    Bus()
]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()


# 3. Abstract BankAccount Class

class BankAccount(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Savings Account Balance:", self.balance)


class CurrentAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Current Account Balance:", self.balance)


savings = SavingsAccount(10000)

savings.deposit(5000)
savings.withdraw(2000)
savings.display()

current = CurrentAccount(20000)

current.deposit(5000)
current.withdraw(3000)
current.display()


# 4. Abstract FoodOrder Class

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price + self.food_price * 0.05

    def delivery_charge(self):
        return 0

    def display(self):
        print("Restaurant Order Bill:", self.calculate_bill())
        print("Delivery Charge:", self.delivery_charge())


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price + self.food_price * 0.05

    def delivery_charge(self):
        return 50

    def display(self):
        print("Home Delivery Bill:", self.calculate_bill())
        print("Delivery Charge:", self.delivery_charge())
        print("Total Bill:", self.calculate_bill() + self.delivery_charge())


restaurant_order = RestaurantOrder(500)
restaurant_order.display()

home_order = HomeDeliveryOrder(500)
home_order.display()


# 5. Abstract Patient Class

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment with hospital admission")

    def display(self):
        self.treatment()
        print("Bill:", self.calculate_bill())


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("Out-patient consultation and treatment")

    def display(self):
        self.treatment()
        print("Bill:", self.calculate_bill())


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("Emergency treatment")

    def display(self):
        self.treatment()
        print("Bill:", self.calculate_bill())


in_patient = InPatient()
out_patient = OutPatient()
emergency_patient = EmergencyPatient()

in_patient.display()
out_patient.display()
emergency_patient.display()


# 6. Abstract Transport Class

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 15


distance = 100

transports = [
    Bus(),
    Train(),
    Taxi(),
    Flight()
]

for transport in transports:
    print("Fare:", transport.calculate_fare(distance))


# 7. Abstract Question Class

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self, answer):
        pass


class MCQQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            print("MCQ Answer: Correct")
        else:
            print("MCQ Answer: Incorrect")


class TrueFalseQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer == self.correct_answer:
            print("True/False Answer: Correct")
        else:
            print("True/False Answer: Incorrect")


class DescriptiveQuestion(Question):
    def __init__(self, correct_answer):
        self.correct_answer = correct_answer

    def evaluate_answer(self, answer):
        if answer.lower() == self.correct_answer.lower():
            print("Descriptive Answer: Correct")
        else:
            print("Descriptive Answer: Needs Evaluation")


mcq = MCQQuestion("A")
true_false = TrueFalseQuestion("True")
descriptive = DescriptiveQuestion("Python is a programming language")

mcq.evaluate_answer("A")
true_false.evaluate_answer("True")
descriptive.evaluate_answer("Python is a programming language")


# 8. Abstract Authentication Class

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


authentications = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for authentication in authentications:
    authentication.authenticate()


# 9. Abstract CloudStorage Class

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")


class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")


storage_services = [
    GoogleDrive(),
    Dropbox(),
    OneDrive()
]

for storage in storage_services:
    storage.upload_file()
    storage.download_file()
    storage.delete_file()


# 10. Abstract Appointment Class

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


appointments = [
    GeneralAppointment(),
    SpecialistAppointment(),
    EmergencyAppointment()
]

for appointment in appointments:
    appointment.book_appointment()
    print("Appointment Fee:", appointment.calculate_fee())

