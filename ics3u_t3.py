# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...

print("1. Weather.")
print("2. Classes")
print("3. Date")
print("4. Schedule")
print(" ")
print("Choose one of the options above")

request = int(input("What do you want to know about your day? \n"))

if request == 1:
    print("The weather in Toronto is currently 16 degrees celsius and cloudy.")
elif request == 2:
    print ("Today you have coding, chemistry, gym, and latin.")
elif request == 3:
    print ("Today is Monday September 16, 2019")
elif request == 4:
    print ("Today is a regular schedule.")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")
