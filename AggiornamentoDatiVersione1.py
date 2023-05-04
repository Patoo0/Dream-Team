#codice base per l'aggiunta e la modifica di record nel database
import mysql.connector
connessione = mysql connector.connect(
    host = "localhost",
    user="<em>nome-utente</em>",
    password="<em>password</em>",
    db="attivitaextracurricolari";
)
cursore = connessione.cursor()
istruzione = "INSERT INTO nominativi (nome, cognome, classe) VALUES (%s, %s, %s)"
valori = ("Rick", "Sanchez", "1b")

cursore.execute(istruzione, valori)
connessione.commit()
print(cursore.rowcount)

cursore = connessione.cursor()

