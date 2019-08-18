from unittest import TestCase

from kv_finder import KVFinder


class TestFVFinder(TestCase):

    def setUp(self):
        with open("test_fixtures.json") as fh:
            self.obj = fh.read()

    def test_simple_search(self):
        search = [
            "address"
        ]
        find = {
            "postcode": "890-567",
            "country": "UK",
            "city": "London",
            "street": "Some Street",
            "house": "67",
            "flat": "45"
        }

        kvf = KVFinder(search_struct=self.obj, search_keys=search)
        assert kvf.search() == find

    def test_simple_search_with_path(self):
        search = [
            "members.country"
        ]
        find = ["Poland", "Malaysia", "Japan", "Bolivia"]

        kvf = KVFinder(search_struct=self.obj, search_keys=search)
        assert kvf.search() == find

    def tearDown(self):
        del(self.obj)
