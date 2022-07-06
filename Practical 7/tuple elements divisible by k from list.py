#author: aditya
#tuple elements divisible by k from list
li = (2,4,6,8,10)
n = 3
for i in li:
    if i%n:
        x=0
        break
    else:
        x=1
if x==0:
    print("Not divisible by ", n)
else:
    print("divisible by ", n)