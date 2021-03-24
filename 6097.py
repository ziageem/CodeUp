h,w=map(int,input().split())
array=[[0 for j in range(w)]for i in range (h)]
n=int(input())

for i in range(n):
  l,d,x,y=map(int,input().split())
  if d==0:
    for j in range(l):
      array[x-1][y+j-1]=1
  else:
    for j in range(l):
      array[x+j-1][y-1]=1

for i in range(h):
  for j in range(w):
    print(array[i][j],end=' ')
  print()