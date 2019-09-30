# vending machine - computer program
# show whats available for purchase
# display prices
# receive input from the user revolving around which item they want
# money transactions (payment and change)
# what items are depleted


print("")
print("Please Make Your Selection" )
print("")
print("1. Chips")
print("2. Water")
print("3. Candy")
print("4. Chocolate Bar")
print("5. Pop")
print(" ")
print("Choose one of the options above")


request = int(input("What Would you Like to Eat?"" \n"))

if request == 1:
    print("Chips cost $2.50")

    request = int(input("Please Enter You Money Below"" \n"))

    if request < 2.50:
    	print("You Need More Money")
    else:
    	print("Thanks for Your Purchase!")
elif request == 2:
    print ("Water costs $1.00")

     request = int(input("Please Enter You Money Below"" \n"))

    if request < 1:
    	print("You Need More Money")
    else:
    	print("Thanks for Your Purchase!")
elif request == 3:
    print ("Candy costs $2.00")

      perequest = int(input("Please Enter You Money Below"" \n"))

    if request < 2:
    	print("You Need More Money")
    else:
    	print("Thanks for Your Purchase!")
elif request == 4:
    print ("Chocolate costs $3.00")

      request = int(input("Please Enter You Money Below"" \n"))

    if request < 3:
    	print("You Need More Money")
    else:
    	print("Thanks for Your Purchase!")

elif request == 4:
    print ("Pop costs $3.00")
    
      request = int(input("Please Enter You Money Below"" \n"))

    if request < 3:
    	print("You Need More Money")
    else:
    	print("Thanks for Your Purchase!")
