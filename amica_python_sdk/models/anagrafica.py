# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — accesso negato (vedi sotto le possibili cause). | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Un `403` può avere tre cause; nelle ultime due il campo `code` della risposta indica quale:  - il token non possiede lo scope richiesto dall'endpoint; - `code: cloud_not_active` — l'account lavora con una connessione locale e la Cloud API non espone i suoi dati. Per attivare il servizio cloud contatta l'assistenza, poi richiedi un nuovo token: lo stato del servizio è letto al rilascio del token; - `code: company_license_not_active` — la licenza dell'azienda indicata nel percorso è scaduta o non è attiva. Le altre aziende con licenza attiva restano accessibili.  Il motivo dell'errore è sempre nel campo `detail`. Ogni risposta di errore riporta inoltre `overridable`: quando vale `true`, l'errore di validazione è *forzabile* e basta ripetere la stessa richiesta aggiungendo `validationOverride=true` alla query string perché il servizio la accetti. È il caso delle anomalie formali su dati reali — la partita IVA di un fornitore estero, per esempio — che il cliente ha comunque bisogno di registrare.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: 3.2.0
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from amica_python_sdk.models.anagrafica_nominativo1 import AnagraficaNominativo1
from amica_python_sdk.models.anagrafica_nominativo2 import AnagraficaNominativo2
from amica_python_sdk.models.anagrafica_sede_legale import AnagraficaSedeLegale
from amica_python_sdk.models.area_geografica import AreaGeografica
from amica_python_sdk.models.banca import Banca
from amica_python_sdk.models.indirizzo import Indirizzo
from amica_python_sdk.models.nazione import Nazione
from amica_python_sdk.models.valuta import Valuta
from typing import Optional, Set
from typing_extensions import Self

