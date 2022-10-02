#python
n=int(input())
fact=1
while (n>0):
    fact=fact*n
    n=n-1
res=dig=0
while (n>0):
    
   dig=n%10
   res=res+dig
   n=n//10
if (res==fact):
    print("Strong number")
else:
    print("Not a strong number")
