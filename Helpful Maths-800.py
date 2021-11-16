s=input()
l=[]
for i in range (0,len(s)):
    if s[i]=='+':
        pass
    else:
        l.append(s[i])

for i in range (0,len(l)):
    print(l.sort()[i])
    
