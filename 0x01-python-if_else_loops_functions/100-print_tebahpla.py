#!/usr/bin/python3
# 100-print_tebahpla.py
for i in range(ord('z'), ord('a') - 1, -1):
    letter = chr(i)
    if i % 2 == 0:
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
