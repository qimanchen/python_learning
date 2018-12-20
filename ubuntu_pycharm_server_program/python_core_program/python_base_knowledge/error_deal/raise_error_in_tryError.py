class Test(object):
    def __init__(self, switch):
        self.switch = switch

    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("error check is open, and the error is :")
                print(result)
            else:
                raise

# test program
a = Test(True)
a.calc(11,0)

print("------------ line dividing line ------------")

a.switch = False
a.calc(11,0)

