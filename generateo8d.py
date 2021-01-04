import csv
import uuid
import xml.etree.ElementTree as ET
import os
from shutil import copyfile
from shutil import make_archive
from shutil import rmtree

fileName = "AsylumUUID.csv"
imageFolder = "asylumImage/"
setName = "Asylum"
language = "French"

folderName = setName + " (" + language + ")"

with open(fileName, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')  
    setUUID =  next(reader)[1]
    
    os.mkdir(folderName)
    os.mkdir(folderName+"/c904355f-7774-43d1-ab8e-f48f0820ad48")
    os.mkdir(folderName+"/c904355f-7774-43d1-ab8e-f48f0820ad48/Sets")
    folderOutImage = folderName+"/c904355f-7774-43d1-ab8e-f48f0820ad48/Sets/" + setUUID
    os.mkdir(folderOutImage)
    os.mkdir(folderOutImage+"/Cards")

       
    indexCard = 1
    for line in reader:
        cardUUID = line[1]
       
        copyfile(imageFolder+str(indexCard)+"b.jpg", folderOutImage+"/Cards/" + cardUUID + ".jpg")
        copyfile(imageFolder+str(indexCard)+"f.jpg", folderOutImage+"/Cards/" + cardUUID + ".b.jpg")

        indexCard += 1
    
    make_archive(folderName,"zip",folderName)
    copyfile(folderName+".zip",folderName+".o8c")
    os.remove(folderName+".zip")
    rmtree(folderName)