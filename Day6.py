#function

'''
#The Hurdles Loop Challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()


for x in range(0,6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

'''

'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def jump():
 turn_left()
 move()
 turn_right()
 move()
 turn_right()
 move()
 turn_left()
    

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
        



'''


'''



def turn_right():
   turn_left()
   turn_left()
   turn_left()

def jump():
    turn_left()
    while wall_on_right():
     move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
      move()
    turn_left()



while not at_goal():
       if wall_in_front():
            jump()
       else:
        move()



'''