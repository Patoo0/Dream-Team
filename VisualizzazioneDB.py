import tkinter as tk
import mysql.connector
from tkinter import ttk

# Connessione al database
db = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="nome_database"
)

# Funzione per eseguire la query di ricerca e popolare la tabella
def cerca_studenti():
    # Prendi il valore di ricerca dal form
    nome = campo_ricerca.get()

    # Esegui la query SQL per cercare gli studenti
    cursor = db.cursor()
    query = "SELECT * FROM studenti WHERE nome LIKE %s"
    values = ("%" + nome + "%",)
    cursor.execute(query, values)
    risultati = cursor.fetchall()

    # Popola la tabella con i risultati della query
    for i in tabella.get_children():
        tabella.delete(i)
    for studente in risultati:
        tabella.insert("", "end", values=studente)

# Creazione della finestra
finestra = tk.Tk()
finestra.title("Ricerca studenti")

# Campo di ricerca
label_ricerca = tk.Label(finestra, text="Ricerca:")
label_ricerca.grid(row=0, column=0)
campo_ricerca = tk.Entry(finestra)
campo_ricerca.grid(row=0, column=1)

# Bottone di ricerca
bottone_ricerca = tk.Button(finestra, text="Cerca", command=cerca_studenti)
bottone_ricerca.grid(row=0, column=2)

# Tabella dei risultati
tabella = ttk.Treeview(finestra, columns=("id", "nome", "cognome", "classe"))
tabella.heading("id", text="ID")
tabella.heading("nome", text="Nome")
tabella.heading("cognome", text="Cognome")
tabella.heading("classe", text="Classe")
tabella.column("id", width=50)
tabella.column("nome", width=100)
tabella.column("cognome", width=100)
tabella.column("classe", width=50)
tabella.grid(row=1, column=0, columnspan=3)

# Esecuzione della finestra
finestra.mainloop()
