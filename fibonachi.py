n0 = 0
n1 = 1
number= int (input ("enter your number :"))
for i in range(number):
    if number ==1:
        print (number)
        break
    else:
        n2 = n0 + n1
        n1 = n0
        n0 = n2
        print (n0)
     