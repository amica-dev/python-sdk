# coding: utf-8

# flake8: noqa
"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — accesso negato (vedi sotto le possibili cause). | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Un `403` può avere tre cause; nelle ultime due il campo `code` della risposta indica quale:  - il token non possiede lo scope richiesto dall'endpoint; - `code: cloud_not_active` — l'account lavora con una connessione locale e la Cloud API non espone i suoi dati. Per attivare il servizio cloud contatta l'assistenza, poi richiedi un nuovo token: lo stato del servizio è letto al rilascio del token; - `code: company_license_not_active` — la licenza dell'azienda indicata nel percorso è scaduta o non è attiva. Le altre aziende con licenza attiva restano accessibili.  Il motivo dell'errore è sempre nel campo `detail`. Ogni risposta di errore riporta inoltre `overridable`: quando vale `true`, l'errore di validazione è *forzabile* e basta ripetere la stessa richiesta aggiungendo `validationOverride=true` alla query string perché il servizio la accetti. È il caso delle anomalie formali su dati reali — la partita IVA di un fornitore estero, per esempio — che il cliente ha comunque bisogno di registrare.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: 3.3.7
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from amica_python_sdk.models.allegato_documento import AllegatoDocumento
from amica_python_sdk.models.anagrafica import Anagrafica
from amica_python_sdk.models.anagrafica_nominativo1 import AnagraficaNominativo1
from amica_python_sdk.models.anagrafica_nominativo2 import AnagraficaNominativo2
from amica_python_sdk.models.anagrafica_sede_legale import AnagraficaSedeLegale
from amica_python_sdk.models.area_geografica import AreaGeografica
from amica_python_sdk.models.articolo import Articolo
from amica_python_sdk.models.articolo_colore import ArticoloColore
from amica_python_sdk.models.articolo_media_file import ArticoloMediaFile
from amica_python_sdk.models.azienda import Azienda
from amica_python_sdk.models.banca import Banca
from amica_python_sdk.models.banca_documento import BancaDocumento
from amica_python_sdk.models.bene_servizio import BeneServizio
from amica_python_sdk.models.bene_servizio_compute_data import BeneServizioComputeData
from amica_python_sdk.models.bene_servizio_compute_result import BeneServizioComputeResult
from amica_python_sdk.models.cassa_previdenziale import CassaPrevidenziale
from amica_python_sdk.models.castelletto_iva import CastellettoIva
from amica_python_sdk.models.categoria_anagrafica import CategoriaAnagrafica
from amica_python_sdk.models.categoria_merceologica import CategoriaMerceologica
from amica_python_sdk.models.causale_documento import CausaleDocumento
from amica_python_sdk.models.causale_iva import CausaleIva
from amica_python_sdk.models.causale_magazzino import CausaleMagazzino
from amica_python_sdk.models.codice_pagamento import CodicePagamento
from amica_python_sdk.models.collega_documento_data import CollegaDocumentoData
from amica_python_sdk.models.componente import Componente
from amica_python_sdk.models.conto_contabile import ContoContabile
from amica_python_sdk.models.conto_contabile_validation_result import ContoContabileValidationResult
from amica_python_sdk.models.credito_debito_mensile import CreditoDebitoMensile
from amica_python_sdk.models.dati_aggiuntivi import DatiAggiuntivi
from amica_python_sdk.models.dati_pa import DatiPA
from amica_python_sdk.models.dati_sdi import DatiSdi
from amica_python_sdk.models.dati_trasporto import DatiTrasporto
from amica_python_sdk.models.ddt_import_data import DdtImportData
from amica_python_sdk.models.distinct_property_group import DistinctPropertyGroup
from amica_python_sdk.models.documento import Documento
from amica_python_sdk.models.documento_collegato import DocumentoCollegato
from amica_python_sdk.models.documento_compute_data import DocumentoComputeData
from amica_python_sdk.models.documento_compute_data_bene_servizio import DocumentoComputeDataBeneServizio
from amica_python_sdk.models.documento_compute_data_spesa import DocumentoComputeDataSpesa
from amica_python_sdk.models.documento_compute_result import DocumentoComputeResult
from amica_python_sdk.models.documento_compute_result_riepilogo_iva import DocumentoComputeResultRiepilogoIva
from amica_python_sdk.models.documento_import_data import DocumentoImportData
from amica_python_sdk.models.documento_media_file import DocumentoMediaFile
from amica_python_sdk.models.documento_totali import DocumentoTotali
from amica_python_sdk.models.fattura_elettronica_export_options import FatturaElettronicaExportOptions
from amica_python_sdk.models.fattura_elettronica_export_result import FatturaElettronicaExportResult
from amica_python_sdk.models.fattura_elettronica_import_result import FatturaElettronicaImportResult
from amica_python_sdk.models.fattura_elettronica_upload_options import FatturaElettronicaUploadOptions
from amica_python_sdk.models.fattura_elettronica_upload_result import FatturaElettronicaUploadResult
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
from amica_python_sdk.models.fattura_elettronica_xml_get_archive_by_date_range_options import FatturaElettronicaXmlGetArchiveByDateRangeOptions
from amica_python_sdk.models.fattura_elettronica_xml_get_archive_by_file_name_options import FatturaElettronicaXmlGetArchiveByFileNameOptions
from amica_python_sdk.models.fattura_elettronica_xml_style_sheet_data import FatturaElettronicaXmlStyleSheetData
from amica_python_sdk.models.fattura_elettronica_xml_template import FatturaElettronicaXmlTemplate
from amica_python_sdk.models.fatturato_mensile import FatturatoMensile
from amica_python_sdk.models.giacenza import Giacenza
from amica_python_sdk.models.gruppo_merceologico import GruppoMerceologico
from amica_python_sdk.models.impostazioni_sdi import ImpostazioniSdi
from amica_python_sdk.models.indirizzo import Indirizzo
from amica_python_sdk.models.inventario import Inventario
from amica_python_sdk.models.inventario_compute_result import InventarioComputeResult
from amica_python_sdk.models.inventario_riga import InventarioRiga
from amica_python_sdk.models.listino import Listino
from amica_python_sdk.models.listino_compute_aggiungi import ListinoComputeAggiungi
from amica_python_sdk.models.listino_compute_data import ListinoComputeData
from amica_python_sdk.models.listino_compute_duplica import ListinoComputeDuplica
from amica_python_sdk.models.listino_compute_modifica_prezzi import ListinoComputeModificaPrezzi
from amica_python_sdk.models.listino_compute_provvigioni import ListinoComputeProvvigioni
from amica_python_sdk.models.listino_compute_result import ListinoComputeResult
from amica_python_sdk.models.listino_compute_sconti import ListinoComputeSconti
from amica_python_sdk.models.magazzino import Magazzino
from amica_python_sdk.models.marca import Marca
from amica_python_sdk.models.modalita_pagamento import ModalitaPagamento
from amica_python_sdk.models.modello_contabile import ModelloContabile
from amica_python_sdk.models.modello_contabile_riga import ModelloContabileRiga
from amica_python_sdk.models.movimento_merce import MovimentoMerce
from amica_python_sdk.models.movimento_merce_riga import MovimentoMerceRiga
from amica_python_sdk.models.movimento_merce_riga_compute_data import MovimentoMerceRigaComputeData
from amica_python_sdk.models.movimento_merce_riga_compute_result import MovimentoMerceRigaComputeResult
from amica_python_sdk.models.natura_iva import NaturaIva
from amica_python_sdk.models.nazione import Nazione
from amica_python_sdk.models.ordini_import_data import OrdiniImportData
from amica_python_sdk.models.pagamento import Pagamento
from amica_python_sdk.models.periodic_invoicing_data import PeriodicInvoicingData
from amica_python_sdk.models.preferenze import Preferenze
from amica_python_sdk.models.prestazione import Prestazione
from amica_python_sdk.models.prezzo import Prezzo
from amica_python_sdk.models.problem_details import ProblemDetails
from amica_python_sdk.models.produttore import Produttore
from amica_python_sdk.models.progressivo_invio import ProgressivoInvio
from amica_python_sdk.models.registrazione_contabile import RegistrazioneContabile
from amica_python_sdk.models.registrazione_contabile_riga import RegistrazioneContabileRiga
from amica_python_sdk.models.registrazione_contabile_validation_result import RegistrazioneContabileValidationResult
from amica_python_sdk.models.reso_import_data import ResoImportData
from amica_python_sdk.models.ricerca_articolo import RicercaArticolo
from amica_python_sdk.models.risorsa_finanziaria import RisorsaFinanziaria
from amica_python_sdk.models.scadenza import Scadenza
from amica_python_sdk.models.scheda_cliente import SchedaCliente
from amica_python_sdk.models.scheda_fornitore import SchedaFornitore
from amica_python_sdk.models.sede_altra import SedeAltra
from amica_python_sdk.models.sede_legale import SedeLegale
from amica_python_sdk.models.sede_operativa import SedeOperativa
from amica_python_sdk.models.spesa import Spesa
from amica_python_sdk.models.spesa_documento import SpesaDocumento
from amica_python_sdk.models.taglia import Taglia
from amica_python_sdk.models.valuta import Valuta
