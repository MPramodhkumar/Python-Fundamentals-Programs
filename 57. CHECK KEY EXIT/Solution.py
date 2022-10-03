#python
d={'A':1,'B':2,'C':3}
inp=input("Enter key to check :")
if inp in d.keys():
    print("Key is present and value of the key is:",d[inp])
else:
    print("Key isn't present!")
