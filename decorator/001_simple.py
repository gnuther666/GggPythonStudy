

def dec1(f):
    def runit():
        print('dec start')
        f()
        print('dec end')
    return runit

@dec1
def func1():
    print('in func1')

func1()