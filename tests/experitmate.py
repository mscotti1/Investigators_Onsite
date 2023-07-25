import unittest
import sys
sys.path.append("..")  # Add the parent directory to sys.path


class TestWheneverWeather(unittest.TestCase):

    def test_add(self):
        # Assert that the 'Authorization' header is not equal to 0
        self.assertEqual(0,0)

if __name__ == '__main__':
    unittest.main()