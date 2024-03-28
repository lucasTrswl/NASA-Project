"""
Classe MultiThread + exemple d'utilisation
"""

import threading
import time


class MultiThread(threading.Thread):
    """
    Extension de la classe Threading
    Params:
    - name : nom du Thread
    - delay : delay pour chaque thread
    """

    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        # exemple de function
        print("Starting " + self.name)
        time.sleep(self.delay)
        print("Exiting {self.name} with delay of {self.delay}s")


# Créer des tâches
thread1 = MultiThread("Thread-1", 10)
thread2 = MultiThread("Thread-2", 5)

# commencer des tâches
thread1.start()
thread2.start()
# Rejoindre la tâche principale
thread1.join()
thread2.join()
print("Exiting Main Thread")
