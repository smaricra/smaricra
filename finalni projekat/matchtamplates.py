# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 03:31:09 2016

@author: Maric
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
from Tkinter import *
import ttk
import import_soft as ims
import pomocni

pocetni_poredak = ''


def onselect0(evt):
    global pocetni_poredak
    global Lb1
    global Lb2
    Lb1.delete(0, END)
    Lb2.delete(0, END)
    widget = evt.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    if( value == 'slika 1'):
        pocetni_poredak = 'pocetni_poredak.jpg'
        promena_slike()
    elif( value == 'slika 3'):
        pocetni_poredak = 'pocetni_poredak3.jpg'
        promena_slike()
    elif( value == 'slika 4'):
        pocetni_poredak = 'pocetni_poredak4.jpg'
        promena_slike()
    elif( value == 'slika 5'):
        pocetni_poredak = 'pocetni_poredak5.jpg'
        promena_slike()
    elif( value == 'slika 6'):
        pocetni_poredak = 'pocetni_poredak6.jpg'
        promena_slike()
    elif( value == 'slika 7'):
        pocetni_poredak = 'pocetni_poredak7.jpg'
        promena_slike()
    elif( value == 'slika 8'):
        pocetni_poredak = 'pocetni_poredak8.jpg'
        promena_slike()
    elif( value == 'slika 9'):
        pocetni_poredak = 'pocetni_poredak9.jpg'
        promena_slike()
    
def onselect(evt):
    
    widget = evt.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    pronalazak_polja(value)   

def onselect2(evt):
    global pocetni_poredak
    widget = evt.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    img_rgb3 = cv2.imread(pocetni_poredak)
    for x in range(8):
        for y in range(8):
            if( pomocni.PoljaIme[x][y] == value):
                for z in range(12):
                    if( pomocni.PoljaFigura[x][y] == pomocni.Pokreti[z][0]):
                        dozvoljeni_pokreti(pomocni.Pokreti[z], value, img_rgb3)
                
    for x11 in range(8):
        for y11 in range(8):
            if( pomocni.PoljaIme[x11][y11] == value):
                cv2.rectangle(img_rgb3, pomocni.PoljaKvadrati[x11][y11][0], pomocni.PoljaKvadrati[x11][y11][1], (255,0,0), 4)
    plt.imshow(img_rgb3)
    plt.show()
    

