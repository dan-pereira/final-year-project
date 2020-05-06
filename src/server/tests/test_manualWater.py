#!/usr/bin/python3
import unittest
from unittest.mock import Mock
from src import manualWater as mw

class TestManualWater(unittest.TestCase):
    def test_waterPlant(self):
        mw.requests.post = Mock()

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
