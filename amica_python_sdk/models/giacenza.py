# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — il token non possiede lo scope richiesto. | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Alcune risposte `400` includono un campo `overridable` che indica se l'errore di validazione può essere ignorato impostando il parametro `validationOverride` a `true`.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: v3
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from amica_python_sdk.models.articolo import Articolo
from amica_python_sdk.models.magazzino import Magazzino
from typing import Optional, Set
from typing_extensions import Self

class Giacenza(BaseModel):
    """
    Giacenza corrente (inventario).
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    magazzino_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.Giacenza.Magazzino.", alias="magazzinoId")
    magazzino: Optional[Magazzino] = None
    articolo_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.Giacenza.Articolo.", alias="articoloId")
    articolo: Optional[Articolo] = None
    quantit_in_giacenza: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità in giacenza.", alias="quantitàInGiacenza")
    quantit_impegnata: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità impegnata.", alias="quantitàImpegnata")
    quantit_ordinata: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità ordinata.", alias="quantitàOrdinata")
    scorta_minima: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Scorta minima.", alias="scortaMinima")
    gestione_sottoscorta: Optional[StrictBool] = Field(default=None, description="Indica se devono essere generati gli avvisi di sottoscorta.", alias="gestioneSottoscorta")
    data_ultimo_carico: Optional[datetime] = Field(default=None, description="Data dell'ultimo carico.", alias="dataUltimoCarico")
    data_ultimo_scarico: Optional[datetime] = Field(default=None, description="Data dell'ultimo scarico.", alias="dataUltimoScarico")
    carico_quantit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità totale caricata.", alias="caricoQuantità")
    carico_valore: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valore totale caricato.", alias="caricoValore")
    scarico_quantit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità totale scaricata.", alias="scaricoQuantità")
    scarico_valore: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Valore totale scaricato.", alias="scaricoValore")
    identificativo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, description="Numero di serie, o qualsiasi altro identificativo.")
    identificativo_esteso: Optional[StrictStr] = Field(default=None, description="Identificativo esteso.", alias="identificativoEsteso")
    data: Optional[datetime] = Field(default=None, description="Data di scadenza, produzione, fine garanzia o altro.")
    colore: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, description="Colore.")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "magazzinoId", "magazzino", "articoloId", "articolo", "quantitàInGiacenza", "quantitàImpegnata", "quantitàOrdinata", "scortaMinima", "gestioneSottoscorta", "dataUltimoCarico", "dataUltimoScarico", "caricoQuantità", "caricoValore", "scaricoQuantità", "scaricoValore", "identificativo", "identificativoEsteso", "data", "colore"]

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
        """Create an instance of Giacenza from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of magazzino
        if self.magazzino:
            _dict['magazzino'] = self.magazzino.to_dict()
        # override the default output from pydantic by calling `to_dict()` of articolo
        if self.articolo:
            _dict['articolo'] = self.articolo.to_dict()
        # set to None if data_ultimo_carico (nullable) is None
        # and model_fields_set contains the field
        if self.data_ultimo_carico is None and "data_ultimo_carico" in self.model_fields_set:
            _dict['dataUltimoCarico'] = None

        # set to None if data_ultimo_scarico (nullable) is None
        # and model_fields_set contains the field
        if self.data_ultimo_scarico is None and "data_ultimo_scarico" in self.model_fields_set:
            _dict['dataUltimoScarico'] = None

        # set to None if identificativo (nullable) is None
        # and model_fields_set contains the field
        if self.identificativo is None and "identificativo" in self.model_fields_set:
            _dict['identificativo'] = None

        # set to None if identificativo_esteso (nullable) is None
        # and model_fields_set contains the field
        if self.identificativo_esteso is None and "identificativo_esteso" in self.model_fields_set:
            _dict['identificativoEsteso'] = None

        # set to None if data (nullable) is None
        # and model_fields_set contains the field
        if self.data is None and "data" in self.model_fields_set:
            _dict['data'] = None

        # set to None if colore (nullable) is None
        # and model_fields_set contains the field
        if self.colore is None and "colore" in self.model_fields_set:
            _dict['colore'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Giacenza from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "magazzinoId": obj.get("magazzinoId"),
            "magazzino": Magazzino.from_dict(obj["magazzino"]) if obj.get("magazzino") is not None else None,
            "articoloId": obj.get("articoloId"),
            "articolo": Articolo.from_dict(obj["articolo"]) if obj.get("articolo") is not None else None,
            "quantitàInGiacenza": obj.get("quantitàInGiacenza"),
            "quantitàImpegnata": obj.get("quantitàImpegnata"),
            "quantitàOrdinata": obj.get("quantitàOrdinata"),
            "scortaMinima": obj.get("scortaMinima"),
            "gestioneSottoscorta": obj.get("gestioneSottoscorta"),
            "dataUltimoCarico": obj.get("dataUltimoCarico"),
            "dataUltimoScarico": obj.get("dataUltimoScarico"),
            "caricoQuantità": obj.get("caricoQuantità"),
            "caricoValore": obj.get("caricoValore"),
            "scaricoQuantità": obj.get("scaricoQuantità"),
            "scaricoValore": obj.get("scaricoValore"),
            "identificativo": obj.get("identificativo"),
            "identificativoEsteso": obj.get("identificativoEsteso"),
            "data": obj.get("data"),
            "colore": obj.get("colore")
        })
        return _obj


