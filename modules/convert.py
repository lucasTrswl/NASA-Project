import os
from PIL import Image

def convertir_fichier(nom_fichier, dossier_source, dossier_destination):
    """
    Convertit un fichier d'image 16 bits en 8 bits et le sauvegarde dans le dossier de destination.
    
    Params:
    - nom_fichier (str): Le nom du fichier à convertir.
    - dossier_source (str): Le chemin du dossier source.
    - dossier_destination (str): Le chemin du dossier de destination.
    """
    chemin_source = os.path.join(dossier_source, nom_fichier)
    image_16bit = Image.open(chemin_source)
    min_val = image_16bit.getextrema()[0]
    max_val = image_16bit.getextrema()[1]
    image_16bit = image_16bit.point(lambda x: 255 * (x - min_val) / (max_val - min_val))
    image_8bit = image_16bit.convert("L")
    nom_fichier_sans_extension = os.path.splitext(nom_fichier)[0]
    nom_fichier_converti = nom_fichier_sans_extension + ".tif"
    chemin_destination = os.path.join(dossier_destination, nom_fichier_converti)
    image_8bit.save(chemin_destination)