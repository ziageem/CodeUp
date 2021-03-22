s=[]
count=0
s=input().split()
s[0],s[1],s[2]=int(s[0]),int(s[1]),int(s[2])
for i in range (s[0]):
    for j in range (s[1]):
       for k in range (s[2]):
           count+=1
           print(i,j,k)
print(count)