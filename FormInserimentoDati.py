import tkinter as tk
import sqlite3
import mysql.connector

# Connessione al database
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="nome_database"
)

# Funzione per inserire i dati nel database
def inserisci_dati():
    # Prendi i valori dal form
    nome = campo_nome.get()
    cognome = campo_cognome.get()
    classe = campo_classe.get()

    # Esegui la query SQL per inserire i dati nel database
    cursor = db.cursor()
    query = "INSERT INTO studenti (nome, cognome, classe) VALUES (%s, %s, %s)"
    values = (nome, cognome, classe)
    cursor.execute(query, values)
    db.commit()

    # Messaggio di conferma
    messagebox.showinfo("Conferma", "Dati inseriti correttamente.")

# Creazione della finestra
finestra = tk.Tk()
finestra.title("Accesso al database")

# Campi del form
label_nome = tk.Label(finestra, text="Nome:")
label_nome.grid(row=0, column=0)
campo_nome = tk.Entry(finestra)
campo_nome.grid(row=0, column=1)

label_cognome = tk.Label(finestra, text="Cognome:")
label_cognome.grid(row=1, column=0)
campo_cognome = tk.Entry(finestra)
campo_cognome.grid(row=1, column=1)

label_classe = tk.Label(finestra, text="Classe:")
label_classe.grid(row=2, column=0)
campo_classe = tk.Entry(finestra)
campo_classe.grid(row=2, column=1)


# Bottone per inserire i dati nel database
bottone_inserisci = tk.Button(finestra, text="Inserisci dati", command=inserisci_dati)
bottone_inserisci.grid(row=3, column=1)

# Esecuzione della finestra

finestra.mainloop()

