"""
KV Finder v0.0.1

author: Zbigniew Szczepański


"""


class KVFinder:
    """
    Object purpose is to search for values through a iterable dictionary with
    keys or path build from keys.
    """

    def __init__(self, json_struct=None, search_keys: list=None):
        """
        Initiate KeyValueFinder with structure to search within and with
        searched .

        :param search_struct: structure to search within
        :param search_keys: keys searched, either as list or keys or paths
        """
        self.json_struct = json_struct
        self.search_keys = search_keys

    def set_struct(self, json_struct):
        self.json_struct = json_struct

    def set_searched(self, search_keys):
        self.search_keys = search_keys

    def check_object(self, current_object):
        if isinstance(current_object, (list, tuple)):
            for item in current_object:
                self.check_object(item)
        elif isinstance(current_object, dict):
            for key, item in current_object:
                self.check_object(item)
        else:
            pass

    def search(self):
        """
        Starting point for search.
        """
        if not self.json_struct:
            raise Exception(
                "Structure on which search should be performed is not provided"
            )
        if not self.search_keys:
            raise Exception("Search keys are not provided.")

        self.check_object(self.json_struct)

    def __iter__(self):
        """
        Iterates over searched keys.
        """
        print("A")
