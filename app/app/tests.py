"""
sample test
"""


from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """tests the calc module"""

    def test_add_num(self):
        """test for adding nums"""
        res = calc.add(1, 9, 1)
        self.assertEqual(res, 11)

    def test_sub_nums(self):
        """test for sub nums"""
        res = calc.sub(10, 4)
        self.assertEqual(res, 6)
