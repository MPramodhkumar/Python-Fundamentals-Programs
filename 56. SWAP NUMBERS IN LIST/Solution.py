#python
#python
n=int(input())

list1=[]

for i in range(n):
    data=int(input())
    list1.append(data)
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print(list1)
