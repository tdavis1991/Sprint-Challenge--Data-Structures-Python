class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
    

class LinkedList:
  def __init__(self):
    self.head = None  
    self.tail = None
  
  def add_to_head(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next_node = self.head
      self.head = new_node

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
    head_value = self.head.value
    self.head = self.head.next_node
    return head_value 

  def contains(self, value):
    if self.head is None:
      return False
    
    current_node = self.head

    while current_node is not None:
      if current_node.value == value:
        return True

      current_node = current_node.next_node
    return False 

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.curr = None
        self.storage = LinkedList()
        self.length = 0

    def append(self, item):
        
        if self.length < self.capacity:
            self.length += 1
            self.storage.add_to_tail(item)
        else:
            if self.curr is None or self.curr.next_node is None:
                self.curr = self.storage.head
            else:
                self.curr = self.storage.head.next_node
            self.curr.value = item
        

    def get(self):
        values = []
        curr = self.storage.head
        while curr != None:
            values.append(curr.value)
            curr = curr.next_node
        return values

new_buffer = RingBuffer(5)
new_buffer.append('a')
print(new_buffer.get())