import unittest
import utilities.api as api


class TestAPI(unittest.TestCase):

    def test_api_result(self):
        """
        Test if the response of the API request is an int (temperature)
        """
        response = api.get_current_temp()
        self.assertIsInstance(response, int)


if __name__ == '__main__':
    unittest.main()
