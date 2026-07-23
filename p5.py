m1=int(input("Enter Your CC Marks:"))
m2=int(input("Enter your DAA Marks:"))
m3=int(input("Enter your APC Marks:"))
per=((m1+m2+m3)/300)*100

if per>90:
    print("Your marks is Excellent",per)
elif per>80:
    print("Your marks is Very Good",per)
elif per>70:
    print("Your marks is Good",per)
elif per>60:
    print("Your marks is Average:",per)
else:
    print("your Performance is Worst:",per)
