#!/usr/bin/python3

import unittest
from datetime import datetime
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """ Unit test for testing the User class"""

    def test_create_instance_no_args(self):
        obj = User()
        self.assertEqual(User, type(obj))

    def test_create_instance_with_args(self):
        today = datetime.today()
        today_iso = today.isoformat()
        obj = User(id="555", created_at=today_iso, updated_at=today_iso)
        self.assertEqual("555", obj.id)
        self.assertEqual(today, obj.created_at)
        self.assertEqual(today, obj.updated_at)

    def test_check_attributes(self):
        obj = User()
        self.assertTrue(hasattr(obj, "email"))
        self.assertTrue(hasattr(obj, "password"))
        self.assertTrue(hasattr(obj, "first_name"))
        self.assertTrue(hasattr(obj, "last_name"))

    def test_create_instance_with_None_args(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_obj_attribute_types(self):
        obj = User()
        self.assertEqual(str, type(obj.id))
        self.assertEqual(datetime, type(obj.created_at))
        self.assertEqual(datetime, type(obj.updated_at))

    def test_string_representation(self):
        obj = User()
        class_str = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertIsNotNone(str(obj))
        self.assertEqual(class_str, str(obj))

    def test_adding_obj_to_objects(self):
        obj = User()
        self.assertIn(obj, storage.all().values())

    def test_unique_id(self):
        self.assertNotEqual(User().id, User().id)

    def test_save_update_at(self):
        obj = User()
        updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(updated_at, obj.updated_at)
        self.assertLess(updated_at, obj.updated_at)

    def test_save(self):
        obj = User()
        obj.save()
        storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, storage.all())
        self.assertEqual(obj.id, storage.all()[key].id)

    def test_multiple_saves_consistency(self):
        obj = User()
        obj.name = "Test"
        obj.save()
        first_updated_at = obj.updated_at
        obj.name = "Test Updated"
        obj.save()
        second_updated_at = obj.updated_at
        self.assertNotEqual(first_updated_at, second_updated_at)
        storage.reload()
        reloaded_obj = storage.all()[f"{obj.__class__.__name__}.{obj.id}"]
        self.assertEqual(reloaded_obj.name, "Test Updated")
        self.assertEqual(reloaded_obj.updated_at, second_updated_at)

    def test_to_dict(self):
        obj = User()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['__class__'], obj.__class__.__name__)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_to_dict_type(self):
        obj = User()
        self.assertTrue(dict, type(obj.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        obj = User()
        self.assertIn("__class__", obj.to_dict())
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())

    def test_to_dict_contains_added_attributes(self):
        obj = User()
        obj.name = "James"
        obj.my_number = 12345
        self.assertIn("name", obj.to_dict())
        self.assertIn("my_number", obj.to_dict())
        self.assertEqual("James", obj.to_dict()['name'])
        self.assertEqual(12345, obj.to_dict()['my_number'])

    def test_to_dict_with_arg(self):
        """Test to_dict raises TypeError if an argument is passed"""
        obj = User()
        with self.assertRaises(TypeError):
            obj.to_dict(None)


if __name__ == "__main__":
    unittest.main()
