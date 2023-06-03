import unittest
from src.utils.dictionary import (filter_dict)
from src.analyser.location import location_count
from src.utils.constants import MU_DISTRICTS


class TestLocations(unittest.TestCase):

    def test_plaine_wilhems(self):
        # test renaming of key for plaine wilhems
        list = ['Plaine Wilhems']
        self.assertEqual(filter_dict(
            location_count(list)), {'Plaines Wilhems': 1})

    def test_districts(self):
        self.assertEqual(filter_dict(
            location_count(MU_DISTRICTS)), {'Black River': 1,
                                            'Flacq': 1,
                                            'Grand Port': 1,
                                            'Moka': 1,
                                            'Pamplemousses': 1,
                                            'Plaines Wilhems': 1,
                                            'Port Louis': 1,
                                            'Riviere du Rempart': 1,
                                            'Savanne': 1
                                            }
        )
