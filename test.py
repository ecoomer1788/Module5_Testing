import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()


"""
Test Results:
The test passed successfully. The program tested the sum function using
the numbers 1, 2, and 3. The function returned 6, which matched the
expected result. The OK result means that the function worked correctly
for this test and no errors or failures were found.
"""
