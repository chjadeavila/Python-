#Inputting name using variable and print statement
name = input("What's your name? ")
print(f"Hello there, {name}!")
#Conditions 
#less than or greater than
n = int(input("Number: ")) #if you would do this again always remember that input doesnt care what you input, it's always string, 'cause what you told it to input is string, but if you want n to produce integer, you should always nest or put input inside int (integer)... arraseo?? so that when you use conditional statements or boolean that only alows int to int comparing, if you're condition is int... it is not supported by ">"... arrachi? 

#Using if, elif, else statement (Condition)
if n > 0:
  print("n is positive")
elif n < 0:
  print("n is negative")
else:
  print("n is 0")

#Asking for age of the user and telling them beautiful things base on their age
age = int(input("How old are you? "))
#Using Conditional Statements
if age > 13:
  print("Ohhh, so you're a teenager now, FIGHTING!")
elif age < 13:
  print("Oaaahhh!!, what a cutie, please don't grow older!! :( ")

#Another try, but concatenating string inside a print statement in conditional statement
gender = input("Gender: ")
age = int(input("Age: "))
#Conditions
if age > 13:
  print(f"oh, {gender}, you're a teenager now!")
elif age < 13:
  print(f"what a young {gender}! grow up and be a good{gender}")

#Another try for conditional statements
name = input("name: ")
gender = input("gender: ")
age = int(input("age: "))
#Conditional statements with if, elif, else 
if age < 18:
  print(f"{name}, you're teenage {gender} now, fighting!")
elif age <= 13:
  print(f"{name}, you're young to be true, {gender}!")
elif age >= 18:
  print(f"{name}, whatever it takes, grab the oppurtunities, and get that career, {gender}!!! HWAITING!!!")
else: 
  print("You still a baby!! hehe :)")

#something is wrong with the code conditional statement above
#I want to know that if the user is 18 below but not below 13, I, also, want to know if the user is 13 below, lastly, I want to know, the user is 18 above... so that the program knows what to say regarding the age of the user,,,, but how would I knoow:??

#I'll find out soon



  