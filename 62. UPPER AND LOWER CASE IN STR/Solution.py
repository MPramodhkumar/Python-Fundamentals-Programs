#python
str1=str(input())
count1=0
count2=0
for i in str1:
    if (i==i.lower()):
        count1=count1+1
    else:
        count2=count2+1
print(count2)
print(count1)
