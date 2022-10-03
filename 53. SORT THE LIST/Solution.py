#python
n=int(input())

list1=[]

for i in range(n):
    data=int(input())
    list1.append(data)
n1=int(input())   
list2=[]
for i in range(n1):
    data=int(input())
    list2.append(data)
list1.sort()
list2.sort()
res=list1+list2
res.sort()
print("sorted list is: ",res)
