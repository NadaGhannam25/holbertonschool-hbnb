#!/usr/bin/env python3
import unittest
import time
from datetime import datetime

from app.models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id_is_string(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertTrue(len(obj.id) > 0)

    def test_timestamps_exist(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_updates_updated_at(self):
        obj = BaseModel()
        old = obj.updated_at
        time.sleep(1)
        obj.save()
        self.assertGreater(obj.updated_at, old)

    def test_update_updates_fields_and_timestamp(self):
        obj = BaseModel()
        obj.some_field = "x"
        old = obj.updated_at
        time.sleep(1)
        obj.update({"some_field": "y"})
        self.assertEqual(obj.some_field, "y")
        self.assertGreater(obj.updated_at, old)


if __name__ == "__main__":
    unittest.main(verbosity=2)
