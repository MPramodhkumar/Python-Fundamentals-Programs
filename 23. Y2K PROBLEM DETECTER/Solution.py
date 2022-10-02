#python
b=int(input("Enter Year of Birth\n"))
c=int(input("Enter Current year\n"))
if c<b:
    b=100-b
    a=b+c
    print("Your age is ",a)
else:
    a=c-b
    print("Your age is ",a)
