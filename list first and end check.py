def chk_first_last_equal(i):
    return i[0] == i[-1]
l=eval(input('Enter the list : '))
result = chk_first_last_equal(l)
print(result)
