def add(a,b):
    if a==0:
        return b
    return add((a&b)<<1,a^b)

def Minus(a,b):
    subtractor = add(~b,1)
    return add(a,subtractor)

if __name__ == '__main__':
    print(Minus(2,4))
