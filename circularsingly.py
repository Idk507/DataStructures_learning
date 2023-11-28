'''Circular singly linkedlist where the last node points to the first node '''

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
class circularsinglylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.data)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            result += '->'
        return result
    
    def append(self,value):
        newnode = node(value)
        if self.length == 0:
            self.head =newnode
            self.tail = newnode
            newnode.next = self.head
        else:
            self.tail.next =newnode
            self.tail = newnode
            newnode.next = self.head
        self.length +=1
    
    def prepend(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            newnode.next = self.head
            self.head = newnode
            self.tail.next = self.head
        self.length+=1
    
    def insert_pos(self,pos,data):
        newnode = node(data)
        if pos == 0:
            if self.length == 0:
                self.head = newnode
                self.tail = newnode
                newnode.next = newnode
            else:
                newnode.next = self.head
                self.head = newnode
                self.tail.next = self.head
        elif pos >=self.length:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head  
        else:   
            temp = self.head
            for _ in range(pos-1):
               temp = temp.next
               newnode.next = temp.next
               temp.next = newnode
        self.length+=1
    def traverse(self):
        current = self.head 
        while current is not None:
            print(current.data)
            current = current.next
            if current.next == self.head:
                break
    def search(self,data): 
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
            if temp.next == self.head:
                break
        return False
    
    def get(self,index):
        temp = self.head
        if index < -1 or index >=self.length:
            return None 
        elif index ==-1:
            return self.tail.data
        for _ in range(index):
            temp = temp.next
        return temp.data
    def set(self,index,data):
        temp = self.get(index)
        if temp :
            temp.data = data
            return True
        return False
    def popfirst(self):
        if self.length == 0:
            return None
        elif self.length ==1:
            self.head = None
            self.tail =None 
            self.length -=1
            return self.head
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            temp.next = None
            self.length -=1
            return temp.data
    def poplast(self):
        if self.length ==1:
            self.head = None
            self.tail = None
            self.length -=1
            return self.tail
        else:
           pop_node = self.tail
           temp = self.head
           while temp.next is not self.tail:
               temp = temp.next
            temp.next = self.head
            self.tail = temp
            pop_node.next = None
            self.length -=1
            return pop_node.data 
    def remove(self,index):
        if index <0 or index >= self.length:
            return None
        elif index == 0:
            return self.popfirst()
        elif index ==  self.length -1:
            return self.poplast()
        prev = self.get(index-1)
        popped_node = prev.next
        prev.next = popped_node.next
        popped_node.next = None
        self.length -=1
        return popped_node.data
    def delete(self):
          self.tail.next = None
          self.head = None
          self.tail = None
          self.length = 0 
        

cl = circularsinglylinkedlist()
cl.append(20)
cl.append(30)
cl.prepend(5)
cl.insert_pos(2,40)
print(cl)
        
        