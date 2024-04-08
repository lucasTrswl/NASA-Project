import os
import tkinter as tk
from modules.progressBar import start_progress, update_progress, stop_progress
from tkinter import ttk, filedialog, messagebox, PhotoImage
from conversion_manager import conversion_manager
from modules.interface import show_folders, configuration_canvas
from global_style import couleur_blanc, SETTINGS_STYLE

WIDTH_WINDOW = 800

liste_projets = []


def afficher_message():
    print("Bonjour, Tkinter!")


from modules.progressBar import start_progress, update_progress, stop_progress


def menu_selection(event=None):
    """
    Fonction pour gérer la sélection dans le menu déroulant.

    Params:
    - event : L'événement de redimensionnement de la fenêtre.
    """
    selected_item = selected_option.get()
    print(f"Menu sélectionné : {selected_item}")
    if selected_item == "Créer un nouveau projet":
        canvas.pack_forget()
        scroll_y.pack_forget()
        scroll_x.pack_forget()
        clear_frame(scrollable_frame)
        content_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        champ_label.pack()
        champ_saisie.pack()
        bouton_importer_dossier.pack()
    elif selected_item == "Afficher tous les projets":
        content_frame.pack_forget()
        # clear_frame(content_frame)
        configuration_canvas(
            canvas=canvas,
            scroll_x=scroll_x,
            scroll_y=scroll_y,
            scrollable_frame=scrollable_frame,
        )
        show_folders(scrollable_frame, fenetre.winfo_width())


def importer_dossier():
    """
    Fonction pour importer un dossier et l'ajouter à la liste des projets.
    """

    global dossier
    dossier = filedialog.askdirectory()
    if dossier:
        print(os.listdir(dossier))
        tif_files = [
            fichier
            for fichier in os.listdir(dossier)
            if fichier.endswith(".tif")
        ]
        if not tif_files:
            return

        nom_dossier = champ_saisie.get()
        if not nom_dossier:
            nom_dossier = os.path.basename(dossier)
        liste_projets.append(nom_dossier)
        progress_bar = start_progress(content_frame, color="#F550E4")
        for i in range(101):
            update_progress(progress_bar, i)
            fenetre.update_idletasks()
            fenetre.after(10)
        stop_progress(progress_bar)
        messagebox.showinfo("Succès", "Dossier importé avec succès")
        creer_nouveau_projet(
            nom_dossier
        )  # Créer un nouveau projet avec le nom du dossier
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


def creer_nouveau_projet(nom_dossier):
    """
    Fonction pour créer un nouveau projet dans le dossier 'Projets'.

    Args:
        nom_dossier (str): Nom du dossier à créer comme nouveau projet.
    """
    chemin_projets = os.path.join(
        os.getcwd(), "Mes projets"
    )  # Chemin du dossier 'Projets'
    nouveau_dossier = os.path.join(chemin_projets, nom_dossier)

    tif_files = [
        fichier for fichier in os.listdir(dossier) if fichier.endswith(".tif")
    ]
    if not tif_files:
        messagebox.showerror(
            "Erreur", "Le dossier ne contient aucun fichier .tif."
        )

        print(f"Le dossier '{nom_dossier}' ne contient aucun fichier .tif.")
        return

    try:
        os.makedirs(nouveau_dossier)  # Créer le nouveau dossier dans 'Projets'
        messagebox.showinfo("Succès", "Dossier importé avec succès")
        print(f"Nouveau projet créé : {nouveau_dossier}")
    except FileExistsError:
        print(f"Le dossier '{nom_dossier}' existe déjà dans 'Projets'.")


def importer_dossier():
    """
    Fonction pour importer un dossier et l'ajouter à la liste des projets.
    """
    global dossier
    dossier = filedialog.askdirectory()
    if dossier:
        nom_dossier = champ_saisie.get()
        if not nom_dossier:
            nom_dossier = os.path.basename(dossier)
        creer_nouveau_projet(
            nom_dossier
        )  # Créer un nouveau projet avec le nom du dossier
        print(f"Dossier importé avec succès : {dossier}")
    else:
        print("Aucun dossier sélectionné.")


fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("800x800")
fenetre.configure(bg="#FFFFFF")
# theme
style = ttk.Style()
style.theme_create("gendarmerie_style", parent="alt", settings=SETTINGS_STYLE)
style.theme_use("gendarmerie_style")

# header
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
# menu
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
menu.bind("<<ComboboxSelected>>", menu_selection)
menu.pack(side=tk.LEFT, padx=10, pady=(0, 10))


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


content_frame = ttk.Frame(fenetre)
champ_label = ttk.Label(
    content_frame, text="Saisissez le nom du dossier", font=("Helvetica", 12)
)
champ_saisie = ttk.Entry(content_frame, font=("Helvetica", 12))
bouton_importer_dossier = ttk.Button(
    content_frame, text="Importer le dossier", command=importer_dossier
)


# footer_frame = ttk.Frame(fenetre)
# footer_frame.pack(side=tk.BOTTOM, fill=tk.X)


dossier = ""
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
    if selected_option.get() == "Afficher tous les projets":
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
