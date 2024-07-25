def tri(n):
    if n<=0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return tri(n-1)+(n-2)+(n-3)
num=int(input("enter the number"))
for i in range(num):
    print(tri(i))
