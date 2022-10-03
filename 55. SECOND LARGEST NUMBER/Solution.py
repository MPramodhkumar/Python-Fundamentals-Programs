#python
#python
n=int(input())

list1=[]

for i in range(n):
    data=int(input())
    list1.append(data)
list1.sort()
print(list1[-2])
