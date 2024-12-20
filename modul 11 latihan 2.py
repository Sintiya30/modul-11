#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:06:13 2024

@author: adesintia
"""

class SimpleInputHandler:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, int):
            self._value = new_value
        else:
            print("Nilai inputan harus berupa integer.")

    def change_value(self):
        while True:
            try:
                new_input = int(input("Masukkan nilai baru: "))
                self.value = new_input
                break
            except ValueError:
                print("Masukkan nilai integer yang valid.")

    def display_value(self):
        print(f"Nilai saat ini: {self._value}")


input_handler = SimpleInputHandler()
input_handler.change_value()
input_handler.display_value()
input_handler.change_value()
input_handler.display_value()