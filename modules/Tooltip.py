import tkinter as tk
from tkinter import ttk
from global_style import couleur_gris


class ToolTip:
    """
    Classe pour afficher une tooltip sur un widget lorsqu'il est survolé par la souris.

    Params:
    - widget: Le widget sur lequel afficher l'tooltip (Widget).
    - text : Le texte à afficher dans  la tooltip (string).
    """

    def __init__(self, widget, text):
        """
        Initialise un nouvel objet ToolTip.

        Parameters:
        - widget : Le widget sur lequel afficher la tooltip. (Widget)
        - text : Le texte à afficher dans la tooltip. (string)
        """
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.on_enter)
        self.widget.bind("<Leave>", self.on_leave)
        self.widget.bind("<Motion>", self.on_motion)

    def on_enter(self, event):
        """
        Méthode appelée lorsque la souris entre dans la zone du widget.

        Params:
        - event : L'événement associé à l'entrée de la souris dans le widget.
        """
        self.tooltip = tk.Toplevel(self.widget)
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 75
        y += self.widget.winfo_rooty() + 50
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        ttk.Label(
            self.tooltip,
            text=self.text,
            background=couleur_gris,
            relief="solid",
            borderwidth=0,
            padding=(5, 5),
        ).pack()

    def on_leave(self, event):
        """
        Méthode appelée lorsque la souris quitte la zone du widget.

        Params:
        - event: L'événement associé à la sortie de la souris du widget.
        """
        if hasattr(self, "tooltip"):
            self.tooltip.destroy()

    def on_motion(self, event):
        """
        Méthode appelée lorsque la souris se déplace sur la zone du widget.

        Params:
        - event : L'événement associé au mouvement de la souris sur le widget.
        """
        if self.tooltip and self.tooltip.winfo_exists():
            x, y = event.x_root + 15, event.y_root + 15
            self.tooltip.geometry(f"+{x}+{y}")
