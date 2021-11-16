n=int(input())
x=0
for i in range(0,n):
    inp=input()
    if inp=="++X" or inp=="X++":
        x+=1
    if inp=="--X" or inp=="X--":
        x-=1
print(x)
    
