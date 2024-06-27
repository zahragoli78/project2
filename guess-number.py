import random
user_count = 0
computer_number = random.randint(10,40)
for i in range(10):
    user_number = int (input())
    
    if computer_number > user_number:
       print("go up")
       user_count +=1
       
    elif computer_number < user_number:
        print("go down")   
        user_count += 1
        
    elif computer_number == user_number:
        print("you win🎉")
        print ("user_count :" , user_count)
        break
        
    
