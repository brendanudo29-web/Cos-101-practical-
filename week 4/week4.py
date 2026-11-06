first_number = float(input("Enter the first number"))
second_number = float(input("Enter the second number"))
if first_number <=0 :
     print(F"{first_number} is not allowed!")
elif second_number <=0 : 
     print(F"{second_number} is not allowed!")
else:
    quotient = first_number / second_number

    print(f"quotient: {quotient: .2f}")
