# caculate a bill of eletricity
customer_name = input("Enter the customer name")
energy_kwh = float(input("Enter energy consumed"))
if energy_kwh < 0:
    print ("invalid consumption. Energy can not be negative.")
else:
    if energy_kwh <= 50:
        bill = energy_kwh * 50

    elif energy_kwh <= 150:
        bill =(50 *50) + ((energy_kwh - 50) * 75)

    else:
            bill = (
                (50 * 50)
                +(100 * 75)
                +((energy_kwh - 150) * 100)
                )
    print()
    print("ELETRICITY BILL")
    print("===============")
    print(F"CUSTOMER: {customer_name}")
    print(F"ENERGY CONSUMED: {energy_kwh:,.2F}KWh")
    print(F"AMOUNT PAYABLE : NGN {bill:,.2f}")
        
        
        
