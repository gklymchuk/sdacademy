# -*- coding: utf-8 -*-
import math


class Quadratic(object):
    notes = ['Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.',
             'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ',
             'Квадратное уравнение имеет два действительных корня: ',
             'коэффициент при первом слагаемом уравнения не может быть равным нулю',
             'коэффициент не целое число',
             'коэффициент не определен']

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def solution(self):
        try:
            a = int(self.a)
            b = int(self.b)
            c = int(self.c)

            d = b ** 2 - 4 * a * c

            if d < 0:
                return 'Дискриминант: %s' % d + "\n" + \
                       self.notes[0]
            elif d == 0:
                x1 = -b / float(2 * a)
                return 'Дискриминант: %s' % d + "\n" + \
                       self.notes[1] + '%s' % round(x1, 1)
            else:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                return 'Дискриминант: %s' % d + "\n" + \
                       self.notes[2] + 'x1 = %s, x2 = %s' % (round(x1, 1), round(x2, 1))
        except (ValueError, TypeError, ZeroDivisionError):
            return ''


