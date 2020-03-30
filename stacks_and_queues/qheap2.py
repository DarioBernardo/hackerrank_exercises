"""
This question is designed to help you get a better understanding of basic heap operations.
You will be given queries of  types:

"1 v" - Add an element  to the heap.
"2 v" - Delete the element  from the heap.
"3" - Print the minimum of all the elements in the heap.
"""


class Heap:
    def __init__(self):
        self.q = []
        self.last_elem = 0

    def __heapify_down(self, index: int):
        children_index = self.__get_children_index(index)
        if len(children_index) == 0:
            return

        for child_index in children_index:
            if self.q[child_index] < self.q[index]:
                self.__swap(index, child_index)
                self.__heapify_down(child_index)

    def __heapify_up(self, index):
        if len(self.q) <= 1:
            return

        if index == 0:
            return

        parent_index = self.__get_parent_index(index)
        if self.q[parent_index] > self.q[index]:
            self.__swap(index, parent_index)
            self.__heapify_up(parent_index)

    def __get_children_index(self, index):
        c1 = 2 * index + 1
        c2 = c1 + 1
        c = []
        if c1 < len(self.q):
            c.append(c1)
        if c2 < len(self.q):
            c.append(c2)
        return c

    def __get_parent_index(self, index):
        if index == 1:
            return 0
        parent = int((index - 1) / 2)
        return parent

    def add(self, value):
        self.q.append(value)
        self.__heapify_up(len(self.q)-1)

    def remove(self, value):
        remove_index = self.q.index(value)
        if remove_index == len(self.q)-1:
            self.q.pop(len(self.q) - 1)
            return

        last_elem = self.q.pop(len(self.q)-1)
        self.q[remove_index] = last_elem
        self.__heapify_down(remove_index)

    def find_min(self):
        return self.q[0]

    def __swap(self, index, child_index):
        parent = self.q[index]
        self.q[index] = self.q[child_index]
        self.q[child_index] = parent


hm = Heap()

hm.add(3)
hm.add(65)
hm.remove(65)
assert hm.find_min() == 3
hm.remove(3)
hm.add(7)
assert hm.find_min() == 7
hm.add(-1)
assert hm.find_min() == -1
hm.remove(-1)
assert hm.find_min() == 7
print(hm.find_min())
print("GOOD!")


hm = Heap()
hm.add(10)
hm.add(9)
assert hm.find_min() == 9
hm.add(3)
assert hm.find_min() == 3
hm.remove(9)
assert hm.find_min() == 3
hm.remove(3)
assert hm.find_min() == 10
hm.add(5)
hm.add(2)
assert hm.find_min() == 2

print(hm.find_min())
print("GOOD AGAIN!")


hm = Heap()
hm.add(10)
hm.add(9)
hm.add(6)
hm.add(8)
hm.add(7)
hm.add(11)
hm.add(110)
hm.add(1)
assert hm.find_min() == 1
hm.add(-3)
assert hm.find_min() == -3
hm.remove(-3)
hm.remove(1)
assert hm.find_min() == 6
hm.remove(11)
assert hm.find_min() == 6
hm.add(5)
hm.add(2)
assert hm.find_min() == 2
hm.remove(2)
assert hm.find_min() == 5
hm.remove(110)
assert hm.find_min() == 5
hm.remove(5)
assert hm.find_min() == 6

print(hm.find_min())
print("GOOD AGAIN!")