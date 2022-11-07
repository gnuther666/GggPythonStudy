def dec1(f):
    def runit(*args, **kwargs):
        print('dec start')
        f(*args, **kwargs)
        print('dec end')
    return runit

class test_dec:
    def __init__(self):
        pass

    @dec1
    def run(self):
        print('888')

obj = test_dec()
obj.run()