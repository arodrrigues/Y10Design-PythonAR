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

money1 = float(input("Please Enter You Money Below"" \n"))

if money1 < 2.50:
    print("You Need More Money")

else:
    print("Thanks for Your Purchase!")

elif request == 2:
	print ("Water costs $1.00")

money2 = float(input("Please Enter You Money Below"" \n"))

if money2 < 1:
    print("You Need More Money")

else:
    print("Thanks for Your Purchase!")

elif request == 3:
	print ("Candy costs $2.00")

money3 = float(input("Please Enter You Money Below"" \n"))

if money3 < 2:
    print("You Need More Money")

else:
    print("Thanks for Your Purchase!")

elif request == 4:
	print ("Chocolate costs $3.00")

money4 = float(input("Please Enter You Money Below"" \n"))

if money4 < 3:
    print("You Need More Money")

else:
    print("Thanks for Your Purchase!")

elif request == 5:
	print ("Pop costs $3.00")

money5 = float(input("Please Enter You Money Below"" \n"))

if money5 < 3:
    print("You Need More Money")

else:
    print("Thanks for Your Purchase!")
    
