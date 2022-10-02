#python
s=str(input("enter the student type\n"))
s=s.lower()
if s=="msds":
    tf=float(input("enter tuition fee\n"))
    bf=float(input("enter bus fee\n"))
    total=tf+bf
    print("The fees to be paid by the student is Rs.%.2f"%total)
elif s=="msh":
    tf=float(input("enter tuition fee\n"))
    hf=float(input("enter hostel fee\n"))
    total=tf+hf
    print("The fees to be paid by the student is Rs.%.2f"%total)
elif s=="mgsds":
    tf=float(input("enter tuition fee\n"))
    bf=float(input("enter busfee fee\n"))
    total=float((150/100)*tf+bf)
    print("The fees to be paid by the student is Rs.%.2f"%total)
elif s=="mgsh":
    tf=float(input("enter tuition fee\n"))
    bf=float(input("enter hostel fee\n"))
    total=float((150/100)*tf+bf)
    print("The fees to be paid by the student is Rs.%.2f"%total)
