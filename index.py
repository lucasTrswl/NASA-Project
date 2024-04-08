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
    Gère l'affichage des cadres (Frame) selon le menu sélectionné.

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

    elif selected_item == "Afficher tous les projets":
        content_frame.pack_forget()
        configuration_canvas(
            canvas=canvas,
            scroll_x=scroll_x,
            scroll_y=scroll_y,
            scrollable_frame=scrollable_frame,
        )
        show_folders(scrollable_frame, fenetre.winfo_width())


# def importer_dossier():
#     global dossier, fichiers_images, destination_source
#     dossier = filedialog.askdirectory()
#     if dossier:
#         print(f"Dossier importé : {dossier}")
#         label_dossier.config(text=f"Dossier sélectionné : {dossier}")
#         destination_source = "project/Echo_dot"
#         conversion_manager("convert", dossier, destination_source)
#         fichiers_images = [
#             f for f in os.listdir(destination_source) if f.endswith((".tif"))
#         ]
#         afficher_images_dossier(destination_source)
#         bouton_suivant.pack()
#         bouton_precedent.pack()


# images_photo = []


# def afficher_images_dossier(dossier):
#     global images_photo
#     images_photo.clear()

#     for widget in canvas_frame.winfo_children():
#         widget.destroy()

#     for fichier in fichiers_images:
#         chemin_image = os.path.join(dossier, fichier)
#         img = Image.open(chemin_image)
#         img = img.resize((400, 400))
#         img = ImageTk.PhotoImage(img)
#         images_photo.append(img)

#     afficher_image(0)


# def afficher_image(index):
#     canvas.delete("all")
#     canvas.create_image(0, 0, anchor="nw", image=images_photo[index])
#     canvas.image = images_photo[
#         index
#     ]  # Référence à l'image pour éviter la suppression par le garbage collector


# def zoom(event):
#     global current_index
#     if event.delta > 0:
#         # Zoom in
#         zoom_factor = 1.1
#     else:
#         # Zoom out
#         zoom_factor = 0.9

#     img = Image.open(os.path.join(dossier, fichiers_images[current_index]))
#     width, height = img.size
#     new_width = int(width * zoom_factor)
#     new_height = int(height * zoom_factor)
#     img = img.resize((new_width, new_height))
#     img = ImageTk.PhotoImage(img)
#     images_photo[current_index] = img

#     canvas.delete("all")
#     canvas.image = img
#     canvas.create_image(0, 0, anchor="nw", image=img)

#     # Réaligner le canvas après le zoom
#     canvas.configure(scrollregion=canvas.bbox("all"))

#     # Ajuster le décalage de défilement pour garder l'image centrée
#     xscroll = (canvas.winfo_width() - new_width) / 2
#     yscroll = (canvas.winfo_height() - new_height) / 2
#     canvas.xview_moveto(xscroll / new_width)
#     canvas.yview_moveto(yscroll / new_height)


fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("800x800")
fenetre.configure(bg=couleur_blanc)

style = ttk.Style()

style.theme_create("gendarmerie_style", parent="alt", settings=SETTINGS_STYLE)

style.theme_use("gendarmerie_style")

header_frame = ttk.Frame(fenetre)
header_frame.pack(side=tk.TOP, fill=tk.X)

header_label = ttk.Label(
    header_frame,
    text="Mon Application Tkinter",
    font=("Helvetica", 20, "bold"),
    background=couleur_bleu,
    foreground=couleur_blanc,
)
header_label.pack(padx=10, pady=10, fill=tk.X)


menu_options = [
    "Afficher tous les projets",
    "Créer un nouveau projet",
    "Option 3",
]
selected_option = tk.StringVar()
menu = ttk.Combobox(
    header_frame,
    textvariable=selected_option,
    values=menu_options,
    width=15,
    font=("Helvetica", 12),
)
menu.bind("<<ComboboxSelected>>", menu_selection)
menu.current(0)
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
# list_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)


# label = ttk.Label(content_frame, font=("Helvetica", 16))
# label.pack(pady=20)

# bouton_importer_dossier = ttk.Button(
#     content_frame, text="Importer Dossier", command=importer_dossier
# )
# bouton_importer_dossier.pack()

# label_dossier = ttk.Label(
#     content_frame, text="", font=("Helvetica", 12), wraplength=400
# )
# label_dossier.pack()

# images_frame = ttk.Frame(content_frame)
# images_frame.pack(pady=20)

# canvas = tk.Canvas(
#     images_frame, bd=0, highlightthickness=0, width=400, height=400
# )
# canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# canvas_frame = ttk.Frame(canvas)
# canvas.create_window((0, 0), window=canvas_frame, anchor=tk.NW)


# def on_configure(event):
#     canvas.configure(scrollregion=canvas.bbox("all"))


# canvas_frame.bind("<Configure>", on_configure)


# def suivante():
#     global current_index
#     current_index = (current_index + 1) % len(images_photo)
#     afficher_image(current_index)


# def precedente():
#     global current_index
#     current_index = (current_index - 1) % len(images_photo)
#     afficher_image(current_index)


# bouton_suivant = ttk.Button(content_frame, text="Suivant", command=suivante)
# bouton_precedent = ttk.Button(
#     content_frame, text="Précédent", command=precedente
# )

# bouton_suivant.pack()
# bouton_precedent.pack()

# # Gestion de zoom par mouvement de souris
# canvas.bind("<MouseWheel>", zoom)

# footer_frame = ttk.Frame(fenetre)
# footer_frame.pack(side=tk.BOTTOM, fill=tk.X)


# current_index = 0
# dossier = ""
# fichiers_images = []


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
