#python
str1=str(input())
count1=0
count2=0
for i in str1:
    if (i.isalpha()):
        count1=count1+1
    else:
        count2=count2+1
print("Characters =",count1)
print("Digits =",count2)
