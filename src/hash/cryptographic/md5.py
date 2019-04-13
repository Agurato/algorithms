# -*- coding: utf-8 -*-
import math


def md5(string):
    K = [0]*64
    for i in range(0, 64):
        K[i] = math.floor(math.pow(2, 32) * math.fabs(math.sin(i+1)))
        print(K[i])

    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

if __name__ == '__main__':
    md5('coucou')
