#Versione per inserire più record con una sola istruzione
istruzione = "INSERT INTO nome(nome, cognome, classe, attivita) VALUES (%s, %s, %s, %s)"
valori = [ 
    ('Morty', 'Smith', '2a', 'GruppoAtletica'),
    ('Summer', 'Smith', '5a', 'CorsaCampestre'),
    ('Mario', 'Rossi', '3b', 'PCTO'),
    ('Federico', 'Brambilla', '3b', 'PCTO')
]
#executemenay consente di eseguire più istruzioni alla volta
cursore.executemany(istruzione, valori)
connessione.commit()
print(cursore.rowcount)

#print(cursore.rowcount) permette di mostrare a video quanti record 
#sono stati modificati nell'istruzione