import os
from modules.thread import MultiThread

def filter_manager(type, dossier_source, dossier_destination):
    """
    Fonction principale pour coordonner la conversion des fichiers en utilisant des threads.
    """
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

    return selected