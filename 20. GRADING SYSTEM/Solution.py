#python
m=int(input())
if m==100:
    print("S")
elif m in range(90,100):
    print("A")
elif m in range(80,91):
    print("B")
elif m in range(70,81):
    print("C")
elif m in range(60,71):
    print("D")
elif m in range(50,61):
    print("E")
elif m<50:
    print("F")
else:
    print("invalid input")
