# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — accesso negato (vedi sotto le possibili cause). | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Un `403` può avere tre cause; nelle ultime due il campo `code` della risposta indica quale:  - il token non possiede lo scope richiesto dall'endpoint; - `code: cloud_not_active` — l'account lavora con una connessione locale e la Cloud API non espone i suoi dati. Per attivare il servizio cloud contatta l'assistenza, poi richiedi un nuovo token: lo stato del servizio è letto al rilascio del token; - `code: company_license_not_active` — la licenza dell'azienda indicata nel percorso è scaduta o non è attiva. Le altre aziende con licenza attiva restano accessibili.  Il motivo dell'errore è sempre nel campo `detail`. Ogni risposta di errore riporta inoltre `overridable`: quando vale `true`, l'errore di validazione è *forzabile* e basta ripetere la stessa richiesta aggiungendo `validationOverride=true` alla query string perché il servizio la accetti. È il caso delle anomalie formali su dati reali — la partita IVA di un fornitore estero, per esempio — che il cliente ha comunque bisogno di registrare.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: 3.0.2
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class FatturaElettronicaXmlTemplate(BaseModel):
    """
    Modello standard di fattura elettronica.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    soggetto_emittente: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="soggettoEmittente")
    id_trasmittente_id_paese: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="idTrasmittenteIdPaese")
    cedente_prestatore_id_paese: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="cedentePrestatoreIdPaese")
    progressivo_invio: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=10)]] = Field(default=None, alias="progressivoInvio")
    albo_professionale: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="alboProfessionale")
    provincia_albo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="provinciaAlbo")
    numero_iscrizione_albo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="numeroIscrizioneAlbo")
    data_iscrizione_albo: Optional[datetime] = Field(default=None, alias="dataIscrizioneAlbo")
    regime_fiscale: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=4)]] = Field(default=None, alias="regimeFiscale")
    sede_nazione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="sedeNazione")
    sede_numero_civico: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=8)]] = Field(default=None, alias="sedeNumeroCivico")
    stabile_organizzazione_indirizzo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="stabileOrganizzazioneIndirizzo")
    stabile_organizzazione_numero_civico: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=8)]] = Field(default=None, alias="stabileOrganizzazioneNumeroCivico")
    stabile_organizzazione_cap: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=5)]] = Field(default=None, alias="stabileOrganizzazioneCap")
    stabile_organizzazione_comune: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="stabileOrganizzazioneComune")
    stabile_organizzazione_provincia: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="stabileOrganizzazioneProvincia")
    stabile_organizzazione_nazione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="stabileOrganizzazioneNazione")
    rea_numero: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, alias="reaNumero")
    rea_ufficio: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="reaUfficio")
    rea_capitale_sociale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="reaCapitaleSociale")
    rea_socio_unico: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="reaSocioUnico")
    rea_stato_liquidazione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="reaStatoLiquidazione")
    rappresentante_id_paese: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="rappresentanteIdPaese")
    rappresentante_id_codice: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=28)]] = Field(default=None, alias="rappresentanteIdCodice")
    rappresentante_codice_fiscale: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16)]] = Field(default=None, alias="rappresentanteCodiceFiscale")
    rappresentante_denominazione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=80)]] = Field(default=None, alias="rappresentanteDenominazione")
    rappresentante_nome: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="rappresentanteNome")
    rappresentante_cognome: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="rappresentanteCognome")
    rappresentante_titolo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=10)]] = Field(default=None, alias="rappresentanteTitolo")
    rappresentante_cod_eori: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=17)]] = Field(default=None, alias="rappresentanteCodEori")
    intermediario_id_paese: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2)]] = Field(default=None, alias="intermediarioIdPaese")
    intermediario_id_codice: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=28)]] = Field(default=None, alias="intermediarioIdCodice")
    intermediario_codice_fiscale: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=16)]] = Field(default=None, alias="intermediarioCodiceFiscale")
    intermediario_denominazione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=80)]] = Field(default=None, alias="intermediarioDenominazione")
    intermediario_nome: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="intermediarioNome")
    intermediario_cognome: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, alias="intermediarioCognome")
    intermediario_titolo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=10)]] = Field(default=None, alias="intermediarioTitolo")
    intermediario_cod_eori: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=17)]] = Field(default=None, alias="intermediarioCodEori")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "soggettoEmittente", "idTrasmittenteIdPaese", "cedentePrestatoreIdPaese", "progressivoInvio", "alboProfessionale", "provinciaAlbo", "numeroIscrizioneAlbo", "dataIscrizioneAlbo", "regimeFiscale", "sedeNazione", "sedeNumeroCivico", "stabileOrganizzazioneIndirizzo", "stabileOrganizzazioneNumeroCivico", "stabileOrganizzazioneCap", "stabileOrganizzazioneComune", "stabileOrganizzazioneProvincia", "stabileOrganizzazioneNazione", "reaNumero", "reaUfficio", "reaCapitaleSociale", "reaSocioUnico", "reaStatoLiquidazione", "rappresentanteIdPaese", "rappresentanteIdCodice", "rappresentanteCodiceFiscale", "rappresentanteDenominazione", "rappresentanteNome", "rappresentanteCognome", "rappresentanteTitolo", "rappresentanteCodEori", "intermediarioIdPaese", "intermediarioIdCodice", "intermediarioCodiceFiscale", "intermediarioDenominazione", "intermediarioNome", "intermediarioCognome", "intermediarioTitolo", "intermediarioCodEori"]

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
        """Create an instance of FatturaElettronicaXmlTemplate from a JSON string"""
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
        # set to None if soggetto_emittente (nullable) is None
        # and model_fields_set contains the field
        if self.soggetto_emittente is None and "soggetto_emittente" in self.model_fields_set:
            _dict['soggettoEmittente'] = None

        # set to None if id_trasmittente_id_paese (nullable) is None
        # and model_fields_set contains the field
        if self.id_trasmittente_id_paese is None and "id_trasmittente_id_paese" in self.model_fields_set:
            _dict['idTrasmittenteIdPaese'] = None

        # set to None if cedente_prestatore_id_paese (nullable) is None
        # and model_fields_set contains the field
        if self.cedente_prestatore_id_paese is None and "cedente_prestatore_id_paese" in self.model_fields_set:
            _dict['cedentePrestatoreIdPaese'] = None

        # set to None if progressivo_invio (nullable) is None
        # and model_fields_set contains the field
        if self.progressivo_invio is None and "progressivo_invio" in self.model_fields_set:
            _dict['progressivoInvio'] = None

        # set to None if albo_professionale (nullable) is None
        # and model_fields_set contains the field
        if self.albo_professionale is None and "albo_professionale" in self.model_fields_set:
            _dict['alboProfessionale'] = None

        # set to None if provincia_albo (nullable) is None
        # and model_fields_set contains the field
        if self.provincia_albo is None and "provincia_albo" in self.model_fields_set:
            _dict['provinciaAlbo'] = None

        # set to None if numero_iscrizione_albo (nullable) is None
        # and model_fields_set contains the field
        if self.numero_iscrizione_albo is None and "numero_iscrizione_albo" in self.model_fields_set:
            _dict['numeroIscrizioneAlbo'] = None

        # set to None if data_iscrizione_albo (nullable) is None
        # and model_fields_set contains the field
        if self.data_iscrizione_albo is None and "data_iscrizione_albo" in self.model_fields_set:
            _dict['dataIscrizioneAlbo'] = None

        # set to None if regime_fiscale (nullable) is None
        # and model_fields_set contains the field
        if self.regime_fiscale is None and "regime_fiscale" in self.model_fields_set:
            _dict['regimeFiscale'] = None

        # set to None if sede_nazione (nullable) is None
        # and model_fields_set contains the field
        if self.sede_nazione is None and "sede_nazione" in self.model_fields_set:
            _dict['sedeNazione'] = None

        # set to None if sede_numero_civico (nullable) is None
        # and model_fields_set contains the field
        if self.sede_numero_civico is None and "sede_numero_civico" in self.model_fields_set:
            _dict['sedeNumeroCivico'] = None

        # set to None if stabile_organizzazione_indirizzo (nullable) is None
        # and model_fields_set contains the field
        if self.stabile_organizzazione_indirizzo is None and "stabile_organizzazione_indirizzo" in self.model_fields_set:
            _dict['stabileOrganizzazioneIndirizzo'] = None

        # set to None if stabile_organizzazione_numero_civico (nullable) is None
        # and model_fields_set contains the field
        if self.stabile_organizzazione_numero_civico is None and "stabile_organizzazione_numero_civico" in self.model_fields_set:
            _dict['stabileOrganizzazioneNumeroCivico'] = None

        # set to None if stabile_organizzazione_cap (nullable) is None
        # and model_fields_set contains the field
        if self.stabile_organizzazione_cap is None and "stabile_organizzazione_cap" in self.model_fields_set:
            _dict['stabileOrganizzazioneCap'] = None

        # set to None if stabile_organizzazione_comune (nullable) is None
        # and model_fields_set contains the field
        if self.stabile_organizzazione_comune is None and "stabile_organizzazione_comune" in self.model_fields_set:
            _dict['stabileOrganizzazioneComune'] = None

        # set to None if stabile_organizzazione_provincia (nullable) is None
        # and model_fields_set contains the field
        if self.stabile_organizzazione_provincia is None and "stabile_organizzazione_provincia" in self.model_fields_set:
            _dict['stabileOrganizzazioneProvincia'] = None

        # set to None if stabile_organizzazione_nazione (nullable) is None
        # and model_fields_set contains the field
        if self.stabile_organizzazione_nazione is None and "stabile_organizzazione_nazione" in self.model_fields_set:
            _dict['stabileOrganizzazioneNazione'] = None

        # set to None if rea_numero (nullable) is None
        # and model_fields_set contains the field
        if self.rea_numero is None and "rea_numero" in self.model_fields_set:
            _dict['reaNumero'] = None

        # set to None if rea_ufficio (nullable) is None
        # and model_fields_set contains the field
        if self.rea_ufficio is None and "rea_ufficio" in self.model_fields_set:
            _dict['reaUfficio'] = None

        # set to None if rea_capitale_sociale (nullable) is None
        # and model_fields_set contains the field
        if self.rea_capitale_sociale is None and "rea_capitale_sociale" in self.model_fields_set:
            _dict['reaCapitaleSociale'] = None

        # set to None if rea_socio_unico (nullable) is None
        # and model_fields_set contains the field
        if self.rea_socio_unico is None and "rea_socio_unico" in self.model_fields_set:
            _dict['reaSocioUnico'] = None

        # set to None if rea_stato_liquidazione (nullable) is None
        # and model_fields_set contains the field
        if self.rea_stato_liquidazione is None and "rea_stato_liquidazione" in self.model_fields_set:
            _dict['reaStatoLiquidazione'] = None

        # set to None if rappresentante_id_paese (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_id_paese is None and "rappresentante_id_paese" in self.model_fields_set:
            _dict['rappresentanteIdPaese'] = None

        # set to None if rappresentante_id_codice (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_id_codice is None and "rappresentante_id_codice" in self.model_fields_set:
            _dict['rappresentanteIdCodice'] = None

        # set to None if rappresentante_codice_fiscale (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_codice_fiscale is None and "rappresentante_codice_fiscale" in self.model_fields_set:
            _dict['rappresentanteCodiceFiscale'] = None

        # set to None if rappresentante_denominazione (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_denominazione is None and "rappresentante_denominazione" in self.model_fields_set:
            _dict['rappresentanteDenominazione'] = None

        # set to None if rappresentante_nome (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_nome is None and "rappresentante_nome" in self.model_fields_set:
            _dict['rappresentanteNome'] = None

        # set to None if rappresentante_cognome (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_cognome is None and "rappresentante_cognome" in self.model_fields_set:
            _dict['rappresentanteCognome'] = None

        # set to None if rappresentante_titolo (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_titolo is None and "rappresentante_titolo" in self.model_fields_set:
            _dict['rappresentanteTitolo'] = None

        # set to None if rappresentante_cod_eori (nullable) is None
        # and model_fields_set contains the field
        if self.rappresentante_cod_eori is None and "rappresentante_cod_eori" in self.model_fields_set:
            _dict['rappresentanteCodEori'] = None

        # set to None if intermediario_id_paese (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_id_paese is None and "intermediario_id_paese" in self.model_fields_set:
            _dict['intermediarioIdPaese'] = None

        # set to None if intermediario_id_codice (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_id_codice is None and "intermediario_id_codice" in self.model_fields_set:
            _dict['intermediarioIdCodice'] = None

        # set to None if intermediario_codice_fiscale (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_codice_fiscale is None and "intermediario_codice_fiscale" in self.model_fields_set:
            _dict['intermediarioCodiceFiscale'] = None

        # set to None if intermediario_denominazione (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_denominazione is None and "intermediario_denominazione" in self.model_fields_set:
            _dict['intermediarioDenominazione'] = None

        # set to None if intermediario_nome (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_nome is None and "intermediario_nome" in self.model_fields_set:
            _dict['intermediarioNome'] = None

        # set to None if intermediario_cognome (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_cognome is None and "intermediario_cognome" in self.model_fields_set:
            _dict['intermediarioCognome'] = None

        # set to None if intermediario_titolo (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_titolo is None and "intermediario_titolo" in self.model_fields_set:
            _dict['intermediarioTitolo'] = None

        # set to None if intermediario_cod_eori (nullable) is None
        # and model_fields_set contains the field
        if self.intermediario_cod_eori is None and "intermediario_cod_eori" in self.model_fields_set:
            _dict['intermediarioCodEori'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FatturaElettronicaXmlTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "soggettoEmittente": obj.get("soggettoEmittente"),
            "idTrasmittenteIdPaese": obj.get("idTrasmittenteIdPaese"),
            "cedentePrestatoreIdPaese": obj.get("cedentePrestatoreIdPaese"),
            "progressivoInvio": obj.get("progressivoInvio"),
            "alboProfessionale": obj.get("alboProfessionale"),
            "provinciaAlbo": obj.get("provinciaAlbo"),
            "numeroIscrizioneAlbo": obj.get("numeroIscrizioneAlbo"),
            "dataIscrizioneAlbo": obj.get("dataIscrizioneAlbo"),
            "regimeFiscale": obj.get("regimeFiscale"),
            "sedeNazione": obj.get("sedeNazione"),
            "sedeNumeroCivico": obj.get("sedeNumeroCivico"),
            "stabileOrganizzazioneIndirizzo": obj.get("stabileOrganizzazioneIndirizzo"),
            "stabileOrganizzazioneNumeroCivico": obj.get("stabileOrganizzazioneNumeroCivico"),
            "stabileOrganizzazioneCap": obj.get("stabileOrganizzazioneCap"),
            "stabileOrganizzazioneComune": obj.get("stabileOrganizzazioneComune"),
            "stabileOrganizzazioneProvincia": obj.get("stabileOrganizzazioneProvincia"),
            "stabileOrganizzazioneNazione": obj.get("stabileOrganizzazioneNazione"),
            "reaNumero": obj.get("reaNumero"),
            "reaUfficio": obj.get("reaUfficio"),
            "reaCapitaleSociale": obj.get("reaCapitaleSociale"),
            "reaSocioUnico": obj.get("reaSocioUnico"),
            "reaStatoLiquidazione": obj.get("reaStatoLiquidazione"),
            "rappresentanteIdPaese": obj.get("rappresentanteIdPaese"),
            "rappresentanteIdCodice": obj.get("rappresentanteIdCodice"),
            "rappresentanteCodiceFiscale": obj.get("rappresentanteCodiceFiscale"),
            "rappresentanteDenominazione": obj.get("rappresentanteDenominazione"),
            "rappresentanteNome": obj.get("rappresentanteNome"),
            "rappresentanteCognome": obj.get("rappresentanteCognome"),
            "rappresentanteTitolo": obj.get("rappresentanteTitolo"),
            "rappresentanteCodEori": obj.get("rappresentanteCodEori"),
            "intermediarioIdPaese": obj.get("intermediarioIdPaese"),
            "intermediarioIdCodice": obj.get("intermediarioIdCodice"),
            "intermediarioCodiceFiscale": obj.get("intermediarioCodiceFiscale"),
            "intermediarioDenominazione": obj.get("intermediarioDenominazione"),
            "intermediarioNome": obj.get("intermediarioNome"),
            "intermediarioCognome": obj.get("intermediarioCognome"),
            "intermediarioTitolo": obj.get("intermediarioTitolo"),
            "intermediarioCodEori": obj.get("intermediarioCodEori")
        })
        return _obj


