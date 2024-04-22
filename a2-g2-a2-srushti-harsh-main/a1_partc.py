# Copy over your a1_partc.py file here
#    Main Author(s): Srushti Patel
#    Main Reviewer(s): Harsh Patel


class Stack:
    def __init__(self, cap=10):
        self.data = [None] * cap
        self.top = -1

    def capacity(self):
        return len(self.data)

    def push(self, data):
        self.top += 1
        if self.top == len(self.data):
            self.data += [None] * len(self.data)
        self.data[self.top] = data

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        value = self.data[self.top]
        self.top -= 1
        return value

    def get_top(self):
        if self.is_empty():
            return None
        return self.data[self.top]

    def is_empty(self):
        return self.top == -1

    def __len__(self):
        return self.top + 1


class Queue:
    def __init__(self, cap=10):
        self.data = [None] * cap
        self.front = 0
        self.size = 0

    def capacity(self):
        return len(self.data)

    def enqueue(self, data):
        if self.size == len(self.data):
            self._resize()
        back = (self.front + self.size) % len(self.data)
        self.data[back] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        value = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def get_front(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def _resize(self):
        new_capacity = 2 * len(self.data)
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % len(self.data)]
        self.data = new_data
        self.front = 0


class Deque:
    def __init__(self, cap=10):
        self.data = [None] * cap
        self.front = 0
        self.size = 0

    def capacity(self):
        return len(self.data)

    def push_front(self, data):
        if self.size == len(self.data):
            self._resize()
        self.front = (self.front - 1) % len(self.data)
        self.data[self.front] = data
        self.size += 1

    def push_back(self, data):
        if self.size == len(self.data):
            self._resize()
        back = (self.front + self.size) % len(self.data)
        self.data[back] = data
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        value = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return value

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        back = (self.front + self.size - 1) % len(self.data)
        value = self.data[back]
        self.size -= 1
        return value

    def get_front(self):
        if self.is_empty():
            return None
        return self.data[self.front]

    def get_back(self):
        if self.is_empty():
            return None
        back = (self.front + self.size - 1) % len(self.data)
        return self.data[back]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        if k < 0 or k >= self.size:
            raise IndexError('Index out of range')
        return self.data[(self.front + k) % len(self.data)]
    
    def _resize(self):
        new_capacity = 2 * len(self.data)
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % len(self.data)]
        self.data = new_data
        self.front = 0