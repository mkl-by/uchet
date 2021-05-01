"""Все о классах

в классах Оne, Two, Tree организовано наледование и
перегрузка операций с использованием методов __х__"""
class Rerepr:
    def __repr__(self):
        a = []
        for i in self.__dict__:
            a.append(getattr(self, i))
        return f'{str(a)} -- {self.__class__.__name__}'

class One(Rerepr):

    def __init__(self):
        self.a = 1
        self.b = 1

    def setdata(self, aaa):
        self.data = aaa

    def setdispl(self):
        print(self.data)

class Two:
    def __init__(self):
        self.b = 2
        self.a = 2
        self.e = 2

    def setdispl(self):
        print('class Two')

    #переопределии метод print
    # def __str__(self):
    #     return f'daty  = {self.data}'

class Tree(Two, One):
    pay = 'qweri'
    def __init__(self, dat):
        #One().__init__()
        # Two().__init__()
        self.d = 3
        self.c = 3
        self.b = 3
        self.daty = dat
        self.pay = 11111


    # переопределяем метод в дереве наследования класса, а именно в классе Twо
    # а он в своею очередь class One
    def setdispl(self):
        print('class Tree', self.data)

    # перегружаем метод __add__
    def __add__(self, data):
        return Tree(self.daty+data)


class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def paynow(self, dollars):
        self.pay += dollars

    def __repr__(self):
        a=[]
        for i in self.__dict__:
            a.append(getattr(self, i))
        return f'{str(a)} -- {self.__class__.__name__}'
        # return f'[Person: {self.name}, job {self.job}, pay={self.pay} == {getattr(self, __class__.__name__)}]'

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mng', pay)
    def paynow(self, dollars, bonus=99):
        Person.paynow(self, dollars+bonus)

class Indexs:
    data = [1,2,3,4,5]
    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

class Aa:
    def __getitem__(self, ii):
        return self.data[ii]

class Setrcontr(Rerepr):

    def __getattr__(self, item):
        if item == 'aaa':
            return 40
        else:
            raise AttributeError(item)

    def __setattr__(self, name, volu):
        if name == 'age':
            self.__dict__['age'] = volu+10

        else:
            raise AttributeError(name)



if __name__=='__main__':

    x = Setrcontr()
    x.aaa
    x.age = 40
    print(x)
    # I = Aa()
    # I.data = 'sasun'
    # for u in I:
    #     print(
    #         u
    #     )
    #
    # index = Indexs()
    # index[4] = 12
    # print(index[0:])
    # for i in range(5):
    #     print(index[i])



    #рассматриваем класс tree переопределяем атрибуты его класса
    # tree = Tree(5)
    #
    # tree.setdata('qwe')
    # tree.setdispl()
    # # если вызываем метод print для объекта, то на выходе получаем то что в __str__
    # print(tree)
    # #создаем новый объект с использованием __add__ передаем данные объекта tree в класс Tree
    # obj_now = tree+3
    # obj_now.setdata('qwe1')
    # print(obj_now)
    # print(Tree.__dict__)
    # print('tree', tree.__dict__)
    # print('obj_now', obj_now.__dict__)
    #
    # # bob = Person('bob')
    # bob1 = Person('bob1', 'adm', 100)
    #
    # print(bob, bob1)
    #
    # tom = Manager('Tom', 100)
    #
    # print(tom)
    # #полиформизм в действии
    # for i in (bob, bob1, tom):
    #     i.paynow(100)
    #     print(i)
