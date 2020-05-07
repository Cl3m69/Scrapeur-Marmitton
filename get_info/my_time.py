##
## EPITECH PROJECT, 2020
## my_scrapeur
## File description:
## my_name
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os
import readline

def get_time(list):
    chaine = "title-2 recipe-infos__total-time__value"
    fz = open("dbrecette.csv", "a")
    for i in range(len(list)):
        a = 1
        if chaine in list[i]:
            while list[i][a] != '>':
                a += 1
            a += 1
            fz.write('"')
            while list[i][a] != '<':
                fz.write(list[i][a])
                a += 1
            fz.write('"')
            fz.write(',')
            return (0)