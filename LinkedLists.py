class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class  LinkedList:
    def __init__(self):
        self.head = None


    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(prev_node, new_data):

        if prev_node is None:
            print("Error")

            new_node = Node(new_data)

            new_node.next = prev_node

            prev_node.next = new_node



    def append(self, new_data):...



a = Node(7)
b = Node(11)
c = Node(13)
d = Node(8)
f = Node(9)


l_list = LinkedList()
l_list.head = a
a.next = b
b.next = c
c.next = d
c.next = f
print(l_list.printList())


a.next = b
b.next = c
d.next = c
c.next = f
#print(l_list.printList())


a.next = c
b.next = c
d.next = c
c.next = f
#print(l_list.printList())


a.next = b
b.next = c
c.next = f
d.next = f
#rint(l_list.printList())


a.next = b
b.next = d
c.next = c
d.next = f
#print(l_list.printList())


l_list.push(23), l_list.push(43), l_list.push(45), l_list.push(51), l_list.push(53)

#print(f"the next case: {l_list.printList}()")

l_list.append(123), l_list.append(124), l_list.append(221), l_list.append(234), l_list.append(241)

#print(f"added new information: {l_list.printList()}")

insert(11, 483), insert(55, 311)
insert(77, 183), insert(333, 422)

#print(l_list.printList())