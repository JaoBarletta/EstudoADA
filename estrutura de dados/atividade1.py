class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_List :
    def __init__ (self):
        self.head = None

    def append (self,data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node = new_node
        return
    
    def lenght(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0

        while current_node :
            total +=1
            current_node.next

            return total
        
    def to_list(self):
        node_data=[]
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data
    
    def display(self):
        contents = self.head

        if contents is None:
            print("List has no element")

        while contents:
            print(contents.data)

            contents = contents.next
        print("-"*10)

    def reverse_linkedlist(self):
        previus_node = None
        current_node = self.head
        while current_node != None:
            next = current_node.next
            current_node = previus_node
            previus_node = current_node
            current_node = next
        self.head = previus_node


#teste 

my_list = Linked_List()
my_list.display()
my_list.append(3)
my_list.append(7)
my_list.append(2)
my_list.append(1)

my_list.display()