class Anagrafica(BaseModel):
    """
    Anagrafica di cliente, fornitore, agente o vettore.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    modello_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Modello`. Sempre null. Questa proprietà è usata solo dal client desktop Amica 20 per Windows ed è da considerarsi obsoleta.", alias="modelloId")
    nazione_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Nazione` (nazione).", alias="nazioneId")
    nazione: Optional[Nazione] = None
    area_geografica_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `AreaGeografica` (area geografica).", alias="areaGeograficaId")
    area_geografica: Optional[AreaGeografica] = Field(default=None, alias="areaGeografica")
    valuta_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Valuta` (valuta).", alias="valutaId")
    valuta: Optional[Valuta] = None
    indirizzo_predefinito_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco dell'`Indirizzo` (indirizzo) predefinito.", alias="indirizzoPredefinitoId")
    indirizzi: Optional[List[Indirizzo]] = Field(default=None, description="Elenco degli `Indirizzo` dell'anagrafica.")
    scheda_cliente: Optional[SchedaCliente] = Field(default=None, alias="schedaCliente")
    scheda_fornitore: Optional[SchedaFornitore] = Field(default=None, alias="schedaFornitore")
    stato: Optional[StrictBool] = Field(default=None, description="Indica se l'anagrafica è attiva o meno.")
    cliente: Optional[StrictBool] = Field(default=None, description="Indica se l'anagrafica è un cliente.")
    fornitore: Optional[StrictBool] = Field(default=None, description="Indica se l'anagrafica è un fornitore.")
    agente: Optional[StrictBool] = Field(default=None, description="Indica se l'anagrafica opera come agente di vendita per conto dell'azienda.")
    vettore: Optional[StrictBool] = Field(default=None, description="Indica se l'anagrafica opera come vettore.")
    capo_area: Optional[StrictBool] = Field(default=None, description="Indica se l'anagrafica opera come capo area.", alias="capoArea")
    persona_giuridica: Optional[StrictBool] = Field(default=None, description="Indica se l'anagrafica è una persona giuridica o meno. `true` indica una persona giuridica, `false` una persona fisica.", alias="personaGiuridica")
    banca: Optional[Banca] = None
    nominativo1: Optional[AnagraficaNominativo1] = None
    nominativo2: Optional[AnagraficaNominativo2] = None
    sede_legale: Optional[AnagraficaSedeLegale] = Field(default=None, alias="sedeLegale")
    codice: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=10)]] = Field(default=None, description="Codice assegnato all'anagrafica.")
    data_inserimento: Optional[datetime] = Field(default=None, description="Data di primo inserimento.", alias="dataInserimento")
    ragione_sociale1: Annotated[str, Field(min_length=0, strict=True, max_length=60)] = Field(description="Ragione sociale, oppure nome e cognome della persona fisica.", alias="ragioneSociale1")
    ragione_sociale2: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Eventuale seconda riga della ragione sociale. Usata principalmente nelle stampe, quando si vuole suddividere la ragione sociale su due righe.", alias="ragioneSociale2")
    e_mail: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Indirizzo email.", alias="eMail")
    sito_web: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Indirizzo web.", alias="sitoWeb")
    partita_iva: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=30)]] = Field(default=None, description="Partita IVA. La correttezza formale è verificata dal servizio al salvataggio: l'errore che ne deriva è forzabile con `validationOverride`.", alias="partitaIva")
    codice_fiscale: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, description="Codice fiscale. Solitamente diverso dalla `PartitaIva`. Come per la partita IVA, la correttezza formale è verificata dal servizio al salvataggio e l'errore è forzabile con `validationOverride`.", alias="codiceFiscale")
    note: Optional[StrictStr] = Field(default=None, description="Note.")
    note_importanti: Optional[StrictStr] = Field(default=None, description="Note rilevanti. I client ufficiali Amica le evidenziano alla creazione di un nuovo documento fiscale.", alias="noteImportanti")
    pec: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=120)]] = Field(default=None, description="Indirizzo Pec (posta elettronica certificata).")
    codice_destinatario: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=7)]] = Field(default=None, description="Codice destinatario per il sistema fiscale italiano. Usato per il recapito delle fatture elettroniche italiane.", alias="codiceDestinatario")
    dichiarazione_intento: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=200)]] = Field(default=None, description="Numero di protocollo della dichiarazione d'intento.", alias="dichiarazioneIntento")
    riferimento_amministrazione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, description="Solitamente necessario quando si ha a che fare con enti della Pubblica Amministrazione italiana. Identifica univocamente l'ufficio di destinazione all'interno della PA.", alias="riferimentoAmministrazione")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "modelloId", "nazioneId", "nazione", "areaGeograficaId", "areaGeografica", "valutaId", "valuta", "indirizzoPredefinitoId", "indirizzi", "schedaCliente", "schedaFornitore", "stato", "cliente", "fornitore", "agente", "vettore", "capoArea", "personaGiuridica", "banca", "nominativo1", "nominativo2", "sedeLegale", "codice", "dataInserimento", "ragioneSociale1", "ragioneSociale2", "eMail", "sitoWeb", "partitaIva", "codiceFiscale", "note", "noteImportanti", "pec", "codiceDestinatario", "dichiarazioneIntento", "riferimentoAmministrazione"]

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
        """Create an instance of Anagrafica from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of nazione
        if self.nazione:
            _dict['nazione'] = self.nazione.to_dict()
        # override the default output from pydantic by calling `to_dict()` of area_geografica
        if self.area_geografica:
            _dict['areaGeografica'] = self.area_geografica.to_dict()
        # override the default output from pydantic by calling `to_dict()` of valuta
        if self.valuta:
            _dict['valuta'] = self.valuta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in indirizzi (list)
        _items = []
        if self.indirizzi:
            for _item_indirizzi in self.indirizzi:
                if _item_indirizzi:
                    _items.append(_item_indirizzi.to_dict())
            _dict['indirizzi'] = _items
        # override the default output from pydantic by calling `to_dict()` of scheda_cliente
        if self.scheda_cliente:
            _dict['schedaCliente'] = self.scheda_cliente.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scheda_fornitore
        if self.scheda_fornitore:
            _dict['schedaFornitore'] = self.scheda_fornitore.to_dict()
        # override the default output from pydantic by calling `to_dict()` of banca
        if self.banca:
            _dict['banca'] = self.banca.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nominativo1
        if self.nominativo1:
            _dict['nominativo1'] = self.nominativo1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nominativo2
        if self.nominativo2:
            _dict['nominativo2'] = self.nominativo2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sede_legale
        if self.sede_legale:
            _dict['sedeLegale'] = self.sede_legale.to_dict()
        # set to None if modello_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_id is None and "modello_id" in self.model_fields_set:
            _dict['modelloId'] = None

        # set to None if nazione_id (nullable) is None
        # and model_fields_set contains the field
        if self.nazione_id is None and "nazione_id" in self.model_fields_set:
            _dict['nazioneId'] = None

        # set to None if area_geografica_id (nullable) is None
        # and model_fields_set contains the field
        if self.area_geografica_id is None and "area_geografica_id" in self.model_fields_set:
            _dict['areaGeograficaId'] = None

        # set to None if valuta_id (nullable) is None
        # and model_fields_set contains the field
        if self.valuta_id is None and "valuta_id" in self.model_fields_set:
            _dict['valutaId'] = None

        # set to None if indirizzo_predefinito_id (nullable) is None
        # and model_fields_set contains the field
        if self.indirizzo_predefinito_id is None and "indirizzo_predefinito_id" in self.model_fields_set:
            _dict['indirizzoPredefinitoId'] = None

        # set to None if indirizzi (nullable) is None
        # and model_fields_set contains the field
        if self.indirizzi is None and "indirizzi" in self.model_fields_set:
            _dict['indirizzi'] = None

        # set to None if codice (nullable) is None
        # and model_fields_set contains the field
        if self.codice is None and "codice" in self.model_fields_set:
            _dict['codice'] = None

        # set to None if data_inserimento (nullable) is None
        # and model_fields_set contains the field
        if self.data_inserimento is None and "data_inserimento" in self.model_fields_set:
            _dict['dataInserimento'] = None

        # set to None if ragione_sociale2 (nullable) is None
        # and model_fields_set contains the field
        if self.ragione_sociale2 is None and "ragione_sociale2" in self.model_fields_set:
            _dict['ragioneSociale2'] = None

        # set to None if e_mail (nullable) is None
        # and model_fields_set contains the field
        if self.e_mail is None and "e_mail" in self.model_fields_set:
            _dict['eMail'] = None

        # set to None if sito_web (nullable) is None
        # and model_fields_set contains the field
        if self.sito_web is None and "sito_web" in self.model_fields_set:
            _dict['sitoWeb'] = None

        # set to None if partita_iva (nullable) is None
        # and model_fields_set contains the field
        if self.partita_iva is None and "partita_iva" in self.model_fields_set:
            _dict['partitaIva'] = None

        # set to None if codice_fiscale (nullable) is None
        # and model_fields_set contains the field
        if self.codice_fiscale is None and "codice_fiscale" in self.model_fields_set:
            _dict['codiceFiscale'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if note_importanti (nullable) is None
        # and model_fields_set contains the field
        if self.note_importanti is None and "note_importanti" in self.model_fields_set:
            _dict['noteImportanti'] = None

        # set to None if pec (nullable) is None
        # and model_fields_set contains the field
        if self.pec is None and "pec" in self.model_fields_set:
            _dict['pec'] = None

        # set to None if codice_destinatario (nullable) is None
        # and model_fields_set contains the field
        if self.codice_destinatario is None and "codice_destinatario" in self.model_fields_set:
            _dict['codiceDestinatario'] = None

        # set to None if dichiarazione_intento (nullable) is None
        # and model_fields_set contains the field
        if self.dichiarazione_intento is None and "dichiarazione_intento" in self.model_fields_set:
            _dict['dichiarazioneIntento'] = None

        # set to None if riferimento_amministrazione (nullable) is None
        # and model_fields_set contains the field
        if self.riferimento_amministrazione is None and "riferimento_amministrazione" in self.model_fields_set:
            _dict['riferimentoAmministrazione'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Anagrafica from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "modelloId": obj.get("modelloId"),
            "nazioneId": obj.get("nazioneId"),
            "nazione": Nazione.from_dict(obj["nazione"]) if obj.get("nazione") is not None else None,
            "areaGeograficaId": obj.get("areaGeograficaId"),
            "areaGeografica": AreaGeografica.from_dict(obj["areaGeografica"]) if obj.get("areaGeografica") is not None else None,
            "valutaId": obj.get("valutaId"),
            "valuta": Valuta.from_dict(obj["valuta"]) if obj.get("valuta") is not None else None,
            "indirizzoPredefinitoId": obj.get("indirizzoPredefinitoId"),
            "indirizzi": [Indirizzo.from_dict(_item) for _item in obj["indirizzi"]] if obj.get("indirizzi") is not None else None,
            "schedaCliente": SchedaCliente.from_dict(obj["schedaCliente"]) if obj.get("schedaCliente") is not None else None,
            "schedaFornitore": SchedaFornitore.from_dict(obj["schedaFornitore"]) if obj.get("schedaFornitore") is not None else None,
            "stato": obj.get("stato"),
            "cliente": obj.get("cliente"),
            "fornitore": obj.get("fornitore"),
            "agente": obj.get("agente"),
            "vettore": obj.get("vettore"),
            "capoArea": obj.get("capoArea"),
            "personaGiuridica": obj.get("personaGiuridica"),
            "banca": Banca.from_dict(obj["banca"]) if obj.get("banca") is not None else None,
            "nominativo1": AnagraficaNominativo1.from_dict(obj["nominativo1"]) if obj.get("nominativo1") is not None else None,
            "nominativo2": AnagraficaNominativo2.from_dict(obj["nominativo2"]) if obj.get("nominativo2") is not None else None,
            "sedeLegale": AnagraficaSedeLegale.from_dict(obj["sedeLegale"]) if obj.get("sedeLegale") is not None else None,
            "codice": obj.get("codice"),
            "dataInserimento": obj.get("dataInserimento"),
            "ragioneSociale1": obj.get("ragioneSociale1"),
            "ragioneSociale2": obj.get("ragioneSociale2"),
            "eMail": obj.get("eMail"),
            "sitoWeb": obj.get("sitoWeb"),
            "partitaIva": obj.get("partitaIva"),
            "codiceFiscale": obj.get("codiceFiscale"),
            "note": obj.get("note"),
            "noteImportanti": obj.get("noteImportanti"),
            "pec": obj.get("pec"),
            "codiceDestinatario": obj.get("codiceDestinatario"),
            "dichiarazioneIntento": obj.get("dichiarazioneIntento"),
            "riferimentoAmministrazione": obj.get("riferimentoAmministrazione")
        })
        return _obj

from amica_python_sdk.models.scheda_cliente import SchedaCliente
from amica_python_sdk.models.scheda_fornitore import SchedaFornitore
# TODO: Rewrite to not use raise_errors
Anagrafica.model_rebuild(raise_errors=False)

