#!/usr/bin/python3
# 6-print_comb3.py
'To print two unidenticak integers'
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{1}{0}".format(digit2, digit1))
        else:
            print("{1}{0}".format(digit2, digit1), end=", ")
