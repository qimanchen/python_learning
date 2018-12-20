import pdb

def add_3_nums(a1,a2,a3):
    result = a1+a2+a3
    return result

def get_3_nums_avarage(s1,s2):
    s3 = s1 + s2 + s1
    result = 0
    result = add_3_nums(s1,s2,s3)/3

if __name__ == '__main__':
    a = 11
    b = 12
    final = get_3_nums_avarage(a,b)
    print(final)
