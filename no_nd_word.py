l1=['ten','twenty','thirty']
l2=[10,20,30]
# store in dictionary like {'ten':10,'twenty':20,'thirty':30}

def no_word(l1,l2):
    out={}
    for i in range(len(l1)):  #0,1,2
        if l1[i] not in out:
            out[l1[i]]=l2[i]
    return out
print(no_word(l1,l2))
