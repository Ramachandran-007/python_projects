'''n=int(input())
for row in range (1,n):
    for star in range (1,row+1):
        print('*',end=' ')
    print()
for row in range (n):
    for star in range(n-row):
        print('*',end=' ')
    print()
'''
n=int(input()) #3
for row in range(1,n+1):#1,2,3
    for col in range (1,row+1):#1 #1,2 #1,2,3
        if row==col or col==1 :
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()
