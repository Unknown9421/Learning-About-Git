"""
    Testing My Function
"""
import sys
# sys.path.append('Learning Testing/My_Package/__init__.py')

# print(sys.path)

# My Function
from My_Package.full_name import get_full_name

# Unittest
import unittest


class GetFullNameTestCase(unittest.TestCase):

    def test_first_last__name(self):
        result = get_full_name('Nguyễn', 'Hoàng', middle_name='Đức')
        self.assertEqual(result, "Nguyễn Ha Hoàng")

    def test_first_last_middle_name(self):
        result = get_full_name('Nguyễn', 'Hoàng', middle_name='Đức')
        self.assertEqual(result, "Nguyễn Đức Hoàng")