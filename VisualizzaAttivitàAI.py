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

# Funzione per aggiornare la tabella con le attività degli studenti
def aggiorna_tabella():
    # Prendi l'ID dello studente selezionato nella lista
    studente_selezionato = lista_studenti.focus()
    id_studente = lista_studenti.item(studente_selezionato)['values'][0]

    # Esegui la query SQL per cercare le attività dello studente
    cursor = db.cursor()
    query = "SELECT attivita.nome, iscrizioni.pagamento FROM iscrizioni JOIN attivita ON iscrizioni.attivita_id = attivita.id WHERE iscrizioni.studente_id = %s"
    values = (id_studente,)
    cursor.execute(query, values)
    risultati = cursor.fetchall()

    # Popola la tabella con i risultati della query
    for i in tabella.get_children():
        tabella.delete(i)
    for attivita in risultati:
        tabella.insert("", "end", values=attivita)

# Creazione della finestra
finestra = tk.Tk()
finestra.title("Attività degli studenti")

# Lista degli studenti
label_studenti = tk.Label(finestra, text="Studenti:")
label_studenti.grid(row=0, column=0)
lista_studenti = ttk.Treeview(finestra, columns=("id", "nome", "cognome"))
lista_studenti.heading("id", text="ID")
lista_studenti.heading("nome", text="Nome")
lista_studenti.heading("cognome", text="Cognome")
lista_studenti.column("id", width=50)
lista_studenti.column("nome", width=100)
lista_studenti.column("cognome", width=100)
lista_studenti.grid(row=1, column=0)
cursor = db.cursor()
query = "SELECT id, nome, cognome FROM studenti"
cursor.execute(query)
risultati = cursor.fetchall()
for studente in risultati:
    lista_studenti.insert("", "end", values=studente)

# Tabella delle attività
tabella = ttk.Treeview(finestra, columns=("nome", "pagamento"))
tabella.heading("nome", text="Attività")
tabella.heading("pagamento", text="Pagamento")
tabella.column("nome", width=200)
tabella.column("pagamento", width=100)
tabella.grid(row=1, column=1)

# Bottone per aggiornare la tabella delle attività
bottone_aggiorna = tk.Button(finestra, text="Aggiorna", command=aggiorna_tabella)
bottone_aggiorna.grid(row=2, column=1)

# Esecuzione della finestra
finestra.mainloop()
