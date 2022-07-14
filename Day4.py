""""# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

# Write the rest of your code below this line 👇
toss = random.randint(0, 1)
if (toss == 1):
    print("Heads")
elif (toss == 0):
    print("Tails")
"""


# import moduleS
# print(moduleS.pi)


"""

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
length = len(names)
choice_list = random.randint(0,length-1)
print(f"{names[choice_list]} is going to buy the meal today!")


"""