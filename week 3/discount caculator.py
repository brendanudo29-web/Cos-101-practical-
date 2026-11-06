purchased_amount = float(input("Enter amount of goods puchased"))
if purchased_amount < 0:
    print("invalid purchase amount")
else:
  if purchased_amount < 10000:
    print (F"your discount is 5%")
    
  elif purchased_amount > 10000 < 50000:
    print(F"your discount is 10%")
    
  else:
    print(F"your discount is 10%")
