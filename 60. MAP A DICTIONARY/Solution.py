#python
n=int(input("Enter number of elements for dictionary:"))
L1=[]
L2=[]
print("For keys:")
for i in range(n):
    data=int(input())
    L1.append(data)
print("For values:")
for i in range(n):
    data=int(input())
    L2.append(data)
d=dict(zip(L1,L2))
print("The dictionary is:",d)
