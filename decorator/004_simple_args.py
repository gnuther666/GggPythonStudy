

def dec1(f):
    def runit(*args, **kwargs):
        print('dec start')
        f(*args, **kwargs)
        print('dec end')
    return runit

@dec1
def func1(p, m):
    print('in func1- %s -%s' % (p, m))

func1('111', '222')