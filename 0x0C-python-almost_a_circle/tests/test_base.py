#!/usr/bin/python3
"""
Module for Base unit tests.
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1_0(self):
        """Create new instances: check for id."""

        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(927)
        self.assertEqual(b4.id, 927)
        b5 = Base(-5)
        self.assertEqual(b5.id, -5)
        b6 = Base(9)
        self.assertEqual(b6.id, 9)

    def test_id_assignment(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)  # First object should have id 1
        self.assertEqual(obj2.id, 2)  # Second object should have id 2

    def test_custom_id(self):
        obj = Base(id=10)
        self.assertEqual(obj.id, 10)  # Object created with custom id should have that id

    def test_id_uniqueness(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)  # IDs of two different objects should not be the same

    def test_id_increment(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj3.id, 3)  # Third object should have id 3

    def test_id_type(self):
        obj = Base()
        self.assertIsInstance(obj.id, int)  # The id should be an integer

    def test_id_uniqueness_across_instances(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        ids = {obj1.id, obj2.id, obj3.id}
        self.assertEqual(len(ids), 3)  # IDs of three different objects should all be unique

    def test_id_non_negative(self):
        obj = Base()
        self.assertGreaterEqual(obj.id, 0)  # The id should be a non-negative integer

    def test_id_uniqueness_with_custom_id(self):
        obj1 = Base(id=5)
        obj2 = Base(id=5)
        self.assertNotEqual(obj1.id, obj2.id)  # Objects created with the same custom id should have different ids


if __name__ == '__main__':
    unittest.main()
