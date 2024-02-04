s=input()
out=[]
value=''
i=0
while i<=len(s)-1:
    if ord(s[i])+1==ord(s[i+1]):
        value+=s[i]
    else:
        value+=s[i]
        out.append(value)
        value=''
        i+=1
value+=s[i]
out.append(value)
print(out)
