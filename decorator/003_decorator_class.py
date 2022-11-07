class mydec():
    def __init__(self, fn):
        print('构造')
        self.fn = fn

    def __call__(self, *argv, **kwargs):
        print('执行')
        self.fn(*argv, **kwargs)


@mydec
def fun(p, m):
    print('func-%s-%s' % (p, m))


print(fun('888', '999'))
