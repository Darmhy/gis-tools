import unittest

from .geopath import GeoPath

class TestPath(unittest.TestCase):
    """Tests the functionality of the Path class using
    a two segment path in the city of Philadelphia."""

    def setUp(self):
        #chestnut and 40th
        #39.955828, -75.202286
        #chesnut and 6th
        #39.949191, -75.150776
        #snyder and 6th
        #39.922669, -75.156699
        #distance from path[0] to path[1] is 4.46 km
        #distance from path[1] to path[2] is 2.97 km
        #total length of path is 7.44 km
        
        self.path = [(39.955828, -75.202286),
                     (39.949191, -75.150776),
                     (39.922669, -75.156699)]
        self.geo_path = GeoPath(self.path)

    def test_path_len(self):
        path_len = self.geo_path.get_len()
        self.assertTrue(abs(path_len - 7.44) < 0.02)

    def test_get_dist(self):
        d = self.geo_path.get_dist(self.path[1], self.path[2])
        self.assertTrue(abs(d - 2.97) < 0.02)

    def test_get_norm_pos(self):
        #should be 4.46 / 7.44 = 0.60
        pos = self.geo_path.get_norm_pos(self.path[1])
        self.assertTrue(abs(pos - 0.6) < 0.02)
