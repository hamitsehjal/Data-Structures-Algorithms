class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in list
    """
    data=None
    next_node=None
    
    def __init__(self,data):
        self.data=data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data 
        

class LinkedList:
    """
    Singly Linked List
    """
    head=None
    
    def __init__(self):
        self.head=None
        
    def is_empty(self):
        return self.head==None
        
    def size(self):
        """
        Returns the number of nodes in the list
        Takes 0(n) time
        """
        current=self.head
        count=0
        # while current!=None: is same as while current:
        while current:
            count+=1
            current=current.next_node
            
        return count
        
    def add(self,data):
        """
        ADDs a new Node containing data at the head of the list
        Takes 0(1) time
        """
        new_node=Node(data)
        new_node.next_node=self.head
        self.head=new_node
    
    def search(self,key):
        """
        Search for the first Node containing data that matches the key
        Returns the node or returns 'None' if not found
        
        Takes O(n) time
        """
        
        current=self.head
        
        while current:
            if current.data==key:
                return current
            else:
                current=current.next_node
        return None

    # Insert operation
    def insert(self,data,index):

        """
        Insert operation inserts a new node at index position
        Inserting at a specific index is a constant time operation O(1), however
        finding the right index where we want to insert the new node take linear time O(n).

        Therefore, overall Insert operation is a linear time operatin O(n).

        """
        if index==0:
            self.add(data)

        if index > 0:
            new_node=Node(data)
            current=self.head
            position=index

            while position>1:
                position-=1
                current=current.next_node

            prev_node=current
            next_node=current.next_node

            prev_node.next_node=new_node
            new_node.next_node=next_node

    #Implementing remove operation
    def remove(self,key):
        """
        Removes Node containing data that matches the key
        Returns the Node or None if doesn't exist!!
        
        Takes linear time O(n)
        """
        Found=False
        previous=None
        current=self.head

        while current and not Found:
            if(current.data == key and current is self.head):
                Found=True
                self.head=current.next_node
            elif current.data==key:
                Found=True
                previous.next_node=current.next_node
            else:
                previous=current
                current=current.next_node

        return current

    def __repr__(self):
        
        nodes=[]
        current=self.head
        
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
                
            current=current.next_node
            
        return '->'.join(nodes)