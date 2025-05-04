class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first_node = Node(30)
second_node = Node(40)
third_node = Node(50)
fourth_node = Node(60)

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

head = first_node
current = head
while current is not None:
    print(current.data, end="->" )
    current = current.next

print("None")



def reverse_linked_list(head):
    current_node = head
    previous = None
    while current_node:
        next_node = current_node.next
        current_node.next = previous
        previous = current_node
        current_node = next_node

    head = previous
    current_node = head
    while current_node is not None:
        print(current_node.data, end="->")
        current_node =current_node.next
    print("None")


reverse_linked_list(head)
