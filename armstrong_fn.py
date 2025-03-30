def digitcount(n):
    c=0
    while n>0:
       c=c+1 
       n=n//10
    return c

def isArmstrong(n):
    s=0
    m=n
    d=digitcount(n)
    while n>0:
        r=n%10
        s=s+(r**d)
        n=n//10
    if m==s:
        return True
    else:
        return False
num=[]
n=int(input("Enter size of list: "))
for i in range(0,n):
    x=int(input("Enter value"))
    num.append(x)
print("Armstrong Numbers are:\n")
for i in range(0,n):
    if isArmstrong(num[i]):
        print(num[i],end=",")
