
# 1. Cree una estructura de objetos que asemeje un Stack.
#     1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como
# `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.top is None:
            print("No stacks")
            return None
        removed_value = self.top.value
        self.top = self.top.next
        return removed_value
    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next
        print("-----")
        
stack = Stack()
stack.push("first stack")
stack.push("second stack")
stack.push("third stack")
stack.print_stack()  

stack.pop()
print("-----")
stack.print_stack()  
        
        
# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#     1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#     2. Debe incluir un método para hacer `print` de toda la estructura.
#     3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Queue:
    def __init__(self):
        self.head = None  
        self.tail = None
        
    def push_left(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
            
    def push_right(self, value):
        new_node = Node(value)
        if self.tail is None:  
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node 
    def pop_left(self):
        if self.head is None:
            print("empty queue.")
            return None
        removed_value = self.head.value
        self.head = self.head.next  
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  
        return removed_value
    
    def pop_right(self):
        if self.tail is None:
            print("empty queue.")
            return None
        removed_value = self.tail.value
        self.tail = self.tail.prev  
        if self.tail:
            self.tail.next = None
        else:
            self.head = None  
        return removed_value

    def print_queue(self):
        current = self.head
        while current:
            print(current.value) 
            current = current.next
        print("---")  
        
queue = Queue()

queue.push_left("Left 1")
queue.push_right("Right 1")
queue.push_left("Left 2")
queue.push_right("Right 2")

queue.print_queue()

queue.pop_left() 
queue.pop_right()

queue.print_queue()


# 3. Cree una estructura de objetos que asemeje un Binary Tree.
#     1. Debe incluir un método para hacer `print` de toda la estructura.
#     2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursively(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursively(current.right, value)
                
    def print_tree(self):
        self._print_recursively(self.root)

    def _print_recursively(self, current):
        if current:
            self._print_recursively(current.left)
            print(current.value)  
            self._print_recursively(current.right)  
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(20)

tree.print_tree()