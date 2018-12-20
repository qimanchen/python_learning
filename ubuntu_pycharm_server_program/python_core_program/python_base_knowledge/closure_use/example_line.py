def line_argument(a, b):

    def line(x):
        return a*x + b
    return line

line1 = line_argument(2,3)
print("---line1---: ", line1(3))
line2 = line_argument(3,4)
print("---line2---: ", line2(2))
