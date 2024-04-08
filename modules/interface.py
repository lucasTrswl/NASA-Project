import os
import tkinter as tk
from tkinter import ttk
from global_style import couleur_blanc, couleur_bleu, couleur_gris_clair
from .Tooltip import ToolTip
import textwrap

DIVIDE_WINDOW_WIDTH_BY = 120


def truncate_text(text, max_lines=2):
    """
    Permet de fractionner un texte en plusieurs ligne et de recupérer un certain nombre de ligne.
    Params:
    - text : Chaine de caractères. (string)
    - max_lines: Nombre de ligne. (int)
    """
    wrapper = textwrap.TextWrapper(width=12)
    wrapped_text = wrapper.wrap(text)
    truncated_text = "\n".join(wrapped_text[:max_lines])
    return truncated_text


def open_folder_window(folder):
    """
    Permet d'ouvrir une fenêtre au clique d'un dossier.
    Params :
    - folder : Nom de fichier. (string)
    """
    new_window = tk.Toplevel()
    new_window.title("Dossier " + folder)
    content_label = ttk.Label(new_window, text="Dossier " + folder)
    content_label.pack()


def show_folders(frame, window_width):
    """
    Affiche la liste de tous les projets créés.
    Params :
    - frame : Instance de tkinter. (Frame)
    - window_width: Largeur de la fenêtre. (float)
    """
    folder_path = "Mes projets"
    style = ttk.Style()
    style.configure(
        "List.TButton",
        padding=(10, 20),
        relief="flat",
        compound=tk.TOP,
        width=10,
        wraplength=90,
        justify="center",
        borderwidth=0,
        foreground=couleur_bleu,
        background=couleur_blanc,
    )
    style.map(
        "List.TButton",
        background=[
            ("active", couleur_gris_clair),
            ("disabled", couleur_blanc),
        ],
    )
    folders = [
        folder
        for folder in os.listdir(folder_path)
        if os.path.isdir(os.path.join(folder_path, folder))
    ]

    for widget in frame.winfo_children():
        widget.destroy()

    num_columns = max(1, window_width // DIVIDE_WINDOW_WIDTH_BY)
    for i, folder in enumerate(folders):
        row = i // num_columns
        column = i % num_columns
        photo_icon = tk.PhotoImage(file="assets/folder.png").subsample(6)
        truncated_title_folder = truncate_text(folder)
        folder_button = ttk.Button(
            frame,
            style="List.TButton",
            text=truncated_title_folder,
            image=photo_icon,
            command=lambda folder=folder: open_folder_window(folder),
        )
        folder_button.image = photo_icon
        ToolTip(folder_button, folder)
        folder_button.grid(row=row, column=column, padx=5, pady=5)


def scroll_with_mousewheel_x(canvas):
    """
    Permet d'activer le scroll horizontal avec la molette ou le pavé tactile.
    Params:
    - canvas : Instance de tkinter. (Canvas)
    """
    canvas.bind_all(
        "<Shift-MouseWheel>", lambda e: on_mousewheel_x(event=e, canvas=canvas)
    )


def on_mousewheel_y(event, canvas):
    """
    Calcul du scroll vertical avec la molette ou le pavé tactile.
    Params:
    - canvas : Instance de tkinter. (Canvas)
    """
    canvas.yview_scroll(int(-1 * (event.delta // 120)), "units")


def on_mousewheel_x(event, canvas):
    """
    Calcul du scroll horizontal avec la molette ou le pavé tactile.
    Params:
    - canvas : Instance de tkinter. (Canvas)
    - event : L'événement associé.
    """
    canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")


def scroll_with_mousewheel_y(canvas):
    """
    Permet d'activer le scroll vertical avec la molette ou le pavé tactile
    Params:
    - canvas : instance de tkinter(Canvas)
    - event : L'événement associé.
    """
    canvas.bind_all(
        "<MouseWheel>", lambda e: on_mousewheel_y(event=e, canvas=canvas)
    )
    canvas.bind_all(
        "<Button-4>", lambda e: on_mousewheel_y(event=e, canvas=canvas)
    )
    canvas.bind_all(
        "<Button-5>", lambda e: on_mousewheel_y(event=e, canvas=canvas)
    )


def unscroll_with_mousewheel_x(canvas):
    """
    Permet de désactiver le scroll horizontal avec la molette ou le pavé tactile
    Params:
    - canvas : instance de tkinter(Canvas)
    """
    canvas.unbind_all("<Shift-MouseWheel>")


def unscroll_with_mousewheel_y(canvas):
    """
    Permet de désactiver le scroll vertical avec la molette ou le pavé tactile
    Params:
    - canvas : instance de tkinter(Canvas)
    """
    canvas.unbind_all("<MouseWheel>")
    canvas.unbind_all("<Button-4>")
    canvas.unbind_all("<Button-5>")


def configuration_canvas(canvas, scroll_x, scroll_y, scrollable_frame):
    """
    Configure le canvas et les paramètres de scroll horizontal et vertical
    Params:
    - canvas : instance de tkinter(Canvas)
    - scroll_x : instance de tkinter(Scrollbar)
    - scroll_y : instance de tkinter(Scrollbar)
    - scroll_frame : instance de tkinter(Frame)
    """

    def on_frame_configure(event):
        """
        Gère l'activation ou la désactivation du scroll
        Params:
        - event : L'événement associé.
        """
        canvas.configure(scrollregion=canvas.bbox("all"))
        if canvas.winfo_width() >= scrollable_frame.winfo_width():
            unscroll_with_mousewheel_x(canvas=canvas)
            scroll_x.grid_remove()
        else:
            scroll_with_mousewheel_x(canvas=canvas)
            scroll_x.pack(side=tk.BOTTOM, fill="x")
        if canvas.winfo_height() >= scrollable_frame.winfo_height():
            unscroll_with_mousewheel_y(canvas=canvas)
            scroll_y.grid_remove()
        else:
            scroll_with_mousewheel_y(canvas=canvas)
            scroll_y.pack(side=tk.RIGHT, fill="y")

    scrollable_frame.bind("<Configure>", on_frame_configure)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    scroll_x.lift()
    scroll_y.lift()
