a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
#a is greatest
if a>b and a>c and a>d and a>e:
    if b>c and b>d and b>e:
        print(f'{b} is 2nd greatest')
    elif c>d and c>e:
        print(f'{c} is 2nd greatest')
    elif d>e:
        print(f'{d} is 2nd greatest')
    else:
        print(f'{e} is 2nd greatest')

#b is greatest
elif b>c and b>d and b>e:
    if a>c and a>d and a>e:
        print(f'{a} is 2nd greatest')
    elif c>d and c>e:
        print(f'{c} is 2nd greatest')
    elif d>e:
        print(f'{d} is 2nd greatest')
    else:
        print(f'{e} is 2nd greatest')

#c is greatest
elif c>d and c>e:
    if a>b and a>d and a>e:
        print(f'{a} is 2nd greatest')
    elif b>d and b>e:
        print(f'{b} is 2nd greatest')
    elif d>e:
        print(f'{d} is 2nd greatest')
    else:
        print(f'{e} is 2nd greatest')

#d is greatest
elif d>e:
    if a>b and a>c and a>e:
        print(f'{a} is 2nd greatest')
    elif b>c and b>e:
        print(f'{b} is 2nd greatest')
    elif c>e:
        print(f'{c} is 2nd greatest')
    else:
        print(f'{e} is 2nd greatest')

#e is greatest
else:
    if a>b and a>c and a>d:
        print(f'{a} is 2nd greatest')
    elif b>c and b>d:
        print(f'{b} is 2nd greatest')
    elif c>d:
        print(f'{c} is 2nd greatest')
    else:
        print(f'{e} is 2nd greatest')
