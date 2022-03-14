a=int(input())
b=0
c=1
if a<=0:
    print(b)
else:
    print(b,c,end=" ")
    for d in range (2,a):
        next =b+c
        print(next, end = " ")
        b=c
        c=next