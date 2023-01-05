def exercise1(data,n):
    for value in data:
       if n == value:
           return True
    return False
# print(exercise1([1, 5, 8, 3], 3))
# print(exercise1([5, 8, 3], -1))


def exercise2(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum
# print(exercise2(2, 1, 2))
# print(exercise2(3, 2, 2))
# print(exercise2(2, 2, 2))
# print(exercise2(1, 2, 3))

def exercise3(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

# print(exercise3(10, 6))
# print(exercise3(10, 2))
# print(exercise3(10, 12))

def exercise4(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
#print(exercise([1,2,-8]))


def exercise5(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
#print(exercise5([1,2,-8]))


def exercise6(list):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
#print(exercise6([1, 2, -8, 0]))

def exercise7(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

#print(exercise7(['abc', 'xyz', 'aba', '1221']))

#Set() list does not allow duplicate values.
def exercise8():
    a = [10,20,30,20,10,50,60,40,80,50,40]

    dup_items = set()
    uniq_items = []
    for x in a:
        uniq_items.append(x)
        dup_items.add(x)

    print(dup_items)
#exercise8()

def exercise9():
    original_list = [10, 22, 44, 23, 4]
    new_list = list(original_list)
    print(original_list)
    print(new_list)

#exercise9()

def exercise10(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
    return result
    

#print(exercise10([1,2,3,4,5], [5,6,7,8,9]))
#print(exercise10([1,2,3,4,5], [6,7,8,9]))

def exercise11():
    list1 = [1, 3, 5, 7, 9]
    list2=[1, 2, 4, 6, 7, 8]
    diff_list1_list2 = list(set(list1) - set(list2))
    diff_list2_list1 = list(set(list2) - set(list1))
    total_diff = diff_list1_list2 + diff_list2_list1
    print(total_diff)

#exercise11()


def exercise12(array,n):
    for i in range(len(array)):
        if array[i] == n:
            print(i)

#exercise12([10, 30, 4, -6],30)

def exercise13():
    x,y=0,1

    while y<50:
        print(y)
        x,y = y,x+y

#exercise13()

def exercise14():
    for fizzbuzz in range(10):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("fizzbuzz")
        elif fizzbuzz % 3 == 0:
            print("fizz")
        elif fizzbuzz % 5 == 0:
            print("buzz")
        print(fizzbuzz)
        
#exercise14()


def exercise15():
    s = input("Input a string") #user gives in "W3resource"
    d=l=0
    for c in s:
        if isinstance(c, int):
            d=d+1
        if isinstance(c, str):
            l=l+1
        else:
            pass
    print("Letters", l)
    print("Digits", d)
    
#exercise15()

def exercise16():
    a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()

#exercise16()

def exercise17():
    a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    s = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            s += a[i][j]
    print(s)

#exercise17()


def exercise18():
    a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    s = 0
    for row in a:
        for elem in row:
            s += elem
    print(s)

#exercise18()

def exercise19(n,total):
    sum = 0
    for i in n:
        sum +=i
    if(sum == total):
        print(True)
    else:
        print(False)

#exercise19([10,20,30],60)

def exercise20(b):
    newArray = []                
    for i in b:                  
        sArray = []              
        for k in i:              
            if( k !=10):         
                sArray.append(k) 
        newArray.append(sArray)

a =     [[1,2,4,58 ], 
         [3,10,5,12], 
         [3,4,10,52]]


