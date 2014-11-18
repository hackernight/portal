BOARD = "This is a board."
OUT = 0
IN = 1
_warnings = True
def setmode(board):
    print_warnings("Setting mode to %s"%board)

def setwarnings(toggle):
    _warnings = toggle
    print_warnings("Setting warnings to %s"%toggle)

def print_warnings(warning_string):
    print "Warnings is %s"%_warnings
    if _warnings == True:
        print(warning_string)

def setup(pin, mode):
    print_warnings("Setting pin %d to mode %d"%(pin, mode))

def output(pin, value):
    print_warnings("Setting pin %d to value %s"%(pin,value))
