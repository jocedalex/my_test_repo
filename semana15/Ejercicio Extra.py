class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node 

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    @property
    def size(self):
        current_node = self.head
        size = 0

        while (current_node is not None):
            size += 1
            current_node = current_node.next

        return size



    def bubble(self):
        current_node = self.head
        n = self.size

        for i in range(n-1):
            current_node = self.head
            changes=False

            while (current_node.next is not None):

                if current_node.data > current_node.next.data:
                    
                    current_node.data, current_node.next.data = current_node.next.data, current_node.data
                    
                    changes=True

                current_node = current_node.next

            if not changes:
                break

                


third_node = Node(5)
second_node = Node(7, third_node)
first_node = Node(10, second_node)

linked_list = LinkedList(first_node)
linked_list.head = Node(4, linked_list.head)
linked_list.head = Node(3, linked_list.head)
linked_list.print_structure()

linked_list.bubble()
linked_list.print_structure()

