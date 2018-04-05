#-------------------------------------------------------------------------------
# Name:       imc.py
# Purpose: imc(Image Metadata Collector).
#The program will collect image metadata.
#Versioning and progress will be managaed through GitHub
#
# Author:      halla, WEGC
#
# Created:     04/04/2018

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
        return self.photoC

    def full_file_name(self): #To show filenames with extensions
        together= fileName + fileExten
        return together

class GUI:

    def writetocsv(self):
        #This what happens upon clicking the "Write to CSV" button
        import csv
        file_name = 'test1.csv' #I prefer csv files are automativally opened by excel rather than notepad

        if self.ready_to_write: #Connects to function that checks data has been validated
            ofile = open(file_name, 'w') #Open file with overwriting permissions.
            writer = csv.writer(ofile, delimiter =",", lineterminator = "\n")
            for record in self.recordlist:
                print(record.full_file_name())
                writer.writerow([record.get_imageID(), record.get_fileName, record.get_fileExtension(), record.get_imageName(), record.get_owner(), record.get_licence(), record.get_photoC()])

            ofile.close()#To Explicitly close file

        else:
            tkinter.messagebox.showwaring("Error!", "You need to validate your data first!")

        self.ready_to_write= False
        tkinter.messagebox.showinfo('Notice',file_name+' File Generated Sucessfully')

GUI()