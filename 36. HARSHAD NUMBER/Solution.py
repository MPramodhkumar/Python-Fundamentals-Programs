num = int(input(" "))    
digit = sum = 0
temp = num   
     
# Calculates sum of digits    
while(temp > 0):    
    digit = temp % 10
    sum = sum + digit    
    temp = temp // 10    
     
# Checks whether the number is divisible by the sum of digits    
if num % sum == 0:    
    print("Harshad Number")    
else:    
    print("Not Harshad Number")
