#!/usr/bin/python3
import unittest
from unittest.mock import Mock, MagicMock, patch, call, mock_open

MockRead = MagicMock()
modules = {
    "readSensors": MockRead
}
patcher = patch.dict("sys.modules", modules)
patcher.start()

from src import store as st


class TestStore(unittest.TestCase):

    @patch('os.path.isfile')
    def test_storeLocal(self, MockOs):
        with patch('builtins.open', new_callable=mock_open()) as mOpen:
            with patch('json.dump') as m_json:
                with patch('json.load') as mLjson:
                    vals = {'a': 21.0, 'b': 46.7}
                    MockOs.return_value = None
                    mm = Mock()
                    mOpen.return_value.__enter__.return_value = mm
                    st.storeLocal(vals)
                    ret = m_json.call_args
                    fn = st.path + st.dt.strftime("%Y%m%d%H") + st.end
                    calls = [call(fn, 'a'), call(fn, 'r+')]
                    MockOs.assert_called_with(fn)
                    self.assertEqual(1, mLjson.call_count)
                    self.assertEqual({'indent': 2}, ret[1])
                    ret = ret[0][0].method_calls[0][1][0]
                    self.assertEqual(vals, ret)
                    self.assertEqual(2, mOpen.call_count)
                    mOpen.assert_has_calls(calls, any_order=True)

                    return

    def test_send(self):
        with patch('mysql.connector.connect') as mock:
            vals = {'d': {'airTemp': 21.0, 'humidity': 46.0, 'mcp00': 7, 'mcp01': 3,
                          'mcp02': 6, 'mcp03': 100, 'mcp04': 100, 'mcp05': 10, 'mcp06': 10,
                          'mcp07': 3, 'soilTemp': 1}}
            connection = mock.return_value
            cursor = connection.cursor.return_value
            st.send(vals)
            mock.assert_called()
            args = mock.call_args_list[0][1]
            self.assertEqual(4, len(args))
            self.assertEqual(1, mock.call_count)
        return
