import unittest
import sys
sys.path.append("..")  # Add the parent directory to sys.path

from api import headers

class TestWheneverWeather(unittest.TestCase):

    def test_correct_url(self):
        # Assert that the 'Authorization' header is not equal to 0
        self.assertNotEqual(headers['Authorization'], 0)

if __name__ == '__main__':
    unittest.main()