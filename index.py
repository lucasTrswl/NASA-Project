import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

def afficher_message():
    print("Bonjour, Tkinter!")

couleur_bleu = "#0055A4"
couleur_blanc = "#FFFFFF"
couleur_gris = "#F0F0F0"

def menu_selection(event):
    selected_item = event.widget.get()
    print(f"Menu sélectionné : {selected_item}")
    if selected_item == "Créer un nouveau projet":
        bouton_importer_dossier.pack()
        bouton_suivant.pack()
        bouton_precedent.pack()
        label_dossier.pack()
        canvas.pack()
    else:
        bouton_importer_dossier.pack_forget()
        bouton_suivant.pack_forget()
        bouton_precedent.pack_forget()
        label_dossier.pack_forget()
        canvas.pack_forget()
        for widget in canvas_frame.winfo_children():
            widget.destroy()


def importer_dossier():
    global dossier, fichiers_images
    dossier = filedialog.askdirectory()
    if dossier:
        print(f"Dossier importé : {dossier}")
        label_dossier.config(text=f"Dossier sélectionné : {dossier}")
        fichiers_images = [f for f in os.listdir(dossier) if f.endswith(('.tif'))]
        afficher_images_dossier(dossier)
        bouton_suivant.pack()
        bouton_precedent.pack()

images_photo = []

def afficher_images_dossier(dossier):
    global images_photo
    images_photo.clear()

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    for fichier in fichiers_images:
        chemin_image = os.path.join(dossier, fichier)
        img = Image.open(chemin_image)
        img = img.resize((400, 400))
        img = ImageTk.PhotoImage(img)
        images_photo.append(img)

    afficher_image(0)

def afficher_image(index):
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=images_photo[index])
    canvas.image = images_photo[index]  # Référence à l'image pour éviter la suppression par le garbage collector

def zoom(event):
    global current_index
    if event.delta > 0:
        # Zoom in
        zoom_factor = 1.1
    else:
        # Zoom out
        zoom_factor = 0.9
        
    img = Image.open(os.path.join(dossier, fichiers_images[current_index]))
    width, height = img.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
    img = img.resize((new_width, new_height))
    img = ImageTk.PhotoImage(img)
    images_photo[current_index] = img
    
    canvas.delete("all")
    canvas.image = img
    canvas.create_image(0, 0, anchor="nw", image=img)
    
    # Réaligner le canvas après le zoom
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    # Ajuster le décalage de défilement pour garder l'image centrée
    xscroll = (canvas.winfo_width() - new_width) / 2
    yscroll = (canvas.winfo_height() - new_height) / 2
    canvas.xview_moveto(xscroll / new_width)
    canvas.yview_moveto(yscroll / new_height)


fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("800x800")
fenetre.configure(bg=couleur_blanc)

style = ttk.Style()

style.theme_create("gendarmerie_style", parent="alt", settings={
    "TLabel": {"configure": {"foreground": couleur_bleu, "background": couleur_blanc, "font": ('Helvetica', 12)}},
    "TButton": {"configure": {"foreground": couleur_blanc, "background": couleur_bleu, "font": ('Helvetica', 12, 'bold')}},
    "TFrame": {"configure": {"background": couleur_blanc}},
    "TCombobox": {"configure": {"foreground": couleur_bleu, "background": couleur_blanc, "font": ('Helvetica', 12)}},
    "TCombobox.Border": {"configure": {"foreground": couleur_bleu, "background": couleur_bleu}},
    "TCombobox.field": {"configure": {"foreground": couleur_bleu, "background": couleur_blanc, "font": ('Helvetica', 12)}},
})

style.theme_use("gendarmerie_style")

header_frame = ttk.Frame(fenetre)
header_frame.pack(side=tk.TOP, fill=tk.X)

header_label = ttk.Label(header_frame, text="Mon Application Tkinter", font=('Helvetica', 20, 'bold'), background=couleur_bleu, foreground=couleur_blanc)
header_label.pack(padx=10, pady=10, fill=tk.X)

menu_options = ["Créer un nouveau projet", "Afficher tous les projets", "Option 3"]
selected_option = tk.StringVar()
menu = ttk.Combobox(header_frame, textvariable=selected_option, values=menu_options, width=15, font=('Helvetica', 12))
menu.bind("<<ComboboxSelected>>", menu_selection)
menu.current(0)
menu.pack(side=tk.LEFT, padx=10, pady=(0, 10))

content_frame = ttk.Frame(fenetre)
content_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

label = ttk.Label(content_frame, font=('Helvetica', 16))
label.pack(pady=20)

bouton_importer_dossier = ttk.Button(content_frame, text="Importer Dossier", command=importer_dossier)
bouton_importer_dossier.pack()

label_dossier = ttk.Label(content_frame, text="", font=('Helvetica', 12), wraplength=400)
label_dossier.pack()

images_frame = ttk.Frame(content_frame)
images_frame.pack(pady=20)

canvas = tk.Canvas(images_frame, bd=0, highlightthickness=0, width=400, height=400)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

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
bouton_precedent = ttk.Button(content_frame, text="Précédent", command=precedente)

bouton_suivant.pack()
bouton_precedent.pack()

# Gestion de zoom par mouvement de souris
canvas.bind("<MouseWheel>", zoom)

footer_frame = ttk.Frame(fenetre)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

current_index = 0
dossier = ""
fichiers_images = []

fenetre.mainloop()
