# 1 student dictionary and DataFrame
import pandas as pd

students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Python": [85, 78, 92, 70, 88],
    "DBMS": [80, 75, 89, 72, 90],
    "Mathematics": [90, 82, 85, 68, 87]
}

df = pd.DataFrame(students)

print("Student DataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]
df["Average"] = df["Total"] / 3

print("Total and Average:")
print(df)

print("Students with average greater than 75:")
print(df[df["Average"] > 75])


# 2 employee dictionary and DataFrame
employees = {
    "Employee_ID": [201, 202, 203, 204, 205],
    "Employee_Name": ["Raj", "Neha", "Amit", "Pooja", "Kiran"],
    "Department": ["CSE", "IT", "HR", "CSE", "Sales"],
    "Salary": [55000, 48000, 62000, 75000, 45000],
    "Experience": [5, 3, 8, 10, 2]
}

df = pd.DataFrame(employees)

print("\nEmployee DataFrame:")
print(df)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())

print("Employee with highest experience:")
print(df.loc[df["Experience"].idxmax()])


# 3 product dictionary and total sales
products = {
    "Product_ID": [301, 302, 303, 304, 305],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor", "Printer"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics"],
    "Price": [50000, 25000, 1500, 12000, 8000],
    "Quantity": [2, 5, 10, 4, 3]
}

df = pd.DataFrame(products)

df["Total_Amount"] = df["Price"] * df["Quantity"]

print("\nProduct DataFrame:")
print(df)

print("Product with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])


# 4 patient dictionary and medical charges
patients = {
    "Patient_ID": [401, 402, 403, 404, 405],
    "Patient_Name": ["Ramesh", "Suresh", "Anita", "Sunita", "Mahesh"],
    "Age": [65, 45, 72, 35, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 25000, 85000, 15000, 55000]
}

df = pd.DataFrame(patients)

print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

print("Average medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())

print("Patients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])


# 5 order dictionary and final amount
orders = {
    "Order_ID": [501, 502, 503, 504, 505],
    "Customer": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Product": ["Laptop", "Mobile", "TV", "Printer", "Tablet"],
    "Quantity": [1, 2, 1, 3, 2],
    "Price": [55000, 25000, 40000, 8000, 15000],
    "Discount": [2000, 1000, 3000, 500, 1000]
}

df = pd.DataFrame(orders)

df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]

print("\nAll Orders:")
print(df)

print("Orders above 5000:")
print(df[df["Final_Amount"] > 5000])

print("Highest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])

print("Average order value:", df["Final_Amount"].mean())


# 6 student attendance
attendance = {
    "Student_ID": [601, 602, 603, 604, 605],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas"],
    "Department": ["CSE", "IT", "CSE", "ECE", "IT"],
    "Total_Classes": [100, 100, 90, 80, 100],
    "Classes_Attended": [85, 70, 60, 75, 65]
}

df = pd.DataFrame(attendance)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("\nAttendance DataFrame:")
print(df)

print("Students with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


# 7 retail shop sales
sales = {
    "Product_ID": [701, 702, 703, 704, 705],
    "Product_Name": ["Laptop", "Mobile", "TV", "Printer", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics", "Office", "Electronics"],
    "Price": [50000, 25000, 45000, 7000, 18000],
    "Quantity": [2, 5, 1, 4, 3]
}

df = pd.DataFrame(sales)

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("\nSales DataFrame:")
print(df)

print("Products with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])

print("Product with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])

print("Average sales:", df["Total_Sales"].mean())


# 8 student marks Series
marks = pd.Series({
    "Amit": 85,
    "Priya": 92,
    "Rahul": 68,
    "Sneha": 78,
    "Vikas": 88
})

print("\nStudent Marks Series:")
print(marks)

print("Marks of Priya:", marks["Priya"])
print("Maximum marks:", marks.max())
print("Minimum marks:", marks.min())
print("Average marks:", marks.mean())

print("Students scoring more than 75:")
print(marks[marks > 75])


# 9 employee salary Series
salary = pd.Series({
    "Amit": 55000,
    "Priya": 48000,
    "Rahul": 65000,
    "Sneha": 75000,
    "Vikas": 45000
})

print("\nEmployee Salary Series:")
print(salary)

print("Highest salary:", salary.max())
print("Lowest salary:", salary.min())
print("Average salary:", salary.mean())

print("Employees earning more than 50000:")
print(salary[salary > 50000])


# 10 # product price Series
prices = pd.Series({
    "Laptop": 50000,
    "Mobile": 25000,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Mouse": 800
})

print("\nProduct Prices:")
print(prices)

prices = prices * 1.10

print("Prices after 10% increase:")
print(prices)

print("Most expensive product:")
print(prices.idxmax(), prices.max())

print("Products costing more than 1000:")
print(prices[prices > 1000])


# 11 patient age Series
ages = pd.Series({
    101: 65,
    102: 45,
    103: 72,
    104: 35,
    105: 68
})

print("\nPatient Ages:")
print(ages)

print("Average age:", ages.mean())
print("Oldest patient:", ages.idxmax(), ages.max())
print("Youngest patient:", ages.idxmin(), ages.min())

print("Patients above 60 years:")
print(ages[ages > 60])


# 12 student attendance Series
attendance = pd.Series({
    "Amit": 85,
    "Priya": 72,
    "Rahul": 95,
    "Sneha": 68,
    "Vikas": 92
})

print("\nStudent Attendance:")
print(attendance)

print("Average attendance:", attendance.mean())

print("Students below 75%:")
print(attendance[attendance < 75])

print("Students above 90%:")
print(attendance[attendance > 90])

print("Highest attendance:", attendance.max())

 
# 13. employees dataset

employees = pd.read_csv("employees.csv")

print("\n1. Employees from CSE department:")
print(employees[employees["Department"] == "CSE"])

print("\n2. Average Salary:")
print(employees["Salary"].mean())

print("\n3. Highest Salary:")
print(employees["Salary"].max())

print("Lowest Salary:")
print(employees["Salary"].min())

print("\n4. Employees having salary greater than ₹50,000:")
print(employees[employees["Salary"] > 50000])

print("\n5. Department-wise Average Salary:")
print(employees.groupby("Department")["Salary"].mean())


# 14. patients dataset

patients = pd.read_csv("patients.csv")

print("\n1. Patients above 60 years:")
print(patients[patients["Age"] > 60])

print("\n2. Average Medical Expense:")
print(patients["Medical_Expense"].mean())

highest_expense = patients["Medical_Expense"].max()

print("\n3. Highest Medical Expense:")
print(highest_expense)

print("Patient with highest medical expense:")
print(patients[patients["Medical_Expense"] == highest_expense])

print("\n4. Number of patients for each disease:")
print(patients["Disease"].value_counts())

print("\n5. Patients whose medical expense exceeds ₹50,000:")
print(patients[patients["Medical_Expense"] > 50000])


# 15. weather dataset

weather = pd.read_csv("weather.csv")

print("\n1. Maximum Temperature:")
print(weather["Temperature"].max())

print("\n2. Minimum Temperature:")
print(weather["Temperature"].min())

print("\n3. Average Temperature:")
print(weather["Temperature"].mean())

print("\n4. Records where temperature is above 35°C:")
print(weather[weather["Temperature"] > 35])

print("\n5. City-wise Average Temperature:")
print(weather.groupby("City")["Temperature"].mean())

 