def figure_na_tabli(slika, figura, bela):
    global pocetni_poredak
    img_rgb2 = cv2.imread(pocetni_poredak)
    img_gray = cv2.cvtColor(img_rgb2, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(slika,0)
    w, h = template.shape[::-1]

    res2 = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    if(bela==0):
        threshold = 0.6
    else:
        threshold = 0.8
    loc = np.where( res2 >= threshold)
    for pt in zip(*loc[::-1]):
        for x1 in range(8):
            for y1 in range(8):
                if( pomocni.PoljaPozicija[x1][y1][0] > pt[0] and pomocni.PoljaPozicija[x1][y1][0]< pt[0] + w
                and pomocni.PoljaPozicija[x1][y1][1] > pt[1] and pomocni.PoljaPozicija[x1][y1][1]< pt[1] + h):
                    pomocni.PoljaFigura[x1][y1] = figura;
                    pomocni.PoljaKvadrati[x1][y1] = (pt, (pt[0] + w, pt[1] + h))

def promena_slike():
    pomocni.PoljaPozicija = [[0 for x in range(8)] for x in range(8)]
    pomocni.PoljaFigura = [["" for x in range(8)] for x in range(8)]
    pomocni.PoljaKvadrati = [[0 for x in range(8)] for x in range(8)]
    Lb1.delete(0, END)
    global pocetni_poredak
    img_rgb = cv2.imread(pocetni_poredak)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('pocetni_polozaj2.jpg',0)
    w, h = template.shape[::-1]
    
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where( res >= threshold)
    
    for pt in zip(*loc[::-1]):
        p_tacka = pt
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,0,0), 2)
        plt.imshow(img_rgb)
        plt.show
    w1 = w/8
    h1 = h/8
    if w%8 > 4:
        w1 = w1+1
    if h%8 > 4:
        h1 = h1+1

    for xx in range(8):
        for yy in range(8):  
            pomocni.PoljaPozicija[xx][yy] = (pt[0] + w1*(yy+1) - w1/2, pt[1] + h1*(xx+1)-h1/2)
            cv2.circle(img_rgb, (pt[0] + w1*(yy+1) - w1/2, pt[1] + h1*(xx+1)-h1/2), 25, (0,255,0), 3)
    cv2.imwrite('res.png',img_rgb)
    plt.imshow(img_rgb)
    plt.show

    figure_na_tabli('beli_skakac.png', 'beli skakac', 0)
    figure_na_tabli('beli_lovac.png', 'beli lovac', 0)
    figure_na_tabli('beli_top.png', 'beli top', 0)
    figure_na_tabli('beli_kralj.png', 'beli kralj', 0)
    figure_na_tabli('beli_pijun.png', 'beli pijun', 0)
    figure_na_tabli('bela_kraljica.png', 'bela kraljica', 0)
    
    figure_na_tabli('crni_skakac.png', 'crni skakac', 1)
    figure_na_tabli('crni_lovac.png', 'crni lovac', 1)
    figure_na_tabli('crni_top.png', 'crni top', 1)
    figure_na_tabli('crni_kralj.png', 'crni kralj', 1)
    figure_na_tabli('crni_pijun.png', 'crni pijun', 1)
    figure_na_tabli('crna_kraljica.png', 'crna kraljica', 1)
    
    punjenje_liste1()

App = Tk()
App.geometry("600x600+350+70")

f1=0; f2=0; f3=0; f4=0; f5=0; f6=0; f7=0; f8=0; f9=0; f10=0; f11=0; f12=0

Lb0 = Listbox(App)
Lb0.insert(1, 'slika 1')
Lb0.insert(3, 'slika 3')
Lb0.insert(4, 'slika 4')
Lb0.insert(5, 'slika 5')
Lb0.insert(6, 'slika 6')
Lb0.insert(7, 'slika 7')
Lb0.insert(8, 'slika 8')
Lb0.insert(9, 'slika 9')
Lb0.pack()

Lb1 = Listbox(App)
def punjenje_liste1():
    Lb1.delete(0, END)
    
    f1=0; f2=0; f3=0; f4=0; f5=0; f6=0; f7=0; f8=0; f9=0; f10=0; f11=0; f12=0
    for s1 in range(8):
        for d1 in range(8):
            if( pomocni.PoljaFigura[s1][d1] == 'beli top' and f1==0):
                Lb1.insert(1, 'beli top')
                f1=1;
            if( pomocni.PoljaFigura[s1][d1] == 'beli skakac' and f2==0):
                Lb1.insert(2, 'beli skakac')
                f2=1;
            if( pomocni.PoljaFigura[s1][d1] == 'beli lovac' and f3==0):
                Lb1.insert(3, 'beli lovac')
                f3=1;
            if( pomocni.PoljaFigura[s1][d1] == 'beli kralj' and f4==0):
                Lb1.insert(4, 'beli kralj')
                f4=1;
            if( pomocni.PoljaFigura[s1][d1] == 'beli pijun' and f5==0):
                Lb1.insert(5, 'beli pijun')
                f5=1;
            if( pomocni.PoljaFigura[s1][d1] == 'bela kraljica' and f6==0):
                Lb1.insert(6, 'bela kraljica')
                f6=1;
            if( pomocni.PoljaFigura[s1][d1] == 'crni top' and f7==0):
                Lb1.insert(7, 'crni top')
                f7=1;
            if( pomocni.PoljaFigura[s1][d1] == 'crni skakac' and f8==0):
                Lb1.insert(8, 'crni skakac')
                f8=1;
            if( pomocni.PoljaFigura[s1][d1] == 'crni lovac' and f9==0):
                Lb1.insert(9, 'crni lovac')
                f9=1;
            if( pomocni.PoljaFigura[s1][d1] == 'crni kralj' and f10==0):
                Lb1.insert(10, 'crni kralj')
                f10=1;
            if( pomocni.PoljaFigura[s1][d1] == 'crni pijun' and f11==0):
                Lb1.insert(11, 'crni pijun')
                f11=1;
            if( pomocni.PoljaFigura[s1][d1] == 'crna kraljica' and f12==0):
                Lb1.insert(12, 'crna kraljica')
                f12=1;
            
