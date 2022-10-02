#python
str=str(input())
n=int(input())
if (str=="front"):
    if (n==1):
        print("Left Handed")
    elif (n==2):
        print("Right handed")
else:
    if (str=="rear"):
        if(n==2):
            print("Left Handed")
        elif (n==1):
            print("Right Handed")
