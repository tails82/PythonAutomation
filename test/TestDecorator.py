__author__ = 'Tails'

class TestDecorator:

    def wrapper1(self, func):
        def inner(*args, **kwargs):
            print "I'm running " + func.__name__
            return func(*args, **kwargs) * 2
        return inner

    def wrapper2(func):
        def inner(*args, **kwargs):
            print "I'm running " + func.__name__
            return func(*args, **kwargs) * 2
        return inner

    def add(self, x, y):
        return x + y

    @wrapper2
    def sub(self, x, y):
        return x - y

    """
    @wrap is equals to:
    add = wrapper(add)
    it overwrite the add function, whenever add is called, it' no longer the original add function.
    """

testDecorator = TestDecorator()
add = testDecorator.wrapper1(testDecorator.add)
print add(1, 2)
print testDecorator.sub(5, 1)