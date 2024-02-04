s1=input()
s2=input()
count=0
i=0
if len(s1)==len(s2):
    while i<len(s1):
        if s1[i]==s2[i]:
            count+=1
        i+=1
    print(count)
else:
    print('len not equal')
