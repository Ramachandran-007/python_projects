n=int(input())
for row in range (1,n+1):
    for i in range (1,row+1):
        print('*',end=' ')
    print()
    for j in range (n-row+1):
        print('*',end=' ')
    print()
 
