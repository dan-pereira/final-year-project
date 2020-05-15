#!/usr/bin/python3
import unittest
from unittest.mock import Mock, MagicMock, patch

MockQDB = MagicMock()

modules = {
    "database_query": MockQDB
    }
patcher = patch.dict("sys.modules", modules)
patcher.start()


from src import sensorLearn as sl


storagePath = "storage/"

class TestSensorLearn(unittest.TestCase):

    #SensorLearn
    def test_getDiscreteState(self):
        print(sl.getDiscreteState(20))
        self.assertEqual(20, sl.getDiscreteState(50.222))
        self.assertEqual(19, sl.getDiscreteState(49.99999))
        self.assertEqual(0, sl.getDiscreteState(0))
        self.assertEqual(40, sl.getDiscreteState(100))
        return

    def test_reverseDiscreteState(self):
        self.assertEqual(25, sl.reverseDiscrete(10))
        self.assertEqual(100, sl.reverseDiscrete(40))
        self.assertEqual(0, sl.reverseDiscrete(0))
        return

    def test_getCurrentState(self):
        sl.queryDB = Mock()
        sl.queryDB.return_value = [(53.8145, 40.7873, 64.3991), (80.3574, 39.6475, 83.6142)]
        self.assertEqual([26,16,29], sl.getCurrentState(2))
        sl.queryDB.return_value = [(0, 0, 0), (100, 100, 100)]
        self.assertEqual([20,20,20], sl.getCurrentState(2))
        return

    def test_rewards(self):
        self.assertEqual(10, sl.getReward(50, 60, 20))
        self.assertEqual(-10, sl.getReward(60, 50, 20))
        self.assertEqual(0, sl.getReward(60, 60, 20))
        return




def runTest():
    print('runtTest')
    unittest.main()
    print('after')
    return 'strrr'
if __name__ == '__main__':
    print('starting tests')
