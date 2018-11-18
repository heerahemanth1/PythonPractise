#!/usr/bin/python
# -*- Coding: utf-8 -*-

import operator

SAVED_STR = ''

if __name__ == '__main__':
    optr_dict = {'+': operator.add,
                 '-': operator.sub,
                 '*': operator.mul,
                 '/': operator.div,
                 '%': operator.mod}
    num1 = float(raw_input('1st number: '))
    optr = str(raw_input('Operator: '))
    num2 = float(raw_input('2nd number: '))
    print optr_dict.get(optr)(num1, num2)
