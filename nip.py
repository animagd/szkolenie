# -*- coding: utf-8 -*-
from random import randint


class NIP(object):
    def __init__(self, NIP_nr=''):
        self.NIP_numbers = []
        if NIP_nr:
            self.NIP_numbers = [int(i) for i in NIP_nr]
        else:
            self.create_NIP_number()

    def create_NIP_number(self):
        # nr urzędów
        self.NIP_numbers.append(randint(1, 9))
        self.NIP_numbers.append(randint(0, 9))
        self.NIP_numbers.append(randint(1, 9))

        # środkowe cyfry
        for i in range(6):
            self.NIP_numbers.append(randint(0, 9))

        self.NIP_numbers.append(self.create_control_sum())

    def create_control_sum(self):
        control_number = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        sum_number = 0

        for i in range(0, len(control_number)):
            sum_number += self.NIP_numbers[i] * control_number[i]

        control_sum = sum_number % 11

        return control_sum

    def equal_control_sum(self):
        if self.NIP_numbers[9] == self.create_control_sum():
            print 'Nr NIP jest prawidłowy'
        else:
            print 'Nr NIP jest nieprawidłowy. Nie zgadza się suma kontrolna'

    def to_string(self):
        print ''.join(str(i) for i in self.NIP_numbers)


def what_to_do():
    print 'Wybierz co chcesz zrobić:'
    print '1. Generowanie nr NIP'
    print '2. Sprawdzenie sumy kontrolnej nr NIP'
    print 'Inny znak - wyjście'

    return raw_input()

def choice1():
    NIP().to_string()
    print 'Czy generować kolejny nr NIP t/n?'
    answer = raw_input()
    while answer == 't':
        NIP().to_string()
        print 'Czy generować kolejny nr NIP t/n?'
        answer = raw_input()
    else:
        quit()

def choice2():
    print 'Podaj nr NIP - ciąg cyfr bez znaków specjalnych'
    user_NIP = raw_input()
    try:
        int(user_NIP)
    except:
        print 'Ciąg znaków nie składa się z samych cyfr'
    if len(user_NIP) == 10:
        NIP(user_NIP).equal_control_sum()
    else:
        print 'Podałeś za krótki ciąg liczb'


choice = what_to_do()
if choice == '1':
    choice1()
elif choice == '2':
    choice2()
else:
    quit()
