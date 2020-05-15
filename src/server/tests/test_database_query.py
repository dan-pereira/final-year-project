#!/usr/bin/python3
import unittest
import datetime
from unittest.mock import Mock
from unittest.mock import patch
from src import database_query as dq


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

    @patch('src.database_query.queryDB')
    def test_formattedQDB(self, MockQ):

        MockQ.return_value = [(datetime.datetime(2020, 5, 15, 15, 15), 74.9837)]

        res = dq.formattedQDB(10)

        MockQ.asset_called_with(10)

        print(res)
        print('nn')
        return
