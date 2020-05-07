##
## EPITECH PROJECT, 2020
## my_scrapeur
## File description:
## my_steps
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os

def get_steps(list):
    z = 0
    e = 0
    chaine = "<ol class=\"recipe-preparation__list\">"
    finchain = "</ol>"
    steps = "<li class=\"recipe-preparation__list__item\">"
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
                if steps in list[i]:
                    i += 1
                while list[i][a] == '\t':
                    a += 1
                while list[i][a] != '\t' and list[i][a] != '<':
                    if list[i][a] != '"':
                        fz.write(list[i][a])
                    a += 1
                i += 1
                fz.write(';')
                if finchain in list[i]:
                    fz.write('"')
                    fz.write(',')
                    return 0