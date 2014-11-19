import unittest
from mockgpio import MockGPIO
import hardware as hw

class PortalHWTest(unittest.TestCase):
    def setUp(self):
        MockGPIO.setwarnings(False)

    def test_identity(self):
        portal = hw.PortalHW()
        self.assertEqual(isinstance(portal, hw.PortalHW), True)


if __name__ == "__main__":
    unittest.main()
