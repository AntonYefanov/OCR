def compare(val1, val2 , val3):
    if val1 == val2:
        return val1
    elif val1 == val3:
        return val1
    elif val2 == val3:
        return val2
    else:
        return None


a = 1
b = 2
c = 3
print(a, b, c)
print(compare(a, b, c))


a = 1
b = 1
c = 3
print(a, b, c)
print(compare(a, b, c))

a = 1
b = 2
c = 2
print(a, b, c)
print(compare(a, b, c))

a = 5
b = 2
c = 5
print(a, b, c)
print(compare(a, b, c))

a = 6
b = 6
c = 6
print(a, b, c)
print(compare(a, b, c))