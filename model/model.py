import mysql.connector
from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        #Metodo per stabilire la connessione con il database MySQL
        cnx = get_connection()
        if cnx is None:
            #Se la connessione fallisce interrompe l'esecuzione e restituisce None
            return None

        #Creo la lista vuota
        strumenti = []
        try:
            #Crea un cursore che restituisce le righe come dizionari (chiave = nome colonna)
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM strumento"
            cursor.execute(query) #Esegue la query SQL di selezione

            for riga in cursor:
                # Creiamo l'oggetto Strumento usando i valori del dizionario
                s = Strumento(**riga) #Crea l'oggetto Strumento usando direttamente i dati della riga estratti dal DB
                strumenti.append(s)

            #Chiude il cursore e la connessione al DB per liberare le risorse
            cursor.close()
            cnx.close()
            return strumenti

        #Intercetta eventuali errori di MySQL durante l'esecuzione della query
        except mysql.connector.Error as err:
            print(f"Errore di lettura dal database: {err}")
            if cnx and cnx.is_connected():
                cnx.close()
            return None

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO

        # Metodo per stabilire la connessione con il database MySQL
        cnx = get_connection()
        if cnx is None:
            # Se la connessione fallisce interrompe l'esecuzione e restituisce None
            return None

        # Creo la lista vuota
        strumenti_filtrati = []
        try:
            # Crea un cursore che restituisce le righe come dizionari (chiave = nome colonna)
            cursor = cnx.cursor(dictionary=True)

            # Query SQL
            query = """SELECT * 
                    FROM strumento 
                    WHERE LOWER(tipo) = LOWER(%s)"""

            # Esegue la query passando la tupla contenente il valore cercato
            cursor.execute(query, (tipo.strip(),))

            for riga in cursor:
                s = Strumento(**riga) #Crea l'oggetto Strumento usando direttamente i dati della riga estratti dal DB
                strumenti_filtrati.append(s)

            # Chiude il cursore e la connessione al DB per liberare le risorse
            cursor.close()
            cnx.close()
            return strumenti_filtrati

        # Intercetta eventuali errori di MySQL durante l'esecuzione della query
        except mysql.connector.Error as err:
            print(f"Errore nella ricerca sul database: {err}")
            if cnx and cnx.is_connected():
                cnx.close()
            return None
