def chk_all_up():
    s=input()
    for i in range(0,len(s)):
        if not ('A'<=s[i]<='Z'):
            return False
    return True
print(chk_all_up())
