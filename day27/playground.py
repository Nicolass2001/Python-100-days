def add(*args):
    res = 0
    for i in args:
        res += i
    return res

print(add(1,2,3,4,5,6))