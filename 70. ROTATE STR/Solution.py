def rotate(s,d): 
    Lfirst = s[0 : d] 
    Lsecond = s[d :] 
    Rfirst = s[0 : len(s)-d] 
    Rsecond = s[len(s)-d : ] 
    
    print ((Rsecond + Rfirst)) 
  
string = input("")
d=int(input())
rotate(string,d) 
