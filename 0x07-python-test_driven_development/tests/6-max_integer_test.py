import unittest

def max_integer(list=[]):
    if len(list) == 0:
        return None
    max_int = list[0]
    for i in list:
        if i > max_int:
            max_int = i
    return max_int

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7, "Single element list should return the element itself")

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4, "Maximum is at the end")

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4, "Maximum is at the beginning")

    def test_max_in_middle(self):
        self.assertEqual(max_integer([2, 3, 4, 1]), 4, "Maximum is in the middle")

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-2, -3, -1, -5]), -1, "List with negative numbers")

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-2, 3, 1, -5, 0]), 3, "List with mixed numbers")

    def test_all_equal(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1, "All elements are equal")

if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/6-max_integer_test.py")
