class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Appends a new node with the given value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, value):
        """Prepends a new node with the given value at the beginning of the list."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """Deletes the first node with the given value."""
        current = self.head
        # If the list is empty
        if not current:
            print("The list is empty.")
            return
        # If the node to be deleted is the head
        if current.value == value:
            self.head = current.next
            current = None
            return
        # Search for the node to delete
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        # If node wasn't found
        if not current:
            print(f"Value {value} not found in the list.")
            return
        # Remove the node
        prev.next = current.next
        current = None

    def delete_at_position(self, position):
        """Deletes a node at the given position."""
        if position < 0:
            print("Invalid position.")
            return
        current = self.head
        if position == 0 and current:
            self.head = current.next
            current = None
            return
        prev = None
        count = 0
        while current and count != position:
            prev = current
            current = current.next
            count += 1
        if not current:
            print(f"No node found at position {position}.")
            return
        prev.next = current.next
        current = None

    def search(self, value):
        """Searches for a node with the given value."""
        current = self.head
        while current:
            if current.value == value:
                print(f"Node with value {value} found.")
                return True
            current = current.next
        print(f"Node with value {value} not found.")
        return False

    def display(self):
        """Displays the entire linked list."""
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Original Linked List:")
    ll.display()

    ll.prepend(0)
    print("\nLinked List after prepending 0:")
    ll.display()

    ll.delete(3)
    print("\nLinked List after deleting value 3:")
    ll.display()

    ll.delete_at_position(2)
    print("\nLinked List after deleting node at position 2:")
    ll.display()

    ll.search(4)
    ll.search(10)

