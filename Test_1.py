from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        res = []
        for key, val in self.data.items():
            if val == value:
                res.append(key)
        return res