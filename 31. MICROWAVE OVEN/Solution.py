#python
n1=int(input("Enter the number of items\n"))
n2=float(input("Enter the single item heating time\n"))
if (n1==2):
    h=n1*n2
    h1=h+((50/100)*h)
    h2=h1/2
    print("The recommended heating time is %.2f"%h2)
elif (n1==3):
    h=n1*n2
    h1=h+((100/100)*h)
    h2=h1/2
    print("The recommended heating time is %.2f"%h2)
else:
    print("Number of items is more")
