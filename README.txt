virtualmethod
=============

Decorator to prevent base class methods from being called directly.

Usage
-----

::

    from virtualmethod import virtualmethod

    class Base(object):
        @virtualmethod
        def my_virtual_method(self):
            print "This is a virtual method. Call me from a subclass!"

    class A(Base):
        pass

    class B(Base):
        def my_virtual_method(self):
            print "I went ahead and implemented my own version."

    base = Base()
    a = A()
    b = B()

    a.my_virtual_method()
    -> This is a virtual method. Call me from a subclass!

    b.my_virtual_method()
    -> I went ahead and implemented my own version.

    base.my_virtual_method()
    -> Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "virtualmethod/core.py", line 11, in __call__
        raise TypeError("Virtual method %s must be called from a subclass." % self.__name__)
    TypeError: Virtual method my_virtual_method must be called from a subclass.

Note(s)
-------

``@virtualmethod`` works with ``@classmethod`` and ``@staticmethod``,
but must be declared first, i.e.:

::

    @virtualmethod
    @classmethod
    def my_virtual_class_method(cls):
        ...

Credit
------

Thanks to `Patrick Hensley <http://github.com/phensley>`_ for his input,
and to `Denis Ryzhkov <http://denis.ryzhkov.org/>`_ for his
``method_decorator`` module.
