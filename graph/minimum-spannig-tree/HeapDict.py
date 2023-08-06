# TO DO: optimize implementation later
import heapq

class Node:
    def __init__(self, key, value) -> None:
        self.data = (key, value)
    def to_list(self):
        return (self.data[0], self.data[1])
    def __lt__(self, Node):
        return self.data[1] < Node.data[1]

class HeapDict:
    def __init__(self, d) -> None:
        l = [Node(k,v) for k,v in d.items()]
        heapq.heapify(l)
        self.data = l
    def pop(self):
        node = heapq.heappop(self.data)
        return node.to_list()
    def update(self, k, v):
        l = ([Node(k,v) if node.to_list()[0] == k else node for node in self.data])
        heapq.heapify(l)
        self.data = l
    def get(self, k):
        return self.__str__()
    def __str__(self):
        return f'{[ "key: {key}, value: {value}".format(key = node.to_list()[0], value =  node.to_list()[1]) for node in self.data]}'
    def __repr__(self) -> str:
        return self.__str__()
