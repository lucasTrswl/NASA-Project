import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

def afficher_message():
    print("Bonjour, Tkinter!")

def menu_selection(event):
    selected_item = event.widget.get()
    print(f"Menu sélectionné : {selected_item}")
    if selected_item == "Option 2":
        bouton_importer_dossier.pack()
        if images_photo:
            bouton_suivant.pack()
            bouton_precedent.pack()
    else:
        bouton_importer_dossier.pack_forget()
        bouton_suivant.pack_forget()
        bouton_precedent.pack_forget()

def importer_dossier():
    global dossier
    dossier = filedialog.askdirectory()
    if dossier:
        print(f"Dossier importé : {dossier}")
        label_dossier.config(text=f"Dossier sélectionné : {dossier}")
        afficher_images_dossier(dossier)
        if selected_option.get() == "Option 2":
            bouton_suivant.pack()
            bouton_precedent.pack()

images_photo = []

def afficher_images_dossier(dossier):
    global images_photo
    images_photo.clear()

    for widget in canvas_frame.winfo_children():
        widget.destroy()

    fichiers_images = [f for f in os.listdir(dossier) if f.endswith(('.tif'))]

    for fichier in fichiers_images:
        chemin_image = os.path.join(dossier, fichier)
        img = Image.open(chemin_image)

        img = img.resize((400, 400))
        img = ImageTk.PhotoImage(img, master=fenetre)  # Ajout du paramètre master pour éviter une erreur de garbage collection
        images_photo.append(img)

    afficher_image(0)
    
def on_image_click(event):
    global fullscreen
    toggle_fullscreen()
    afficher_image(current_index)

def afficher_image(index):
    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=images_photo[index])

    global image_name_text
    if show_image_name:  # Vérifier l'état du bouton
        # Affichage du nom de l'image en haut à gauche
        image_name = os.path.basename(os.path.splitext(os.listdir(dossier)[index])[0])
        image_name_text = canvas.create_text(10, 10, anchor="nw", text=image_name, fill="white", font=('Helvetica', int(-10 * fenetre.winfo_height() / 800), 'bold'))

def toggle_image_name():
    global show_image_name
    show_image_name = not show_image_name

    if show_image_name:
        bouton_toggle.config(text="Masquer Nom Image")
        afficher_image(current_index)
    else:
        bouton_toggle.config(text="Afficher Nom Image")
        canvas.delete(image_name_text)

def on_resize(event):
    # Appelé lors du redimensionnement de la fenêtre
    # Ajuste la taille de la police en fonction de la taille de la fenêtre
    new_font_size = int(-10 * event.height / 800)
    canvas.itemconfig(image_name_text, font=('Helvetica', new_font_size, 'bold'))

def suivante(event=None):
    global current_index
    current_index = (current_index + 1) % len(images_photo)
    afficher_image(current_index)

def precedente(event=None):
    global current_index
    current_index = (current_index - 1) % len(images_photo)
    afficher_image(current_index)

def on_mouse_wheel(event):
    if event.delta < 0:
        suivante()
    else:
        precedente()

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    fenetre.attributes('-fullscreen', fullscreen)

fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("800x800")
fenetre.bind("<Configure>", on_resize)  # Appeler on_resize lors du redimensionnement
fenetre.bind("<MouseWheel>", on_mouse_wheel)  # Gestion du scroll de la souris

style = ttk.Style()

style.theme_create("gendarmerie_style", parent="alt", settings={
    "TLabel": {"configure": {"foreground": "#0055A4", "background": "#FFFFFF", "font": ('Helvetica', 12)}},
    "TButton": {"configure": {"foreground": "#FFFFFF", "background": "#0055A4", "font": ('Helvetica', 12, 'bold')}},
    "TFrame": {"configure": {"background": "#FFFFFF"}},
    "TCombobox": {"configure": {"foreground": "#0055A4", "background": "#FFFFFF", "font": ('Helvetica', 12)}},
    "TCombobox.Border": {"configure": {"foreground": "#0055A4", "background": "#0055A4"}},
    "TCombobox.field": {"configure": {"foreground": "#0055A4", "background": "#FFFFFF", "font": ('Helvetica', 12)}},
})

style.theme_use("gendarmerie_style")

header_frame = ttk.Frame(fenetre)
header_frame.pack(side=tk.TOP, fill=tk.X)

header_label = ttk.Label(header_frame, text="Mon Application Tkinter", font=('Helvetica', 20, 'bold'), background="#0055A4", foreground="#FFFFFF")
header_label.pack(padx=10, pady=10, fill=tk.X)

menu_options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar()
menu = ttk.Combobox(header_frame, textvariable=selected_option, values=menu_options, width=15, font=('Helvetica', 12))
menu.bind("<<ComboboxSelected>>", menu_selection)
menu.current(0)
menu.pack(side=tk.LEFT, padx=10, pady=(0, 10))

content_frame = ttk.Frame(fenetre)
content_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

label = ttk.Label(content_frame, text="Ceci est une interface graphique avec Tkinter!", font=('Helvetica', 16))
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

# Créer les boutons pour passer aux images suivante et précédente
bouton_precedent = ttk.Button(content_frame, text="Précédent", command=precedente)
bouton_precedent.pack(side=tk.LEFT, padx=10)

bouton_suivant = ttk.Button(content_frame, text="Suivant", command=suivante)
bouton_suivant.pack(side=tk.LEFT, padx=10)

# Bouton pour afficher/masquer le nom de l'image
show_image_name = True
bouton_toggle = ttk.Checkbutton(content_frame, text="Masquer Nom Image", command=toggle_image_name)
bouton_toggle.pack(pady=10)

footer_frame = ttk.Frame(fenetre)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

bouton = ttk.Button(footer_frame, text="Cliquez ici", command=afficher_message)
bouton.pack(pady=10)

current_index = 0
image_name_text = None  # Pour stocker l'ID du texte du nom de l'image

# Passer en plein écran lorsqu'on clique sur une image
def on_image_click(event):
    global fullscreen
    toggle_fullscreen()

canvas.bind("<Button-1>", on_image_click)

fullscreen = False

fenetre.mainloop()
    