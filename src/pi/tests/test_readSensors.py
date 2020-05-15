#!/usr/bin/python3
import unittest
from unittest.mock import Mock, MagicMock, patch, call, mock_open

Mockgpz = MagicMock()
MockMcp = MagicMock()
MockAda = MagicMock()
modules = {
    "gpiozero": Mockgpz,
    "gpiozero.MCP3008": MockMcp,
    "Adafruit_DHT": MockAda,
}
patcher = patch.dict("sys.modules", modules)
patcher.start()
from src import readSensors as rs


class TestReadSensors(unittest.TestCase):

    def test_mcp(self):
        mm = Mock()
        mm.value = 0.5
        Mockgpz.MCP3008.return_value = mm
        values = {}
        rs.mcp3008(values)

        res = {'mcp00': 58.33333333333333, 'mcp01': 58.33333333333333, 'mcp02': 58.33333333333333,
               'mcp03': 58.33333333333333, 'mcp04': 58.33333333333333, 'mcp05': 58.33333333333333,
               'mcp06': 58.33333333333333, 'mcp07': 100}
        calls = [call(channel=i) for i in range(8)]

        self.assertEqual(res, values)
        self.assertEqual(8, Mockgpz.MCP3008.call_count)
        Mockgpz.MCP3008.assert_has_calls(calls, any_order=True)
        return

    def test_dht(self):
        MockAda.DHT11 = 20
        MockAda.read_retry.return_value = 25, 27

        values = {}
        rs.DHT11(values)
        res = {'airTemp': 27, 'humidity': 25}
        MockAda.read_retry.assert_called_with(20, 4)
        self.assertEqual(res, values)
        return

    @patch('os.system')
    def test_ds18(self, sts):
        with patch('builtins.open', new_callable=mock_open()) as mOpen:
            with patch('src.readSensors.glob.glob') as mockG:
                mm = Mock()
                mm.readlines.return_value = ['one', 'test val t=2006']  # resulting t should be 200 -> /1000
                mOpen.return_value.__enter__.return_value = mm
                mockG.return_value = ['test']
                values = {}

                rs.DS18B20(values)

                res = {'soilTemp': 0.2}
                self.assertEqual(res, values)
                mOpen.assert_called_with('test/w1_slave', 'r')
                mockG.assert_called_with('/sys/bus/w1/devices/28*')
        return
