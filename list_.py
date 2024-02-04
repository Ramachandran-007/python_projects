l1=[10,20,25,30,35] #get odd no from this list
l2=[40,45,60,75,90] #get even no from this list

def even_odd_list(l1,l2):
    out=[]
    for i in l1:
        if i%2!=0 :
            out.append(i)
    for j in l2:
        if j%2==0 :
            out.append(j)
    return out
print(even_odd_list(l1,l2))

    
