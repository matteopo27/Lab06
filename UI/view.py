import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.scroll = ft.ScrollMode.AUTO #Metodo per ottenere una pagine flet scorrevole e non fissa

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Elementi UI
        self.txt_titolo = None
        self.txt_responsabile = None

        # Non obbligatorio mettere già qui tutti gli elementi UI

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        """ Imposta il controller alla pagina """
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge Elementi di UI alla pagina e la aggiorna. """
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )
        #Crea il titolo "Strumenti
        self.txt_strumento= ft.Text(value="Strumenti", size=20, weight=ft.FontWeight.BOLD)
        #Crea il contenitore elenco per mostrare tutti gli strumenti letti dal database
        self.lista_strumento = ft.ListView(spacing=5, height=150)

        #Crea il titolo "Cerca Strumento Per Tipo"
        self.txt_tipo_stru= ft.Text(value="Cerca Strumento Per Tipo", size=20, weight=ft.FontWeight.BOLD)
        #Crea la casella di testo in cui l'utente scrive il tipo di strumento da cercare
        self.txt_tipo= ft.TextField(label="Tipo", value="", width=300)
        #Crea il contenitore elenco per mostrare solo gli strumenti trovati dalla ricerca
        self.lista_per_tipo= ft.ListView(spacing=5, height=150)





        # TextField per responsabile
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")

        # ListView per mostrare la lista di strumenti aggiornata
        self.lista_strumenti = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # TextField per ricerca strumento per tipo
        self.input_tipo_strumento = ft.TextField(label="Tipo")

        # ListView per mostrare il risultato della ricerca strumenti per tipo
        self.lista_strumenti_ricerca = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- PULSANTI e TOGGLE associati a EVENTI ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.Button("Conferma", on_click=self.controller.conferma_responsabile)

        # Altri Pulsanti da implementare (es. "Mostra" e "Cerca")
        # TODO
        #Crea il pulsante "Cerca" e lo collega alla funzione cerca_strumento del controller
        self.tasto_cerca= ft.Button("Cerca", on_click=self.controller.cerca_strumento)
        #Crea il pulsante "Mostra" e lo collega alla funzione mostra_strumento del controller
        self.tasto_mostra= ft.Button("Mostra", on_click=self.controller.mostra_strumento)
        #Dispone in orizzontale il campo di testo per il tipo e il pulsante "Cerca"
        self.myRow = ft.Row(controls=[self.txt_tipo, self.tasto_cerca])

        # --- LAYOUT ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3
            # TODO
            #Metodo per organizzare gli elementi in verticale
            ft.Column(
                controls=[self.txt_strumento, self.tasto_mostra, self.lista_strumento]),


            # Sezione 4
            # TODO
            # Metodo per organizzare gli elementi in verticale
            ft.Column(
                controls=[self.txt_tipo_stru,self.myRow,self.lista_per_tipo]
            )
        )




    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
