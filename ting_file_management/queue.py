class Queue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        removed_value = self._data[0]
        del self._data[0]
        return removed_value

    def search(self, index):
        list_size = len(self._data)
        if index in range(list_size):
            return self._data[index]
        else:
            raise IndexError("Invalid index")

