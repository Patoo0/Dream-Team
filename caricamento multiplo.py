import sqlite3

# Connessione al database
conn = sqlite3.connect('nome_database.db')
cursore = conn.cursor()


# Lettura dei dati dal file e inserimento nella tabella
with open('nome_file.txt', 'r') as file:
    for riga in file:
        dati = riga.strip().split(',')
        cursore.execute("INSERT INTO alunno (CFalunni,nome, cognome,classe) VALUES (?, ?, ?,?)",
                        (dati[0], dati[1], dati[2], dati[3])
        cursore.execute("INSERT INTO attivita (nome,codattivita,approvata,CFaccompagnatori,CFalunno,DataInizio,indirizzo,Datafine) VALUES (?, ?, ?,?,?,?,?,?)",
                        (dati[4], dati[5], dati[6], dati[7],dati[8],dati[9],dati[10],dati[11])
        cursore.execute("INSERT INTO accompagnatore (cognome,nome,CFaccompagnatori) VALUES (?, ?, ?)",
                        (dati[12], dati[13], dati[14])

# Salvataggio dei dati nel database
conn.commit()

# Chiusura della connessione
conn.close()
