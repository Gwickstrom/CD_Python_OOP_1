class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def PrintAllVals(self):
        current = list.head
        while(current != None):
            print(current.value)
            current = current.next
    def AddBack(self,value):

        if not self.tail:
          self.tail=Node(value)
          self.head=self.tail
        else:
          self.tail.next = Node(value)
          self.tail = self.tail.next

    # def AddFront(self,val):

    # def InsertBefore(self,nextVal,val):

    # def InsertAfter(self, preval, val):

    # def RemoveNode(self,val):

    # def ReverseList(self):

list = SinglyLinkedList()
list.head = Node('Alice')
list.head.next = Node('Chad')
list.head.next.next = Node('Debra')
list.tail = Node('Greg')



list.AddBack("Greg")
list.PrintAllVals()
