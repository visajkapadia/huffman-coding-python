start = None

class Node:

    def __init__(self, letter, probability):
        self.letter = letter
        self.probability = probability
        self.next = None


class LinkedList:

    LENGTH = 0

    def insertAtEnd(self, letter, probability):
        node = Node(letter, probability)
        global start

        self.LENGTH = self.LENGTH + 1
        ptr = start

        if ptr is None:
            start = node
            return
        else:
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = node

    def removeAtStart(self):
        global start

        self.LENGTH = self.LENGTH - 1

        if start is None:
            return

        ptr = start
        start = start.next
        return ptr

    def sortLinkedList(self):
        global start

        if start is None:
            return

        ptr = start
        while ptr.next is not None:
            nxt = ptr.next
            while nxt is not None:
                if ptr.probability > nxt.probability:
                    ptr.probability, nxt.probability = nxt.probability, ptr.probability
                    ptr.letter, nxt.letter = nxt.letter, ptr.letter
                nxt = nxt.next
            ptr = ptr.next

    def insertSorted(self, letter, probability):
        global start

        self.LENGTH = self.LENGTH + 1

        node = Node(letter, probability)

        if start is None:
            start = node
            return

        prev = start
        curr = prev.next

        if curr is None:
            prev.next = node
            return

        while curr.probability <= probability:
            curr = curr.next
            prev = prev.next
            if curr is None:
                break

        node.next = curr
        prev.next = node

    def printLinkedList(self):
        global start
        ptr = start

        while ptr is not None:
            print(ptr.letter, ptr.probability)
            ptr = ptr.next
        print()


linkedlist = LinkedList()
linkedlist.insertAtEnd('a', 0.20)
linkedlist.insertAtEnd('b', 0.20)
linkedlist.insertAtEnd('c', 0.15)
linkedlist.insertAtEnd('d', 0.15)
linkedlist.insertAtEnd('e', 0.15)
linkedlist.insertAtEnd('f', 0.10)
linkedlist.insertAtEnd('g', 0.05)

mydict = {"a" : "",
        "b" : "",
        "c" : "",
        "d" : "",
        "e" : "",
        "f" : "",
        "g" : ""}

linkedlist.sortLinkedList()

for i in range(1, linkedlist.LENGTH):
    x = linkedlist.removeAtStart()
    for character in x.letter:
        mydict[character] = "0" + mydict[character]
    y = linkedlist.removeAtStart()
    for character in y.letter:
        mydict[character] = "1" + mydict[character]
    linkedlist.insertSorted(x.letter + y.letter, x.probability + y.probability)


print("a :", mydict['a'])
print("b :", mydict['b'])
print("c :", mydict['c'])
print("d: ", mydict['d'])
print("e: ", mydict['e'])
print("f: ", mydict['f'])
print("g: ", mydict['g'])
