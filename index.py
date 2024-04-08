import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from conversion_manager import conversion_manager
from modules.interface import show_folders, configuration_canvas
from global_style import (
    couleur_blanc,
    couleur_bleu,
    SETTINGS_STYLE,
)

WIDTH_WINDOW = 800


def afficher_message():
    print("Bonjour, Tkinter!")


def menu_selection(event):
    """
    Fonction pour gérer la sélection dans le menu déroulant.

    Params:
    - event : L'événement de redimensionnement de la fenêtre.
    """
    global page
    selected_item = event.widget.get()
    page = selected_item
    print(f"Menu sélectionné : {selected_item}")
    if selected_item == "Créer un nouveau projet":
        canvas.pack_forget()
        scroll_y.pack_forget()
        scroll_x.pack_forget()
        content_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        champ_label.pack()
        champ_saisie.pack()
        bouton_importer_dossier.pack()
        clear_frame(frame_projets)
        # Masquer la Frame des projets
        frame_projets.pack_forget()
    elif selected_item == "Afficher tous les projets":
        content_frame.pack_forget()
        configuration_canvas(
            canvas=canvas,
            scroll_x=scroll_x,
            scroll_y=scroll_y,
            scrollable_frame=scrollable_frame,
        )
        show_folders(scrollable_frame, fenetre.winfo_width())


def importer_dossier():
    """
    Fonction pour importer un dossier et l'ajouter à la liste ds projets.

    """
    global dossier
    dossier = filedialog.askdirectory()
    if dossier:
        nom_dossier = champ_saisie.get()
        if not nom_dossier:
            nom_dossier = os.path.basename(dossier)
        liste_projets.append(nom_dossier)
        messagebox.showinfo("Succès", "Dossier importé avec succès")
        print(f"Dossier importé avec succès : {dossier}")
    else:
        print("Aucun dossier sélectionné.")


def clear_frame(frame):
    """
    Fonction pour effacer tous les widgets d'un cadre.

    Args:
        frame (Frame): Cadre dont les widgets doivent être effacés.

    """
    for widget in frame.winfo_children():
        widget.destroy()


fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("800x800")
fenetre.configure(bg="#FFFFFF")

header_frame = ttk.Frame(fenetre)
header_frame.pack(side=tk.TOP, fill=tk.X)

header_label = ttk.Label(
    header_frame,
    text="Outil de rétro-conception hardware",
    font=("Helvetica", 20, "bold"),
    background="#0055A4",
    foreground="#FFFFFF",
)
header_label.pack(padx=10, pady=10, fill=tk.X)

menu_options = ["Créer un nouveau projet", "Afficher tous les projets"]
selected_option = tk.StringVar()
menu = ttk.Combobox(
    header_frame,
    textvariable=selected_option,
    values=menu_options,
    width=15,
    font=("Helvetica", 12),
)
selected_option.set("Afficher tous les projets")
menu = ttk.Combobox(
    header_frame,
    textvariable=selected_option,
    values=menu_options,
    width=15,
    font=("Helvetica", 12),
)
menu.bind("<<ComboboxSelected>>", menu_selection)
menu.pack(side=tk.LEFT, padx=10, pady=(0, 10))

content_frame = ttk.Frame(fenetre)

# frame pour la liste des dossiers
canvas = tk.Canvas(
    fenetre,
    background=couleur_blanc,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)
scroll_y = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scroll_x = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
scrollable_frame = ttk.Frame(canvas)
configuration_canvas(
    canvas=canvas,
    scroll_x=scroll_x,
    scroll_y=scroll_y,
    scrollable_frame=scrollable_frame,
)

# show_folders(scrollable_frame, fenetre.winfo_width())

page = "Afficher tous les projets"
# list_frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

champ_label = ttk.Label(
    content_frame, text="Saisissez le nom du dossier", font=("Helvetica", 12)
)
champ_saisie = ttk.Entry(content_frame, font=("Helvetica", 12))
bouton_importer_dossier = ttk.Button(
    content_frame, text="Importer le dossier", command=importer_dossier
)

folder_icon = PhotoImage(file="folder.png").subsample(5)

frame_projets = ttk.Frame(content_frame)
frame_projets.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

canvas_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor=tk.NW)


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


canvas_frame.bind("<Configure>", on_configure)


def suivante():
    global current_index
    current_index = (current_index + 1) % len(images_photo)
    afficher_image(current_index)


def precedente():
    global current_index
    current_index = (current_index - 1) % len(images_photo)
    afficher_image(current_index)


bouton_suivant = ttk.Button(content_frame, text="Suivant", command=suivante)
bouton_precedent = ttk.Button(
    content_frame, text="Précédent", command=precedente
)

bouton_suivant.pack()
bouton_precedent.pack()

# Gestion de zoom par mouvement de souris
canvas.bind("<MouseWheel>", zoom)

footer_frame = ttk.Frame(fenetre)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)


# # dossier = ""
#
menu_selection()


# Définir les dimensions précédentes avec les dimensions initiales de la fenêtre
def on_window_resize(event):
    """
    Met à jour l'affichage lors du redimensionnement de la fenêtre principale.

    Params:
    - event : L'événement de redimensionnement de la fenêtre.
    - page : L'onglet sur lequel se trouve l'utilisateur. ((string))
    - fenetre : Instance de la fenêtre principale de Tkinter. (Tk)
    - scrollable_frame : Instance du cadre scrollable de Tkinter. (Frame)

    """
    if page == "Afficher tous les projets":
        global previous_width, previous_height
        current_width = fenetre.winfo_width()
        current_height = fenetre.winfo_height()

        if (
            current_width != previous_width
            or current_height != previous_height
        ):

            show_folders(scrollable_frame, current_width)
            previous_width = current_width
            previous_height = current_height


previous_width = fenetre.winfo_width()
previous_height = fenetre.winfo_height()


fenetre.bind("<Configure>", on_window_resize)

fenetre.mainloop()
