
num=input()
x=int(n)
a=input().split()
out=0
y=0
b=[]
c=[1,2,3]
for i in range(0,x):
    b.append(int(a[i]))
if(b==c):
  print("1")
else:
  for i in range(1,x):
      y=b[i]-b[0]
      out=out+y
  if(out>0):
      print(out)
  else:
      print("0")
