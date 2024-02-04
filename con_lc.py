def con_lc():
    s=input()
    out=''
    for i in s:
        if 'A' <= i <='Z':
            out+= i.swapcase()
        else:
            out+=i
    return out
print(con_lc())
