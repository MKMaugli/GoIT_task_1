from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for i in filter(lambda x: x.isnumeric(), self.data):
            count += 1
        return count