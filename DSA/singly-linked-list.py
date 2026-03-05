class SinglyLinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)
d = SinglyLinkedListNode(4)

Head.next = b
b.next = c
c.next = d

def showLinkedlList(head):
    current = head
    while current:
        print(current.val)
        current = current.next

showLinkedlList(Head)

def display(head):
    current = head
    elements = []

    while current:
      elements.append(str(current.val))
      current = current.next
    print(' -> '.join(elements))

display(Head)

def search(head, value):
    current = head
    while current:
        if current.val == value:
            return True
        current = current.next
    return False
print(search(Head, 3))