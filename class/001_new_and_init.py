class A:
    def __init__(self):
        print('init:', id(self))

    def __new__(cls):
        print('new:', id(cls))
        r = super().__new__(cls)
        return r

    def __class__(self):
        print('class')

    def run(self):
        print('run')

obj1 = A()
obj1.run()
print(dir(A))