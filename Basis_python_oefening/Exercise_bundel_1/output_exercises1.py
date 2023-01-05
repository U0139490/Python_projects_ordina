def exercise1():
    a = "5"
    b = 3
    print("I want ", a, "puppies and " + str(b), "kats!")

def exercise2():
    print(f'{(41 + 200) % 24}:00')

def exercise3():
    a = input("Give a number: ") #user gave in 7
    print(a)

def exercise4():
    a = input("what's your firstname? ") #user gave in "Jef"
    b = int(input("what's your age? ")) #user gave in 18

    print(a + b)


def exercise5():
    amount = 99
    a = amount // 15
    b = amount % 15
    c = a // 3
    d = b % 3
    print(a, b, c, d)


def exercise6():
    answer = input('Enter a string: ') #user gave in "I like programming!"
    print(len(answer))

def exercise7():
    score = int(input())
    # determine corresponding letter grade
    if score <= 30:
        letter_grade = 'Max score'
    elif score >= 15:
        letter_grade = 'You just passed!'
    else:
        letter_grade = 'failed!'
    print(letter_grade)


def exercise8():
    number = int(input())
    if number == 10:
        print("A")
    if number < 30:
        print("B")
    if number > 5:
        print("C")
    if number < 11:
        print("D")
    if number < 4:
        print("E")

#In Python, AND operator has higher precedence than OR operator. So, it is evaluated first. i.e, (b and c) evaluates to false.Now OR operator is evaluated. Here, (True or False) evaluates to True. 
def exercise9():
    a = True
    b = False
    c = False
    
    if a or b and c:
        print ("A")
    else:
        print ("B")

#In Python the precedence order is first NOT then AND and in last OR. So the if condition and second elif condition evaluates to False while third elif condition is evaluated to be True resulting in 3 as output.
def exercise10():
    a = True
    b = False
    c = False
    
    if not a or b:
        print (1)
    elif not a or not b and c:
        print (2)
    elif not a or b or not b and a:
        print (3)
    else:
        print (4)

def exercise11():
    count = 1
    for i in range(3): 
        count += 1
    print (count)


def exercise12():
    for i in range(3,10):
        j = i + 2
        print(j)

def exercise13():
    a = int(input()) #user gave in 0
    b = int(input()) #user gave in 10
    total = 0
    while(a <= b):
        total += a
        a += 1
    print(total)



def exercise14():
    array = [1, 6.0, "9", 1.34, 32]
    for i in array:
        if isinstance(i, int): #isinstance checkt of de type van "i" gelijk is aan de meegeven type
            print(i)


def exercise15():
    a = []
    # betere manier om dit te programmeren a = [x for x in range(5)]
    for i in range(5):
        a.append(i)

    b= []
    # betere manier om dit te programmeren b = [x for x in range(7) if x in a and x%2==0]
    for i in range(7): 
        if i in a and i%2 == 0:
            b.append(i)
    print(b)
    
def exercise16():
    temp = ['Geeks', 'for', 'Geeks']
    array = []
    for i in temp:
        array.append(i[0].upper()) #upper() returend a copy of the string to uppercase
    print(array)

def exercise17():
    n=5;
    for i in range(n):
        for j in range(i):
            print ('* ', end="")
        print('')

    for i in range(n,0,-1):
        for j in range(i):
            print('* ', end="")
        print('')

exercise17()

def exercise18():
    array = []
    for i in range(3):
        sArray = []
        for k in range(3):
            sArray.append(i)
            
        array.append(sArray)

    print(array)

exercise18()
def exercise19(array2D,getal):
    for i in array2D:
        for k in i:
            if k % getal == 0:
                print(k)

a = [[1,3,4], [12,9,45]]
b = 3
exercise19(a, b)
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

