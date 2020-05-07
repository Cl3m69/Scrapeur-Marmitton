##
## EPITECH PROJECT, 2020
## my_scrapeur
## File description:
## my_rating
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os

def get_rating(list):
    u = 0
    chaine = "recipe-infos-users__rating"
    fz = open("dbrecette.csv", "a")

    for i in range(len(list)):
        a = 0
        if chaine in list[i]:
            while u == 0:
                if list[i][a] == 'r' and list[i][a+1] == 'a' and list[i][a+2] == 't' and list[i][a+3] == 'i':
                    while list[i][a] != '>':
                        a += 1
                    a += 1
                    fz.write('"')
                    while list[i][a] != '<':
                        if list[i][a] == '.':
                            fz.write(',')
                        else: 
                            fz.write(list[i][a])
                        a += 1
                    fz.write('"')
                    fz.write(',')
                    return (0)
                a += 1