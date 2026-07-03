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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from amica_python_sdk.models.registrazione_contabile_riga import RegistrazioneContabileRiga
from typing import Optional, Set
from typing_extensions import Self

class RegistrazioneContabile(BaseModel):
    """
    Registrazione contabile.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    data: Optional[datetime] = Field(default=None, description="Data della registrazione contabile.")
    data_competenza: Optional[datetime] = Field(default=None, description="Data di competenza.", alias="dataCompetenza")
    numero: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=1)]] = Field(default=None, description="Numero della registrazione contabile.")
    tipo_registrazione: Optional[StrictStr] = Field(default=None, description="Tipo di registrazione.", alias="tipoRegistrazione")
    segno_iva: Optional[StrictStr] = Field(default=None, description="Positività o negatività dell'IVA.", alias="segnoIva")
    tipo_operazione: Optional[StrictStr] = Field(default=None, description="Tipo di operazione contabile.", alias="tipoOperazione")
    registro_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `RegistroIva`.", alias="registroIvaId")
    anagrafica_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.Anagrafica.", alias="anagraficaId")
    pagamento_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.Pagamento.", alias="pagamentoId")
    documento_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.RegistrazioneContabile.Documento.", alias="documentoId")
    documento: Optional[Documento] = None
    data_documento: Optional[datetime] = Field(default=None, description="Data del documento di riferimento.", alias="dataDocumento")
    documento_numero_parte_testo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=40)]] = Field(default=None, description="La parte alfanumerica del numero documento, se presente (es. \"bis\").", alias="documentoNumeroParteTesto")
    documento_numero_parte_numerica: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=1)]] = Field(default=None, description="La parte numerica del numero documento (es. \"99\").", alias="documentoNumeroParteNumerica")
    documento_numero: Optional[StrictStr] = Field(default=None, description="Numero documento completo, es. \"99/bis\". Il documento deve essere già stato salvato sul backend.", alias="documentoNumero")
    protocollo: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=1)]] = Field(default=None, description="Numero di protocollo.")
    descrizione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=60)]] = Field(default=None, description="Descrizione.")
    note: Optional[StrictStr] = Field(default=None, description="Note.")
    righe: Optional[List[RegistrazioneContabileRiga]] = Field(default=None, description="Righe della registrazione contabile.")
    castelletto_iva: Optional[List[CastellettoIva]] = Field(default=None, description="Importo IVA da versare.", alias="castellettoIva")
    scadenze: Optional[List[Scadenza]] = Field(default=None, description="Scadenze.")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "data", "dataCompetenza", "numero", "tipoRegistrazione", "segnoIva", "tipoOperazione", "registroIvaId", "anagraficaId", "pagamentoId", "documentoId", "documento", "dataDocumento", "documentoNumeroParteTesto", "documentoNumeroParteNumerica", "documentoNumero", "protocollo", "descrizione", "note", "righe", "castellettoIva", "scadenze"]

    @field_validator('tipo_registrazione')
    def tipo_registrazione_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Acquisto', 'Vendita', 'Contabile']):
            raise ValueError("must be one of enum values ('Acquisto', 'Vendita', 'Contabile')")
        return value

    @field_validator('segno_iva')
    def segno_iva_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Positivo', 'Negativo']):
            raise ValueError("must be one of enum values ('Positivo', 'Negativo')")
        return value

    @field_validator('tipo_operazione')
    def tipo_operazione_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Apertura', 'Chiusura', 'Normale']):
            raise ValueError("must be one of enum values ('Apertura', 'Chiusura', 'Normale')")
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
        """Create an instance of RegistrazioneContabile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of documento
        if self.documento:
            _dict['documento'] = self.documento.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in righe (list)
        _items = []
        if self.righe:
            for _item_righe in self.righe:
                if _item_righe:
                    _items.append(_item_righe.to_dict())
            _dict['righe'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in castelletto_iva (list)
        _items = []
        if self.castelletto_iva:
            for _item_castelletto_iva in self.castelletto_iva:
                if _item_castelletto_iva:
                    _items.append(_item_castelletto_iva.to_dict())
            _dict['castellettoIva'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in scadenze (list)
        _items = []
        if self.scadenze:
            for _item_scadenze in self.scadenze:
                if _item_scadenze:
                    _items.append(_item_scadenze.to_dict())
            _dict['scadenze'] = _items
        # set to None if data_competenza (nullable) is None
        # and model_fields_set contains the field
        if self.data_competenza is None and "data_competenza" in self.model_fields_set:
            _dict['dataCompetenza'] = None

        # set to None if registro_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.registro_iva_id is None and "registro_iva_id" in self.model_fields_set:
            _dict['registroIvaId'] = None

        # set to None if anagrafica_id (nullable) is None
        # and model_fields_set contains the field
        if self.anagrafica_id is None and "anagrafica_id" in self.model_fields_set:
            _dict['anagraficaId'] = None

        # set to None if pagamento_id (nullable) is None
        # and model_fields_set contains the field
        if self.pagamento_id is None and "pagamento_id" in self.model_fields_set:
            _dict['pagamentoId'] = None

        # set to None if documento_id (nullable) is None
        # and model_fields_set contains the field
        if self.documento_id is None and "documento_id" in self.model_fields_set:
            _dict['documentoId'] = None

        # set to None if data_documento (nullable) is None
        # and model_fields_set contains the field
        if self.data_documento is None and "data_documento" in self.model_fields_set:
            _dict['dataDocumento'] = None

        # set to None if documento_numero_parte_testo (nullable) is None
        # and model_fields_set contains the field
        if self.documento_numero_parte_testo is None and "documento_numero_parte_testo" in self.model_fields_set:
            _dict['documentoNumeroParteTesto'] = None

        # set to None if documento_numero_parte_numerica (nullable) is None
        # and model_fields_set contains the field
        if self.documento_numero_parte_numerica is None and "documento_numero_parte_numerica" in self.model_fields_set:
            _dict['documentoNumeroParteNumerica'] = None

        # set to None if documento_numero (nullable) is None
        # and model_fields_set contains the field
        if self.documento_numero is None and "documento_numero" in self.model_fields_set:
            _dict['documentoNumero'] = None

        # set to None if protocollo (nullable) is None
        # and model_fields_set contains the field
        if self.protocollo is None and "protocollo" in self.model_fields_set:
            _dict['protocollo'] = None

        # set to None if descrizione (nullable) is None
        # and model_fields_set contains the field
        if self.descrizione is None and "descrizione" in self.model_fields_set:
            _dict['descrizione'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if righe (nullable) is None
        # and model_fields_set contains the field
        if self.righe is None and "righe" in self.model_fields_set:
            _dict['righe'] = None

        # set to None if castelletto_iva (nullable) is None
        # and model_fields_set contains the field
        if self.castelletto_iva is None and "castelletto_iva" in self.model_fields_set:
            _dict['castellettoIva'] = None

        # set to None if scadenze (nullable) is None
        # and model_fields_set contains the field
        if self.scadenze is None and "scadenze" in self.model_fields_set:
            _dict['scadenze'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegistrazioneContabile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "data": obj.get("data"),
            "dataCompetenza": obj.get("dataCompetenza"),
            "numero": obj.get("numero"),
            "tipoRegistrazione": obj.get("tipoRegistrazione"),
            "segnoIva": obj.get("segnoIva"),
            "tipoOperazione": obj.get("tipoOperazione"),
            "registroIvaId": obj.get("registroIvaId"),
            "anagraficaId": obj.get("anagraficaId"),
            "pagamentoId": obj.get("pagamentoId"),
            "documentoId": obj.get("documentoId"),
            "documento": Documento.from_dict(obj["documento"]) if obj.get("documento") is not None else None,
            "dataDocumento": obj.get("dataDocumento"),
            "documentoNumeroParteTesto": obj.get("documentoNumeroParteTesto"),
            "documentoNumeroParteNumerica": obj.get("documentoNumeroParteNumerica"),
            "documentoNumero": obj.get("documentoNumero"),
            "protocollo": obj.get("protocollo"),
            "descrizione": obj.get("descrizione"),
            "note": obj.get("note"),
            "righe": [RegistrazioneContabileRiga.from_dict(_item) for _item in obj["righe"]] if obj.get("righe") is not None else None,
            "castellettoIva": [CastellettoIva.from_dict(_item) for _item in obj["castellettoIva"]] if obj.get("castellettoIva") is not None else None,
            "scadenze": [Scadenza.from_dict(_item) for _item in obj["scadenze"]] if obj.get("scadenze") is not None else None
        })
        return _obj

from amica_python_sdk.models.castelletto_iva import CastellettoIva
from amica_python_sdk.models.documento import Documento
from amica_python_sdk.models.scadenza import Scadenza
# TODO: Rewrite to not use raise_errors
RegistrazioneContabile.model_rebuild(raise_errors=False)

