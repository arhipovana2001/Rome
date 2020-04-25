class Rome:
    def __init__(self, number: str, number_bool=True):
        self.number = number
        self.number_bool = number_bool

    # проверка введенного римского числа
    def check(self):
        convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        counter = 0
        digit = 0
        for ch, j in zip(self.number, self.number[::-1]):
            if ch not in convert or self.number.count(ch * 4) > 0:
                self.number_bool = False
                break
            elif convert[j] >= digit:
                digit = convert[j]
                counter = 0
            else:
                if convert[j] < digit / 10:
                    self.number_bool = False
                    break
                else:
                    counter += 1
                    if counter > 1:
                        self.number_bool = False
                        break
        return self.number_bool

    # перевод римского числа в арабское
    def convert_to_int(self):
        if self.check():
            convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            total = 0
            for d in range(len(self.number)):
                try:
                    if convert[self.number[d]] < convert[self.number[d + 1]]:
                        total -= convert[self.number[d]]
                    else:
                        total += convert[self.number[d]]
                except IndexError:
                    total += convert[self.number[d]]
            return str(total)
        else:
            return str(False)

    # функция print
    def __str__(self):
        return self.convert_to_int()

    # перевод арабского числа в римское
    def convert_to_roman(self, number):
        roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'LX': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                 'D': 500, 'CM': 900, 'M': 1000}
        roman_numerals = []
        for key, value in zip(reversed(list(roman.keys())), reversed(list(roman.values()))):
            count = number // value
            number -= count * value
            roman_numerals.append(key * count)
        return ''.join(roman_numerals)

    # сложение
    def __add__(self, other):
        if self.check() and other.check():
            return self.convert_to_roman(int(self.convert_to_int()) + int(other.convert_to_int()))
        else:
            return False

    # вычитание
    def __sub__(self, other):
        if self.check() and other.check():
            if int(self.convert_to_int()) < int(other.convert_to_int()):
                return False
            else:
                return self.convert_to_roman(int(self.convert_to_int()) - int(other.convert_to_int()))
        else:
            return False

    # умножение
    def __mul__(self, other):
        if self.check() and other.check():
            return self.convert_to_roman(int(self.convert_to_int()) * int(other.convert_to_int()))
        else:
            return False

    # деление
    def __truediv__(self, other):
        if self.check() and other.check():
            return self.convert_to_roman(int(float(self.convert_to_int()) / float(other.convert_to_int())))
        else:
            return False

    # сравнение ==
    def __eq__(self, other):
        if self.check() and other.check():
            return int(self.convert_to_int()) == int(other.convert_to_int())
        else:
            return False

    # сравнение !=
    def __ne__(self, other):
        if self.check() and other.check():
            return int(self.convert_to_int()) != int(other.convert_to_int())
        else:
            return False

    # сравнение >
    def __gt__(self, other):
        if self.check() and other.check():
            return int(self.convert_to_int()) > int(other.convert_to_int())
        else:
            return False

    # сравнение <
    def __lt__(self, other):
        if self.check() and other.check():
            return int(self.convert_to_int()) < int(other.convert_to_int())
        else:
            return False

    # сравнение >=
    def __ge__(self, other):
        if self.check() and other.check():
            return int(self.convert_to_int()) >= int(other.convert_to_int())
        else:
            return False

    # сравнение <=
    def __le__(self, other):
        if self.check() and other.check():
            return int(self.convert_to_int()) <= int(other.convert_to_int())
        else:
            return False
