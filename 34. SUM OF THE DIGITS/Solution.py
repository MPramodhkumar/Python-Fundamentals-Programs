#python
n=int(input())
res=0
while n>0:
    dig=n%10
    res=res+dig
    n=n//10
print(res)
