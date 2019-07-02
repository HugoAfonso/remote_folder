def array_diff(a, b):
    abba = []
    #your code here
    for i in a:
        if i not in b:
            abba.append(i)
    return abba


a = [1,2,2,2]
b = [2]

print(array_diff(a,b))