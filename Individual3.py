# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово. Переставить его первую букву на место последней. При этом вторую, третью, ..., -ю буквы сдвинуть влево на одну позицию.

if __name__ == '__main__':
    s = str(input("Введите слово: "))
    k = 1
    a = s.replace(s[k - 1], s[0])
    s1 = 1
    print(a[s1:] + a[:s1])

