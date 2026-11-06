number=input("Enter number greater than 1 or type 'e' or 'exit' to stop: ")

while number !="e" and number!="exit":
        number=int(number)

        if number>1:
                for count in range(1,13):
                        multiply=number*count
                        print(f"{number} * {count} ={multiply}")
        else:
                print("The number is greater than 1")

        number=input("Enter another number or type 'e' to exit to end the code:")

        print("Program has ended")
