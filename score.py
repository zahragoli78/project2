counter = 0 
avrage = 0
while True:
    score = input ("enter your score :")
    if score == "exit":
        break
    else:
        avrage += float (score )
        counter += 1
print (avrage / counter)        
        
