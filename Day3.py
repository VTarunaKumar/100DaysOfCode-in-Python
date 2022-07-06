
"""
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result = round((weight) /(height*height))
if(result>0 and result<18.5):
    print(f"Your BMI is {result}, you are underweight.")
elif(result>18.5 and result<25):
    print(f"Your BMI is {result},you have a normal weight.")
elif(result>25 and result<30):
    print(f"Your BMI is {result},you are slightly overweight.")
elif(result>30 and result<35):
    print(f"Your BMI is {result},you are obese.")
else:
    print(f"Your BMI is {result},you are clinically obese.")
    """


""""
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
sPizza=15
mPizza=20
lPizza=25
if(add_pepperoni == "Y"):
    sPizza += 2
    mPizza += 3
    lPizza += 3
if(extra_cheese=="Y"):
    sPizza += 1
    mPizza += 1
    lPizza += 1

if(size == "L"):
    print(f"Your final bill is: ${lPizza}")
if(size == "S"):
    print(f"Your final bill is: ${sPizza}")
if(size == "M"):
    print(f"Your final bill is: ${mPizza}")
    
                                """


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

cost = 0

if(size == "S"):
    cost += 15
if(size == "L"):
    cost += 25
if(size == "M"):
    cost += 20

if(add_pepperoni == "Y"):
    if (size == "S"):
        cost += 2
    elif(size == "M" or size == "L"):
        cost += 3
if(extra_cheese == "Y"):
    cost += 1
print(f"Your final bill is: ${cost}")

