class Ternary:
    def __init__(self, num):  # инициализация объекта Binary (num - число в 10 сс)
        self.num = num

    def __add__(self, other):  # сложение объекта Binary и other
        list1 = list(self.num)
        list2 = list(other)
        list3 = []
        list1.reverse()
        for i in range(0, len(list1)):
            list1[i] = int(list1[i])
        u = 0
        for i in range(0, len(list1)):
            u = u + (list1[i] * (3**i))
        list2.reverse()
        for i in range(0, len(list2)):
            list2[i] = int(list2[i])
        j = 0
        for i in range(0, len(list2)):
            j += list2[i] * (3**i)
        u += j
        while(u != 0):
            list3.append(u % 3)
            u //= 3
        if(len(list3) == 0):
            return 0
        else:
            list3.reverse()
            return "".join(map(str, list3))


    def __sub__(self, other):  # вычитание other из объекта Binary
        list1 = list(self.num)
        list2 = list(other)
        list3 = []
        list1.reverse()
        for i in range(0, len(list1)):
            list1[i] = int(list1[i])
        u = 0
        for i in range(0, len(list1)):
            u = u + (list1[i] * (3**i))
        list2.reverse()
        for i in range(0, len(list2)):
            list2[i] = int(list2[i])
        j = 0
        for i in range(0, len(list2)):
            j += list2[i] * (3**i)
        u -= j
        if u > 0:
            while(u != 0):
                list3.append(u % 3)
                u //= 3
            list3.reverse()
            return "".join(map(str, list3))
        elif u < 0:
            u = abs(u)
            while(u != 0):
               list3.append(u % 3)
               u //= 3
            list3.append('-')
            list3.reverse()
            return "".join(map(str, list3))
        elif u == 0:
            return 0

    def __mul__(self, other):  # умножение объекта Binary на other
        list1 = list(self.num)
        list2 = list(other)
        list3 = []
        list1.reverse()
        for i in range(0, len(list1)):
            list1[i] = int(list1[i])
        u = 0
        for i in range(0, len(list1)):
            u = u + (list1[i] * (3**i))
        list2.reverse()
        for i in range(0, len(list2)):
            list2[i] = int(list2[i])
        j = 0
        for i in range(0, len(list2)):
            j += list2[i] * (3**i)
        u *= j
        while(u != 0):
            list3.append(u % 3)
            u //= 3
        if(len(list3) == 0):
            return 0
        else:
            list3.reverse()
            return "".join(map(str, list3))

    def __floordiv__(self, other):  # целочисленное деление объекта Binary на other
        list1 = list(self.num)
        list2 = list(other)
        list3 = []
        list1.reverse()
        for i in range(0, len(list1)):
            list1[i] = int(list1[i])
        u = 0
        for i in range(0, len(list1)):
            u = u + (list1[i] * (3**i))
        list2.reverse()
        for i in range(0, len(list2)):
            list2[i] = int(list2[i])
        j = 0
        for i in range(0, len(list2)):
            j += list2[i] * (3**i)
        u //= j
        while(u != 0):
            list3.append(u % 3)
            u //= 3
        if(len(list3) == 0):
            return 0
        else:
            list3.reverse()
            return "".join(map(str, list3))

    def __str__(self):  # конвертирование объекта Binary в строку
        pass

a = Ternary(input())
b = input()
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
print(a.__floordiv__(b))
