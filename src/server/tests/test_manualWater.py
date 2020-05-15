#!/usr/bin/python3
import unittest
from unittest.mock import Mock, patch, mock_open, call
from src import manualWater as mw


class TestManualWater(unittest.TestCase):
    # check endpoint
    def test_waterPlant(self):
        with patch('requests.post') as mock:
            # print(mock.return_value)
            i = 2
            mw.waterPlant(i)
            result = mw.piEndpoint+'water_plant'
            dic = {'plantNo': i}
            mock.assert_called()
            print(mock.call_args_list)
            mock.assert_called_with(result,data = dic)
        return

    def test_writeConfig(self):
        with patch('builtins.open', new_callable=mock_open()) as mOpen:
            with patch('json.dump') as m_json:
                fileName = mw.path + 'defaultConfig.json'
                with patch('requests.post', call(fileName, 'rb')) as mReq:
                    calls = [call(fileName, 'w'), call(fileName, 'rb')]
                    dic = {'file': mOpen.name}
                    result = mw.piEndpoint + 'update_config'

                    mw.writeConfig(dic)

                    # print(mOpen.call_args_list)
                    # print(m_json.call_args_list)

                    self.assertEqual(2, mOpen.call_count)
                    self.assertEqual(1, m_json.call_count)
                    mReq.assert_called_with(result, file=dic)
                    mOpen.assert_has_calls(calls, any_order=True)
        return

    @patch('src.manualWater.readConfig')
    def test_manAutoSelect(self, readC):
        with patch('src.manualWater.writeConfig') as writeC:
            testDic = {'manual_mode': 0}
            readC.return_value = testDic

            mw.manAutoSelect(1)
            r = writeC.call_args[0][0]
            testDic['manual_mode'] = 1
            print(type(r), r)
            print(type(testDic), testDic)
            self.assertEqual(testDic, r)
        return


if __name__ == '__main__':
    unittest.main()
