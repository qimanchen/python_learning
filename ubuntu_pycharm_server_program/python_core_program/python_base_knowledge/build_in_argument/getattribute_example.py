class Itcast(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'

    # attribute is called which log some info
    def __getattribute__(self,obj):
        if obj == 'subject1':
            print('log subject1')
            return 'redirct python'
        else:
            return object.__getattribute__(self,obj)

    def show(self):
        print('this is Itcast')

# creat a instance
s = Itcast("python")
print(s.subject1)
print(s.subject2)

"""
Attention:
    Don't use self.xxx in __getattribute__ function
"""
