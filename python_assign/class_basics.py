class Test:
    a=10
    def __init__(self):
        self.x=5

    def fun1(self):
        self.i=10
        print(self.i)

    def fun2(self):
        self.a=15
        print(self.a,"CANNOT CHANGE")
        Test.a=50
        print(Test.a)
    @classmethod
    def fun3(cls):
        cls.a=12
        Test.y=30
        print(cls.a,Test.y)
    @staticmethod
    def f4():
        Test.e = 50

t1=Test()
print(t1.x)
print(t1.fun1())
print(t1.fun2())
print(Test.a)
