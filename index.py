import tkinter as tk
from tkinter import ttk, filedialog

def afficher_message():
    print("Bonjour, Tkinter!")

# Couleurs Gendarmerie Française
couleur_bleu = "#0055A4"
couleur_blanc = "#FFFFFF"
couleur_gris = "#F0F0F0"

def menu_selection(event):
    selected_item = event.widget.get()
    print(f"Menu sélectionné : {selected_item}")
    if selected_item == "Option 2":
        bouton_importer.pack()
    else:
        bouton_importer.pack_forget()

def importer_fichier():
    fichier = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt"), ("Fichiers TIFF", "*.tif;*.tiff"), ("Tous les fichiers", "*.*")])
    if fichier:
        print(f"Fichier importé : {fichier}")
        label_fichier.config(text=f"Fichier sélectionné : {fichier}")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("600x400")
fenetre.configure(bg=couleur_blanc)

# Style pour les widgets ttk
style = ttk.Style()

# Couleurs pour le style
style.theme_create("gendarmerie_style", parent="alt", settings={
    "TLabel": {"configure": {"foreground": couleur_bleu, "background": couleur_blanc, "font": ('Helvetica', 12)}},
    "TButton": {"configure": {"foreground": couleur_blanc, "background": couleur_bleu, "font": ('Helvetica', 12, 'bold')}},
    "TFrame": {"configure": {"background": couleur_blanc}},
    "TCombobox": {"configure": {"foreground": couleur_bleu, "background": couleur_blanc, "font": ('Helvetica', 12)}},
    "TCombobox.Border": {"configure": {"foreground": couleur_bleu, "background": couleur_bleu}},
    "TCombobox.field": {"configure": {"foreground": couleur_bleu, "background": couleur_blanc, "font": ('Helvetica', 12)}},
})

style.theme_use("gendarmerie_style")

# Créer un Frame pour le header
header_frame = ttk.Frame(fenetre)
header_frame.pack(side=tk.TOP, fill=tk.X)

# Ajouter un Label dans le header
header_label = ttk.Label(header_frame, text="Mon Application Tkinter", font=('Helvetica', 20, 'bold'), background=couleur_bleu, foreground=couleur_blanc)
header_label.pack(padx=10, pady=10, fill=tk.X)

# Menu déroulant dans le header
menu_options = ["Option 1", "Option 2", "Option 3"]
selected_option = tk.StringVar()
menu = ttk.Combobox(header_frame, textvariable=selected_option, values=menu_options, width=15, font=('Helvetica', 12))
menu.bind("<<ComboboxSelected>>", menu_selection)
menu.current(0)  # Sélectionner le premier élément par défaut
menu.pack(side=tk.LEFT, padx=10, pady=(0, 10))

# Créer un Frame pour le contenu principal
content_frame = ttk.Frame(fenetre)
content_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Ajouter un Label dans le contenu
label = ttk.Label(content_frame, text="Ceci est une interface graphique avec Tkinter!", font=('Helvetica', 16))
label.pack(pady=20)

# Bouton "Importer Fichier"
bouton_importer = ttk.Button(content_frame, text="Importer Fichier", command=importer_fichier)
bouton_importer.pack(pady=10)

# Label pour afficher le chemin du fichier sélectionné
label_fichier = ttk.Label(content_frame, text="", font=('Helvetica', 12), wraplength=400)
label_fichier.pack(pady=10)

# Masquer le bouton "Importer Fichier" initialement
bouton_importer.pack_forget()

# Créer un Frame pour le footer
footer_frame = ttk.Frame(fenetre)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Créer un bouton pour le footer
bouton = ttk.Button(footer_frame, text="Cliquez ici", command=afficher_message)
bouton.pack(pady=10)

# Lancer la boucle principale
fenetre.mainloop()
