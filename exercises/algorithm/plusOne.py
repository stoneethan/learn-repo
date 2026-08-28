

def plusone(digit:list )->list:
    for i in range(len(digit)-1,-1,-1):
        if digit[i]<9:
            digit[i]+=1
            return digit
        digit[i]=0
    return [1]+digit

print(plusone([1,9,9,9]))