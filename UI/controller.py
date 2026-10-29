import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO

    def mostra_strumento(self, e):
        """Gestisce il click sul pulsante 'Mostra' (Sezione 3)."""
        #Pulisce la ListView della Sezione 3
        self._view.lista_strumento.controls.clear()

        #Recupera gli strumenti dal modello
        strumenti = self._model.get_strumenti()

        if strumenti is None or len(strumenti) == 0:
            self._view.show_alert("Nessuno strumento presente nel database.")
            self._view.update()
            return

        # Aggiunge ogni strumento alla ListView
        for s in strumenti:
            self._view.lista_strumento.controls.append(ft.Text(str(s)))

        #Aggiorna la grafica
        self._view.update()

    def cerca_strumento(self, e):
        """Gestisce il click sul pulsante 'Cerca' (Sezione 4)."""
        tipo_inserito = self._view.txt_tipo.value

        # Controllo campo vuoto
        if not tipo_inserito or tipo_inserito.strip() == "":
            self._view.show_alert("Inserire un tipo di strumento per la ricerca.")
            return

        #Pulisce la ListView della Sezione 4
        self._view.lista_per_tipo.controls.clear()

        #Cerca nel modello gli strumenti di quel tipo
        risultati = self._model.cerca_strumenti_per_tipo(tipo_inserito)

        if risultati is None or len(risultati) == 0:
            self._view.show_alert(f"Nessuno strumento trovato per il tipo: '{tipo_inserito}'.")
            self._view.update()
            return

        #Popola la ListView con i risultati trovati
        for s in risultati:
            self._view.lista_per_tipo.controls.append(ft.Text(str(s)))

        #Aggiorna la grafica
        self._view.update()