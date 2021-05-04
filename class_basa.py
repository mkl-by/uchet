from pars import Parss

class Rerepr:
    """отображает все что есть в экземпляре и имя класса к которому он относится"""
    def __repr__(self):
        a = []
        for i in self.__dict__:
            a.append((i, getattr(self, i)))
        return f'{str(a)} -- {self.__class__.__name__}'


class Papers(Rerepr, Parss):

    def __init__(self,
                   whence,
                   out_number,
                   data_out,
                   in_number,
                   data_in,
                   deposit,
                   number=None,
                   exemplar=None,
                   ):
        """ name - наименование объекта
        whence - откуда поступил,
        out_number - номер за которым поступил,
        data_out - дата регистрации out_number,
        in_number - номер за которым зарегистрировали,
        data_in - дата номера in_number,
        deposit - где хранится,
        number - номер самого объекта, если есть
        exemplar - экземпляр если у номера объекта их несколько
        """
        self.name = 'papers'
        self.whence = whence
        self.out_number = out_number
        self.data_out = data_out
        self.in_number = in_number
        self.data_in = data_in
        self.deposit = deposit
        self.number = number
        self.exemplar = exemplar
        # self.parsing()
        Parss.__init__(self, number)

    #
    # def parsing(self):
    #     # print(self.__class__.__name__)
    #     if self.__class__.__name__ == "Technics" or "Technics_papers":


class Technics(Papers):
    #поступил с предприятия
    def __init__(self, whence, out_number, data_out, in_number, data_in, deposit, number=None, exemplar=None):
        Papers.__init__(self, whence, out_number, data_out, in_number, data_in, deposit, number, exemplar)
        self.name = 'technics'


class Technics_papers(Papers):
    #поступил с предприятия
    def __init__(self, whence, out_number, data_out, in_number, data_in, deposit, number=None, exemplar=None):
        Papers.__init__(self, whence, out_number, data_out, in_number, data_in, deposit, number, exemplar)
        self.name = 'technics_papers'




if __name__=='__main__':

    d = Papers('moskvva', 1111, '1.1.1111', 2222, '1.1.1111', 'minsk', '00001-00005', '014')
    dd = Technics('moskvva', 1111, '1.1.1111', 2222, '1.1.1111', 'minsk', '00001-00005', '014')
    ddd = Technics_papers('moskvva', 1111, '1.1.1111', 2222, '1.1.1111', 'brest', '00001-00005', '014')
    print(d)
    print(dd)
    print(ddd)