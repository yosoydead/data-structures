from linkedList import MyLinkedList

def main():
    ll = MyLinkedList()
    ll.addAtTheEndOfTheList("radu")
    ll.addAtTheEndOfTheList("bogdan")
    ll.addAtTheEndOfTheList("mircea")
    ll.addAtTheEndOfTheList("bla")
    ll.addAtTheEndOfTheList("bla")
    ll.addAtTheEndOfTheList("another radu")
    # print("head", ll.head.data)
    # print("tail",ll.tail.data)
    # ll.addAtTheStartOfTheList("radu")
    # ll.addAtTheStartOfTheList("bogdan")
    # ll.addAtTheStartOfTheList("mircea")
    # ll.addAtTheStartOfTheList("bla")
    # print("head", ll.head.data)
    # print("tail",ll.tail.data)
    print("size of the list", ll.size())
    print("head:",ll.seeHeadItem())
    print("tail:",ll.seeTailItem())
    ll.iterateThroughTheList()
    ll.removeTheHeadItem()
    ll.removeTheTailItem()
    print("head:",ll.seeHeadItem())
    print("tail:",ll.seeTailItem())
    ll.addAtTheEndOfTheList("test")
    ll.iterateThroughTheList()
    print("get function at index 4", ll.get(4).data)
    print("set function at index 3", ll.set(3, "new value added"))
    ll.iterateThroughTheList()
    #ll.iter()
    #print("new tail", ll.seeTailItem())

if __name__ == "__main__":
    main()