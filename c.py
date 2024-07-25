def fibi(n):
    if n<0:
        return 0
    elif n==0 or n==1 or n==2:
        return 1
    else:
        return fibi(n-2)+fibi(n-3)
num=int(input("enter the number"))
for i in range(num):
    print(fibi(i))    