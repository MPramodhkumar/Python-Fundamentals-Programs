n=int(input())
res=0
for i in range(1,n):
    if (n%i==0):
        res=res+i
    
if (res==n):
    print("\nperfect number")
else:
    print("\nnot a perfect number")
