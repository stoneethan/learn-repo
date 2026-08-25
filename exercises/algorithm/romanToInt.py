def romanToInt(s:str):
    map={
        "I":"1","V":"5","X":"10","L":"50","C":"100","D":"500","M":"1000"    }

    pre=0
    total=0

    for char in reversed(s):
        cur=int(map[char])
        if pre<=cur:
            total+=cur
        else:
            total-=cur
        pre=cur
        

    return total


romanToInt("III")



