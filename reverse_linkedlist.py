class Node:
  def __init__(self,val):
    self.val = val
    self.next = None

def reverse(ll):
  head = ll
  p = ll
  q = ll.next
  while(head != None):
    head = q.next
    q.next = p
    p = q
    q = head
  ll.next = None
  ll = p
  return ll
  

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)
node4 = Node(45)
node1.next = node2
node2.next = node3
node3.next = node4
