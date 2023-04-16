#Importar Librería
import pywhatkit
from tkinter import filedialog

# https://github.com/Ankit404butfound/PyWhatKit/wiki/ASCII-Art


#Seleccionar Imgagen (PNG / JPG)
img1 = filedialog.askopenfilename(initialdir="/", title="Seleccionar imagen", filetypes=(("Archivos PNG","*.png"),("Archivos JPG","*.jpg")))
img_str=str(img1)

#Crear Ascii text
pywhatkit.image_to_ascii_art(img_str)

