#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 10:38:03 2024

@author: adesintia
"""

class Mahasiswa:
    def __init__(self, nama, nim, angkatan):
        self.nama = nama
        self.nim = nim
        self.angkatan = angkatan

    def tampilkan_biodata(self):
        print(f"Nama: {self.nama}\nNIM: {self.nim}\nAngkatan: {self.angkatan}")



nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
angkatan = input("Masukkan Angkatan: ")


mahasiswa = Mahasiswa(nama, nim, angkatan)
print("\nData Mahasiswa:")
mahasiswa.tampilkan_biodata()

print("\nTotal Mahasiswa: 1")