# -*- coding: utf-8 -*-

import os

class date_of_birth(object):
    def __init__(self, pesel):
        self.pesel = pesel
        self.date_of_birth = ''

    def create_date_of_birth(self):
        for i in self.pesel[4:6]:
            self.date_of_birth += i

        self.date_of_birth += '-'
        self.year()
        self.date_of_birth += str(self.first_month_el)
        self.date_of_birth += self.pesel[3]
        self.date_of_birth += '-'
        self.date_of_birth += self.first_year_el
        self.date_of_birth += self.pesel[0]
        self.date_of_birth += self.pesel[1]

        return self.date_of_birth

    def year(self):
        self.first_year_el = ''
        if int(self.pesel[2]) == 0 or int(self.pesel[2]) == 1:
            self.first_year_el = '19'
            self.first_month_el = int(self.pesel[2])
        elif int(self.pesel[2]) - 2 == 0 or int(self.pesel[2]) - 2 == 1:
            self.first_year_el = '20'
            self.first_month_el = int(self.pesel[2]) - 2
        elif int(self.pesel[2]) - 4 == 0 or int(self.pesel[2]) - 4 == 1:
            self.first_year_el = '21'
            self.first_month_el = int(self.pesel[2]) - 4
        elif int(self.pesel[2]) - 6 == 0 or int(self.pesel[2]) - 6 == 1:
            self.first_year_el = '22'
            self.first_month_el = int(self.pesel[2]) - 6
        elif int(self.pesel[2]) - 8 == 0 or int(self.pesel[2]) - 8 == 1:
            self.first_year_el = '18'
            self.first_month_el = int(self.pesel[2]) - 8


def create_control_sum(pesel):
    control_number = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
    sum_number = 0

    for i in range(0,len(control_number)):
        sum_number += int(pesel[i]) * control_number[i]

    control_sum = 10 - (sum_number % 10)
    control_sum = control_sum % 10

    return control_sum


def equal_control_sum(pesel):
    if int(pesel[10]) == create_control_sum(pesel):
        return True
    else:
        return False


def reading_file():
    path = r'C:\git_szkolenie' + os.sep
    file_name = 'nr_pesel.txt'

    read_file = open(path + file_name)
    read_line = read_file.read().splitlines()

    return read_line

    read_file.close()


def writing_file(date_of_births, valid_pesels):
    path = r'C:\git_szkolenie' + os.sep
    write_file_name = 'pesel and date.txt'
    write_file = open(path + write_file_name, 'w')
    for i in range(len(date_of_births)):
        write_file.write(valid_pesels[i] + ' ' + date_of_births[i] + '\n')

    write_file.close()


read_lines = reading_file()
date_of_births = []
pesels = []
valid_pesels = []

pesels = [i for i in read_lines]
for pesel_nr in range(len(pesels)):
    pesel = [i for i in pesels[pesel_nr]]
    if equal_control_sum(pesel):
        date_of_births.append(date_of_birth(pesel).create_date_of_birth())
        valid_pesels.append(''.join(str(i) for i in pesel))
        writing_file(date_of_births, valid_pesels)
    else:
        print 'Błędny nr pesel %s w linii %d' % (''.join(str(i) for i in pesel), pesel_nr + 1)