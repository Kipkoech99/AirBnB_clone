#!/usr/bin/python3
"""Module with all unittests for the base_model.py(BaseModel class)"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Test class for BaseModel attributes and methods

    Methods:
        test-id_uuid: tests id(uuid) creation
        test_str_method: tests str method / representation
        test_to_dict_method: tests if to_dict method is as desired
    '''
    def test_id_uuid(self):
        ''' tests object id creation'''
        instance = BaseModel()
        self.assertIsInstance(instance.id, str) # check if id is str

        # check if id is valid UUID
        try:
            uuid.UUID(instance.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID")

    def test_created_updated_at(self):
        ''' tests that created_at & updated_at behavior is as expected'''
        instance = BaseModel()
        now = datetime.datetime.now()

        # check if created_at & updated_at are datetime objects
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

        # created_at & updated_at should be approximately as now
        self.assertAlmostEqual(instance.created_at, now, delta=datetime.timedelta(seconds=1))
        self.assertAlmostEqual(instance.updated_at, now, delta=datetime.timedelta(seconds=1))

    def test_save_method(self):
        ''' test save method to update the object updated_at'''
        instance = BaseModel()
        now = datetime.datetime.now()
        instance.save()
        self.assertNotEqual(instance.updated_at, now)

    def test_str_method(self):
        '''tests str representation of the object'''
        instance = BaseModel() # get str instance of the class
        class_name = instance.__class__.__name__
        expected_str = f"[{class_name}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

    def test_to_dict_method(self):
        '''ensures dict instance of the object is as intended'''
        instance = BaseModel() # create an instance
        instance_dict = instance.to_dict() # get dict repr of the instance
        self.assertIsInstance(instance_dict, dict) # test if is intance

        self.assertIn('__class__', instance_dict)  # if __class__ key present
        self.assertEqual(instance_dict['__class__'],
                instance.__class__.__name__)  # check its value if it exists

        # check if created_at / updated_at exists in ISO format(str)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
