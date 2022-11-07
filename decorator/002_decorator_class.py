class mydec():
    def __init__(self, fn):
        print('构造')
        self.fn = fn
    def __call__(self):
        print('执行')
        self.fn()

@mydec
def fun():
    print('func')
print(fun())