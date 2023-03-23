import tkinter as tk
import sqlite3

#queste due librerie servono per la creazione dell'interfaccia e per il collegamento al db

def login():
    #recupera il nome utente e la password inseriti dall'utente
    username = username_entry.get()
    password = password_entry.get()

    #serve per connettersi al Database
    conn = sqlite3.connect('Gestionale.db')

    #esegue la query per vedere se l'utente esiste

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utenti WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone

    #se l'utente esiste mostra il messaggio di benvenuto

    if user:
        message_label.config(text = "Benvenuto, " + username + "!")
    #altrimenti visualizza il messaggio di errore
    else:
        message_label.config(text="Nome utente o password non validi.")
    conn.close()
    #per chiudere la connessione

    #il codice seguente apre la finestra dell'applicazione
    root = tk.Tk()

    #crea i widget per la finestra

    