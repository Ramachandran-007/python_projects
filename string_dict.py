'''
s=input()
out={}
for i in s:
    if i not in out:
        out[i]=1
    else:
        out[i]+=1
print(out)
'''

s=input()
out={}
i=0
while i<len(s):
    if s[i] not in out:
        out[s[i]]=1
    else:
        out[s[i]]+=1
    i+=1
print(out)
