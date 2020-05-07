#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 
## File description:
## 
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os
import readline
from get_info.my_image import get_image
from get_info.my_name import get_name
from get_info.my_time import get_time
from get_info.my_nbpers import get_nbpers
from get_info.my_steps import get_steps
from get_info.my_rating import get_rating
from get_info.my_particulier import get_particularite
from get_info.my_ingredients import get_ingredients

def my_scrap_no_script():
    fd = open("info_recette_script.txt", "r")
    info_script = fd.read()
    list = info_script.split('\n')
    get_name(list)
    get_image(list)
    get_time(list)
    get_nbpers(list)
    get_steps(list)
    get_ingredients(list)
    get_rating(list)
    get_particularite(list)

def get_info_recette(get_body):
    i = 0
    a = 0

    fl = open("info_recette_script.txt", "a")
    while i < len(get_body):
        if get_body[i] == 'a' and get_body[i+1] == 'f' and get_body[i+2] == '-' and get_body[i+3] == 'c' and get_body[i+4] == 'o' and get_body[i+5] == 'l' and get_body[i+6] == 's':
            i += 6
            while a == 0:
                if get_body[i] == 'a' and get_body[i+1] == 'f' and get_body[i+2] == '-' and get_body[i+3] == 'c' and get_body[i+4] == 'o' and get_body[i+5] == 'l' and get_body[i+6] == 's':
                    a = 1
                fl.write(get_body[i])
                i += 1
        i += 1

def my_scrap_html_script(url):
    b_obj = BytesIO() 
    crl = pycurl.Curl() 

    # Set URL value
    crl.setopt(crl.URL, url)

    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)

    # Perform a file transfer 
    crl.perform() 

    # End curl session
    crl.close()

    # Get the content stored in the BytesIO object (in byte characters) 
    get_body = b_obj.getvalue()

    # Decode the bytes stored in get_body to HTML and print the result
    get_info_recette(get_body.decode('utf8'))

if __name__=="__main__":
    i = 0
    
    fd = open("linkentre.csv", "r")
    stringlink = fd.read()
    list = stringlink.split('\n')
    while i < 20:
        url = list[i]
        my_scrap_html_script(url)
        my_scrap_no_script()
        os.remove("info_recette_script.txt")
        i += 1
    exit (0)