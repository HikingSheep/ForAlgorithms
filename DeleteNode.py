class Node(object):
  def __init__(self, value):
      print( "Just created a totally new node with a value of", value )
      self.value=value
      self.next=None
      self.prev=None

class List(object):
  def __init__(self):
      self.head=None
      self.tail=None
      
  def insert(self,n,x):
      #Not actually perfect: how do we prepend to an existing list?
      if n!=None:
          x.next=n.next
          n.next=x
          x.prev=n
          if x.next!=None:
              x.next.prev=x              
      if self.head==None:
          self.head=self.tail=x
          x.prev=x.next=None
      elif self.tail==n:
          self.tail=x
          
  def display(self):
      values=[]
      n=self.head
      while n!=None:
          values.append(str(n.value))
          n=n.next
          print ("List:",values)


  def delete(self,n):
##      if n == self.head:
##          n.next = n.next.next
##          n.prev = None
##      if n == self.tail:
##          n.next = None   
##          n.prev.prev = n.prev
##      else:

        if n.prev != None:
          n.prev.next = n.next
        else:
          l.head = n.next;

        if n.next != None:
          n.next.prev = n.prev
        else:
          l.tail = n.prev;
          

      

if __name__ == '__main__':
  l=List()
  l.insert(None, Node(4))
  m = Node(8)
  l.insert(l.head,Node(6))
  l.insert(l.head,m)
  l.display()


