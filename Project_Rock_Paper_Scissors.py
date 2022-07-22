import random


print('''$$\   $$\ $$$$$$$$\ $$\       $$\       $$$$$$\    
$$ |  $$ |$$  _____|$$ |      $$ |     $$  __$$\   
$$ |  $$ |$$ |      $$ |      $$ |     $$ /  $$ |  
$$$$$$$$ |$$$$$\    $$ |      $$ |     $$ |  $$ |  
$$  __$$ |$$  __|   $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$ |      $$ |      $$ |     $$ |  $$ |  
$$ |  $$ |$$$$$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |  
\__|  \__|\________|\________|\________|\______/''')

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''
image = [rock,paper,scissors]
chooseNum = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n "))
computerNum = random.randint(0,2)
print(f"Computer Choose {computerNum}")
if(chooseNum>2):
    print("Invalid Input")
else:
    print("Your Choice")
    print(image[chooseNum])
    print("\n")
    print("Computer Choice")
    print(image[computerNum])
    if(chooseNum == 0 and computerNum == 2):
        print("You win!!!")
    elif(chooseNum == 2 and computerNum==0):
        print("You Lose!!!")
    elif(chooseNum > computerNum):
        print("You win!!!!")
    elif(chooseNum == computerNum):
        print("Draw!!!!!!")
