class Test(object):
    def __init__(self,func):
        print("---Initial---")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self,*args,**kwargs):
        print("---function from decorator---")
        ret = self.__func(*args,**kwargs)
        return ret

@Test
def test(a,b):
    print("---test--- a=%d,b=%d"%(a,b))
    return "Test function return value"

print(test(10,29))
