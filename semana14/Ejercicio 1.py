class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            raise Exception("Stack is empty")
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def print_stack(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# Example usage
stack = Stack()
stack.push("Hola")
stack.push("Mundo")
stack.print_stack()  # Mundo -> Hola
print("Popped:", stack.pop())  # Mundo
stack.print_stack()  # Hola