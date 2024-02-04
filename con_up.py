def con_up():
    s=input()
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=i.swapcase()
        else:
            out+=i
    return out
print(con_up())
