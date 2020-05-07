##
## EPITECH PROJECT, 2020
## my_scrapeur
## File description:
## my_particulier
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os

def get_particularite(list):
    chaine = "recipe-particularities__container"
    fz = open("dbrecette.csv", "a")

    for i in range(len(list)):
        a = 0
        if chaine in list[i]:
            while list[i+1][a] != ':':
                a += 1
            a += 2
            fz.write('"')
            while list[i+1][a] != '<' and list[i+1][a] != 0:
                fz.write(list[i+1][a])
                a += 1
            fz.write('"')
            fz.write('\n')
            return (0)
    fz.write('\n')