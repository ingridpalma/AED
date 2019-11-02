class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1


class BinomialHeap:
    def __init__(self):
        self.trees = []

    def extract_min(self):
        if self.trees == []:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)

        return smallest_node.key

    def get_min(self):
        if self.trees == []:
            return None
        least = self.trees[0].key
        for tree in self.trees:
            if tree.key < least:
                least = tree.key
        return least

    def combine_roots(self, h):
        self.trees.extend(h.trees)
        self.trees.sort(key=lambda tree: tree.order)

    def merge(self, h):
        self.combine_roots(h)
        if self.trees == []:
            return
        i = 0
        while i < len(self.trees) - 1:
            current = self.trees[i]
            after = self.trees[i + 1]
            if current.order == after.order:
                if (i + 1 < len(self.trees) - 1
                        and self.trees[i + 2].order == after.order):
                    after_after = self.trees[i + 2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i + 1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i = i + 1

    def insert(self, key):
        g = BinomialHeap()
        g.trees.append(BinomialTree(key))
        self.merge(g)

    def push(self, item):
        self.insert(item)

    def pop(self):
        return self.extract_min()



if __name__ == "__main__":

    myheap = BinomialHeap()

    """ myheap.push(5)
    print(myheap.get_min())
    myheap.push(3)
    print(myheap.get_min())
    myheap.push(1)
    print(myheap.get_min())
    print(myheap.pop())
    print(myheap.get_min()) 
    """


    myheap.push("{'device_id': 9, 'id': '6fb1c8b0-ded1-460f-b582-eedb45ff1b13', 'ts': 1572732196.217073, 'value': 25}")
    print(myheap.get_min())

    myheap.push("{'device_id': 5, 'id': '2a3bbe23-0f72-429d-a886-b13e4b1223c5', 'ts': 1572732196.2146401, 'value': 21}")
    print(myheap.get_min())

    myheap.push("{'device_id': 1, 'id': 'f875048d-0301-432f-a600-055f5c72facd', 'ts': 1572732196.211217, 'value': 63}")
    print(myheap.get_min())

    print(myheap.pop())

    print(myheap.get_min())


