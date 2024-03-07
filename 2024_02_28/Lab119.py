# Hybrid inheritance

class A:
    def methodA(self):
        return "A"


class B(A):
    def methodA(self):
        return "B"


class C(A):
    def methodA(self):
        return "A"


# Multiple inheritance


class D(B,C):
    def methodA(self):
        return "A"
