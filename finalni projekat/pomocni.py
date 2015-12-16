# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 00:43:39 2016

@author: Maric
"""

PoljaPozicija = [[0 for x in range(8)] for x in range(8)]
PoljaIme = [[0 for x in range(8)] for x in range(8)]
PoljaFigura = [["" for x in range(8)] for x in range(8)]
PoljaKvadrati = [[0 for x in range(8)] for x in range(8)]
Pokreti = [[0 for x in range(4)] for x in range(12)]

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

PoljaIme[0][0] = 'A8'; PoljaIme[0][1] = 'B8'; PoljaIme[0][2] = 'C8'; PoljaIme[0][3] = 'D8'
PoljaIme[0][4] = 'E8'; PoljaIme[0][5] = 'F8'; PoljaIme[0][6] = 'G8'; PoljaIme[0][7] = 'H8'
PoljaIme[1][0] = 'A7'; PoljaIme[1][1] = 'B7'; PoljaIme[1][2] = 'C7'; PoljaIme[1][3] = 'D7'
PoljaIme[1][4] = 'E7'; PoljaIme[1][5] = 'F7'; PoljaIme[1][6] = 'G7'; PoljaIme[1][7] = 'H7'
PoljaIme[2][0] = 'A6'; PoljaIme[2][1] = 'B6'; PoljaIme[2][2] = 'C6'; PoljaIme[2][3] = 'D6'
PoljaIme[2][4] = 'E6'; PoljaIme[2][5] = 'F6'; PoljaIme[2][6] = 'G6'; PoljaIme[2][7] = 'H6'
PoljaIme[3][0] = 'A5'; PoljaIme[3][1] = 'B5'; PoljaIme[3][2] = 'C5'; PoljaIme[3][3] = 'D5'
PoljaIme[3][4] = 'E5'; PoljaIme[3][5] = 'F5'; PoljaIme[3][6] = 'G5'; PoljaIme[3][7] = 'H5'
PoljaIme[4][0] = 'A4'; PoljaIme[4][1] = 'B4'; PoljaIme[4][2] = 'C4'; PoljaIme[4][3] = 'D4'
PoljaIme[4][4] = 'E4'; PoljaIme[4][5] = 'F4'; PoljaIme[4][6] = 'G4'; PoljaIme[4][7] = 'H4'
PoljaIme[5][0] = 'A3'; PoljaIme[5][1] = 'B3'; PoljaIme[5][2] = 'C3'; PoljaIme[5][3] = 'D3'
PoljaIme[5][4] = 'E3'; PoljaIme[5][5] = 'F3'; PoljaIme[5][6] = 'G3'; PoljaIme[5][7] = 'H3'
PoljaIme[6][0] = 'A2'; PoljaIme[6][1] = 'B2'; PoljaIme[6][2] = 'C2'; PoljaIme[6][3] = 'D2'
PoljaIme[6][4] = 'E2'; PoljaIme[6][5] = 'F2'; PoljaIme[6][6] = 'G2'; PoljaIme[6][7] = 'H2'
PoljaIme[7][0] = 'A1'; PoljaIme[7][1] = 'B1'; PoljaIme[7][2] = 'C1'; PoljaIme[7][3] = 'D1'
PoljaIme[7][4] = 'E1'; PoljaIme[7][5] = 'F1'; PoljaIme[7][6] = 'G1'; PoljaIme[7][7] = 'H1'
