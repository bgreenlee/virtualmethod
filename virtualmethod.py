import types

class virtualmethod(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, ownerClass=None):
        # return a wrapper that binds self as a method of obj
        return types.MethodType(self, obj)

    def __call__(self, *args, **kwargs):
        cls_dict = args[0].__class__.__dict__
        func_name = self.func.__name__
        # check to see if the virtualmethod is defined in this class
        if cls_dict.has_key(func_name) and cls_dict[func_name].__class__ == self.__class__:
            raise TypeError("Virtual method %s must be called from a subclass." % func_name)
        return self.func(*args, **kwargs)