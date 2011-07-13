from method_decorator import method_decorator

class virtualmethod(method_decorator):
    def __call__(self, *args, **kwargs):
        if self.cls and self.cls.__dict__.has_key(self.__name__):
            raise TypeError("Virtual method %s must be called from a subclass." % self.__name__)
        return method_decorator.__call__( self, *args, **kwargs )
        