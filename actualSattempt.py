# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 01:42:16 2016
Modified on Sat Jul 14 12:50:45 2019

@author: Ryan Asher
"""

import random as rn
import os
import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def gal(g_url, name):    
    """Finds the link and name of galleries for name. Passes them
       to get_images.
       
       g_url (string) -- the url for the girl
       name  (string) -- the name of the girl
    """
    
    #initializing bs4 with the g_url
    r = requests.get(g_url)
    soup = BeautifulSoup(r.content, 'lxml')
    
    #creates a list of lists of all html div elements with the id tmbcont
    g_data = soup.find_all("div", {"id":"tmbcont"})
    
    #parses through g_data, for html img elements with class t
    #then saves all g_names and g_links. Determines dl path, then
    #passes data to get_images.
    for link in g_data:
         for lnk in link:
            if lnk.find_all("img", {"class":"t"}):
                try:
                    g_name = lnk.contents[0].find_all("img")[0]['alt']
                    rg_name = g_name + str(rn.randrange(1,1000))
                    g_link = 'http://shemalestardb.com' + \
                             lnk.contents[0].get('href')
                    
                    #Creates download directory
                    path = r"C:/Users/RyanTAsher/Desktop/Downloads"
                    path = os.path.join(path, name)
                    path = os.path.join(path, rg_name)
                    if not os.path.exists(path):
                        os.makedirs(path)    
                        
                    get_images(g_link, rg_name, path, name)
                    
                except:
                    pass
                
def get_images(g_link, rg_name, path, name):
    """Retrieves the images from each gallery for the girl.
    
    g_link  (string) -- the link of the gallery
    rg_name (string) -- the girls name appended with a random number
    path    (string) -- the designated path for download
    """
    
    #initializing bs4 with the g_link
    r = requests.get(g_link)
    soup = BeautifulSoup(r.content, 'lxml')
    
    #creates a list of lists of all div elements with the class 
    #gallery-content container
    g_data = soup.find_all("div", {"class":"gallery-conent container"})
    
    #downloads each picture from each gallery by parsing g_data
    #while counting with number
    number = 1
    while number <= 1:
        for link in g_data:
            for each in link:
                try:
                    final_links = each['href']
                    final_url = 'http://www.shemalestardb.com' + final_links
                    print(str(number)) 
                    urlretrieve(final_url, path + "\\" + name + "_" + \
                                str(number) + ".jpg")
                    number += 1
                except:
                    pass
        break


def start(name):
    """Starts the program given name(s)
    
    names (list/string) -- A list of names, or a single name
    """
    
    #generates url based on name
    f_letter = name[0]
    g_url = "http://shemalestardb.com/stars/" + f_letter + "/" + name               
    gal(g_url, name)


if __name__ == "__main__":
    
    #prompt user for entry choice
    choice = input("Name List (1) or Individual (2): ")
    
    #if choice 1, start program with a namelist
    if int(choice) == 1:
        with open(r'C:/Users/RyanTAsher/names.txt') as f:
            lines = f.read().splitlines()
        for names in lines:
            start(names)
    
    #if choice 2, start program with no namelist
    elif int(choice) == 2:
        name = input("What is the name? (If space, use underscore): ")
        start(name)
        
    
    

    

