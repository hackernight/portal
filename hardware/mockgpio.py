class MockGPIO:
    BOARD = "This is a board."
    OUT = 0
    IN = 1
    _warnings = True
    @staticmethod
    def setmode(board):
        MockGPIO.print_warnings("Setting mode to %s"%board)

    @staticmethod
    def setwarnings(toggle):
        MockGPIO._warnings = toggle
        MockGPIO.print_warnings("Setting warnings to %s"%toggle)

    @staticmethod
    def print_warnings(warning_string):
        if MockGPIO._warnings == True:
            print(warning_string)

    @staticmethod
    def setup(pin, mode):
        MockGPIO.print_warnings("Setting pin %d to mode %d"%(pin, mode))

    @staticmethod
    def output(pin, value):
        MockGPIO.print_warnings("Setting pin %d to value %s"%(pin,value))
