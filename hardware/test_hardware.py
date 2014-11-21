import unittest
import mock
from mockgpio import MockGPIO
from hardware import PortalHW

class PortalHWTest(unittest.TestCase):
    def setUp(self):
        MockGPIO.setwarnings(False)
        MockGPIO.references = {} #reset the method reference counts.

    def test_identity(self):
        portal = PortalHW()
        self.assertEqual(isinstance(portal, PortalHW), True)
        self.assertEqual(MockGPIO.references["setup"][0], 2)
        self.assertEqual(MockGPIO.references["setmode"][0], 1)
        #TODO: When door id's get refactored, make this less magic numbery
        self.assertTrue((38, MockGPIO.OUT) in MockGPIO.references["setup"][1])
        self.assertTrue((40, MockGPIO.OUT) in MockGPIO.references["setup"][1])
        self.assertTrue((MockGPIO.BOARD,) in MockGPIO.references["setmode"][1])


    @mock.patch('time.sleep')
    def test_toggle(self, mock_sleep):
        p = PortalHW()
        p.toggle_door("ONE")
        mock_sleep.assert_called_with(1)
        self.assertEqual(MockGPIO.references["output"][0], 2)
        self.assertEqual(MockGPIO.references["output"][1], [(38,1),(38,0)])

    def test_toggle_invalid_door(self):
        p = PortalHW()
        self.assertRaises(KeyError, p.toggle_door, "THREE")



if __name__ == "__main__":
    unittest.main()
