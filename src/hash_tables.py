'''
Hash Tables: Javascript objects, python dictionaries, hashmaps
    - Made up of key/value pairs
    - get --> O(1) Time complexity
    - insert --> O(1) Time complexity
    - delete --> O(1) Time complexity
    - Space Complexity --> O(n)
    - not good for searching, no order
    - Are built by abstracting on top of an array
        - keys are run through a hashing function to convert it to an index number, then the value is placed into the corresponding index of an array of pre-determined length.
        - when the value is retrieved, the key is hashed again and the operation becomes a simple array index lookup O(1) operation
    - Hash Function: takes an input (in this case a string) and outputs a number
        - for a specific input, it must ALWAYS return the same output
'''
# Construct a class that builds a hash table dictionary instance
class Dict:

    def __init__(self, capacity=8):
        self.storage = [None] * capacity # initializes specified storage capacity of the array
        self.capacity = capacity # stores capacity as a variable
        self.item_count = 0 # keeps track of how many real items are in storage

    # Hashing Function: pass in a string (key) and the size of the array the values will be stored in
    def hash(self, string):
        # encode turns a string into its binary representation --> O(n) Time complexity
        bytes = string.encode()
        # transform out bytes representation of the string into a number
        sum = 0
        for byte in bytes: # --> O(n) Time complexity
            sum += byte
        return sum % self.capacity # by modulating the sum, the resulting integer will always be between 0 and the modulator (capacity defined upon instantiating the dictionary) ensuring a corresponding index in the array exists
    
    def load_factor(self):
        # calculate how full our storage array is
        return self.item_count / self.capacity

    def get(self, key):
        # use class method hash to hash the key to get an index
        index = self.hash(key)
        # store the array at this index as a variable
        array_at_index = self.storage[index]
        # check if the slot has anything in it
        if array_at_index is None:
            # the slot is empty, throw an error
            return
        # Find the correct key/value in our array_at_index
        for key_value in array_at_index:
            # if this is the key we want, return its value
            if key_value[0] == key:
                return key_value[1]
        # item not found, throw error
        return

    def insert(self, key, value):
        # use class method hash to hash the key to get an index
        index = self.hash(key)
        # store the array at this index as a variable
        array_at_index = self.storage[index]
        # check for a collision
        if array_at_index is not None:
            print('having a collision!!!', key)
            # first check if this key already exists in the array at this index
            for key_value in array_at_index:
                # item already exists, update its value
                if key_value[0] == key:
                    key_value[1] = value
                    return
            # append the key value array to the initialized array at this index if loop didn't return out
            array_at_index.append([key, value])
        else:
            # no collision--> use the hashed index derived from the key to set the index of our storage to a tuple containing the key name and the corresponding value
            # store the intial array inside an array that can be added to if a collision occurs in a later insertion
            self.storage[index] = [[key, value]]

        #increment the item count, if we get here the loop that replaces existing values hasn't returned us out of this function, therefore a new item has been added to storage
        self.item_count += 1
        # new item added, check if we need to re-size
        if self.load_factor() > 0.7:
            # re-size
            self.resize()

    # when resizing, elements will land at a different place in the container. The hashed index will almost always be different 
    def resize(self):
        print(f'need to resize, load factor is {self.load_factor()}')   
        # double the size of storage capacity
        # save our items to a new variable
        old_storage = self.storage
        # create a new storage array and update properties of the dictionary
        self.storage = [None] * len(old_storage) * 2
        self.capacity = len(self.storage)
        self.item_count = 0
        # for each item in the old storage, insert them again in the new storage
        for slot in old_storage:
            if slot is None:
                continue
            # loop through each slot, and insert each item found in old storage
            for key_value in slot:
                self.insert(key_value[0], key_value[1])
        print(f'new load factor is {self.load_factor()}')   

    def delete(self, key):
        # use class method hash to hash the key to get an index
        index = self.hash(key)
        # if there is an item at the hashed index, decrement count
        self.item_count -= 1
        # set the index derived from the hashed key back to None
        self.storage[index] = None

    # these dunder methods allow some default behavior expected of a python dictionary, i.e. square bracket notation to access the dict, curly brackets to instantiate one, and len to get count of items
    def __setitem__(self, key, value):
        return self.insert(key, value)
    def __getitem__(self, key):
        return self.get(key)
    def __len__(self):
        return self.item_count


food = Dict()

food.insert('apple', 'fruit')
food['banana'] = 'fruit'
food['cucumber'] = 'vegetable'
food['peach'] = 'not a banana'
food['pineapple'] = 'citrus'
print("storage array:", food.storage)
food['papaya'] = 'tropical'
print("resized storage array:", food.storage)

# print('apple value:', food['apple'])
# print('should be banana value, hash collision with peach:', food['banana'])
# print("Item count", food.item_count)