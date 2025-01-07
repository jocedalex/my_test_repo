# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleEndedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            raise Exception("Queue is empty")
        popped_node = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return popped_node.data

    def pop_right(self):
        if self.tail is None:
            raise Exception("Queue is empty")
        popped_node = self.tail
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return popped_node.data

    def print_queue(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        
        print()

# Example usage
deque = DoubleEndedQueue()
deque.push_left("Hola")
deque.push_right("Mundo")
deque.push_right("Mundo2")
deque.push_right("Mundo3")
deque.print_queue()  # Hola <-> Mundo <-> None
print("Popped left:", deque.pop_left())  # Hola
deque.print_queue()  # Mundo <-> None
print("Popped right:", deque.pop_right())  # Mundo
deque.print_queue()  # None