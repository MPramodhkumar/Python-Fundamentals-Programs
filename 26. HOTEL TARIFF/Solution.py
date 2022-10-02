#python
m=int(input())
r=float(input())
n=int(input())
if(m<12):
    if (m==4 or  m==6 or m==11 or m==12):
        t=r+((20/100)*r)
        a=t*n
        print("Hotel Tariff:Rs.%.2f"%a)
    else :
        t=r*n
        print("Hotel Tariff:Rs.%.2f"%t)
else:
    print("Invalid input")
