"""
KV Finder v0.0.1

author: Zbigniew Szczepański


"""


class KVFinder:
    """
    Object purpose is to search for values through a iterable dictionary with
    keys or path build from keys.
    """

    def __init__(self, search_struct=None, search_keys=None):
        self.search_struct = search_struct
        self.search_keys = search_keys

    def set_struct(self, search_struct):
        self.search_struct = search_struct

    def set_searched(self, search_keys):
        self.search_keys = search_keys

    def search(self):
        pass

    def __iter__(self):
        print("A")
