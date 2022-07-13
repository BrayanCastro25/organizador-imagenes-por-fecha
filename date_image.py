from PIL import Image
from PIL.ExifTags import TAGS
import pathlib
import os
import re

directory_actual = pathlib.Path(__file__).parent.absolute()

print(directory_actual)
contenido = os.listdir(directory_actual)

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret['DateTimeOriginal']

cont = 0
screen = 0
what = 0
no_type = 0


name_months = ["1. Enero", "2. Febrero", "3. Marzo", "4. Abril", "5. Mayo", "6. Junio", 
          "7. Julio", "8. Agosto", "9. Septiembre", "10. Octubre", "11. Noviembre", "12. Diciembre"]

for i in contenido:
    
    print(i)

    try:
        direc = "{}/{}".format(directory_actual, i)
        date = get_exif(direc)
        date = date.replace(" ", ":")
        date = date.split(":")
        year = date[0]
        month = date[1]
        folder_month = name_months[int(month) - 1]
        print("Año:", year, "Mes:", folder_month, "[ORIGINAL]")
        cont += 1
        if i.find("Screenshot") != -1:
            folder_principal = "Screenshot"
        else:    
            folder_principal = "Cámara"

    except:
        if i.find("Screenshot") != -1:
            screen += 1
            date = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", i)
            date = date[0] 
            year = date[0:4]
            month = date[4:6]
            folder_month = name_months[int(month) - 1]
            print("Año:", year, "Mes:", folder_month, "[SCREENSHOT]")
            folder_principal = "Screenshot"

        elif i.find("WA") != -1:
            what += 1
            date = re.findall("[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]", i)
            date = date[0]
            year = date[0:4]
            month = date[4:6]
            folder_month = name_months[int(month) - 1]
            print("Año:", year, "Mes:", folder_month, "[WHATSAPP]")
            folder_principal = "Whatsapp"

        elif i.find("WhatsApp Image") != -1:
            what += 1
            date = re.findall("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", i)
            date = date[0]
            year = date[0:4]
            month = date[5:7]
            folder_month = name_months[int(month) - 1]
            print("Año:", year, "Mes:", folder_month, "[WHATSAPP]")
            folder_principal = "Whatsapp"
            
        else:
            print("NO TYPE")
            no_type += 1
            folder_principal = "Desconocido"

    if i != "date_image.py":
        if(folder_principal == "Desconocido"):
            new_folder = "{}/{}/".format(directory_actual, folder_principal)
        else:
            new_folder = "{}/{}/{}/{}/".format(directory_actual, folder_principal, year, folder_month)
        pathlib.Path(new_folder).mkdir(parents = True, exist_ok = True)
        os.rename(direc, "{}/{}".format(new_folder, i))

    print()

print(cont, len(contenido))
print("Screen:", screen)
print("What:", what)
print("No type", no_type)

