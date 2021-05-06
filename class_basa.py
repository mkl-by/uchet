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
                   out_local_number=None,
                    out_lokal_data=None,
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
        out_local_number - исходящий номер
        out_local_data - исходящая дата
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
        self.out_local_number = None,
        self.out_lokal_data = None,

        # self.parsing()
        Parss.__init__(self, number, exemplar)

    def view(self, outNloc, outDloc, number, exem, deposit):
        # номер документа number 0001...
        self.out_local_number = outNloc
        self.out_lokal_data = outDloc
        self.pars_number[number][0] = deposit
        self.pars_number[number][2] = exem

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

    d = Papers('moskvva', 1111, '1.1.1111', 2222, '1.1.1111', 'minsk', '00001-00003')
    # dd = Technics('moskvva', 1111, '1.1.1111', 2222, '1.1.1111', 'minsk', '00001-00005', '014')
    # ddd = Technics_papers('moskvva', 1111, '1.1.1111', 2222, '1.1.1111', 'brest', '00001-00005', '014')
    print(d)
    # d.view('1234', '1.22.1212', '00003', '002', 'brest')

    # print(dd)
    # print(ddd)