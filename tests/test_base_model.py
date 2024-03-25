#!/usr/bin/python3
import unittest
from .base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_base_model_attributes(self):
        """testing if Base Model has public instance attributes"""
        my_model = BaseModel()
        self.assertEqual(my_model.id, None)
        self.assertEqual(my_model.created_at, None)
        self.assertEqual(my_model.updated_at, None)

    def test_base_model_methods(self):
        """testing for correct instance methods"""
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'save'))
        self.assertTrue(hasattr(my_model, 'to_dict'))

    def test_save_method(self):
        """Testing save method"""
        my_model = BaseModel()
        my_model.save()
        self.assertIsNotNone(my_model.updated_at)

    def test_to_dict_method(self):
        """Testing if method returns dictionary with correct key and values"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        self.assertEqual(my_model_dict['name'], "My First Model")
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(my_model_dict['__class__'], "BaseModel")
        self.assertIsNotNone(my_model_dict['updated_at'])
        self.assertIsNotNone(my_model_dict['created_at'])

    def test_create_from_dict(self):
        """Creating a new base model class"""
        my_model_dict = {
            'name': "My First Model",
            'my_number': 89,
            '__class__': "BaseModel",
            'updated_at': "2017-09-28T21:03:54.052302",
            'created_at': "2017-09-28T21:03:54.052298",
        }
        my_model = BaseModel(**my_model_dict)
        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertEqual(my_model.updated_at, datetime.datetime(2017, 9, 28, 21, 3, 54, 52302))
        self.assertEqual(my_model.created_at, datetime.datetime(2017, 9, 28, 21, 3, 54, 52298))


if __name__ == '__main__':
    unittest.main()
