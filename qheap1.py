class HeapManager:
    def __init__(self):
        self.heap = None
        self.end_of_queue = None

    def find_min(self):
        return self.end_of_queue.value

    def add_value(self, data):
        if self.heap is None:
            self.heap = Node(data, None)
            self.end_of_queue = self.heap
        elif self.heap.value < data:
            temp = Node(data, None)
            self.heap.father = temp
            temp.son = self.heap
            self.heap = temp
        else:
            min_node = self.heap.add_value(data)
            if min_node is not None:
                self.end_of_queue = min_node

    def remove_value(self, data):
        if self.heap.value == data:
            self.heap = self.heap.son
        else:
            min_node = self.heap.remove_value(data)
            if min_node is not None:
                self.end_of_queue = min_node


class Node:

    def __init__(self, data, father):
        self.value = data
        self.father = father
        self.son = None

    def add_value(self, data):
        if data < self.value:
            if self.son is None:
                self.son = Node(data, self)
                return self.son
            else:
                return self.son.add_value(data)
        else:
            temp = Node(data, self.father)
            self.father.son = temp
            self.father.son.son = self
            self.father = temp
            return None

    def remove_value(self, data):
        if data == self.value:
            self.father.son = self.son
            if self.son is not None:
                self.son.father = self.father
                return None
            else:
                return self.father
        else:
            return self.son.remove_value(data)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


hm = HeapManager()
hm.add_value(3)
hm.add_value(65)
hm.remove_value(65)
assert hm.find_min() == 3
hm.remove_value(3)
hm.add_value(7)
assert hm.find_min() == 7
hm.add_value(-1)
assert hm.find_min() == -1
hm.remove_value(-1)
assert hm.find_min() == 7

print(hm.find_min())
print("GOOD!")

# 1 10
# 1 9
# 3
# 1 3
# 3
# 2 9
# 3
# 2 3
# 3
# 1 5
# 1 2
# 3


# 9
# 3
# 3
# 10
# 2
hm = HeapManager()
hm.add_value(10)
hm.add_value(9)
assert hm.find_min() == 9
hm.add_value(3)
assert hm.find_min() == 3
hm.remove_value(9)
assert hm.find_min() == 3
hm.remove_value(3)
assert hm.find_min() == 10
hm.add_value(5)
hm.add_value(2)
assert hm.find_min() == 2

print(hm.find_min())
print("GOOD AGAIN!")

