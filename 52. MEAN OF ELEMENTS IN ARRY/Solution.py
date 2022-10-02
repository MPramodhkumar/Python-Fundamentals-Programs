#python
n=int(input())
list=[]
for i in range(n):
    data=int(input())
    list.append(data)
sum=0
for i in list:
    sum=sum+i
res=sum/n
print(res)
