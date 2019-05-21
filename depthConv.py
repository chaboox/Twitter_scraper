# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:30:09 2019

@author: deboosere_am
"""
import PIL
from PIL import Image
import os

def load_images_from_folder(folder):

    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        img = img.convert('RGB')
        imageWithColorPalette = img.convert( palette=Image.ADAPTIVE, colors=256)
        imageWithColorPalette.save('femalev3/' + filename)


load_images_from_folder('femaleFinal')