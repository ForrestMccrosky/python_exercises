## This exercise is going to working with python operators, booleans, variables, and many types of strings

## going to print the results of x plus y
x = 3 
y = 4
print(x+y)

## going to return the boolean value false because x does not equal y
print(x == y)

## going to return the boolean value true because x does not equal y
print(x != y)


## Problem 1
## You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
## and Hercules (1 day, you don't know yet if they're going to like it). 
## If price for a movie per day is 3 dollars, how much will you have to pay?

# little mermaid days rented
lm = 3
# brotherbear days rented
bb = 5
# hercules time rented
H = 1
# price per day
price = 3
print("-------------------------------------------------------------")

print("Problem 1")
print("The price for all the movie rentals is ") 
print((lm * price) + (bb * price) + (H * price))


## Problem 2
## Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a 
# different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

# variables for each companies pay
gp = 400
ap = 380
fbp = 350
# variables for each companies time worked by contractor
fbt = 10
gt = 6
at = 4
print("-------------------------------------------------------------")
print("Problem 2")
print("The amount you were payed as a contractor this week is:")
print((gp * gt) + (ap * at) + (fbp * fbt))
## Problem 3
## A student can be enrolled to a class only if the class is not full and the class 
# schedule does not conflict with her current schedule.

classfull = 'no'
scheduleclear = 'yes'
print("-------------------------------------------------------------")

print("Problem 3")
print("Can I enroll if the class is not full and my schedule is clear")
print(classfull == 'no' and scheduleclear == 'yes')
print("Can I enroll if the class is not full but my schedule has a conflict")
print(classfull == 'no ' and scheduleclear == 'no')
print("Can I enroll if the class is full and my schedule is conflicted")
print(classfull == 'yes' and scheduleclear == 'no')

print("-------------------------------------------------------------")
## Problem 4
## A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.
print("Problem 4")

## asking for inputs 
print("How many items did you buy:")
quantity = input()
print("Is the offer expired? (Please answer in lowercase 'yes' or 'no')")
offer = input()
print("Are you a premium member (Please answer in lowercase 'yes or 'no')")
member = input()

## creating an if else statement usinng boolean operands and >= to determine if the user's input
## matches the credentials to qualify for an offer
if (int(quantity) >= 2 or member == 'yes')  and offer == 'no': 
    print("Congratulations you qualify for this offer")
else:
    print("I'm sorry you don't qualify for any offers at this time")

print("-------------------------------------------------------------")
## Problem 5
## Use the code below to complete your python problem using a username and password with 
# certain parameters
username = 'codeup'
password = 'notastrongpassword'

if len(username) >= 5:
    passlength = True 
    print("Your Username length is good")
else:
    print("Username requires 5 or more characters")

if len(password) < 21:
    userlength = True 
    print("You password length is good")
else:
    print("Please create a stronger password")

if username != password:
    passcheck = True
    print("You are all set up please check your email for a confirmation code")
else:
    print("Please choose a password not similar to your username")


    


