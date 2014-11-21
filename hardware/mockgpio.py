black_list = ["increment_references", "print_warnings"]

class MockGPIOMetaClass(type):
    '''
    This class is meant to be a meta class that is purely responsible
    for incrementing reference counts and logging arguments for the
    purpose of unit testing since MockGPIO will only ever be used
    in an environment that is not production.
    '''
    def __getattribute__(cls, name):
        attr = object.__getattribute__(cls, name)
        if hasattr(attr, '__func__'):
            def newfunc(*args, **kwargs):
                if name not in black_list:
                    cls.increment_references(name, args)
                result = attr.__func__(cls, *args, **kwargs)
                return result
            return newfunc
        else:
            return attr

    def increment_references(cls, name, args):
        if name not in cls.references.keys():
            cls.references[name] = (1, [args])
        else:
            original = cls.references[name]
            original[1].append(args)
            cls.references[name] = (original[0]+1, original[1])

class MockGPIO(object):
    '''
    A class to mock out the RPi.GPIO library for local testing
    '''
    __metaclass__ = MockGPIOMetaClass

    BOARD = "This is a board."
    OUT = 0
    IN = 1
    _warnings = True
    references = {} #read comments on metaclass, this is just for unit testing.

    @classmethod
    def print_warnings(cls, warning_string):
        if MockGPIO._warnings == True:
            print(warning_string)

    @classmethod
    def setmode(cls, board):
        MockGPIO.print_warnings("Setting mode to %s"%board)

    @classmethod
    def setwarnings(cls, toggle):
        MockGPIO._warnings = toggle
        MockGPIO.print_warnings("Setting warnings to %s"%toggle)

    @classmethod
    def setup(cls, pin, mode):
        MockGPIO.print_warnings("Setting pin %d to mode %d"%(pin, mode))

    @classmethod
    def output(cls, pin, value):
        MockGPIO.print_warnings("Setting pin %d to value %s"%(pin,value))
