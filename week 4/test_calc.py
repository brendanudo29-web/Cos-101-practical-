
number = int(input("Enter number above 1 or press 5 to exit"))
print(f"Multiplication table for {number}")
if number < 1:
        print("Number can be less than 1 or press 5 to exit !")
elif number  ==1:
    print("Number must be higher than 1!")
elif number  > 12:
    print("Number must be higher than 12!")
else:
    for count in range (1, 13):
       result = number * count 
       print(f"Result {number} * {count} = {result} ")

