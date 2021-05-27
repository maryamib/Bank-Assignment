print("1. Access Bank - *901# ")
print("2. UBA - *919# ")
print("3. FCMB - *329# ")
print("4. Polaris - *833# ")
print("5. GTBank - *737# ")
print("6. Zenith - *966# ")
print("7. Eco Bank - *326# ")
print("8. First Bank - *894# ")
print("9. Stanbic IBTC Bank - *909# ")
print("10. Diamond Bank - *426# ")
print("11. Fidelity Bank - *770# ")
print("12. Sterling Bank - *822# ")
print("13. Unity Bank - *7799# ")
bank = int (input ("please enter your bank USSD code: "))
if  bank == 919 :
    print("You have entered the code for UBA mobile banking")
    print("1. Check your balance")
    print("2. Transfer")
    print("3. Airtime")
    print("4. Transaction History")
    a = int (input ("Please select an option: \n"))

    if a == 1:
        print("Your Account Balance is 33463 naira \n")
    elif a == 2:
        acc = int (input ("please enter account number: \n"))
        amm = int (input ("please enter Amount: \n"))
        pin = int (input ("please enter your pin: \n"))
        print("Do you want to send "+ str(amm) + " to "+ str(acc) + "  ? \n")
        print("1. YES")
        print("2. NO")
        yorno = int (input ("Enter 1 or 2 \n"))
        if yorno == 1:
            print("TRANSACTION SUCCESSFUL!!")
        else:
            print("TRANSACTION FAILED")
    elif a == 3:
        cacc = int (input ("please enter phone number: \n"))
        camm = int (input ("please enter Amount: \n"))
        cpin = int (input ("please enter your pin: \n"))
        print("Do you want to buy "+ str(camm) +" airtime to "+ str(cacc) + "  ?")
        print("1. YES")
        print("2. NO")
        yornoo = int (input ("Enter 1 or 2 \n"))
        if yornoo == 1:
            print("TRANSACTION SUCCESSFUL!!")
        else:
                    print("TRANSACTION FAILED")

    elif a == 4:
        print("A message would be sent to you shortly")

    else:
        print("Please enter a valid number")
else:
    print("please the bank code for UBA bank")
