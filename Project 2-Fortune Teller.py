import random

answer = 'y'

print("Welcome to the Fortune Teller")
print("You will select color and a number and I will tell you what the future holds for you")

while answer == 'y':

    color = input("Select a Colour [yellow,green,blue,red] ")
    if color == "yellow" or color == "green":
        number = int(input("Select a number [1,2,5,6]:- "))
        if number == 1:
            print("worried about your future career?, Don't worry. You'll 100% get what you want, be patient")
        elif number == 2:
            print("You will become a millonaire at the age of 35")
        elif number == 5:
            print("You will have a great family with 4 Kids")
        elif number == 6:
            print("You will become a famous and everyone love you ")
        else:
            print("Number 1,2,5,6 are the only number allowed")

    elif color == "blue" or  color == "red":
        number = int(input("Select a number [3,4,7,8]:- "))
        if number == 3:
            print("You will Leave a Happy Life")
        if number == 4:
            print("Ypu will become a sucessful doctor one day")
        if number == 7:
            print("All your dream will true, Just Patient")
        if number == 8:
            print("You're lucky, You will have all it one day ")
        else:
            print("Number 3,4,7,8 are the only number allowed")
       
    else:
        print("Colors [Yellow, green, red, blue] are only allowed")

    answer = input("Play again? insert 'y' for Yes and 'n' for No :-")