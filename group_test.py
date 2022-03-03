from unittest import TestCase

from .group_cars import construct_rows, read_data, get_groups

class TestRead(TestCase):
    def test_cars_read_1(self):
        l = list(read_data("autovertailu/data/cars_test.json"))
        assert str(l) == "[(2000, 100000, 16000, 'test1'), (2014, 200000, 10000, 'test12')]"


    def test_get_groups_1(self):
        l = list(get_groups("autovertailu/data/cars_test.json"))
        assert str(l) == "[[(2000, 100000, 16000, 'test1'), (2014, 200000, 10000, 'test12')]]"


    