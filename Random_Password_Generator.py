import random
number_alphabets=int(input("Enter the number of character"))
number_num=int(input("Enter no of Numeric Value"))
number_symbol = int(input("Enter no of symbols"))
alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",'a'
    , 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=["0","1","2","3","4","5","6","7","8","9"]

symbol=["!","@","#","$","%","^","&","*"]
password=[]
password1 =[]
for x in range (1,number_alphabets+1):
    password.append(random.choice(alphabets))
for y in range (1,number_num+1):
    password.append(random.choice(alphabets))
for x in range (1,number_symbol+1):
    password += random.choice(symbol)
# print(password)
random.shuffle(password)
password2=""
# print(password)
for a in password:
    password2 += a
print(password2)