import tkinter as tk
from tkinter import messagebox

def calcola_contatore():
    try:
        eta_media_vita = 80  # Imposta qui l'età media di vita
        eta_inserita = int(eta_entry.get())
        
        if eta_inserita <= 0:
            messagebox.showerror("Errore", "Inserisci un'età valida maggiore di 0.")
            return
        
        contatore = eta_media_vita - eta_inserita
        contatore_label.config(text=f"Conto alla rovescia: {contatore} anni")
    except ValueError:
        messagebox.showerror("Errore", "Inserisci un'età valida.")

# Configurazione dell'interfaccia grafica
root = tk.Tk()
root.title("Contatore Vita")
root.geometry("400x200")  # Dimensione più grande

# Cambio dello sfondo a grigio scuro
root.configure(bg="#333333")

eta_label = tk.Label(root, text="Inserisci l'età:", fg="white", bg="#333333")  # Testo bianco su sfondo grigio scuro
eta_label.pack(pady=20)

eta_entry = tk.Entry(root)
eta_entry.pack(pady=10)

calcola_button = tk.Button(root, text="Calcola Contatore", command=calcola_contatore)
calcola_button.pack(pady=15)

contatore_label = tk.Label(root, text="", fg="white", bg="#333333")  # Testo bianco su sfondo grigio scuro
contatore_label.pack(pady=15)

root.mainloop()

