#!/usr/bin/python3
import unittest
from unittest.mock import Mock
from unittest.mock import patch
from src import database_query as dq
# import database_query as dq


class TestDatabaseQuery(unittest.TestCase):

    def test_queryDB(self):
        with patch('mysql.connector.connect') as mock:
            connection = mock.return_value
            cursor = connection.cursor.return_value
            feed = 'test feed'
            dq.queryDB(feed)
            mock.assert_called()
            args = mock.call_args
            self.assertEqual(4, len(args[1]))
            cursor.execute.assert_called_with(feed)
        return

def runDBtest():
    print('runtTest')
    unittest.main()
    print('after')
    return('finnn')

if __name__ == '__main__':
    unittest.main()
