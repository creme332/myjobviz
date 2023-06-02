import unittest
from src.utils.dictionary import (filter_dict)
from src.analyser.location import location_count


class TestLocations(unittest.TestCase):

    def test_plaine_wilhems(self):
        list = ['Plaine Wilhems']
        self.assertEqual(filter_dict(
            location_count(list)), {'Plaines Wilhems': 1})

    def test_countries(self):
        list = ['Rodrigues', 'Mauritius']
        self.assertEqual(filter_dict(
            location_count(list)), {})

    def test_exceptions(self):
        list = ['fs', 'Mauritius']
        self.assertEqual(filter_dict(
            location_count(list)), {})
