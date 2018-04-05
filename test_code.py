#-------------------------------------------------------------------------------
# Name:        test code
# Purpose: To trial and test small sections of code
#
# Author:      halla
#
# Created:     06/04/2018

file_name = "."
while "." in file_name:
    file_name = input("Please create a file name for information to be written to. Do not include file extension.")
    if "." in file_name: #This because most file extensions have leeding full stops
        print ("Please no file extensions or punctuation")
    file_name = file_name + ".csv"
    print (file_name)