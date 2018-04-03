#-------------------------------------------------------------------------------
# Name:       imc.py
# Purpose: imc(Image Metadata Collector).
#The program will collect image metadata.
#Versioning and progress will be managaed through GitHub
#
# Author:      halla, WEGC
#
# Created:     04/04/2018

#import GUI library
from tkinter import *

#for Python V3 you must explicitely load the messagebox
import tkinter.messagebox

class ImageMD:
    #Image Metadata
    def __init__(self, imageID, fileName, fileExtension, imageName, owner, licence, photoCategory):
        self.imageID= imageID
        self.fileName= fileName
        self.fileExten= fileExtension
        self.name= imageName
        self.owner= owner
        self.licence= licence
        self.photoC= photoCategory

    def get_imageID(self):
        return self.imageID

    def get_fileName(self):
        return self.fileName

    def get_fileExten(self):
        return self.fileExten

    def get_name(self):
        return self.name

    def get_owner(self):
        return self.owner

    def get_licence(self):
        return self.licence

    def get_photoC(self):
        return self.photoT


class GUI:
    #default colour variables makes changing colours easier
    bkcolour= '#c0deed'
    maintxtcolour= 'black'
    mainfont = ('Times', '24')

    def __init__(self):

        window = Tk()
        window.title("Data Entry for Image Metadata")
        window.minsize(width = 400, height= 600)

        heading_label = Lable(window, bg = bkcolour, fg = maintxtcolour, text= "TITLE HERE", font= mainfont)
        header_label.pack()

        #creating label and field variable in GUI for each entry field
        fileName_label = Label(window, text='Please enter the filename:')
        fileName_label.pack(anchor="c") #.pack() places the component in the window
        self.fileName_field = Entry(window)
        self.fileName_field.pack(anchor="c")

        #code for dropdown menu
