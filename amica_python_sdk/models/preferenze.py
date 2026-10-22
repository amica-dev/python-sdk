# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — accesso negato (vedi sotto le possibili cause). | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Un `403` può avere tre cause; nelle ultime due il campo `code` della risposta indica quale:  - il token non possiede lo scope richiesto dall'endpoint; - `code: cloud_not_active` — l'account lavora con una connessione locale e la Cloud API non espone i suoi dati. Per attivare il servizio cloud contatta l'assistenza, poi richiedi un nuovo token: lo stato del servizio è letto al rilascio del token; - `code: company_license_not_active` — la licenza dell'azienda indicata nel percorso è scaduta o non è attiva. Le altre aziende con licenza attiva restano accessibili.  Il motivo dell'errore è sempre nel campo `detail`. Ogni risposta di errore riporta inoltre `overridable`: quando vale `true`, l'errore di validazione è *forzabile* e basta ripetere la stessa richiesta aggiungendo `validationOverride=true` alla query string perché il servizio la accetti. È il caso delle anomalie formali su dati reali — la partita IVA di un fornitore estero, per esempio — che il cliente ha comunque bisogno di registrare.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: 3.2.3
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from amica_python_sdk.models.impostazioni_sdi import ImpostazioniSdi
from amica_python_sdk.models.ricerca_articolo import RicercaArticolo
from amica_python_sdk.models.sede_altra import SedeAltra
from amica_python_sdk.models.sede_legale import SedeLegale
from amica_python_sdk.models.sede_operativa import SedeOperativa
from typing import Optional, Set
from typing_extensions import Self

