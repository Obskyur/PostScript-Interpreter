class LimitedDict:
    def __init__(self, max_size):
        self.max_size = max_size
        self.dict = {}

    def __setitem__(self, key, value):
        if len(self.dict) >= self.max_size:
            raise Exception("Dictionary has reached its maximum size")
        self.dict[key] = value

    def __getitem__(self, key):
        return self.dict[key]

    def __delitem__(self, key):
        del self.dict[key]

    def __contains__(self, key):
        return key in self.dict

    def __len__(self):
        return len(self.dict)

    def __repr__(self):
        return repr(self.dict)