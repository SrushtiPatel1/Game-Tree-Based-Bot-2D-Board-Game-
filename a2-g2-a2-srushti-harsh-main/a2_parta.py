#    Main Author(s): Harsh Patel
#    Main Reviewer(s): Srushti Patel

class HashTable:
    """
    A class representing a hash table.

    Attributes:
    - cap (int): The capacity of the hash table.
    - myTable (dict): The dictionary representing the hash table.
    """

    def __init__(self, cap=32):
        """
        Initializes a new instance of the HashTable class.

        Parameters:
        - cap (int): The capacity of the hash table.
        """
        self.cap = cap
        self.myTable = {}

    def insert(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        Parameters:
        - key: The key of the pair.
        - value: The value associated with the key.

        Returns:
        - True if the insertion is successful, False if the key already exists in the hash table.
        """
        if key in self.myTable:
            return False
        else:
            self.myTable[key] = value
            if len(self.myTable) / self.cap > 0.7:
                self.cap *= 2
            return True

    def modify(self, key, value):
        """
        Modifies the value associated with a given key in the hash table.

        Parameters:
        - key: The key of the pair.
        - value: The new value to be associated with the key.

        Returns:
        - True if the modification is successful, False if the key does not exist in the hash table.
        """
        if key in self.myTable:
            self.myTable[key] = value
            return True
        else:
            return False

    def remove(self, key):
        """
        Removes a key-value pair from the hash table.

        Parameters:
        - key: The key of the pair.

        Returns:
        - True if the removal is successful, False if the key does not exist in the hash table.
        """
        if key in self.myTable:
            del self.myTable[key]
            return True
        else:
            return False

    def search(self, key):
        """
        Searches for a value associated with a given key in the hash table.

        Parameters:
        - key: The key to search for.

        Returns:
        - The value associated with the key if found, None if the key does not exist in the hash table.
        """
        return self.myTable.get(key)

    def capacity(self):
        """
        Returns the capacity of the hash table.

        Returns:
        - The capacity of the hash table.
        """
        return self.cap

    def __len__(self):
        """
        Returns the number of elements in the hash table.

        Returns:
        - The number of elements in the hash table.
        """
        return len(self.myTable)
