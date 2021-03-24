array=[[0 for j in range(10)]for i in range (10)]
for i in range(10):
  array[i]=list(map(int,input().split()))
x,y=1,1
array[x][y]=9

while True:
  if array[x][y]==2:
    array[x][y]=9
    break
  if array[x][y+1]!=1:
    array[x][y]=9
    y+=1
  else:
    if array[x+1][y]!=1:
      array[x][y]=9
      x+=1
    else:
      array[x][y]=9
      break

for i in range(10):
  for j in range(10):
    print(array[i][j],end=' ')
  print()