#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock, patch

MockRPi = MagicMock()
modules = {
    "RPi": MockRPi,
    "RPi.GPIO": MockRPi.GPIO,
}
patcher = patch.dict("sys.modules", modules)
patcher.start()
from src import controllers as control


class TestControllers(unittest.TestCase):
    def test_water(self):
        with patch('RPi.GPIO.output') as mock:
            # print(MockRPi.GPIO)

            tVal = 4
            control.water(tVal, 2)
            mock.assert_called()
            args = mock.call_args_list
            self.assertEqual(2, len(args[1]))
            for calls in args:
                self.assertEqual(tVal, calls[0][0])

            return

    @patch('src.controllers.water')
    def test_manWater(self, water):
        tVal = 1
        control.manWater(tVal)
        water.assert_called_with(15, 0.2)
        tVal = 3
        with self.assertRaises(IndexError):
            control.manWater(tVal)
        return
