def exercise1():
    array = [1, 2, 3, 4]
    print(array[1])

#exercise1()

def exercise2():
    array = ["A", 2, "B", 4]
    print(array[3])

#exercise2()

def exercise3():
    array = [[1], [2,3], [4]]
    print(array[2])

#exercise3()

def exercise4():
    array = [[1], [2,3], [4]]
    for i in array:
        print(array[i])

#exercise4()

def exercise5():
    array = ["A", "B", "C", "D"]
    for i in range(len(array)):
        print(i)

#exercise5()

def exercise6():
    array = [1, "B", 4, "D"]
    for i in range(len(array)):
        if isinstance(array[i], int):
            print(i)

#exercise6()

def exercise7():
    array = [1, "B", 4, "D"]
    for i in range(len(array)):
        if isinstance(i, int):
            print(i)

#exercise7()

def exercise8():
    array = [[1, "B", 4, "D"], [1,2], [3,4,5]]
    for i in array:
        print(len(i))

#exercise8()

def exercise9():
    array = [3]
    array.append(4)
    array.append(7)
    array.append([1,2,3])
    print(array)

#exercise9()

def exercise10():
    array = [1,2,3,4]
    array2 = [4,5,6,7]

    for i in array:
        if i <3:
            print(i)
    for i in array2:
        if i >5 :
            print(i)
exercise10()