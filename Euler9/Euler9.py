def find_triples():
    list = [1, 1, 1]
    for ii in range(1,1000):
        list[0] = ii
        for jj in range(1,1000):
            list[1] = jj
            for kk in range(1,1000):
                list[2] = kk
                if (list[0] ** 2 + list[1] ** 2 == list[2] ** 2) and list[0] + list[1] + list[2] == 1000:
                    print("The solution is: " + str(list))
                    print("And the product is: " + str((list[0]) * (list[1] * list[2])))
                    break

find_triples()
