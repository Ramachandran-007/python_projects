list1=[10,20,25,30,35]
list2=[40,45,60,75,90]
out=[]
for i in list1: #odd
    if i%2 != 0:
        out.append(i)
for j in list2: #even
    if j%2 == 0:
        out.append(j)
print(out)
        
    
