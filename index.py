import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, PhotoImage

liste_projets = []

def menu_selection(event=None):
    selected_item = selected_option.get()
    print(f"Menu sélectionné : {selected_item}")
    if selected_item == "Créer un nouveau projet":
        # Masquer les éléments du carrousel d'images
        
        # Afficher les éléments du champ de formulaire
        champ_label.pack()
        champ_saisie.pack()
        bouton_importer_dossier.pack()
        
        # Masquer la Frame des projets
        frame_projets.pack_forget()
    elif selected_item == "Afficher tous les projets":
        # Masquer les éléments du champ de formulaire
        champ_label.pack_forget()
        champ_saisie.pack_forget()
        bouton_importer_dossier.pack_forget()
        
        # Afficher la Frame des projets
        frame_projets.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        # Effacer la liste précédente
        clear_frame(frame_projets)
        
        # Afficher les dossiers importés dans la Frame avec des icônes de dossier
        for projet in liste_projets:
            icon_label = ttk.Label(frame_projets, image=folder_icon)
            icon_label.pack()
            name_label = ttk.Label(frame_projets, text=projet)
            name_label.pack()
    else:
        # Réinitialiser le champ de formulaire et masquer le bouton d'importation
        champ_label.pack_forget()
        champ_saisie.pack_forget()
        bouton_importer_dossier.pack_forget()
        
        # Masquer la Frame des projets
        frame_projets.pack_forget()

def importer_dossier():
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
    for widget in frame.winfo_children():
        widget.destroy()

fenetre = tk.Tk()
fenetre.title("Mon Application")
fenetre.geometry("800x800")
fenetre.configure(bg="#FFFFFF")

header_frame = ttk.Frame(fenetre)
header_frame.pack(side=tk.TOP, fill=tk.X)

header_label = ttk.Label(header_frame, text="Outil de rétro-conception hardware", font=('Helvetica', 20, 'bold'), background="#0055A4", foreground="#FFFFFF")
header_label.pack(padx=10, pady=10, fill=tk.X)

menu_options = ["Créer un nouveau projet", "Afficher tous les projets"]
selected_option = tk.StringVar()
selected_option.set("Afficher tous les projets")
menu = ttk.Combobox(header_frame, textvariable=selected_option, values=menu_options, width=15, font=('Helvetica', 12))
menu.bind("<<ComboboxSelected>>", menu_selection)
menu.pack(side=tk.LEFT, padx=10, pady=(0, 10))

content_frame = ttk.Frame(fenetre)
content_frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

champ_label = ttk.Label(content_frame, text="Saisissez le nom du dossier", font=('Helvetica', 12))
champ_saisie = ttk.Entry(content_frame, font=('Helvetica', 12))
bouton_importer_dossier = ttk.Button(content_frame, text="Importer le dossier", command=importer_dossier)

folder_icon = PhotoImage(file="folder.png").subsample(5)

frame_projets = ttk.Frame(content_frame)
frame_projets.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

style = ttk.Style()

style.theme_create("gendarmerie_style", parent="alt", settings={
    "TLabel": {"configure": {"foreground": "#0055A4", "background": "#FFFFFF", "font": ('Helvetica', 12)}},
    "TEntry": {"configure": {"foreground": "#000000", "font": ('Helvetica', 12)}},
    "TButton": {"configure": {"foreground": "#FFFFFF", "background": "#0055A4", "font": ('Helvetica', 12, 'bold')}},
    "TFrame": {"configure": {"background": "#FFFFFF"}},
    "TCombobox": {"configure": {"foreground": "#000000", "background": "#FFFFFF", "font": ('Helvetica', 12)}},
    "TCombobox.Border": {"configure": {"foreground": "#0055A4", "background": "#0055A4"}},
    "TCombobox.field": {"configure": {"foreground": "#000000", "background": "#FFFFFF", "font": ('Helvetica', 12)}},
})

style.theme_use("gendarmerie_style")

footer_frame = ttk.Frame(fenetre)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

dossier = ""

menu_selection()

fenetre.mainloop()
