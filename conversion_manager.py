import os
import time
from modules.thread import MultiThread

def conversion_manager():
    """
    Fonction principale pour coordonner la conversion des fichiers en utilisant des threads.
    """
    # Mesurer le temps écoulé avant de commencer les opérations
    debut_total = time.time()

    # Chemins des dossiers source et destination
    dossier_source = "../ECHO-DOT"
    dossier_destination = "../MultiThread-Converted-ECHO-DOT"

    # Vérifier si le dossier de destination existe, sinon le créer
    if not os.path.exists(dossier_destination):
        os.makedirs(dossier_destination)

    # Parcourir tous les fichiers dans le dossier source
    fichiers = os.listdir(dossier_source)

    # Créer les threads par lots de 50 fichiers
    batch_size = 50 
    threads = []

    num_files = len(fichiers)
    num_threads = (num_files + batch_size - 1) // batch_size

    for i in range(num_threads):
        debut_batch = i * batch_size
        fin = min(debut_batch + batch_size, num_files)
        batch_files = fichiers[debut_batch:fin]
        thread = MultiThread("Thread-" + str(i + 1), batch_files, dossier_source, dossier_destination)
        threads.append(thread)

    # Démarrer les threads
    for thread in threads:
        thread.start()

    # Attendre la fin de chaque thread
    for thread in threads:
        thread.join()

    # Calculer le temps écoulé
    temps_ecoule_total = time.time() - debut_total
    print("La conversion a pris", temps_ecoule_total, "secondes.")

if __name__ == "__main__":
    conversion_manager()
