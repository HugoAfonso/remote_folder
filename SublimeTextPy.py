def is_isogram(string):
    #your code here
    check = []
    lowString = string.lower()
    for l in lowString:
        if l not in check:
            check.append(l)
#        if l not in check.keys():
#            check[l] = check.get(l,0)+1
    return len(check) == len(string)
#    return len(check.keys()) == len(string)

print(is_isogram('abba'))
print(is_isogram('alef'))
    