registration_status = input("Registration complete? Enter yes or no: ")
if registration_status == "no":
    print("not eligible")
else:
    attendance = float(input("Enter attendance percentage: "))
 
    if attendance < 0 or attendance  > 100:
         print ("unrecogonized response")
    elif attendance < 75:
        print("Not eligible")
    else:
        print("eligible")
                         
