import numpy as np
from PIL import Image


def discover(image_name):
    image = Image.open(image_name)
    data = np.array(image).copy()

    tour =0
    taille = ""
    message = ""
    taille_new = 12673
    y=0
    for line in data:
        x=0
        for colonne in line:
            rgb=0
            for color in colonne:
                valeur = data[y][x][rgb]
                binaire = bin(valeur)[2:]
                last = binaire[-1]
                if tour <16:
                    taille += last
                if tour == 16:
                    taille_new=int(taille,2)
                if tour-16 < taille_new :
                    message += last
                if tour -16 >= taille_new :
                    break
                tour +=1
                rgb +=1
                if tour -16 >= taille_new :
                    break
            x +=1
            if tour -16 >= taille_new :
                    break
        y +=1
    print(message)
    octet=[]
    result=""
    for i in range(len(message)//8):
        octet.append(message[i*8:(i+1)*8])
    # print(octet)
    for oct in octet :
        index=int(oct,2)
        lettre_ascii=chr(index)
        print(lettre_ascii)
        result+=lettre_ascii
    print("MESSAGE:", str(result)[2:])


discover("SECRET.png")