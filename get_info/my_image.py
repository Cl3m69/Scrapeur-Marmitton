##
## EPITECH PROJECT, 2020
## my_scrapeur
## File description:
## get_image
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os

def get_image(list):
    chaine = "af-diapo-desktop-0_img"
    fz = open("dbrecette.csv", "a")

    for i in range(len(list)):
        a = 0
        if chaine in list[i]:
            while list[i+1][a] != '"':
                a += 1
            a += 1
            fz.write('"')
            while list[i+1][a] != '"':
                fz.write(list[i+1][a])
                a += 1
            fz.write('"')
            fz.write(',')
            return (0)