class Preferenze(BaseModel):
    """
    Preferenze aziendali.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    ragione_sociale1: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Ragione sociale.", alias="ragioneSociale1")
    ragione_sociale2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Eventuale seconda riga della ragione sociale. Utile soprattutto in fase di stampa, quando si desidera spezzare una ragione sociale molto lunga su due righe distinte.", alias="ragioneSociale2")
    partita_iva: Optional[StrictStr] = Field(default=None, description="Partita IVA.", alias="partitaIva")
    registro_imprese: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=15)]] = Field(default=None, description="Numero di iscrizione al Registro Imprese.", alias="registroImprese")
    codice_fiscale: Optional[StrictStr] = Field(default=None, description="Codice fiscale.", alias="codiceFiscale")
    codice_sia: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=10)]] = Field(default=None, description="Codice SIA.", alias="codiceSia")
    codice_rea: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=10)]] = Field(default=None, description="Codice REA.", alias="codiceRea")
    persona_giuridica: Optional[StrictBool] = Field(default=None, description="Indica se l'organizzazione è una persona giuridica oppure no. `true` indica una persona giuridica, `false` indica una persona fisica.", alias="personaGiuridica")
    data_nascita: Optional[datetime] = Field(default=None, description="Data di nascita (persona fisica).", alias="dataNascita")
    localita_nascita: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=40)]] = Field(default=None, description="Luogo di nascita (persona fisica).", alias="localitaNascita")
    provincia_nascita: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=3)]] = Field(default=None, description="Provincia di nascita (persona fisica).", alias="provinciaNascita")
    sesso: Optional[StrictStr] = Field(default=None, description="Sesso (persona fisica).")
    attivita: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Tipo di attività svolta dall'azienda o dalla persona fisica.")
    iva_esclusa: Optional[StrictBool] = Field(default=None, description="Indica se, in modo predefinito, i prezzi riportati sui documenti fiscali devono essere considerati al netto dell'IVA. Se `false`, l'IVA viene applicata ai prezzi quando possibile.", alias="ivaEsclusa")
    decimali_prezzo_unitario: Optional[Annotated[int, Field(le=5, strict=True, ge=1)]] = Field(default=None, description="Numero di decimali ammessi nei prezzi unitari. Minimo 1, massimo 5.", alias="decimaliPrezzoUnitario")
    causale_produzione_componenti_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `CausaleMagazzino` Identificativo univoco della `CausaleMagazzino` da usare nella produzione di componenti.", alias="causaleProduzioneComponentiId")
    causale_produzione_composti_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della `CausaleMagazzino` da usare per gli articoli composti nella produzione di componenti.", alias="causaleProduzioneCompostiId")
    causale_magazzino_vendita_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della `CausaleMagazzino` da usare nei documenti di vendita.", alias="causaleMagazzinoVenditaId")
    causale_magazzino_acquisto_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della `CausaleMagazzino` da usare nei documenti di acquisto.", alias="causaleMagazzinoAcquistoId")
    ricerca_articolo: Optional[RicercaArticolo] = Field(default=None, alias="ricercaArticolo")
    data_speciale1: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=5)]] = Field(default=None, description="Eventuali scadenze che cadono in questa data verranno posticipate del numero di giorni indicato da `GiorniExtraDataSpeciale1`.", alias="dataSpeciale1")
    data_speciale2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=5)]] = Field(default=None, description="Eventuali scadenze che cadono in questa data verranno posticipate del numero di giorni indicato da `GiorniExtraDataSpeciale2`.", alias="dataSpeciale2")
    giorni_extra_data_speciale1: Optional[StrictInt] = Field(default=None, description="Numero di giorni da aggiungere a `DataSpeciale1`.", alias="giorniExtraDataSpeciale1")
    giorni_extra_data_speciale2: Optional[StrictInt] = Field(default=None, description="Numero di giorni da aggiungere a `DataSpeciale1`.", alias="giorniExtraDataSpeciale2")
    pagato_manuale: Optional[StrictBool] = Field(default=None, description="Indica se il pagamento delle scadenze viene gestito manualmente. Se `false`, lo stato del pagamento viene determinato in base alle registrazioni contabili (il modulo <a href=\"https://gestionaleamica.com/Software/ContabilitaOrdinaria\">Contabilità</a> deve essere attivo).", alias="pagatoManuale")
    causale_magazzino_merci_id: Optional[StrictInt] = Field(default=None, description="Identificativo della `CausaleMagazzino` predefinita nei movimenti merci.", alias="causaleMagazzinoMerciId")
    magazzino_merci_id: Optional[StrictInt] = Field(default=None, description="Identificativo del `Magazzino` predefinito nei movimenti merci.", alias="magazzinoMerciId")
    listino_merci_id: Optional[StrictInt] = Field(default=None, description="Identificativo del `Listino` predefinito nei movimenti merci.", alias="listinoMerciId")
    modalita_pagamento_merci_id: Optional[StrictInt] = Field(default=None, description="Identificativo della `ModalitaPagamento` predefinita nei movimenti merci.", alias="modalitaPagamentoMerciId")
    documenti_causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo della `CausaleIva` predefinita nei documenti fiscali.", alias="documentiCausaleIvaId")
    documenti_magazzino_id: Optional[StrictInt] = Field(default=None, description="Identificativo del `Magazzino` predefinito nei documenti fiscali.", alias="documentiMagazzinoId")
    documenti_listino_id: Optional[StrictInt] = Field(default=None, description="`DocumentiListinoId` predefinito nei documenti fiscali.", alias="documentiListinoId")
    e_mail: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Email aziendale.", alias="eMail")
    sito_web: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Sito web aziendale.", alias="sitoWeb")
    anno_contabile: Optional[StrictInt] = Field(default=None, description="Anno contabile corrente (es. '2023').", alias="annoContabile")
    unit_di_misura: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=15)]] = Field(default=None, description="Unità di misura predefinita.", alias="unitàDiMisura")
    causale_pagamento_modello_cu: Optional[StrictStr] = Field(default=None, description="Causale del modello CU (es. 'A').", alias="causalePagamentoModelloCU")
    impostazioni_sdi: Optional[ImpostazioniSdi] = Field(default=None, alias="impostazioniSdi")
    tipo_bilancio: Optional[StrictStr] = Field(default=None, description="Tipo di bilancio predefinito: analitico o sintetico.", alias="tipoBilancio")
    periodo_iva: Optional[StrictStr] = Field(default=None, description="Periodicità IVA: mensile o trimestrale.", alias="periodoIva")
    liquidazione_iva: Optional[StrictStr] = Field(default=None, description="Tipo di liquidazione IVA: per competenza o per cassa.", alias="liquidazioneIva")
    modifica_registrazione_contabile_alla_emissione: Optional[StrictBool] = Field(default=None, description="Indica se si desidera modificare la registrazione contabile creata all'emissione di un documento. Si applica ad Amica20 WebApp e ad Amica 20 per Windows.", alias="modificaRegistrazioneContabileAllaEmissione")
    ottimizza_emissione_ordini: Optional[StrictBool] = Field(default=None, description="Indica se l'ottimizzazione per l'emissione di documenti di grandi dimensioni è attiva oppure no. Si applica ad Amica20 per Windows.", alias="ottimizzaEmissioneOrdini")
    aggiungi_anno_in_corso_al_numero_documento: Optional[StrictBool] = Field(default=None, description="Indica se si desidera aggiungere l'anno in corso al numero del documento (es. 1/2022). Si applica ad Amica 20 WebApp e ad Amica 20 per Windows.", alias="aggiungiAnnoInCorsoAlNumeroDocumento")
    consenti_cambio_manuale_stato_ddt: Optional[StrictBool] = Field(default=None, description="Indica se si desidera abilitare l'opzione di modifica dello stato dei DDT. Si applica ad Amica 20 WebApp e ad Amica 20 per Windows.", alias="consentiCambioManualeStatoDdt")
    email_body: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=1024)]] = Field(default=None, description="Testo del messaggio email inviato all'emissione di un documento. Il documento stesso viene allegato al messaggio. Si applica ad Amica 20 per Windows.", alias="emailBody")
    email_auto_send: Optional[StrictBool] = Field(default=None, description="Indica se inviare un'email all'emissione di un documento.", alias="emailAutoSend")
    auto_produzione: Optional[StrictBool] = Field(default=None, description="Indica se la produzione automatica dei composti è attiva.", alias="autoProduzione")
    codice_destinatario: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=7)]] = Field(default=None, description="'Codice destinatario' per il sistema fiscale italiano. Utilizzato per il recapito delle fatture elettroniche italiane.", alias="codiceDestinatario")
    pec: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=120)]] = Field(default=None, description="Indirizzo PEC italiano.")
    modello_vendite_nota_debito_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le note di debito emesse.", alias="modelloVenditeNotaDebitoId")
    modello_vendite_nota_credito_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le note di credito emesse.", alias="modelloVenditeNotaCreditoId")
    modello_vendite_ricevuta_fiscale_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le ricevute fiscali emesse.", alias="modelloVenditeRicevutaFiscaleId")
    modello_vendite_fattura_professionista_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture professionisti emesse.", alias="modelloVenditeFatturaProfessionistaId")
    modello_vendite_fattura_differita_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture differite emesse.", alias="modelloVenditeFatturaDifferitaId")
    modello_vendite_fattura_acconto_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture di acconto emesse.", alias="modelloVenditeFatturaAccontoId")
    modello_acquisti_fattura_accompagnatoria_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture accompagnatorie fornitori emesse.", alias="modelloAcquistiFatturaAccompagnatoriaId")
    modello_vendite_fattura_accompagnaoria_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture accompagnatorie emesse.", alias="modelloVenditeFatturaAccompagnaoriaId")
    modello_acquisti_nota_debito_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le note di debito fornitori emesse.", alias="modelloAcquistiNotaDebitoId")
    modello_acquisti_nota_credito_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le note di credito emesse.", alias="modelloAcquistiNotaCreditoId")
    modello_acquisti_fattura_professionisti_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture professionisti fornitori emesse.", alias="modelloAcquistiFatturaProfessionistiId")
    modello_acquisti_fattura_differita_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture differite fornitori emesse.", alias="modelloAcquistiFatturaDifferitaId")
    modello_acquisti_fattura_acconto_id: Optional[StrictInt] = Field(default=None, description="`ModelloContabile` predefinito per le fatture di acconto fornitori emesse.", alias="modelloAcquistiFatturaAccontoId")
    sede_legale: Optional[SedeLegale] = Field(default=None, alias="sedeLegale")
    sede_operativa: Optional[SedeOperativa] = Field(default=None, alias="sedeOperativa")
    sede_altra: Optional[SedeAltra] = Field(default=None, alias="sedeAltra")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "ragioneSociale1", "ragioneSociale2", "partitaIva", "registroImprese", "codiceFiscale", "codiceSia", "codiceRea", "personaGiuridica", "dataNascita", "localitaNascita", "provinciaNascita", "sesso", "attivita", "ivaEsclusa", "decimaliPrezzoUnitario", "causaleProduzioneComponentiId", "causaleProduzioneCompostiId", "causaleMagazzinoVenditaId", "causaleMagazzinoAcquistoId", "ricercaArticolo", "dataSpeciale1", "dataSpeciale2", "giorniExtraDataSpeciale1", "giorniExtraDataSpeciale2", "pagatoManuale", "causaleMagazzinoMerciId", "magazzinoMerciId", "listinoMerciId", "modalitaPagamentoMerciId", "documentiCausaleIvaId", "documentiMagazzinoId", "documentiListinoId", "eMail", "sitoWeb", "annoContabile", "unitàDiMisura", "causalePagamentoModelloCU", "impostazioniSdi", "tipoBilancio", "periodoIva", "liquidazioneIva", "modificaRegistrazioneContabileAllaEmissione", "ottimizzaEmissioneOrdini", "aggiungiAnnoInCorsoAlNumeroDocumento", "consentiCambioManualeStatoDdt", "emailBody", "emailAutoSend", "autoProduzione", "codiceDestinatario", "pec", "modelloVenditeNotaDebitoId", "modelloVenditeNotaCreditoId", "modelloVenditeRicevutaFiscaleId", "modelloVenditeFatturaProfessionistaId", "modelloVenditeFatturaDifferitaId", "modelloVenditeFatturaAccontoId", "modelloAcquistiFatturaAccompagnatoriaId", "modelloVenditeFatturaAccompagnaoriaId", "modelloAcquistiNotaDebitoId", "modelloAcquistiNotaCreditoId", "modelloAcquistiFatturaProfessionistiId", "modelloAcquistiFatturaDifferitaId", "modelloAcquistiFatturaAccontoId", "sedeLegale", "sedeOperativa", "sedeAltra"]

    @field_validator('tipo_bilancio')
    def tipo_bilancio_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Analitico', 'Sintentico']):
            raise ValueError("must be one of enum values ('Analitico', 'Sintentico')")
        return value

    @field_validator('periodo_iva')
    def periodo_iva_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Mensile', 'Trimestrale']):
            raise ValueError("must be one of enum values ('Mensile', 'Trimestrale')")
        return value

    @field_validator('liquidazione_iva')
    def liquidazione_iva_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Competenza', 'Cassa']):
            raise ValueError("must be one of enum values ('Competenza', 'Cassa')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Preferenze from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ricerca_articolo
        if self.ricerca_articolo:
            _dict['ricercaArticolo'] = self.ricerca_articolo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of impostazioni_sdi
        if self.impostazioni_sdi:
            _dict['impostazioniSdi'] = self.impostazioni_sdi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sede_legale
        if self.sede_legale:
            _dict['sedeLegale'] = self.sede_legale.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sede_operativa
        if self.sede_operativa:
            _dict['sedeOperativa'] = self.sede_operativa.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sede_altra
        if self.sede_altra:
            _dict['sedeAltra'] = self.sede_altra.to_dict()
        # set to None if ragione_sociale1 (nullable) is None
        # and model_fields_set contains the field
        if self.ragione_sociale1 is None and "ragione_sociale1" in self.model_fields_set:
            _dict['ragioneSociale1'] = None

        # set to None if ragione_sociale2 (nullable) is None
        # and model_fields_set contains the field
        if self.ragione_sociale2 is None and "ragione_sociale2" in self.model_fields_set:
            _dict['ragioneSociale2'] = None

        # set to None if partita_iva (nullable) is None
        # and model_fields_set contains the field
        if self.partita_iva is None and "partita_iva" in self.model_fields_set:
            _dict['partitaIva'] = None

        # set to None if registro_imprese (nullable) is None
        # and model_fields_set contains the field
        if self.registro_imprese is None and "registro_imprese" in self.model_fields_set:
            _dict['registroImprese'] = None

        # set to None if codice_fiscale (nullable) is None
        # and model_fields_set contains the field
        if self.codice_fiscale is None and "codice_fiscale" in self.model_fields_set:
            _dict['codiceFiscale'] = None

        # set to None if codice_sia (nullable) is None
        # and model_fields_set contains the field
        if self.codice_sia is None and "codice_sia" in self.model_fields_set:
            _dict['codiceSia'] = None

        # set to None if codice_rea (nullable) is None
        # and model_fields_set contains the field
        if self.codice_rea is None and "codice_rea" in self.model_fields_set:
            _dict['codiceRea'] = None

        # set to None if data_nascita (nullable) is None
        # and model_fields_set contains the field
        if self.data_nascita is None and "data_nascita" in self.model_fields_set:
            _dict['dataNascita'] = None

        # set to None if localita_nascita (nullable) is None
        # and model_fields_set contains the field
        if self.localita_nascita is None and "localita_nascita" in self.model_fields_set:
            _dict['localitaNascita'] = None

        # set to None if provincia_nascita (nullable) is None
        # and model_fields_set contains the field
        if self.provincia_nascita is None and "provincia_nascita" in self.model_fields_set:
            _dict['provinciaNascita'] = None

        # set to None if sesso (nullable) is None
        # and model_fields_set contains the field
        if self.sesso is None and "sesso" in self.model_fields_set:
            _dict['sesso'] = None

        # set to None if attivita (nullable) is None
        # and model_fields_set contains the field
        if self.attivita is None and "attivita" in self.model_fields_set:
            _dict['attivita'] = None

        # set to None if causale_produzione_componenti_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_produzione_componenti_id is None and "causale_produzione_componenti_id" in self.model_fields_set:
            _dict['causaleProduzioneComponentiId'] = None

        # set to None if causale_produzione_composti_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_produzione_composti_id is None and "causale_produzione_composti_id" in self.model_fields_set:
            _dict['causaleProduzioneCompostiId'] = None

        # set to None if causale_magazzino_vendita_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_magazzino_vendita_id is None and "causale_magazzino_vendita_id" in self.model_fields_set:
            _dict['causaleMagazzinoVenditaId'] = None

        # set to None if causale_magazzino_acquisto_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_magazzino_acquisto_id is None and "causale_magazzino_acquisto_id" in self.model_fields_set:
            _dict['causaleMagazzinoAcquistoId'] = None

        # set to None if data_speciale1 (nullable) is None
        # and model_fields_set contains the field
        if self.data_speciale1 is None and "data_speciale1" in self.model_fields_set:
            _dict['dataSpeciale1'] = None

        # set to None if data_speciale2 (nullable) is None
        # and model_fields_set contains the field
        if self.data_speciale2 is None and "data_speciale2" in self.model_fields_set:
            _dict['dataSpeciale2'] = None

        # set to None if giorni_extra_data_speciale1 (nullable) is None
        # and model_fields_set contains the field
        if self.giorni_extra_data_speciale1 is None and "giorni_extra_data_speciale1" in self.model_fields_set:
            _dict['giorniExtraDataSpeciale1'] = None

        # set to None if giorni_extra_data_speciale2 (nullable) is None
        # and model_fields_set contains the field
        if self.giorni_extra_data_speciale2 is None and "giorni_extra_data_speciale2" in self.model_fields_set:
            _dict['giorniExtraDataSpeciale2'] = None

        # set to None if causale_magazzino_merci_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_magazzino_merci_id is None and "causale_magazzino_merci_id" in self.model_fields_set:
            _dict['causaleMagazzinoMerciId'] = None

        # set to None if magazzino_merci_id (nullable) is None
        # and model_fields_set contains the field
        if self.magazzino_merci_id is None and "magazzino_merci_id" in self.model_fields_set:
            _dict['magazzinoMerciId'] = None

        # set to None if listino_merci_id (nullable) is None
        # and model_fields_set contains the field
        if self.listino_merci_id is None and "listino_merci_id" in self.model_fields_set:
            _dict['listinoMerciId'] = None

        # set to None if modalita_pagamento_merci_id (nullable) is None
        # and model_fields_set contains the field
        if self.modalita_pagamento_merci_id is None and "modalita_pagamento_merci_id" in self.model_fields_set:
            _dict['modalitaPagamentoMerciId'] = None

        # set to None if documenti_causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.documenti_causale_iva_id is None and "documenti_causale_iva_id" in self.model_fields_set:
            _dict['documentiCausaleIvaId'] = None

        # set to None if documenti_magazzino_id (nullable) is None
        # and model_fields_set contains the field
        if self.documenti_magazzino_id is None and "documenti_magazzino_id" in self.model_fields_set:
            _dict['documentiMagazzinoId'] = None

        # set to None if documenti_listino_id (nullable) is None
        # and model_fields_set contains the field
        if self.documenti_listino_id is None and "documenti_listino_id" in self.model_fields_set:
            _dict['documentiListinoId'] = None

        # set to None if e_mail (nullable) is None
        # and model_fields_set contains the field
        if self.e_mail is None and "e_mail" in self.model_fields_set:
            _dict['eMail'] = None

        # set to None if sito_web (nullable) is None
        # and model_fields_set contains the field
        if self.sito_web is None and "sito_web" in self.model_fields_set:
            _dict['sitoWeb'] = None

        # set to None if anno_contabile (nullable) is None
        # and model_fields_set contains the field
        if self.anno_contabile is None and "anno_contabile" in self.model_fields_set:
            _dict['annoContabile'] = None

        # set to None if unit_di_misura (nullable) is None
        # and model_fields_set contains the field
        if self.unit_di_misura is None and "unit_di_misura" in self.model_fields_set:
            _dict['unitàDiMisura'] = None

        # set to None if causale_pagamento_modello_cu (nullable) is None
        # and model_fields_set contains the field
        if self.causale_pagamento_modello_cu is None and "causale_pagamento_modello_cu" in self.model_fields_set:
            _dict['causalePagamentoModelloCU'] = None

        # set to None if email_body (nullable) is None
        # and model_fields_set contains the field
        if self.email_body is None and "email_body" in self.model_fields_set:
            _dict['emailBody'] = None

        # set to None if codice_destinatario (nullable) is None
        # and model_fields_set contains the field
        if self.codice_destinatario is None and "codice_destinatario" in self.model_fields_set:
            _dict['codiceDestinatario'] = None

        # set to None if pec (nullable) is None
        # and model_fields_set contains the field
        if self.pec is None and "pec" in self.model_fields_set:
            _dict['pec'] = None

        # set to None if modello_vendite_nota_debito_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_vendite_nota_debito_id is None and "modello_vendite_nota_debito_id" in self.model_fields_set:
            _dict['modelloVenditeNotaDebitoId'] = None

        # set to None if modello_vendite_nota_credito_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_vendite_nota_credito_id is None and "modello_vendite_nota_credito_id" in self.model_fields_set:
            _dict['modelloVenditeNotaCreditoId'] = None

        # set to None if modello_vendite_ricevuta_fiscale_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_vendite_ricevuta_fiscale_id is None and "modello_vendite_ricevuta_fiscale_id" in self.model_fields_set:
            _dict['modelloVenditeRicevutaFiscaleId'] = None

        # set to None if modello_vendite_fattura_professionista_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_vendite_fattura_professionista_id is None and "modello_vendite_fattura_professionista_id" in self.model_fields_set:
            _dict['modelloVenditeFatturaProfessionistaId'] = None

        # set to None if modello_vendite_fattura_differita_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_vendite_fattura_differita_id is None and "modello_vendite_fattura_differita_id" in self.model_fields_set:
            _dict['modelloVenditeFatturaDifferitaId'] = None

        # set to None if modello_vendite_fattura_acconto_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_vendite_fattura_acconto_id is None and "modello_vendite_fattura_acconto_id" in self.model_fields_set:
            _dict['modelloVenditeFatturaAccontoId'] = None

        # set to None if modello_acquisti_fattura_accompagnatoria_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_acquisti_fattura_accompagnatoria_id is None and "modello_acquisti_fattura_accompagnatoria_id" in self.model_fields_set:
            _dict['modelloAcquistiFatturaAccompagnatoriaId'] = None

        # set to None if modello_vendite_fattura_accompagnaoria_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_vendite_fattura_accompagnaoria_id is None and "modello_vendite_fattura_accompagnaoria_id" in self.model_fields_set:
            _dict['modelloVenditeFatturaAccompagnaoriaId'] = None

        # set to None if modello_acquisti_nota_debito_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_acquisti_nota_debito_id is None and "modello_acquisti_nota_debito_id" in self.model_fields_set:
            _dict['modelloAcquistiNotaDebitoId'] = None

        # set to None if modello_acquisti_nota_credito_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_acquisti_nota_credito_id is None and "modello_acquisti_nota_credito_id" in self.model_fields_set:
            _dict['modelloAcquistiNotaCreditoId'] = None

        # set to None if modello_acquisti_fattura_professionisti_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_acquisti_fattura_professionisti_id is None and "modello_acquisti_fattura_professionisti_id" in self.model_fields_set:
            _dict['modelloAcquistiFatturaProfessionistiId'] = None

        # set to None if modello_acquisti_fattura_differita_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_acquisti_fattura_differita_id is None and "modello_acquisti_fattura_differita_id" in self.model_fields_set:
            _dict['modelloAcquistiFatturaDifferitaId'] = None

        # set to None if modello_acquisti_fattura_acconto_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_acquisti_fattura_acconto_id is None and "modello_acquisti_fattura_acconto_id" in self.model_fields_set:
            _dict['modelloAcquistiFatturaAccontoId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Preferenze from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "ragioneSociale1": obj.get("ragioneSociale1"),
            "ragioneSociale2": obj.get("ragioneSociale2"),
            "partitaIva": obj.get("partitaIva"),
            "registroImprese": obj.get("registroImprese"),
            "codiceFiscale": obj.get("codiceFiscale"),
            "codiceSia": obj.get("codiceSia"),
            "codiceRea": obj.get("codiceRea"),
            "personaGiuridica": obj.get("personaGiuridica"),
            "dataNascita": obj.get("dataNascita"),
            "localitaNascita": obj.get("localitaNascita"),
            "provinciaNascita": obj.get("provinciaNascita"),
            "sesso": obj.get("sesso"),
            "attivita": obj.get("attivita"),
            "ivaEsclusa": obj.get("ivaEsclusa"),
            "decimaliPrezzoUnitario": obj.get("decimaliPrezzoUnitario"),
            "causaleProduzioneComponentiId": obj.get("causaleProduzioneComponentiId"),
            "causaleProduzioneCompostiId": obj.get("causaleProduzioneCompostiId"),
            "causaleMagazzinoVenditaId": obj.get("causaleMagazzinoVenditaId"),
            "causaleMagazzinoAcquistoId": obj.get("causaleMagazzinoAcquistoId"),
            "ricercaArticolo": RicercaArticolo.from_dict(obj["ricercaArticolo"]) if obj.get("ricercaArticolo") is not None else None,
            "dataSpeciale1": obj.get("dataSpeciale1"),
            "dataSpeciale2": obj.get("dataSpeciale2"),
            "giorniExtraDataSpeciale1": obj.get("giorniExtraDataSpeciale1"),
            "giorniExtraDataSpeciale2": obj.get("giorniExtraDataSpeciale2"),
            "pagatoManuale": obj.get("pagatoManuale"),
            "causaleMagazzinoMerciId": obj.get("causaleMagazzinoMerciId"),
            "magazzinoMerciId": obj.get("magazzinoMerciId"),
            "listinoMerciId": obj.get("listinoMerciId"),
            "modalitaPagamentoMerciId": obj.get("modalitaPagamentoMerciId"),
            "documentiCausaleIvaId": obj.get("documentiCausaleIvaId"),
            "documentiMagazzinoId": obj.get("documentiMagazzinoId"),
            "documentiListinoId": obj.get("documentiListinoId"),
            "eMail": obj.get("eMail"),
            "sitoWeb": obj.get("sitoWeb"),
            "annoContabile": obj.get("annoContabile"),
            "unitàDiMisura": obj.get("unitàDiMisura"),
            "causalePagamentoModelloCU": obj.get("causalePagamentoModelloCU"),
            "impostazioniSdi": ImpostazioniSdi.from_dict(obj["impostazioniSdi"]) if obj.get("impostazioniSdi") is not None else None,
            "tipoBilancio": obj.get("tipoBilancio"),
            "periodoIva": obj.get("periodoIva"),
            "liquidazioneIva": obj.get("liquidazioneIva"),
            "modificaRegistrazioneContabileAllaEmissione": obj.get("modificaRegistrazioneContabileAllaEmissione"),
            "ottimizzaEmissioneOrdini": obj.get("ottimizzaEmissioneOrdini"),
            "aggiungiAnnoInCorsoAlNumeroDocumento": obj.get("aggiungiAnnoInCorsoAlNumeroDocumento"),
            "consentiCambioManualeStatoDdt": obj.get("consentiCambioManualeStatoDdt"),
            "emailBody": obj.get("emailBody"),
            "emailAutoSend": obj.get("emailAutoSend"),
            "autoProduzione": obj.get("autoProduzione"),
            "codiceDestinatario": obj.get("codiceDestinatario"),
            "pec": obj.get("pec"),
            "modelloVenditeNotaDebitoId": obj.get("modelloVenditeNotaDebitoId"),
            "modelloVenditeNotaCreditoId": obj.get("modelloVenditeNotaCreditoId"),
            "modelloVenditeRicevutaFiscaleId": obj.get("modelloVenditeRicevutaFiscaleId"),
            "modelloVenditeFatturaProfessionistaId": obj.get("modelloVenditeFatturaProfessionistaId"),
            "modelloVenditeFatturaDifferitaId": obj.get("modelloVenditeFatturaDifferitaId"),
            "modelloVenditeFatturaAccontoId": obj.get("modelloVenditeFatturaAccontoId"),
            "modelloAcquistiFatturaAccompagnatoriaId": obj.get("modelloAcquistiFatturaAccompagnatoriaId"),
            "modelloVenditeFatturaAccompagnaoriaId": obj.get("modelloVenditeFatturaAccompagnaoriaId"),
            "modelloAcquistiNotaDebitoId": obj.get("modelloAcquistiNotaDebitoId"),
            "modelloAcquistiNotaCreditoId": obj.get("modelloAcquistiNotaCreditoId"),
            "modelloAcquistiFatturaProfessionistiId": obj.get("modelloAcquistiFatturaProfessionistiId"),
            "modelloAcquistiFatturaDifferitaId": obj.get("modelloAcquistiFatturaDifferitaId"),
            "modelloAcquistiFatturaAccontoId": obj.get("modelloAcquistiFatturaAccontoId"),
            "sedeLegale": SedeLegale.from_dict(obj["sedeLegale"]) if obj.get("sedeLegale") is not None else None,
            "sedeOperativa": SedeOperativa.from_dict(obj["sedeOperativa"]) if obj.get("sedeOperativa") is not None else None,
            "sedeAltra": SedeAltra.from_dict(obj["sedeAltra"]) if obj.get("sedeAltra") is not None else None
        })
        return _obj


