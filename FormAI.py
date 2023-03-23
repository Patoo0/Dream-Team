import pymysql.cursors

# Connessione al database
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='Gestionale',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# Creazione della tabella utenti
with conn.cursor() as cursor:
    sql = "CREATE TABLE IF NOT EXISTS utenti (id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(255) NOT NULL, cognome VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, PRIMARY KEY (id))"
    cursor.execute(sql)

# Funzione di accesso al sistema
def accesso():
    email = input("Inserisci la tua email: ")
    password = input("Inserisci la tua password: ")
    with conn.cursor() as cursor:
        sql = "SELECT * FROM utenti WHERE email=%s AND password=%s"
        cursor.execute(sql, (email, password))
        result = cursor.fetchone()
        if result:
            print("Accesso riuscito!")
        else:
            print("Email o password errate.")

# Funzione di registrazione al sistema
def registrazione():
    nome = input("Inserisci il tuo nome: ")
    cognome = input("Inserisci il tuo cognome: ")
    email = input("Inserisci la tua email: ")
    password = input("Inserisci la tua password: ")
    with conn.cursor() as cursor:
        sql = "INSERT INTO utenti (nome, cognome, email, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, cognome, email, password))
        conn.commit()
    print("Registrazione completata!")

# Esecuzione del programma
print("Benvenuto!")
risposta = input("Vuoi accedere al sistema? (s/n): ")

