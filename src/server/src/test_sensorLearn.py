import unittest
import sensorLearn as sl

'''
manualWater
printQtable
'''

class TestSensorLearn(unittest.TestCase):

    def test_getDiscreteState(self):
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

    def test_rewards(self):
        self.assertEqual(10, sl.getReward(50, 60, 20))
        self.assertEqual(-10, sl.getReward(60, 50, 20))
        self.assertEqual(0, sl.getReward(60, 60, 20))
        return

    def test_calculate(self):
        pass

    def test_getState(self):
        res = sl.getCurrentState()
        self.assertEqual(3, len(res))
        for val in res:
            self.assertIs(int, type(val))
        return

    def test_databaseQuery(self):
        res = sl.queryDB('SELECT moisture1,moisture2, moisture3 FROM mydb.sensor_val order by timer desc limit 5')
        self.assertEqual(5, len(res))
        return

if __name__ == '__main__':
    print('starting tests')
    unittest.main()
