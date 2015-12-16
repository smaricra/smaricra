# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 10:38:13 2016


@author: Maric
"""
import numpy
print 478/8, 478%8

Pokreti = [["" for x in range(4)] for x in range(12)]
print Pokreti
Pokreti[0][0] = 'crni lovac';       Pokreti[0][1]= [-1, -1, 1, 1];                      Pokreti[0][2] = [-1, 1, -1, 1];                  Pokreti[0][3]=0
Pokreti[1][0] = 'beli lovac';       Pokreti[1][1]= [-1, -1, 1, 1];                      Pokreti[1][2] = [-1, 1, -1, 1];                  Pokreti[1][3]=0
Pokreti[2][0] = 'crni top';         Pokreti[2][1]= [-1, 1, 0, 0];                       Pokreti[2][2] = [ 0, 0, -1, 1];                  Pokreti[2][3]=0
Pokreti[3][0] = 'beli top';         Pokreti[3][1]= [-1, 1, 0, 0];                       Pokreti[3][2] = [ 0, 0, -1, 1];                  Pokreti[3][3]=0
Pokreti[4][0] = 'crni pijun';       Pokreti[4][1]= [ 1, 1, 1];                          Pokreti[4][2] = [-1, 0, 1];                      Pokreti[4][3]=2
Pokreti[5][0] = 'beli pijun';       Pokreti[5][1]= [-1, -1, -1];                        Pokreti[5][2] = [-1, 0, 1];                      Pokreti[5][3]=2
Pokreti[6][0] = 'crni skakac';      Pokreti[6][1]= [-1, -2, -2, -1, 1, 2, 2, 1];        Pokreti[6][2] = [-2, -1, 1, 2, -2, -1, 1, 2];    Pokreti[6][3]=1
Pokreti[7][0] = 'beli skakac';      Pokreti[7][1]= [-1, -2, -2, -1, 1, 2, 2, 1];        Pokreti[7][2] = [-2, -1, 1, 2, -2, -1, 1, 2];    Pokreti[7][3]=1
Pokreti[8][0] = 'crna kraljica';    Pokreti[8][1]= [ 0, -1, -1, -1, 0, 1, 1, 1];        Pokreti[8][2] = [-1, -1, 0, 1, 1, 1, 0, -1];     Pokreti[8][3]=0
Pokreti[9][0] = 'bela kraljica';    Pokreti[9][1]= [ 0, -1, -1, -1, 0, 1, 1, 1];        Pokreti[9][2] = [-1, -1, 0, 1, 1, 1, 0, -1];     Pokreti[9][3]=0
Pokreti[10][0] = 'crni kralj';      Pokreti[10][1]= [ 0, -1, -1, -1, 0, 1, 1, 1];       Pokreti[10][2] = [-1, -1, 0, 1, 1, 1, 0, -1];    Pokreti[10][3]=1
Pokreti[11][0] = 'beli kralj';      Pokreti[11][1]= [ 0, -1, -1, -1, 0, 1, 1, 1];       Pokreti[11][2] = [-1, -1, 0, 1, 1, 1, 0, -1];    Pokreti[11][3]=1
 
A = [2,3]*10
print A
