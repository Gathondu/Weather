import unittest

from weather import getWeather


class TestWeather(unittest.TestCase):

    def test_returns_response(self):
        result = getWeather('x')
        self.assertEqual(result, 'Could not find that location', 'The locationx should fail')

if __name__ == "__main__":
    unittest.main()