Lb1.pack()
Lb2 = Listbox(App)
def pronalazak_polja(val):
    Lb2.delete(0, END)
    i = 1
    for x in range(8):
        for y in range(8):
            if( pomocni.PoljaFigura[x][y] == val):
                Lb2.insert(i, pomocni.PoljaIme[x][y])
                i = i+1
    return val

Lb2.pack()

Lb0.bind('<<ListboxSelect>>', onselect0)
Lb1.bind('<<ListboxSelect>>', onselect)
Lb2.bind('<<ListboxSelect>>', onselect2)


def dozvoljeni_pokreti(Pokret, polje, img_rgb3):
    if( Pokret[3]==1):
        for x in range(8):
            for y in range(8):
                if( pomocni.PoljaIme[x][y] == polje):
                    i = 0;
                    for pokret in Pokret[1]:
                        if( x + Pokret[1][i] <= 7 and x + Pokret[1][i]>=0 and 
                        y + Pokret[2][i] <= 7 and y + Pokret[2][i]>=0 and "kralj" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]):
                            if ("crn" in Pokret[0] and "crn" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                            or "bel" in Pokret[0] and "bel" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]):
                                if( ugrozeno_polje(Pokret[0], pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]], polje) == True):
                                    if( "beli kralj" not in Pokret[0] and "crni kralj" not in Pokret[0]):
                                        cv2.circle(img_rgb3, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]], 10, (0,0,255), 3)
                                    else:
                                        t1 = (pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][0] -13, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][1] -13)
                                        t2 = (pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][0] +13, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][1] +13)
                                        t3 = (pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][0] +13, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][1] -13)
                                        t4 = (pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][0] -13, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]][1] +13)
                                        cv2.line(img_rgb3, t1, t2, (255,0,0), 3)
                                        cv2.line(img_rgb3, t3, t4, (255,0,0), 3)
                                else:
                                    cv2.circle(img_rgb3, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]], 25, (0,255,0), 3)
                        i = i+1
    elif( Pokret[3]==0):
        for x in range(8):
            for y in range(8):
                if( pomocni.PoljaIme[x][y] == polje):
                    i = 0;
                    for pokret in Pokret[1]:
                        xx = x;
                        yy = y;
                        while True:
                            if( xx + Pokret[1][i] <= 7 and xx + Pokret[1][i]>=0 and 
                            yy + Pokret[2][i] <= 7 and yy + Pokret[2][i]>=0 and "kralj" not in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]]):
                                if ("crn" in Pokret[0] and "crn" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]]
                                or "bel" in Pokret[0] and "bel" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]]):
                                    break;
                                elif ("crn" in Pokret[0] and "bel" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]]
                                or "bel" in Pokret[0] and "crn" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]]):
                                    #print PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]]
                                    xx = xx + Pokret[1][i]
                                    yy = yy + Pokret[2][i]
                                    if( ugrozeno_polje(Pokret[0], pomocni.PoljaIme[xx][yy], polje) == True):
                                        if( "beli kralj" not in Pokret[0] and "crni kralj" not in Pokret[0]):
                                            cv2.circle(img_rgb3, pomocni.PoljaPozicija[xx][yy], 10, (0,0,255), 3)
                                    else:
                                        cv2.circle(img_rgb3, pomocni.PoljaPozicija[xx][yy], 25, (0,255,0), 3)
                                    break
                                else:
                                    #print PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]]
                                    xx = xx + Pokret[1][i]
                                    yy = yy + Pokret[2][i]
                                    if( ugrozeno_polje(Pokret[0], pomocni.PoljaIme[xx][yy], polje) == True):
                                        if( "beli kralj" not in Pokret[0] and "crni kralj" not in Pokret[0]):
                                            cv2.circle(img_rgb3, pomocni.PoljaPozicija[xx][yy], 10, (0,0,255), 3)
                                    else:
                                        cv2.circle(img_rgb3, pomocni.PoljaPozicija[xx][yy], 25, (0,255,0), 3)
                            else:
                                break
                        i = i+1
    elif( Pokret[3]==2):
        for x in range(8):
            for y in range(8):
                if( pomocni.PoljaIme[x][y] == polje):
                    i = 0;
                    for pokret in Pokret[1]:
                        if( x + Pokret[1][i] <= 7 and x + Pokret[1][i]>=0 and 
                        y + Pokret[2][i] <= 7 and y + Pokret[2][i]>=0 and "kralj" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]):
                            if( Pokret[1][i] ==0 or Pokret[2][i]==0):
                                if (("crn" in Pokret[0] and "crn" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                                or "bel" in Pokret[0] and "bel" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]])
                                and ("crn" in Pokret[0] and "bel" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                                or "bel" in Pokret[0] and "crn" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]])):
                                    #print PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]]
                                    if( ugrozeno_polje(Pokret[0], pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]], polje) == True):
                                        if( "beli kralj" not in Pokret[0] and "crni kralj" not in Pokret[0]):
                                            cv2.circle(img_rgb3, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]], 10, (0,0,255), 3)
                                    else:
                                        cv2.circle(img_rgb3, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]], 25, (0,255,0), 3)
                            else:
                                if("crn" in Pokret[0] and "bel" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                                or "bel" in Pokret[0] and "crn" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]):
                                    #print PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]]
                                    if( ugrozeno_polje(Pokret[0], pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]], polje) == True):
                                        if( "beli kralj" not in Pokret[0] and "crni kralj" not in Pokret[0]):
                                            cv2.circle(img_rgb3, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]], 10, (0,0,255), 3)
                                    else:
                                        cv2.circle(img_rgb3, pomocni.PoljaPozicija[x + Pokret[1][i]][y + Pokret[2][i]], 25, (0,255,0), 3)
                        i = i+1
                        
                        
