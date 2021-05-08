#! /usr/bin/env python3

# Author: Dennis Chukwunta (c) 2021
# Email: chuksmcdennis@yahoo.com

''' An attempt at a simple Hash Table using only Arrays(lists) '''


class HashTable:
    ''' To create a new HashTable object:
        hash_object = HashTable()

        To add a new item to the HashTable object:
        hash_object.add_item(key, value)

        To delete an item from the HashTable object:
        hash_object.del_item(key)

        To get an an item from the object:
        hash_object.get_item(key)

        To get the number of items in the HashTable:
        len(hash_object) 
    '''

    def __init__(self, size=1000):
        self._slots = [None]*size
        self._count = 0

    def __len__(self):
        return self._count

    def add_item(self, key, value):
        index = hash(key) % len(self._slots)
        if self._slots[index] != None:
            return "The key '{}' already exists.".format(key)
        else:
            self._slots[index] = value
            self._count = self._count + 1

    def get_item(self, key):
        index = hash(key) % len(self._slots)
        if self._slots[index]:
            return self._slots[index]
        else:
            return "The key '{}' does not exist.".format(key)

    def del_item(self, key):
        index = hash(key) % len(self._slots)
        if self._slots[index]:
            self._slots[index] = None
            self._count = self._count - 1
        else:
            raise KeyError(key)
