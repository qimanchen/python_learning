def decorator(log_info):
    print("---start decorating---")
    def wraped(func):
        print("---wraped runing---")
        print(log_info)
        return func
    print("---end---")
    return wraped


@decorator("---print info---")
def test(a,b):
    print("---test running---")
    print("---arguments is a=%d,b=%d---"%(a,b))
    return "---test end---"

ret = test(10,20)
print("---return value is %s---" % ret)
print(test.__name__)

