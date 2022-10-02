#python
#python
n=int(input())
list=[]
list1=[]
list2=[]
for i in range(n):
    data=int(input())
    list.append(data)
for i in list:
    if ((i%2)==0):
        list1.append(i)
    else:
        list2.append(i)
print("The even list ",list1)
print("The odd list ",list2)
