import unittest
from unittest import mock
import client
import get_url_new


class TestClient(unittest.TestCase):

    def test_success_request(self):
        success_send = mock.Mock(return_value='200')
        client.send_request = success_send
        self.assertEqual(client.visit_baidu(), '200')

    def test_fail_request(self):
        fail_send = mock.Mock(return_value='404')
        get_url_new.get_url = fail_send
        self.assertEqual(get_url_new.get_url(), '404')
