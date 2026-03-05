class DoublyNode:
  def __init__(self, value, next=None, prev= None):
    self.value = value
    self.next = next
    self.prev=prev

  def __str__(self):
    return str(self.value)
  

head = tail = DoublyNode(1)

def display(head):
  current = head
  elements = []

  while current:
    elements.append(str(current.value))
    current = current.next
  print(' <-> '.join(elements))


def insertAtHead(head, tail, value):
  new_node = DoublyNode(value,next=head)
  head.prev = new_node
  return new_node, tail

head, tail = insertAtHead(head, tail, 3)
display(head)

def insertAtTail(head, tail, value):
  new_node = DoublyNode(value, prev=tail)
  tail.next = new_node
  return head, new_node

head, tail = insertAtTail(head, tail, 4)
display(head)