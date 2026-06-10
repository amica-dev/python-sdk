# coding: utf-8

# flake8: noqa

"""
    Customers API

    La Customers API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare la Customers API registra la tua applicazione sull'**App Store di Amica**. Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  - **Authorization Code con PKCE** (consigliato per app che operano per conto di un utente Amica): l'utente autorizza la tua app tramite la pagina di consenso dell'identity provider; la tua app riceve un `code` da scambiare con un access token.    ```   GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256   POST {identity-provider}/connect/token        grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri>   ```  - **Client Credentials** (per integrazioni server-to-server, senza utente interattivo):    ```   POST {identity-provider}/connect/token   Content-Type: application/x-www-form-urlencoded    grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=read write documenti contabilita   ```    > **Nota:** il flusso Client Credentials è disponibile solo per le **app private**, non per quelle pubblicate sul marketplace.  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-------|-------------| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-----------|-------------| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |--------|-------------| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-----------|-------------| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |--------|-------------| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — il token non possiede lo scope richiesto. | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Alcune risposte `400` includono un campo `overridable` che indica se l'errore di validazione può essere ignorato impostando il parametro `validationOverride` a `true`.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: v3
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from amica_sdk.api.anagrafica_api import AnagraficaApi
from amica_sdk.api.area_geografica_api import AreaGeograficaApi
from amica_sdk.api.articolo_api import ArticoloApi
from amica_sdk.api.articolo_media_file_api import ArticoloMediaFileApi
from amica_sdk.api.azienda_api import AziendaApi
from amica_sdk.api.bene_servizio_api import BeneServizioApi
from amica_sdk.api.cassa_previdenziale_api import CassaPrevidenzialeApi
from amica_sdk.api.castelletto_iva_api import CastellettoIvaApi
from amica_sdk.api.categoria_anagrafica_api import CategoriaAnagraficaApi
from amica_sdk.api.categoria_merceologica_api import CategoriaMerceologicaApi
from amica_sdk.api.causale_documento_api import CausaleDocumentoApi
from amica_sdk.api.causale_iva_api import CausaleIvaApi
from amica_sdk.api.causale_magazzino_api import CausaleMagazzinoApi
from amica_sdk.api.codice_pagamento_api import CodicePagamentoApi
from amica_sdk.api.conto_contabile_api import ContoContabileApi
from amica_sdk.api.distinta_base_api import DistintaBaseApi
from amica_sdk.api.documento_api import DocumentoApi
from amica_sdk.api.documento_media_file_api import DocumentoMediaFileApi
from amica_sdk.api.evento_api import EventoApi
from amica_sdk.api.fattura_elettronica_xml_api import FatturaElettronicaXmlApi
from amica_sdk.api.fattura_elettronica_xml_template_api import FatturaElettronicaXmlTemplateApi
from amica_sdk.api.giacenza_api import GiacenzaApi
from amica_sdk.api.giornale_magazzino_api import GiornaleMagazzinoApi
from amica_sdk.api.gruppo_merceologico_api import GruppoMerceologicoApi
from amica_sdk.api.indirizzo_api import IndirizzoApi
from amica_sdk.api.listino_api import ListinoApi
from amica_sdk.api.magazzino_api import MagazzinoApi
from amica_sdk.api.marca_api import MarcaApi
from amica_sdk.api.modalita_pagamento_api import ModalitaPagamentoApi
from amica_sdk.api.modello_contabile_api import ModelloContabileApi
from amica_sdk.api.movimento_merce_api import MovimentoMerceApi
from amica_sdk.api.natura_iva_api import NaturaIvaApi
from amica_sdk.api.nazione_api import NazioneApi
from amica_sdk.api.pagamento_api import PagamentoApi
from amica_sdk.api.preferenze_api import PreferenzeApi
from amica_sdk.api.prestazione_api import PrestazioneApi
from amica_sdk.api.prezzo_api import PrezzoApi
from amica_sdk.api.produttore_api import ProduttoreApi
from amica_sdk.api.progressivo_invio_api import ProgressivoInvioApi
from amica_sdk.api.registrazione_contabile_api import RegistrazioneContabileApi
from amica_sdk.api.reparto_api import RepartoApi
from amica_sdk.api.risorsa_finanziaria_api import RisorsaFinanziariaApi
from amica_sdk.api.scadenza_api import ScadenzaApi
from amica_sdk.api.situazione_api import SituazioneApi
from amica_sdk.api.spesa_api import SpesaApi
from amica_sdk.api.spesa_documento_api import SpesaDocumentoApi
from amica_sdk.api.taglia_api import TagliaApi
from amica_sdk.api.valuta_api import ValutaApi
from amica_sdk.api.web_hook_api import WebHookApi

# import ApiClient
from amica_sdk.api_response import ApiResponse
from amica_sdk.api_client import ApiClient
from amica_sdk.configuration import Configuration
from amica_sdk.exceptions import OpenApiException
from amica_sdk.exceptions import ApiTypeError
from amica_sdk.exceptions import ApiValueError
from amica_sdk.exceptions import ApiKeyError
from amica_sdk.exceptions import ApiAttributeError
from amica_sdk.exceptions import ApiException

# import models into sdk package
from amica_sdk.models.allegato_documento import AllegatoDocumento
from amica_sdk.models.anagrafica import Anagrafica
from amica_sdk.models.anagrafica_nominativo1 import AnagraficaNominativo1
from amica_sdk.models.anagrafica_nominativo2 import AnagraficaNominativo2
from amica_sdk.models.anagrafica_sede_legale import AnagraficaSedeLegale
from amica_sdk.models.area_geografica import AreaGeografica
from amica_sdk.models.articolo import Articolo
from amica_sdk.models.articolo_media_file import ArticoloMediaFile
from amica_sdk.models.azienda import Azienda
from amica_sdk.models.banca import Banca
from amica_sdk.models.banca_documento import BancaDocumento
from amica_sdk.models.bene_servizio import BeneServizio
from amica_sdk.models.bene_servizio_compute_data import BeneServizioComputeData
from amica_sdk.models.bene_servizio_compute_result import BeneServizioComputeResult
from amica_sdk.models.cassa_previdenziale import CassaPrevidenziale
from amica_sdk.models.castelletto_iva import CastellettoIva
from amica_sdk.models.categoria_anagrafica import CategoriaAnagrafica
from amica_sdk.models.categoria_merceologica import CategoriaMerceologica
from amica_sdk.models.causale_documento import CausaleDocumento
from amica_sdk.models.causale_iva import CausaleIva
from amica_sdk.models.causale_magazzino import CausaleMagazzino
from amica_sdk.models.codice_pagamento import CodicePagamento
from amica_sdk.models.collega_documento_data import CollegaDocumentoData
from amica_sdk.models.componente import Componente
from amica_sdk.models.conto_contabile import ContoContabile
from amica_sdk.models.conto_contabile_validation_result import ContoContabileValidationResult
from amica_sdk.models.credito_debito_mensile import CreditoDebitoMensile
from amica_sdk.models.dati_aggiuntivi import DatiAggiuntivi
from amica_sdk.models.dati_pa import DatiPA
from amica_sdk.models.dati_sdi import DatiSdi
from amica_sdk.models.dati_trasporto import DatiTrasporto
from amica_sdk.models.ddt_import_data import DdtImportData
from amica_sdk.models.distinct_property_group import DistinctPropertyGroup
from amica_sdk.models.documento import Documento
from amica_sdk.models.documento_collegato import DocumentoCollegato
from amica_sdk.models.documento_compute_data import DocumentoComputeData
from amica_sdk.models.documento_compute_data_bene_servizio import DocumentoComputeDataBeneServizio
from amica_sdk.models.documento_compute_data_spesa import DocumentoComputeDataSpesa
from amica_sdk.models.documento_compute_result import DocumentoComputeResult
from amica_sdk.models.documento_compute_result_riepilogo_iva import DocumentoComputeResultRiepilogoIva
from amica_sdk.models.documento_import_data import DocumentoImportData
from amica_sdk.models.documento_media_file import DocumentoMediaFile
from amica_sdk.models.evento import Evento
from amica_sdk.models.fattura_elettronica_export_options import FatturaElettronicaExportOptions
from amica_sdk.models.fattura_elettronica_export_result import FatturaElettronicaExportResult
from amica_sdk.models.fattura_elettronica_import_result import FatturaElettronicaImportResult
from amica_sdk.models.fattura_elettronica_upload_options import FatturaElettronicaUploadOptions
from amica_sdk.models.fattura_elettronica_upload_result import FatturaElettronicaUploadResult
from amica_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
from amica_sdk.models.fattura_elettronica_xml_get_archive_by_date_range_options import FatturaElettronicaXmlGetArchiveByDateRangeOptions
from amica_sdk.models.fattura_elettronica_xml_get_archive_by_file_name_options import FatturaElettronicaXmlGetArchiveByFileNameOptions
from amica_sdk.models.fattura_elettronica_xml_style_sheet_data import FatturaElettronicaXmlStyleSheetData
from amica_sdk.models.fattura_elettronica_xml_template import FatturaElettronicaXmlTemplate
from amica_sdk.models.fatturato_mensile import FatturatoMensile
from amica_sdk.models.giacenza import Giacenza
from amica_sdk.models.gruppo_merceologico import GruppoMerceologico
from amica_sdk.models.impostazioni_sdi import ImpostazioniSdi
from amica_sdk.models.indirizzo import Indirizzo
from amica_sdk.models.listino import Listino
from amica_sdk.models.magazzino import Magazzino
from amica_sdk.models.marca import Marca
from amica_sdk.models.modalita_pagamento import ModalitaPagamento
from amica_sdk.models.modello_contabile import ModelloContabile
from amica_sdk.models.modello_contabile_riga import ModelloContabileRiga
from amica_sdk.models.movimento_merce import MovimentoMerce
from amica_sdk.models.movimento_merce_riga import MovimentoMerceRiga
from amica_sdk.models.natura_iva import NaturaIva
from amica_sdk.models.nazione import Nazione
from amica_sdk.models.ordini_import_data import OrdiniImportData
from amica_sdk.models.pagamento import Pagamento
from amica_sdk.models.periodic_invoicing_data import PeriodicInvoicingData
from amica_sdk.models.preferenze import Preferenze
from amica_sdk.models.prestazione import Prestazione
from amica_sdk.models.prezzo import Prezzo
from amica_sdk.models.problem_details import ProblemDetails
from amica_sdk.models.produttore import Produttore
from amica_sdk.models.progressivo_invio import ProgressivoInvio
from amica_sdk.models.registrazione_contabile import RegistrazioneContabile
from amica_sdk.models.registrazione_contabile_riga import RegistrazioneContabileRiga
from amica_sdk.models.registrazione_contabile_validation_result import RegistrazioneContabileValidationResult
from amica_sdk.models.reparto import Reparto
from amica_sdk.models.reso_import_data import ResoImportData
from amica_sdk.models.ricerca_articolo import RicercaArticolo
from amica_sdk.models.risorsa_finanziaria import RisorsaFinanziaria
from amica_sdk.models.scadenza import Scadenza
from amica_sdk.models.scheda_cliente import SchedaCliente
from amica_sdk.models.scheda_fornitore import SchedaFornitore
from amica_sdk.models.sede_altra import SedeAltra
from amica_sdk.models.sede_legale import SedeLegale
from amica_sdk.models.sede_operativa import SedeOperativa
from amica_sdk.models.spesa import Spesa
from amica_sdk.models.spesa_documento import SpesaDocumento
from amica_sdk.models.taglia import Taglia
from amica_sdk.models.valuta import Valuta
from amica_sdk.models.web_hook import WebHook
