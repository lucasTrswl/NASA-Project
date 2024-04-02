import os
import time
from PIL import Image
import threading

# DEBUG : Mesurer le temps écoulé
debut = time.time()

# Chemins des dossiers source et destination
dossier_source = "../../ECHO-DOT"
dossier_destination = "../../MultiThread-Converted-ECHO-DOT"

# Vérifier si le dossier de destination existe, sinon le créer
if not os.path.exists(dossier_destination):
    os.makedirs(dossier_destination)

# Fonction pour convertir et renommer un fichier
def convertir_fichier(nom_fichier):
    chemin_source = os.path.join(dossier_source, nom_fichier)
    image_16bit = Image.open(chemin_source)
    min_val = image_16bit.getextrema()[0]
    max_val = image_16bit.getextrema()[1]
    image_16bit = image_16bit.point(lambda x: 255 * (x - min_val) / (max_val - min_val))
    image_8bit = image_16bit.convert("L")
    nom_fichier_sans_extension = os.path.splitext(nom_fichier)[0]
    nom_fichier_converti = nom_fichier_sans_extension + "_8bit.tif"
    chemin_destination = os.path.join(dossier_destination, nom_fichier_converti)
    image_8bit.save(chemin_destination)

# Fonction pour convertir et renommer une liste de fichiers
def convertir_fichiers(files):
    for fichier in files:
        if fichier.endswith('.tif'):
            convertir_fichier(fichier)

# Fonction pour créer les threads
def creer_threads(fichiers, batch_size):
    threads = []
    num_files = len(fichiers)
    num_threads = (num_files + batch_size - 1) // batch_size

    for i in range(num_threads):
        debut = i * batch_size
        fin = min(debut + batch_size, num_files)
        batch_files = fichiers[debut:fin]
        thread = MultiThread("Thread-" + str(i + 1), batch_files)
        threads.append(thread)
    return threads


# Classe MultiThread
class MultiThread(threading.Thread):
    """
    Extension de la classe Threading
    Params:
    - name : nom du Thread
    - files : liste des fichiers à traiter par ce thread
    """

    def __init__(self, name, files):
        threading.Thread.__init__(self)
        self.name = name
        self.files = files

    def run(self):
        print("Starting " + self.name)
        convertir_fichiers(self.files)
        print("Exiting", self.name)

# Parcourir tous les fichiers dans le dossier source
fichiers = os.listdir(dossier_source)

# Créer les threads par lots de 50 fichiers
batch_size = 50 
threads = creer_threads(fichiers, batch_size)

# Commencer les threads
for thread in threads:
    thread.start()

# Attendre la fin de chaque thread
for thread in threads:
    thread.join()

# DEBUG : Calculer le temps écoulé
temps_ecoule = time.time() - debut
print("La conversion a pris", temps_ecoule, "secondes.")
