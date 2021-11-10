# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 22:23:55 2021

@author: Rudolf
"""

def faktorial(angka):
    faktor = 1
    for i in range(1, angka + 1):
        faktor *= i
    return faktor

masuk = int(input("PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA\nMasukkan angka: "))
print("Nilai faktorialnya adalah:", faktorial(masuk))