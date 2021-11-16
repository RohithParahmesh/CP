s=input()
n=len(s)
c=0
for i in range(0,n):
    for j in range(i+1,n):
        if s[i]==s[j]:
            c+=1
ans=n-c
if ans%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
    
