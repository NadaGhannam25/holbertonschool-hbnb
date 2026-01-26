#!/usr/bin/env python3
import unittest

from app.models.user import User
from app.models.place import Place
from app.models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.user = User(first_name="U", last_name="1", email="u1@hbnb.com")
        self.place = Place(owner=self.user, title="P", price=10, latitude=0, longitude=0)

    def test_create_valid_review(self):
        r = Review(text="Great", rating=5, place=self.place, user=self.user)
        self.assertEqual(r.text, "Great")
        self.assertEqual(r.rating, 5)
        self.assertEqual(r.place.id, self.place.id)
        self.assertEqual(r.user.id, self.user.id)

    def test_empty_text_should_fail(self):
        with self.assertRaises(Exception):
            Review(text="", rating=5, place=self.place, user=self.user)
        with self.assertRaises(Exception):
            Review(text="   ", rating=5, place=self.place, user=self.user)

    def test_invalid_rating_should_fail(self):
        with self.assertRaises(Exception):
            Review(text="X", rating=0, place=self.place, user=self.user)
        with self.assertRaises(Exception):
            Review(text="X", rating=6, place=self.place, user=self.user)

    def test_to_dict_contains_ids(self):
        r = Review(text="Ok", rating=4, place=self.place, user=self.user)
        d = r.to_dict()
        self.assertIn("id", d)
        self.assertIn("text", d)
        self.assertIn("rating", d)
        self.assertEqual(d["user_id"], self.user.id)
        self.assertEqual(d["place_id"], self.place.id)


if __name__ == "__main__":
    unittest.main(verbosity=2)
