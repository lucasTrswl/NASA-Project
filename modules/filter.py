import cv2
import numpy as np
import os
from tqdm import tqdm
import time

def filter_images(filename, folder_source, folder_destination):
    """
    Compare les images dans un dossier et filtre celles qui ont une différence de niveau de gris de 1.5% ou plus par rapport à la première image.
    Et le sauvegarde dans le dossier de destination.

    Params:
    - filname (str): Le nom du fichier à traiter.
    - folder_source (str): Le chemin du dossier source.
    - folder_destination (str): Le chemin du dossier de destination.
    """

    # Seuil de différence en pourcentage (Default = 1.5%)
    difference_threshold = 1.5

    # Charger la première image pour obtenir sa valeur moyenne
    first_image_path = os.path.join(folder_source, "slice00000.tif")
    first_image = cv2.imread(first_image_path, cv2.IMREAD_GRAYSCALE)
    first_mean = np.mean(first_image)

    # Comparer le fichier avec la première image
    image_path = os.path.join(folder_source, filename)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    mean_value = np.mean(image)
    difference_percentage = ((mean_value - first_mean) / first_mean) * 100
    if abs(difference_percentage) >= difference_threshold:
        return filename
    else:
        return None