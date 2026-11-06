university = input("Enter the name of your university")
student_name = input("Enter your name")
matric_no =input("enter your matric number")
print()
print()
transport = float(input("how much do you spend on transport"))
feeding = float(input("how much do you spend on food"))
days_spent_on_campus = int(input("how many days have you spent in the university"))
other_expenses_of_the_week = int(input("other money spent"))
print()
print()
total_transport = transport*days_spent_on_campus
feeding_total = feeding*days_spent_on_campus
weekely_total = total_transport + feeding_total + other_expenses_of_the_week
print()
print()
print(f"your transport total is NGN {total_transport:,.2F}")
print(f" your feeding total is NGN {feeding_total:,.2F}")
print(f" your weekly total is  NGN {weekely_total:,.2F}")
print()
print()
budjet = float(input("Enter your weekely budjet"))
print()
print(f"your budjet is NGN {budjet:,.2f}")
print()
print()
if budjet < 0 or weekely_total < 0:
    print("Error : your budjet can not be negative!")
elif weekely_total == budjet:
    print("Exactly on budjet")
elif weekely_total >  budjet:
    print("Above budjet")
else:
    print("within budjet!")
print()
print()
difference = weekely_total - budjet
print ("difference")
if difference == 0:
    print("you were on budjet")
elif difference < 0:
    print (F"you were below your budjet by NGN {difference:,.2F}")
else:
    print (F"you exceded your budjet by NGN{difference:,.2F}")
    


