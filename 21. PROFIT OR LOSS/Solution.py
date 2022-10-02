#python
a=float(input())
b=float(input())
print("Enter the price of a dozen mangoes")
print("Enter the price at which 1 mango is being sold")
c=b*12
if a < c:
    p=c-a
    print("Profit : RS.%.2f"%p)
elif a > c:
    l= a-c
    print("Loss : RS.%.2f"%l)
else:
    print("No profit nor loss")
