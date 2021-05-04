
class Parss:
    """разбиваем строку вида '00001-00011, 00013, 00017-00020'
    в список вида ['00001', '00002', '00003', '00004', '00005', '00006', '00007', '00008',
    '00009', '00010', '00011', '00013', '00017', '00018', '00019', '00020']
"""
    def __init__(self, text = None, exem = None):
        # номера как выше в описании
        self.deposit = 'minsk'  # убрать потом использовать для тестирования

        if text:
            self.pars_number = self.parsing_text(text, True)
            print(self.pars_number)
        if exem:
            self.pars_exem = self.parsing_text(exem, False)
            print(self.pars_exem)
        if self.pars_number and self.pars_exem:
            for key in self.pars_number:
                self.pars_number [key].append(self.pars_exem)
            print(self.pars_number)

    def parsing_text(self, text, yesno):
        pars_number = dict()
        pars_ex = []
        num = None
        numbers = text.split(', ') # разбиваем строку на части
        sum_num = len(numbers[0].split('-')[0]) # определяем длинну цифры
        for i in numbers:
            s = i.split('-') # если есть дефис, снова разбиваем
            if len(s) > 1:
                for ii in range(int(s[0]), int(s[1])+1):
                    num = '0'*(sum_num-len(str(ii)))+str(ii) # добавляем нули
                    if yesno:
                        pars_number[num] = [self.deposit, True] # True означает что документ не уничтожен и не возвращен
                    else:
                        pars_ex.append(num)
            else:
                if yesno:
                    pars_number[s[0]] = [self.deposit, True]
                else:
                    pars_ex.append(s[0])
        if yesno:
            return pars_number
        else:
            return pars_ex


#проверку на колличество цифр в номерах, проверку на наличие букав в цифрах, проверку на повторения одинаковых цифр реализовать


if __name__=='__main__':


    d = Parss('00001-00002, 00004, 00007-00008', '001-002')
