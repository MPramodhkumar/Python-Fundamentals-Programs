#python
n=int(input())

list1=[]

for i in range(n):
    data=int(input())
    list1.append(data)
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
