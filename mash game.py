"""
Austin Krehbiel
9 August 2017

I am bored and the internet is down. Here is a program to entertain me.
I wanted to re-create the MASH game (mansion, apartment, shed, house).

I forgot how the game is played though so I'm trying to redo it from memory.


"""

from random import randint


print("Hello, welcome to M.A.S.H.!")
print("This game will determine the course of your life based on your answers.")
print("")





shelterArray = ["a mansion", "an apartment",
                "a shack", "a house"]

shelterChoice = randint(0,3)

#partner

partnerArray = []
loop = True
partnerCount = 0
while loop:
    partner = input("Enter the name of a person you would like to marry! Enter DONE when finished. ")
    if partner == "DONE":
        loop = False
    else:
        partnerArray.append(partner)
        partnerCount = partnerCount + 1

partnerChoice = randint(0, partnerCount-1)

#car
carArray = []
loop = True
carCount = 0
while loop:
    car = input("Enter the name of a vehicle you would like to drive! Enter DONE when finished. ")
    if car == "DONE":
        loop = False
    else:
        carArray.append(car)
        carCount = carCount + 1

carChoice = randint(0, carCount-1)
#number of children

numChildrenArray = []
loop = True
numChildrenCount = 0
while loop:
    numChildren = input("Enter the number of children you would like to have! Enter DONE when finished. ")
    if numChildren == "DONE":
        loop = False
    else:
        numChildrenArray.append(numChildren)
        numChildrenCount = numChildrenCount + 1

numChildrenChoice = randint(0, numChildrenCount-1)
#job

occupationArray = []
loop = True
occupationCount = 0
while loop:
    occupation = input("Enter the name of a career you'd like to have! Enter DONE when finished. ")
    if occupation == "DONE":
        loop = False
    else:
        occupationArray.append(occupation)
        occupationCount = occupationCount + 1

occupationChoice = randint(0, occupationCount-1)
#what city you'll live in

cityArray = []
loop = True
cityCount = 0
while loop:
    city = input("Enter the name of a city you would like to live in! Enter DONE when finished. ")
    if city == "DONE":
        loop = False
    else:
        cityArray.append(city)
        cityCount = cityCount + 1

cityChoice = randint(0, cityCount-1)
#what college you'll go to

collegeArray = []
loop = True
collegeCount = 0
while loop:
    college = input("Enter the name of a college you would like to go to! Enter DONE when finished. ")
    if college == "DONE":
        loop = False
    else:
        collegeArray.append(college)
        collegeCount = collegeCount + 1

collegeChoice = randint(0, collegeCount-1)
#what you'll major in

majorArray = []
loop = True
majorCount = 0
while loop:
    major = input("Enter the name of what you would like to study in college! Enter DONE when finished. ")
    if major == "DONE":
        loop = False
    else:
        majorArray.append(major)
        majorCount = majorCount + 1

majorChoice = randint(0, majorCount-1)
#how you'll die
"""
deathArray = []
loop = True
deathCount = 0
while loop:
    death = input("Enter the name of a way you might die! Enter DONE when finished. ")
    if death == "DONE":
        loop = False
    deathArray.append(death)
    deathCount = deathCount + 1

deathChoice = randint(1, deathCount+1)
"""
### RESULTS ###

print("")
print("You will marry " + partnerArray[partnerChoice] +"!")
print("You will drive a " + carArray[carChoice] +"!")
print("You will have " + numChildrenArray[numChildrenChoice] +" children!")
print("You will work as a " + occupationArray[occupationChoice] +"!")
print("You will live in " + cityArray[cityChoice] +"!")
print("You will get accepted by and attend " + collegeArray[collegeChoice] +"!")
print("You will study " + majorArray[majorChoice] +" at " + collegeArray[collegeChoice] + "!")
print("You will live in " + shelterArray[shelterChoice] + "!")

def shuffle():
    majorChoice = randint(0, majorCount-1)
    collegeChoice = randint(0, collegeCount-1)
    cityChoice = randint(0, cityCount-1)
    occupationChoice = randint(0, occupationCount-1)
    numChildrenChoice = randint(0, numChildrenCount-1)
    carChoice = randint(0, carCount-1)
    partnerChoice = randint(0, partnerCount-1)
    shelterChoice = randint(0,3)
    print("")
    print("You will marry " + partnerArray[partnerChoice] +"!")
    print("You will drive a " + carArray[carChoice] +"!")
    print("You will have " + numChildrenArray[numChildrenChoice] +" children!")
    print("You will work as a " + occupationArray[occupationChoice] +"!")
    print("You will live in " + cityArray[cityChoice] +"!")
    print("You will get accepted by and attend " + collegeArray[collegeChoice] +"!")
    print("You will study " + majorArray[majorChoice] +" at " + collegeArray[collegeChoice] + "!")
    print("You will live in " + shelterArray[shelterChoice] + "!")
    
loop = True
while loop:
    redo = input("Enter 'REDO' to get different answers!")
    if redo == "REDO":
        shuffle()
    else:
        loop = False
