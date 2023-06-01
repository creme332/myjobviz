import unittest
from analyser.dictionaryUtils import filter_dict


def location_count(location_list):
    """Identifies the most common location for IT jobs.

    Args:
        destination_filename (str): path where statistics will be saved.
    """
    JobCountPerDistrict = {'Black River': 0, 'Flacq': 0,
                           'Grand Port': 0, 'Moka': 0, 'Pamplemousses': 0,
                           'Plaine Wilhems': 0, 'Port Louis': 0,
                           'Riviere du Rempart': 0, 'Savanne': 0}
    skipped_locations = []

    for location in location_list:
        location = location.replace('\r\n', '',).strip()
        if location != "Mauritius" and location != "Rodrigues":
            if (location not in JobCountPerDistrict.keys()):
                skipped_locations.append(location)
                continue
            JobCountPerDistrict[location] += 1

    # Rename Plaine Wilhems to Plaines Wilhems
    # (myjob.mu incorrectly wrote "Plaine Wilhems")
    JobCountPerDistrict['Plaines Wilhems'] = JobCountPerDistrict.pop(
        'Plaine Wilhems')
    if (len(skipped_locations) > 0):
        print('Unknown districts found :', skipped_locations)
    return JobCountPerDistrict


class Test(unittest.TestCase):

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
