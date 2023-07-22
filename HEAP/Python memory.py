def simulate_shortest_path():
    list1 = [1, 2, 3]
    condition = False
    queue = [list1]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        new_path = path  # list(path) # path
        new_path.append(4)

        if not condition:
            queue.append(new_path)


if __name__ == "__main__":
    a = 2
    b = 2
    c = int(2)
    print(id(a), id(b), id(c))

    list1 = [1, 2, 3]

    list2 = list1

    list2.append(4)
    print(f"list1:{list1}-> id:{id(list1)}\nlist2:{list2}-> id:{id(list2)}")
    print("--------------------------------------------------------------")
    list3 = list(list1)
    list3.append(5)
    print(f"list1:{list1}   -> id:{id(list1)}\nlist3:{list3}-> id:{id(list3)}")
