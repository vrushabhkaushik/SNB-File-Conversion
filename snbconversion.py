import os
import glob
import zipfile
import xml.etree.ElementTree as ET

path = "C:\\Users\\VrushabhKaushik\\Downloads\\SMemo\\SMemo"
#filename = "Shun am jivi janashe khrekhar"

for filename in glob.glob(os.path.join(path, '*.snb')):
    zip_ref = zipfile.ZipFile(filename, 'r')
    
    #getting file name without extension
    file_name = filename.split('.')

    #unzipping snb file to a folder
    zip_ref.extractall(file_name[0])
    zip_ref.close()

    #parsing snote.xml where the whole content of snb file exists
    xmlTree = ET.parse(file_name[0]+"\\snote\\snote.xml")
    root = xmlTree.getroot()

    #getting textual data to string from xml
    data = (ET.tostring(root, encoding='utf-8', method='text')).decode('utf-8')

    #removing extra spaces and formatting the textual data
    formatted_data = ' '.join(data.split())
    print(formatted_data)
    f = open(file_name[0]+".txt", 'w', encoding='utf-8')
    f.write(formatted_data)
    f.close()

