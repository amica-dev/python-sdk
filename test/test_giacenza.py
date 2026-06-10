# coding: utf-8

"""
    Customers API

    La Customers API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare la Customers API registra la tua applicazione sull'**App Store di Amica**. Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  - **Authorization Code con PKCE** (consigliato per app che operano per conto di un utente Amica): l'utente autorizza la tua app tramite la pagina di consenso dell'identity provider; la tua app riceve un `code` da scambiare con un access token.    ```   GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256   POST {identity-provider}/connect/token        grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri>   ```  - **Client Credentials** (per integrazioni server-to-server, senza utente interattivo):    ```   POST {identity-provider}/connect/token   Content-Type: application/x-www-form-urlencoded    grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=read write documenti contabilita   ```    > **Nota:** il flusso Client Credentials è disponibile solo per le **app private**, non per quelle pubblicate sul marketplace.  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-------|-------------| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-----------|-------------| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |--------|-------------| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-----------|-------------| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |--------|-------------| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — il token non possiede lo scope richiesto. | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Alcune risposte `400` includono un campo `overridable` che indica se l'errore di validazione può essere ignorato impostando il parametro `validationOverride` a `true`.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: v3
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from amica_sdk.models.giacenza import Giacenza

class TestGiacenza(unittest.TestCase):
    """Giacenza unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Giacenza:
        """Test Giacenza
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Giacenza`
        """
        model = Giacenza()
        if include_optional:
            return Giacenza(
                id = 1,
                concurrency_token = 12345,
                magazzino_id = 1,
                magazzino = amica_sdk.models.magazzino.Magazzino(
                    id = 1, 
                    concurrency_token = 12345, 
                    nome = 'Magazzino centrale', 
                    indirizzo = 'Via Roma 10', 
                    località = 'Bologna', 
                    cap = '40121', 
                    provincia = 'BO', 
                    note = 'Magazzino principale per la sede operativa.', ),
                articolo_id = 1,
                articolo = amica_sdk.models.articolo.Articolo(
                    id = 1, 
                    concurrency_token = 12345, 
                    categoria_merceologica_id = 1, 
                    categoria_merceologica = amica_sdk.models.categoria_merceologica.CategoriaMerceologica(
                        id = 1, 
                        concurrency_token = 12345, 
                        nome = 'Calzature', ), 
                    gruppo_merceologico_id = 1, 
                    gruppo_merceologico = amica_sdk.models.gruppo_merceologico.GruppoMerceologico(
                        id = 1, 
                        concurrency_token = 12345, 
                        nome = 'Abbigliamento', ), 
                    causale_iva_id = 1, 
                    causale_iva = amica_sdk.models.causale_iva.CausaleIva(
                        id = 1, 
                        concurrency_token = 12345, 
                        codice = '22', 
                        nome = 'IVA 22%', 
                        aliquota = 22, 
                        indeducibilità = 0.0, 
                        intracomunitaria = False, 
                        non_imponibile = False, 
                        natura = 'N1', 
                        split_payment = False, 
                        fattura_elettronica = False, ), 
                    taglia_id = 1, 
                    taglia = amica_sdk.models.taglia.Taglia(
                        id = 1, 
                        concurrency_token = 12345, 
                        nome = 'Taglia M', 
                        taglia1 = 'XL', 
                        taglia2 = 'L', 
                        taglia3 = 'M', 
                        taglia4 = 'S', 
                        taglia5 = 'XS', 
                        taglia6 = '38', 
                        taglia7 = '40', 
                        taglia8 = '42', 
                        taglia9 = '44', 
                        taglia10 = '46', 
                        taglia11 = '48', 
                        taglia12 = '50', 
                        taglia13 = '52', 
                        taglia14 = '54', 
                        taglia15 = '56', 
                        taglia16 = '58', ), 
                    marca_id = 1, 
                    marca = amica_sdk.models.marca.Marca(
                        id = 1, 
                        concurrency_token = 12345, 
                        nome = 'Nike', ), 
                    produttore_id = 1, 
                    produttore = amica_sdk.models.produttore.Produttore(
                        id = 1, 
                        concurrency_token = 12345, 
                        nome = 'Acme S.p.A.', ), 
                    reparto_id = 1, 
                    reparto = amica_sdk.models.reparto.Reparto(
                        id = 1, 
                        concurrency_token = 12345, 
                        causale_iva_id = 1, 
                        numero = 1, 
                        prezzo = 9.9, 
                        sconto = 10, ), 
                    nome = 'Cacciavite a croce', 
                    codice = 'ART001', 
                    nome_breve = 'Cacciavite', 
                    codice_fornitore = 'FORN-789', 
                    codice_produttore = 'PROD-456', 
                    gestione_articolo = 'Standard', 
                    contesto_articolo = 'Sempre', 
                    bar_code = '8001234567890', 
                    costo_ultimo = 8.9, 
                    costo_medio = 9.2, 
                    unitàmisura_intera = False, 
                    articolo_composto = False, 
                    stato = True, 
                    data_inserimento = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    unitàmisura_movimenti = 'PZ', 
                    unitàmisura_inventario = 'PZ', 
                    fattore_conversione_unitàmisura = 1.0, 
                    note = 'Articolo soggetto a riordino automatico.', 
                    media_file = amica_sdk.models.articolo_media_file.ArticoloMediaFile(
                        id = 1, 
                        concurrency_token = 12345, 
                        data = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==', 
                        articolo_id = 1, 
                        field_name = 'immagine', ), 
                    conto_raw_vendita = '40.05.001', 
                    conto_raw_acquisto = '60.05.001', 
                    distinta_base = [
                        amica_sdk.models.componente.Componente(
                            id = 1, 
                            concurrency_token = 12345, 
                            articolo_id = 1, 
                            articolo = amica_sdk.models.articolo.Articolo(
                                id = 1, 
                                concurrency_token = 12345, 
                                categoria_merceologica_id = 1, 
                                gruppo_merceologico_id = 1, 
                                causale_iva_id = 1, 
                                taglia_id = 1, 
                                marca_id = 1, 
                                produttore_id = 1, 
                                reparto_id = 1, 
                                nome = 'Cacciavite a croce', 
                                codice = 'ART001', 
                                nome_breve = 'Cacciavite', 
                                codice_fornitore = 'FORN-789', 
                                codice_produttore = 'PROD-456', 
                                gestione_articolo = 'Standard', 
                                contesto_articolo = 'Sempre', 
                                bar_code = '8001234567890', 
                                costo_ultimo = 8.9, 
                                costo_medio = 9.2, 
                                unitàmisura_intera = False, 
                                articolo_composto = False, 
                                stato = True, 
                                data_inserimento = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                unitàmisura_movimenti = 'PZ', 
                                unitàmisura_inventario = 'PZ', 
                                fattore_conversione_unitàmisura = 1.0, 
                                note = 'Articolo soggetto a riordino automatico.', 
                                conto_raw_vendita = '40.05.001', 
                                conto_raw_acquisto = '60.05.001', ), 
                            articolo_componente_id = 1, 
                            articolo_componente = , 
                            quantita_necessaria = 10, )
                        ], ),
                quantit_in_giacenza = 150.0,
                quantit_impegnata = 25.0,
                quantit_ordinata = 50.0,
                scorta_minima = 10.0,
                gestione_sottoscorta = True,
                data_ultimo_carico = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                data_ultimo_scarico = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                carico_quantit = 500.0,
                carico_valore = 6250.0,
                scarico_quantit = 350.0,
                scarico_valore = 4375.0,
                identificativo = 'SN-2026-00123',
                identificativo_esteso = 'LOTTO-A-2026',
                data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                colore = 'Rosso'
            )
        else:
            return Giacenza(
        )
        """

    def testGiacenza(self):
        """Test Giacenza"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
