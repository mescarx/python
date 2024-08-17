class A:
    def feature1(self):
        print("Feature 1 is working")

class B(A):
    def feature2(self):
        print("Feature 2 is working")

class C(A):
    def feature3(self):
        print("Feature 3 is working")

class D(B, C):
    def feature4(self):
        print("Feature 4 is working")

d = D()
d.feature1()
d.feature2()
d.feature3()
d.feature4()
