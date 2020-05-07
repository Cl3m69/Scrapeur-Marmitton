##
## EPITECH PROJECT, 2020
## my_scrapeur
## File description:
## scrap_info_recette
##

import readline
from sys import argv, stderr
import pycurl
from io import BytesIO 
import subprocess
import os
import readline

def newnumber(i):
    numberpage = str(i)
    return numberpage

def my_scrap(string_url):
    b_obj = BytesIO() 
    crl = pycurl.Curl() 

    # Set URL value
    crl.setopt(crl.URL, string_url)

    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)

    # Perform a file transfer 
    crl.perform() 

    # End curl session
    crl.close()

    # Get the content stored in the BytesIO object (in byte characters) 
    get_body = b_obj.getvalue()

    # Decode the bytes stored in get_body to HTML and print the result 
    # print('Output of GET request:\n%s' % get_body.decode('utf8'))
    fd = open("scriptrecette.txt", "w")
    fd.write(get_body.decode('utf8'))
    results = subprocess.check_output('cat scriptrecette.txt | grep "recipe-card-link"', shell=True)
    fs = open("linkrecette.txt", "a")
    fs.write(results.decode('utf8'))

if __name__=="__main__":
    i = 0
    a = 35
    p = 0
    string_urle = "https://www.marmiton.org/recettes/?page="

    while i < 450:
        numberpage = newnumber(i)
        string_url = string_urle + numberpage
        my_scrap(string_url)
        i += 1
    i = 0
    fl = open("linkentre.txt", "a")
    fd = open("linkrecette.txt", "r")
    link = fd.read()
    list = link.split('\n')
    while i < len(list):
        while a < len(list[i]) - 2:
            fl.write(list[i][a])
            a += 1
        fl.write("\n")
        a = 35
        i += 1
    exit (0)