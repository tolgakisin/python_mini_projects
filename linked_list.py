class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.root
        self.root = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.root is None:
            self.root = new_node
            return

        last = self.root
        while (last.next):
            last = last.next
        last.next = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Previous Node boş durumda")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, key):
        temp = self.root
        if temp is not None:
            if (temp.data == key):
                self.root = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def search(self, aranan):
        current = self.root

        while current != None:
            if current.data == aranan:
                return True
            current = current.next
        return False

    def printlist(self):
        temp = self.root
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(5)
    llist.push(4)
    llist.append(7)
    llist.printlist()
    print("new list:")
    llist.insertAfter(llist.root.next.next, 8)
    llist.printlist()
    llist.deleteNode(7)
    print("new list:")
    llist.printlist()

    x = int(input("aramak istediğiniz değeri giriniz"))
    if llist.search(x):
        print(x, "bulundu")
    else:
        print("Bulunamadı")
