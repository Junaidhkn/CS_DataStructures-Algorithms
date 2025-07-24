class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * 10


    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def insert(self, key,value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self,key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    # def get(self, key):
    #     index = self.__hash(key)
    #     bucket = self.data_map[index]
    #     if bucket is not None:
    #         for k, v in bucket:
    #             if k == key:
    #                 return v
    #     return None


    def print_hash(self):
        for i,val in enumerate(self.data_map):
            print(i,":", val)





my_hash_table = HashTable()
my_hash_table.insert('jobs',1)
my_hash_table.insert('cars',1)
my_hash_table.insert('jeeps',3)
my_hash_table.insert('employees',3)

print('Get method:',my_hash_table.get_item('jobs'))
my_hash_table.print_hash()