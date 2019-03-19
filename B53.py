x=int(input("Enter a number:"))
tot=0
while(x>0):
    dig=x%10
    tot=tot+dig
    x=x//10
print("The total sum of digits is:",tot)
