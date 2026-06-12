# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'**App Store di Amica**. Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  - **Authorization Code con PKCE** (consigliato per app che operano per conto di un utente Amica): l'utente autorizza la tua app tramite la pagina di consenso dell'identity provider; la tua app riceve un `code` da scambiare con un access token.    ```   GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256   POST {identity-provider}/connect/token        grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri>   ```  - **Client Credentials** (per integrazioni server-to-server, senza utente interattivo):    ```   POST {identity-provider}/connect/token   Content-Type: application/x-www-form-urlencoded    grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=read write documenti contabilita   ```    > **Nota:** il flusso Client Credentials è disponibile solo per le **app private**, non per quelle pubblicate sul marketplace.  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — il token non possiede lo scope richiesto. | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Alcune risposte `400` includono un campo `overridable` che indica se l'errore di validazione può essere ignorato impostando il parametro `validationOverride` a `true`.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from amica_python_sdk.models.anagrafica import Anagrafica
from amica_python_sdk.models.causale_magazzino import CausaleMagazzino
from amica_python_sdk.models.modalita_pagamento import ModalitaPagamento
from amica_python_sdk.models.movimento_merce_riga import MovimentoMerceRiga
from typing import Optional, Set
from typing_extensions import Self

class MovimentoMerce(BaseModel):
    """
    Movimento di magazzino.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    modalita_pagamento_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.MovimentoMerce.ModalitaPagamento.", alias="modalitaPagamentoId")
    modalita_pagamento: Optional[ModalitaPagamento] = Field(default=None, alias="modalitaPagamento")
    causale_magazzino_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.MovimentoMerce.CausaleMagazzino.", alias="causaleMagazzinoId")
    causale_magazzino: Optional[CausaleMagazzino] = Field(default=None, alias="causaleMagazzino")
    anagrafica_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.MovimentoMerce.Anagrafica.", alias="anagraficaId")
    anagrafica: Optional[Anagrafica] = None
    documento_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di Amica.Documento.", alias="documentoId")
    iva_esclusa: Optional[StrictBool] = Field(default=None, description="Indica se i prezzi inseriti sono da considerarsi al netto dell'IVA. Se `false`, l'IVA verrà scorporata in fase di elaborazione (app ufficiali).", alias="ivaEsclusa")
    data: Optional[datetime] = Field(default=None, description="Data del movimento.")
    descrizione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Descrizione.")
    documento_numero: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, description="Numero del documento di riferimento.", alias="documentoNumero")
    documento_data: Optional[datetime] = Field(default=None, description="Data del documento di riferimento.", alias="documentoData")
    note: Optional[StrictStr] = Field(default=None, description="Note.")
    righe: Optional[List[MovimentoMerceRiga]] = Field(default=None, description="Righe del movimento.")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "modalitaPagamentoId", "modalitaPagamento", "causaleMagazzinoId", "causaleMagazzino", "anagraficaId", "anagrafica", "documentoId", "ivaEsclusa", "data", "descrizione", "documentoNumero", "documentoData", "note", "righe"]

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
        """Create an instance of MovimentoMerce from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of modalita_pagamento
        if self.modalita_pagamento:
            _dict['modalitaPagamento'] = self.modalita_pagamento.to_dict()
        # override the default output from pydantic by calling `to_dict()` of causale_magazzino
        if self.causale_magazzino:
            _dict['causaleMagazzino'] = self.causale_magazzino.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anagrafica
        if self.anagrafica:
            _dict['anagrafica'] = self.anagrafica.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in righe (list)
        _items = []
        if self.righe:
            for _item_righe in self.righe:
                if _item_righe:
                    _items.append(_item_righe.to_dict())
            _dict['righe'] = _items
        # set to None if modalita_pagamento_id (nullable) is None
        # and model_fields_set contains the field
        if self.modalita_pagamento_id is None and "modalita_pagamento_id" in self.model_fields_set:
            _dict['modalitaPagamentoId'] = None

        # set to None if anagrafica_id (nullable) is None
        # and model_fields_set contains the field
        if self.anagrafica_id is None and "anagrafica_id" in self.model_fields_set:
            _dict['anagraficaId'] = None

        # set to None if documento_id (nullable) is None
        # and model_fields_set contains the field
        if self.documento_id is None and "documento_id" in self.model_fields_set:
            _dict['documentoId'] = None

        # set to None if descrizione (nullable) is None
        # and model_fields_set contains the field
        if self.descrizione is None and "descrizione" in self.model_fields_set:
            _dict['descrizione'] = None

        # set to None if documento_numero (nullable) is None
        # and model_fields_set contains the field
        if self.documento_numero is None and "documento_numero" in self.model_fields_set:
            _dict['documentoNumero'] = None

        # set to None if documento_data (nullable) is None
        # and model_fields_set contains the field
        if self.documento_data is None and "documento_data" in self.model_fields_set:
            _dict['documentoData'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if righe (nullable) is None
        # and model_fields_set contains the field
        if self.righe is None and "righe" in self.model_fields_set:
            _dict['righe'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovimentoMerce from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "modalitaPagamentoId": obj.get("modalitaPagamentoId"),
            "modalitaPagamento": ModalitaPagamento.from_dict(obj["modalitaPagamento"]) if obj.get("modalitaPagamento") is not None else None,
            "causaleMagazzinoId": obj.get("causaleMagazzinoId"),
            "causaleMagazzino": CausaleMagazzino.from_dict(obj["causaleMagazzino"]) if obj.get("causaleMagazzino") is not None else None,
            "anagraficaId": obj.get("anagraficaId"),
            "anagrafica": Anagrafica.from_dict(obj["anagrafica"]) if obj.get("anagrafica") is not None else None,
            "documentoId": obj.get("documentoId"),
            "ivaEsclusa": obj.get("ivaEsclusa"),
            "data": obj.get("data"),
            "descrizione": obj.get("descrizione"),
            "documentoNumero": obj.get("documentoNumero"),
            "documentoData": obj.get("documentoData"),
            "note": obj.get("note"),
            "righe": [MovimentoMerceRiga.from_dict(_item) for _item in obj["righe"]] if obj.get("righe") is not None else None
        })
        return _obj


