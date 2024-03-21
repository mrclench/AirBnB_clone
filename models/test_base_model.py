#!/usr/bin/python3
"""from base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model) """
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

if __name__ == '__main__':
    unittest.main()