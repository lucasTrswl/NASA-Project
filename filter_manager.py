import os
import time
from modules.thread import MultiThread

import os
import time
from modules.thread import MultiThread

def filter_manager(type, dossier_source, dossier_destination):
    """
    Fonction principale pour coordonner la conversion des fichiers en utilisant des threads.
    """
    debut_total = time.time()

    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    fichiers = sorted(os.listdir(dossier_source))
    batch_size = 50
    threads = []
    selected = []

    num_files = len(fichiers)
    num_threads = (num_files + batch_size - 1) // batch_size
    for i in range(num_threads):
        debut_batch = i * batch_size
        fin = min(debut_batch + batch_size, num_files)
        batch_files = fichiers[debut_batch:fin]
        thread = MultiThread("Thread-" + str(i + 1), batch_files, dossier_source, dossier_destination, type, selected)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    temps_ecoule_total = time.time() - debut_total
    print("\nLa conversion a pris", temps_ecoule_total, "secondes.")
    return selected

# if __name__ == "__main__":
#     # Définir le type de traitement à effectuer : 'convert' ou 'filter'
#     type = "filter"
#     print("Type de traitement:", type)

#     # Chemins des dossiers source et destination
#     dossier_source = "../img_source/ECHO-DOT"
#     # dossier_source = "../MultiThread-Converted-ECHO-DOT"
#     # dossier_source = "../uSD"
#     # dossier_source = '../MultiThread-Converted-uSD'

#     dossier_destination = "../filtered_images"
    
#     # filter_manager(type, dossier_source, dossier_destination)
#     print(filter_manager(type, dossier_source, dossier_destination))
