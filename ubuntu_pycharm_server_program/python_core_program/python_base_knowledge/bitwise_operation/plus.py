def add(a, b):
    if a==0:
        return b
    return add((a&b)<<1, a^b)

if __name__ == '__main__':
    # test add function
    print(add(2,3))