def ugrozeno_polje( figura, polje_provere, polje_figure):
    for x in range(8):
        for y in range(8):
            if( "bel" in figura):
                if( "crn" in pomocni.PoljaFigura[x][y]):
                    for Pokret in pomocni.Pokreti:
                        if Pokret[0] == pomocni.PoljaFigura[x][y]:
                            if(ugrozeno_polje_provera( Pokret, pomocni.PoljaIme[x][y], polje_provere, polje_figure)== True):
                                return True
            elif( "crn" in figura):
                if( "bel" in pomocni.PoljaFigura[x][y]):
                    for Pokret in pomocni.Pokreti:
                        if Pokret[0] == pomocni.PoljaFigura[x][y]:
                            if(ugrozeno_polje_provera( Pokret, pomocni.PoljaIme[x][y], polje_provere, polje_figure)== True):
                                return True
    return False
def ugrozeno_polje_provera(Pokret, polje, polje_provere, polje_figure):
    print Pokret[0]
    if( Pokret[3]==1):
        for x in range(8):
            for y in range(8):
                if( pomocni.PoljaIme[x][y] == polje):
                    i = 0;
                    for pokret in Pokret[1]:
                        if( (x + Pokret[1][i] <= 7 and x + Pokret[1][i]>=0 and 
                        y + Pokret[2][i] <= 7 and y + Pokret[2][i]>=0 and "kralj" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]])
                        or (x + Pokret[1][i] <= 7 and x + Pokret[1][i]>=0 and 
                        y + Pokret[2][i] <= 7 and y + Pokret[2][i]>=0 and "kralj" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]] and pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_figure)):
                            if ("crn" in Pokret[0] and "crn" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                            or "crn" in Pokret[0] and "crn" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]] and pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_figure
                            or "crn" in Pokret[0] and "crn" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]] and pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_provere
                            or "bel" in Pokret[0] and "bel" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]] and pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_provere
                            or "bel" in Pokret[0] and "bel" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]] and pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_figure
                            or "bel" in Pokret[0] and "bel" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]):
                                if(pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_provere):
                                    return True
                        i = i+1
    elif( Pokret[3]==0):
        for x in range(8):
            for y in range(8):
                if( pomocni.PoljaIme[x][y] == polje):
                    i = 0;
                    for pokret in Pokret[1]:
                        xx = x;
                        yy = y;
                        while True:
                            if( (xx + Pokret[1][i] <= 7 and xx + Pokret[1][i]>=0 and 
                            yy + Pokret[2][i] <= 7 and yy + Pokret[2][i]>=0 and "kralj" not in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]])
                            or (xx + Pokret[1][i] <= 7 and xx + Pokret[1][i]>=0 and 
                            yy + Pokret[2][i] <= 7 and yy + Pokret[2][i]>=0 and "kralj" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]] and pomocni.PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]] == polje_figure)):
                                if ("crn" in Pokret[0] and "crn" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]] and pomocni.PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]] != polje_figure and pomocni.PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]] != polje_provere
                                or "bel" in Pokret[0] and "bel" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]] and pomocni.PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]] != polje_figure and pomocni.PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]] != polje_provere):
                                    break;
                                elif ("crn" in Pokret[0] and "bel" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]] and pomocni.PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]]!= polje_figure
                                or "bel" in Pokret[0] and "crn" in pomocni.PoljaFigura[xx + Pokret[1][i]][yy + Pokret[2][i]] and pomocni.PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]]!= polje_figure):
                                    #print PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]]
                                    xx = xx + Pokret[1][i]
                                    yy = yy + Pokret[2][i]
                                    if(pomocni.PoljaIme[xx][yy] == polje_provere):
                                        return True
                                    break
                                else:
                                    #print PoljaIme[xx + Pokret[1][i]][yy + Pokret[2][i]]
                                    xx = xx + Pokret[1][i]
                                    yy = yy + Pokret[2][i]
                                    if(pomocni.PoljaIme[xx][yy] == polje_provere):
                                        return True
                            else:
                                break
                        i = i+1
    elif( Pokret[3]==2):
        for x in range(8):
            for y in range(8):
                if( pomocni.PoljaIme[x][y] == polje):
                    i = 0;
                    for pokret in Pokret[1]:
                        if( (x + Pokret[1][i] <= 7 and x + Pokret[1][i]>=0 and 
                        y + Pokret[2][i] <= 7 and y + Pokret[2][i]>=0 and "kralj" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]])
                        or(x + Pokret[1][i] <= 7 and x + Pokret[1][i]>=0 and 
                        y + Pokret[2][i] <= 7 and y + Pokret[2][i]>=0 and "kralj" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]] and pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_figure)):
                            if( Pokret[1][i] ==0 or Pokret[2][i]==0):
                                if (("crn" in Pokret[0] and "crn" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                                or "bel" in Pokret[0] and "bel" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]])
                                and ("crn" in Pokret[0] and "bel" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                                or "bel" in Pokret[0] and "crn" not in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]])):
                                    #print PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]]
                                    aaaa = 5
                            else:
                                if("crn" in Pokret[0] and "bel" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                                or "bel" in Pokret[0] and "crn" in pomocni.PoljaFigura[x + Pokret[1][i]][y + Pokret[2][i]]
                                or pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_provere):
                                    #print PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]]
                                    if(pomocni.PoljaIme[x + Pokret[1][i]][y + Pokret[2][i]] == polje_provere):
                                        return True
                        i = i+1
    return False
                    
        
        
    




App.mainloop()
            
