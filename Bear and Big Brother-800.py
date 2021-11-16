s=input()
lim,bob=[int(x) for x in s.split()]
c=0
while lim<=bob:
    bob=bob*2
    lim=lim*3
    c+=1
print(c)
