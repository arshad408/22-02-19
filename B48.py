n=int(input("Enter number of Elements:"))
a=[]
for i in range(0,n):
	el=int(input("Enter elements:"))
	a.append(el)
avg=sum(a)/n
print(avg)
