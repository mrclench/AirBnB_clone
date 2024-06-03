#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):

    def test_instance_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instance_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_instance_has_attributes(self):
        obj = FileStorage()
        self.assertTrue(hasattr(obj, '_FileStorage__objects'))
        self.assertTrue(hasattr(obj, '_FileStorage__file_path'))

    def test_instance_attributes_type(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class Test_FileStorage_methods(unittest.TestCase):

    def test_all(self):
        self.assertEqual(dict, type(storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        base = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        self.assertIn(base, storage.all().values())
        self.assertIn(f"BaseModel.{base.id}", storage.all().keys())
        self.assertIn(user, storage.all().values())
        self.assertIn(f"User.{user.id}", storage.all().keys())
        self.assertIn(state, storage.all().values())
        self.assertIn(f"State.{state.id}", storage.all().keys())
        self.assertIn(place, storage.all().values())
        self.assertIn(f"Place.{place.id}", storage.all().keys())
        self.assertIn(city, storage.all().values())
        self.assertIn(f"City.{city.id}", storage.all().keys())
        self.assertIn(amenity, storage.all().values())
        self.assertIn(f"Amenity.{amenity.id}", storage.all().keys())
        self.assertIn(review, storage.all().values())
        self.assertIn(f"Review.{review.id}", storage.all().keys())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_save(self):
        base = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        storage.save()
        storage.reload()
        self.assertIn(f"BaseModel.{base.id}", storage.all())
        self.assertEqual(base.to_dict(),
                         storage.all()[f"BaseModel.{base.id}"].to_dict())
        self.assertIn(f"User.{user.id}", storage.all())
        self.assertEqual(user.to_dict(),
                         storage.all()[f"User.{user.id}"].to_dict())
        self.assertIn(f"State.{state.id}", storage.all())
        self.assertEqual(state.to_dict(),
                         storage.all()[f"State.{state.id}"].to_dict())
        self.assertIn(f"Place.{place.id}", storage.all())
        self.assertEqual(place.to_dict(),
                         storage.all()[f"Place.{place.id}"].to_dict())
        self.assertIn(f"City.{city.id}", storage.all())
        self.assertEqual(city.to_dict(),
                         storage.all()[f"City.{city.id}"].to_dict())
        self.assertIn(f"Amenity.{amenity.id}", storage.all())
        self.assertEqual(amenity.to_dict(),
                         storage.all()[f"Amenity.{amenity.id}"].to_dict())
        self.assertIn(f"Review.{review.id}", storage.all())
        self.assertEqual(review.to_dict(),
                         storage.all()[f"Review.{review.id}"].to_dict())

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload(self):
        base = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        storage.save()
        storage.reload()
        self.assertIn(f"BaseModel.{base.id}", storage.all())
        self.assertEqual(base.to_dict(),
                         storage.all()[f"BaseModel.{base.id}"].to_dict())
        self.assertIn(f"User.{user.id}", storage.all())
        self.assertEqual(user.to_dict(),
                         storage.all()[f"User.{user.id}"].to_dict())
        self.assertIn(f"State.{state.id}", storage.all())
        self.assertEqual(state.to_dict(),
                         storage.all()[f"State.{state.id}"].to_dict())
        self.assertIn(f"Place.{place.id}", storage.all())
        self.assertEqual(place.to_dict(),
                         storage.all()[f"Place.{place.id}"].to_dict())
        self.assertIn(f"City.{city.id}", storage.all())
        self.assertEqual(city.to_dict(),
                         storage.all()[f"City.{city.id}"].to_dict())
        self.assertIn(f"Amenity.{amenity.id}", storage.all())
        self.assertEqual(amenity.to_dict(),
                         storage.all()[f"Amenity.{amenity.id}"].to_dict())
        self.assertIn(f"Review.{review.id}", storage.all())
        self.assertEqual(review.to_dict(),
                         storage.all()[f"Review.{review.id}"].to_dict())

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            storage.reload(None)


if __name__ == '__main__':
    unittest.main()
