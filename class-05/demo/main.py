from linkedlist import LinkedList

if __name__ == "__main__":

    linked_list1 = LinkedList()

    linked_list1.append("A")
    linked_list1.append("B")
    linked_list1.append("C")
    linked_list1.append("D")

    print(linked_list1)

    linked_list1.delete_node("E")

    print(linked_list1)
