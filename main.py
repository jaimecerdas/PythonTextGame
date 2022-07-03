#Videotutorial https://www.youtube.com/watch?v=_ZqAVck-WeM&ab_channel=freeCodeCamp.org


#Print statement
print ("Welcome to my first Python Text Game!")
# Variable
x = 5
# Print a variable
#print(x)
# User input
name = input("What is your name? ")
age = input("What is your age? ")

print ("Hello,",name,"you are",age,"years old.")

health = 10


#conditionals 

if int(age) >= 18:
    print("You are old enough!")
    # .lower() method converts strings to lowercase. .uper() works similarly.
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
        print ("You are starting with", health, "health")
        #this is the start of the game
        left_or_right = input ("First choise, do you want to go left or right? (left/right) ")
        if left_or_right == "left":
            ans = input ("Nice, you follow a path and reach a lake... Do you swim across or go around? (across/around) ")
            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across but were bit by a fish and lost 5 health...")
                health -= 5
            ans = input("You noticed a house and a river, where do you go? (river/house) ")
            if ans == "house":
                print("You go to the house and are greted by the owner, he doesn't like you and you lose 5 health")
                health -= 5
                if health <= 0:
                    print("You now have 0 health and you lost the game")
                else:
                    print("You survived and won the game!")
            else:
                    ("You fell in the river and lost")
        else:
            print("You fell down and lost")
    else:
        print("ok, whatever...")
elif int(age) ==17:
    print("Almost old enough but not yet!")
# You can add as many elif as you want.
else:
    print ("Not old enough to play")






'''
Comments:
#Can also comment like that.

Variables
Name has to follow rules: no special caracters 
and cannot start with a number. No spaces, use _.


Operators

x =+ y, is the same as x = x + y
x**y, x raised to the power of y
% mod operator, remainder of division.
// integer division, the whole number. 5/2, 2 is the integer division.

Comparaison operators
<
>
<= 
>=
==  Asking if X is equal to y, not assigning value.
!= NOT the same, not equal.

IF you compare different files, it will get false when comparing.
For strings capitalization is important.

OR one or the other
AND both

True or False -> tru


#jaicerpe 2022

'''