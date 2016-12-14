# -*- coding: utf-8 -*-

from random import randint
from random import choice
import copy
import re

class PESEL(object):
    def __init__(self,date):
        self.pesel = []
        self.man_pesel = []
        self.date = [int(i) for i in date if '-' not in i]
        self.create_PESEL_number()

    def create_PESEL_number(self):
        self.pesel.append(self.date[6]) #1
        self.pesel.append(self.date[7]) #2
        self.month()
        self.pesel.append(self.date[3]) #4
        self.pesel.append(self.date[0]) #5
        self.pesel.append(self.date[1]) #6
        for i in range(3): #7-9
            self.pesel.append(randint(0, 9))
        self.man_pesel = copy.copy(self.pesel)
        self.pesel.append(choice(range(0, 8, 2))) # liczba parzysta - kobieta
        self.man_pesel.append(choice(range(1, 9, 2))) # liczba nieparzysta - mężczyzna
        self.pesel.append(self.create_control_sum(self.pesel))
        self.man_pesel.append(self.create_control_sum(self.man_pesel))

    def month(self):
        year = ''.join([str(i) for i in self.date[4:]])
        if 1800 <= int(year) <= 1899:
            self.pesel.append(self.date[2] + 8)
        elif 1900 <= int(year) <= 1999:
            self.pesel.append(self.date[2])
        elif 2000 <= int(year) <= 2099:
            self.pesel.append(self.date[2] + 2)
        elif 2100 <= int(year) <= 2199:
            self.pesel.append(self.date[2] + 4)
        elif 2200 <= int(year) <= 2299:
            self.pesel.append(self.date[2] + 6)

    def create_control_sum(self, pesel):
        control_number = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        sum_number = 0

        for i in range(0,len(control_number)):
            sum_number += pesel[i] * control_number[i]

        control_sum = 10 - (sum_number % 10)
        control_sum = control_sum % 10

        return control_sum

    def to_string(self):
        print 'Nr pesel dla kobiety to ' + ''.join(str(i) for i in self.pesel)
        print 'Nr pesel dla mężczyzny to ' + ''.join(str(i) for i in self.man_pesel)


end = None
while end != 1:
    print 'Podaj datę urodzenia w formacie DD-MM-RRRR'
    user_date = raw_input()
    str_equals = re.compile("^\d{2}-\d{2}-\d{4}$")  #zapamiętuje wzór, który będzie porównywał
    is_valid = str_equals.match(user_date) #porównuje wzór ze stringiem
    '''
    ^        początek stringa
    \d{2}   dwie cyfry
    -         znak "-"
    \d{2}   dwie cyfry
    -         znak "-"
    \d{4}   cztery cyfry
    $        koniec stringa
    czyli ^\d{2}-\d{2}-\d{4}$
    '''
    if is_valid:
        PESEL(user_date).to_string()
        end = 1
    else:
        print 'Wpisano błędne znaki i/lub podano datę w formacie innym niż DD-MM-RRRR '