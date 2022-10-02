   class HashTable():
    def __init__(self, data_list):
        self.data_list = data_list

    def get_index_hashing(self,key):
        result = 0
        for char in key:
            result+= ord(char)
        return result  % len(self.data_list)

    def insert(self, key_, value_):
        idx = HashTable.get_index_hashing(key_)
        self.data_list[idx] = (key_, value_)
        return("inserted")

    def find(self, key_):
        # getting the index/hash of the key
        idx = HashTable.get_index_hashing(key_)
        key_, value_ = self.data_list[idx]
        return(value_)

    def update(self, key, new_value):
        idx = HashTable.get_index_hashing(key)
        self.data_list[idx] = (key, new_value)

    # listing all Non-empty keys
    def list_all(self):
        keys = [key for key in self.data_list if key is not None]
        return(keys)
