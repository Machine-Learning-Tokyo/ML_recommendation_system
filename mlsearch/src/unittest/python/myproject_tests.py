from unittest import TestCase
from mock import Mock
from mlsearch import greet
from mlsearch.api_requester import APIRequest


class Test(TestCase):
    def test_should_write_hello_world(self):
        mock_stdout = Mock()

        greet(mock_stdout)

        mock_stdout.write.assert_called_with("Hello world!\n")