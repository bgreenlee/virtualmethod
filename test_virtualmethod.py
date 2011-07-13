import unittest
from virtualmethod import virtualmethod

class Base(object):
    @virtualmethod
    def my_virtual_method(self):
        print "Hi from my virtual method!"
        return True

class A(Base):
    pass

class B(Base):
    def my_virtual_method(self):
        print "Hey there, I overrode my virtual method!"
        return True

class VirtualMethodTest(unittest.TestCase):
    def setUp(self):
        self.base = Base()
        self.sub_a = A()
        self.sub_b = B()

    def test_virtualmethod(self):
        self.assertTrue(self.sub_a.my_virtual_method())
        self.assertTrue(self.sub_b.my_virtual_method())
        self.assertRaises(TypeError, self.base.my_virtual_method)

def main():
    unittest.main()


if __name__ == "__main__":
    main()