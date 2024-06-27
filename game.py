import random
computer_score = 0
user_score = 0
equal = 0
for i in range (100):
    x = random.randint(1,3)

    if x == 1 :
        computer_choice = "rock"
    elif x == 2 :
        computer_choice = "paper"
    elif x == 3 :
        computer_choice = "scissors"

        user_choice = input("enter your choice : ")

        if computer_choice == "rock" and user_choice == "paper":
            user_score += 1
        elif computer_choice == "paper" and user_choice == "rock":    
            computer_score +=1
        elif computer_choice and user_score == "rock":
            equal +=1
        elif computer_score and user_score == "paper":
            print ("0")
        elif computer_choice == "scissors" and user_choice == "paper":
            computer_score += 1
        elif computer_choice == "paper" and user_choice == "scissors":
            user_score +=1 
        elif computer_choice and user_choice == "scissors":
            equal +=1
        elif computer_choice == "rock" and user_choice == "scissors":
            computer_score +=1
        elif computer_choice == "scissors" and user_choice == "rock":
            user_score +=1
        print (user_choice)    
        print (computer_choice)
        print ("user_score" , user_score)     
        print ("computer_score" , computer_score)         


