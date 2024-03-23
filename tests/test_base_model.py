#!/usr/bin/python3
if __name__ == '__main__':
    unittest.main()
from models.base_model import BaseModel

import unittest
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_attributes_initialization(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_string_representation(self):
        my_model = BaseModel()
        expected_str = f"[{my_model.__class__.__name__}] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(str(my_model), expected_str)


