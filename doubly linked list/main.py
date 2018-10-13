from lst import DoublyLinkedList

def main():
    x = DoublyLinkedList()

    x.addToLast(4)
    print("head", x.head.data, "tail", x.tail.data)
    x.addToLast(5)
    print("head", x.head.data, "tail", x.tail.data)
    x.addToLast(6)
    print("head", x.head.data, "tail", x.tail.data)
    x.addToStart("Radu")
    print("head", x.head.data, "tail", x.tail.data)
    x.addToStart("Bogdan")
    print("head", x.head.data, "tail", x.tail.data)

    # x.addToStart("Radu")
    # print("head", x.head.data, "tail", x.tail.data)
    # x.addToStart("Bogdan")
    # print("head", x.head.data, "tail", x.tail.data)
    # x.addToStart("Mircea")
    # print("head", x.head.data, "tail", x.tail.data)

    x.iteratefromTail()


if __name__ == '__main__':
    main()