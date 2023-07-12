l1=int(input())
l2=int(input())
l3=int(input())
n=int(input())
l=[l1,l2,l3]
l.sort()

if(n<l[0]):
    result=l[0]
elif(n>l[0] and n>l[1]):
    result=l[2]
else:
    result=l[1]

if(result==l1):
    print("lab1")
elif(result==l2):
    print("lab2")
else:
    print("lab3")
