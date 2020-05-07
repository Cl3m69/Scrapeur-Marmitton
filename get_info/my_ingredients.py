##
## EPITECH PROJECT, 2020
## my_scrapeur
## File description:
## my_ingredients
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os

def get_ingredients(list):
    z = 0
    e = 0
    chaine = "<ul class=\"recipe-ingredients__list\">"
    finchain = "</ul>"
    ingredients = "data-name-plural"
    fz = open("dbrecette.csv", "a")

    for i in range(len(list)):
        a = 0
        if chaine in list[i]:
            while e == 0:
                if z == 0:
                    fz.write('"')
                    i += 1
                    z = 1
                a = 0
                if ingredients in list[i]:
                    while list[i][a] != '=':
                        a += 1
                    a += 1
                    while list[i][a] != '=':
                        a += 1
                    a += 2
                    while list[i][a] != '"' and list[i][a] != 0:
                        if list[i][a] == '&' and list[i][a+1] == 'i':
                            fz.write('î')
                            a += 6
                        elif list[i][a] == '&' and list[i][a+1] == 'e':
                            fz.write('é')
                            a += 7
                        else:
                            fz.write(list[i][a])
                        a += 1
                    fz.write(';')
                i += 1
                if finchain in list[i]:
                    fz.write('"')
                    fz.write(',')
                    return 0