list=[15,30,23,76,99,100]
# output as [15,30,100]

def div_5 (list):
    out=[]
    for i in list:
        if i%5==0 :
            out.append(i)
    return out
print(div_5 (list))
            
