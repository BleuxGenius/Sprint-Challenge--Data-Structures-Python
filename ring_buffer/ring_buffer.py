class RingBuffer:
    def __init__(self, capacity):
        self.size = 0 
        self.storage = []
        self.capacity = capacity
        self.oldest = 0

# adds the item to the buffer
    def append(self, item):
        # check if size is less than capacity
        if self.size < self.capacity:
            # if size is less than capacity, append item to buffer and increase the size by 1
            self.storage.append(item)
            self.size += 1 
            # when size of buffer reaches capacity , overwrite elements oldest index
        elif self.size == self.capacity:
            # once overwritten the element in the oldest index increase oldest by 1 and is now 1 to place over to the right 
                self.storage[self.oldest] = item
                self.oldest += 1 
                # once self.oldest reaches capacity, oldest element is now in the index 0. and i must reset the tracker 
                if self.oldest == self.capacity:
                    self.oldest = 0

    def get(self):
        # returns the present state of the ring buffer list 
        print(self.storage)
        return self.storage
