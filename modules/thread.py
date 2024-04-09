import threading
from .convert import convertir_fichier
from .filter import filter_images
from .utils import is_valid_image


class MultiThread(threading.Thread):
    """
    Extension de la classe Threading utilisée pour le traitement multitâche des fichiers.

    Params:
    - threading.Thread: Classe de base pour créer des threads.
    """

    def __init__(
        self,
        name,
        files,
        dossier_source,
        dossier_destination,
        type,
        selected=[],
    ):
        """
        Initialisation de la classe MultiThread.

        Params:
        - self (MultiThread): L'instance de la classe MultiThread.
        - name (str): Nom du thread.
        - files (list): Liste des fichiers à traiter par ce thread.
        - dossier_source (str): Le chemin du dossier source.
        - dossier_destination (str): Le chemin du dossier de destination.
        """
        threading.Thread.__init__(self)
        self.name = name
        self.files = files
        self.dossier_source = dossier_source
        self.dossier_destination = dossier_destination
        self.type = type
        self.selected = selected

    def run(self):
        """
        Méthode exécutée lorsqu'un thread est démarré.
        Elle appelle la fonction pour convertir les fichiers.

        Params:
        - self (MultiThread): L'instance de la classe MultiThread.
        """
        print("Starting " + self.name)
        for fichier in self.files:
            if (
                fichier.endswith(".tif")
                and is_valid_image(self.dossier_source, fichier) == True
            ):
                if self.type == "convert":
                    convertir_fichier(
                        fichier, self.dossier_source, self.dossier_destination
                    )
                elif self.type == "filter":
                    file = filter_images(
                        fichier, self.dossier_source, self.dossier_destination
                    )
                    if file:
                        self.selected.append(file)
                else:
                    print("Type de traitement non reconnu.")
            else:
                print(f"Le fichier {fichier} n'est pas un fichier TIFF.")
        print("Exiting", self.name)
