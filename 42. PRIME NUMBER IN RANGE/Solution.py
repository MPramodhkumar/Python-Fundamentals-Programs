#python
num=int(input())
num2=int(input())
for i in range(num,num2):
    if (i>1):
        for x in range(2,i):
            if (i%x)==0:
              break
        else:
            print(i)
            
