# fruits = ["apple","banana","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)
# print("Hello")



"""
student_height = input("Input Student Height").split()
print(student_height)
count = 0
for n in range(0,len(student_height)):
    student_height[n] = int(student_height[n])

# for n in student_height:
sum = 0
for i in student_height:
    sum += i
    count = count + 1
avg = round(sum/count)
print(avg)

"""

"""
numbers = input("Enter the numbers").split()
for n in range(0,len(numbers)):
    numbers[n] = int(numbers[n])
max_value = 0
for x in numbers:
    if(x>max_value):
        max_value = x
print(max_value)

"""
# total = 0
# for i in range (1,101):
#     total += i
#
# print(total)
# total = 0
# for i in range (1,101):
#     if(i%2==0):
#       total += i

# print(total)
# total = 0
# for i in range (2,101,2):
#     total += i
#
# print(total)


for i in range (1,101):
    if(i % 3 ==0 and i%5 == 0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz .")
    elif(i%5==0):
        print("Buzz .")
    else:
     print(i)




