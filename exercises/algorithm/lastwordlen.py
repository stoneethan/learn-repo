def lenoflastword(s):
   
    length=0
    flag=True
    for pointer in reversed(s):
        if length==0 and pointer==" ":
            continue
        elif  pointer!=" ":
            length+=1
            flag=False
        else :
            if not flag and pointer==" ": 
                break
            pass
    return length

lenoflastword("sd awe")
        

