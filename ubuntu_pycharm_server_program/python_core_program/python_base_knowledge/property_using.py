"""Tow way -- achieve property"""

class PropertyTest(object):

    def __init__(self, num):
        self.__num = num

    # get num values
    @property
    def num(self):
        return self.__num

    # achieve value set
    @num.setter
    def num(self, value):
        self.__num = value


class PropertyTest2(object):
    def __init__(self,num):
        self.__num = num

    def get_num(self):
        return self.__num

    def set_num(self,value):
        self.__num = value

    # set property
    num = property(get_num,set_num)


if __name__ == "__main__":
    # Test
    p = PropertyTest2(20)
    print("Initial value is %d..."%p.num)
    p.num = 100
    print("Modiry value to %d..."%p.num)
