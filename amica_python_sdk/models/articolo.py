# coding: utf-8

"""
    Customers API

    La Customers API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare la Customers API registra la tua applicazione sull'**App Store di Amica**. Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  - **Authorization Code con PKCE** (consigliato per app che operano per conto di un utente Amica): l'utente autorizza la tua app tramite la pagina di consenso dell'identity provider; la tua app riceve un `code` da scambiare con un access token.    ```   GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256   POST {identity-provider}/connect/token        grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri>   ```  - **Client Credentials** (per integrazioni server-to-server, senza utente interattivo):    ```   POST {identity-provider}/connect/token   Content-Type: application/x-www-form-urlencoded    grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=read write documenti contabilita   ```    > **Nota:** il flusso Client Credentials è disponibile solo per le **app private**, non per quelle pubblicate sul marketplace.  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — il token non possiede lo scope richiesto. | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Alcune risposte `400` includono un campo `overridable` che indica se l'errore di validazione può essere ignorato impostando il parametro `validationOverride` a `true`.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from amica_python_sdk.models.articolo_media_file import ArticoloMediaFile
from amica_python_sdk.models.categoria_merceologica import CategoriaMerceologica
from amica_python_sdk.models.causale_iva import CausaleIva
from amica_python_sdk.models.gruppo_merceologico import GruppoMerceologico
from amica_python_sdk.models.marca import Marca
from amica_python_sdk.models.produttore import Produttore
from amica_python_sdk.models.reparto import Reparto
from amica_python_sdk.models.taglia import Taglia
from typing import Optional, Set
from typing_extensions import Self

class Articolo(BaseModel):
    """
    Articolo di magazzino o prodotto.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    categoria_merceologica_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della Amica.Articolo.CategoriaMerceologica (categoria merceologica).", alias="categoriaMerceologicaId")
    categoria_merceologica: Optional[CategoriaMerceologica] = Field(default=None, alias="categoriaMerceologica")
    gruppo_merceologico_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del Amica.Articolo.GruppoMerceologico (gruppo merceologico).", alias="gruppoMerceologicoId")
    gruppo_merceologico: Optional[GruppoMerceologico] = Field(default=None, alias="gruppoMerceologico")
    causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della Amica.Articolo.CausaleIva (causale IVA). Id univoco della <a href=\"#tag/CausaleIva\">causale IVA</a> predefinita per l'articolo.", alias="causaleIvaId")
    causale_iva: Optional[CausaleIva] = Field(default=None, alias="causaleIva")
    taglia_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della Amica.Articolo.Taglia (taglia).", alias="tagliaId")
    taglia: Optional[Taglia] = None
    marca_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della Amica.Articolo.Marca.", alias="marcaId")
    marca: Optional[Marca] = None
    produttore_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del Amica.Articolo.Produttore (produttore).", alias="produttoreId")
    produttore: Optional[Produttore] = None
    reparto_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del Amica.Articolo.Reparto (reparto).", alias="repartoId")
    reparto: Optional[Reparto] = None
    nome: Annotated[str, Field(min_length=0, strict=True, max_length=254)] = Field(description="Nome.")
    codice: Annotated[str, Field(min_length=0, strict=True, max_length=30)] = Field(description="Identificativo, o codice.")
    nome_breve: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=25)]] = Field(default=None, description="Nome breve.", alias="nomeBreve")
    codice_fornitore: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=30)]] = Field(default=None, description="Codice dell'articolo o prodotto presso il fornitore.", alias="codiceFornitore")
    codice_produttore: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=30)]] = Field(default=None, description="Codice dell'articolo o prodotto presso il produttore.", alias="codiceProduttore")
    gestione_articolo: Optional[StrictStr] = Field(default=None, description="Modalità di gestione.", alias="gestioneArticolo")
    contesto_articolo: Optional[StrictStr] = Field(default=None, description="Contesto in cui viene utilizzato.", alias="contestoArticolo")
    bar_code: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=128)]] = Field(default=None, description="Codice a barre.", alias="barCode")
    costo_ultimo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Ultimo prezzo di costo.", alias="costoUltimo")
    costo_medio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Prezzo di costo medio.", alias="costoMedio")
    unit_misura_intera: Optional[StrictBool] = Field(default=None, description="Indica se l'unità di misura deve essere arrotondata all'intero più vicino.", alias="unitàMisuraIntera")
    articolo_composto: Optional[StrictBool] = Field(default=None, description="Indica se è composto assemblando altri articoli.", alias="articoloComposto")
    stato: Optional[StrictBool] = Field(default=None, description="Stato. `true` se attivo, `false` altrimenti.")
    data_inserimento: Optional[datetime] = Field(default=None, description="Data di primo inserimento.", alias="dataInserimento")
    unit_misura_movimenti: Optional[StrictStr] = Field(default=None, description="Unità di misura da utilizzare nei movimenti di magazzino.", alias="unitàMisuraMovimenti")
    unit_misura_inventario: Optional[StrictStr] = Field(default=None, description="Unità di misura da utilizzare nelle elaborazioni di inventario.", alias="unitàMisuraInventario")
    fattore_conversione_unit_misura: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Fattore di conversione tra unità di movimento e unità di inventario.", alias="fattoreConversioneUnitàMisura")
    note: Optional[StrictStr] = Field(default=None, description="Note.")
    media_file: Optional[ArticoloMediaFile] = Field(default=None, alias="mediaFile")
    conto_raw_vendita: Optional[StrictStr] = Field(default=None, description="Conto da utilizzare nelle registrazioni contabili di vendita.", alias="contoRawVendita")
    conto_raw_acquisto: Optional[StrictStr] = Field(default=None, description="Conto da utilizzare nelle registrazioni contabili di acquisto.", alias="contoRawAcquisto")
    distinta_base: Optional[List[Componente]] = Field(default=None, description="Distinta base.", alias="distintaBase")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "categoriaMerceologicaId", "categoriaMerceologica", "gruppoMerceologicoId", "gruppoMerceologico", "causaleIvaId", "causaleIva", "tagliaId", "taglia", "marcaId", "marca", "produttoreId", "produttore", "repartoId", "reparto", "nome", "codice", "nomeBreve", "codiceFornitore", "codiceProduttore", "gestioneArticolo", "contestoArticolo", "barCode", "costoUltimo", "costoMedio", "unitàMisuraIntera", "articoloComposto", "stato", "dataInserimento", "unitàMisuraMovimenti", "unitàMisuraInventario", "fattoreConversioneUnitàMisura", "note", "mediaFile", "contoRawVendita", "contoRawAcquisto", "distintaBase"]

    @field_validator('gestione_articolo')
    def gestione_articolo_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Standard', 'TaglieColori', 'NumeriSeriali', 'Lotti']):
            raise ValueError("must be one of enum values ('Standard', 'TaglieColori', 'NumeriSeriali', 'Lotti')")
        return value

    @field_validator('contesto_articolo')
    def contesto_articolo_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Sempre', 'Vendite', 'Acquisti', 'Mai']):
            raise ValueError("must be one of enum values ('Sempre', 'Vendite', 'Acquisti', 'Mai')")
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
        """Create an instance of Articolo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of categoria_merceologica
        if self.categoria_merceologica:
            _dict['categoriaMerceologica'] = self.categoria_merceologica.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gruppo_merceologico
        if self.gruppo_merceologico:
            _dict['gruppoMerceologico'] = self.gruppo_merceologico.to_dict()
        # override the default output from pydantic by calling `to_dict()` of causale_iva
        if self.causale_iva:
            _dict['causaleIva'] = self.causale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taglia
        if self.taglia:
            _dict['taglia'] = self.taglia.to_dict()
        # override the default output from pydantic by calling `to_dict()` of marca
        if self.marca:
            _dict['marca'] = self.marca.to_dict()
        # override the default output from pydantic by calling `to_dict()` of produttore
        if self.produttore:
            _dict['produttore'] = self.produttore.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reparto
        if self.reparto:
            _dict['reparto'] = self.reparto.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_file
        if self.media_file:
            _dict['mediaFile'] = self.media_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in distinta_base (list)
        _items = []
        if self.distinta_base:
            for _item_distinta_base in self.distinta_base:
                if _item_distinta_base:
                    _items.append(_item_distinta_base.to_dict())
            _dict['distintaBase'] = _items
        # set to None if categoria_merceologica_id (nullable) is None
        # and model_fields_set contains the field
        if self.categoria_merceologica_id is None and "categoria_merceologica_id" in self.model_fields_set:
            _dict['categoriaMerceologicaId'] = None

        # set to None if gruppo_merceologico_id (nullable) is None
        # and model_fields_set contains the field
        if self.gruppo_merceologico_id is None and "gruppo_merceologico_id" in self.model_fields_set:
            _dict['gruppoMerceologicoId'] = None

        # set to None if causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_iva_id is None and "causale_iva_id" in self.model_fields_set:
            _dict['causaleIvaId'] = None

        # set to None if taglia_id (nullable) is None
        # and model_fields_set contains the field
        if self.taglia_id is None and "taglia_id" in self.model_fields_set:
            _dict['tagliaId'] = None

        # set to None if marca_id (nullable) is None
        # and model_fields_set contains the field
        if self.marca_id is None and "marca_id" in self.model_fields_set:
            _dict['marcaId'] = None

        # set to None if produttore_id (nullable) is None
        # and model_fields_set contains the field
        if self.produttore_id is None and "produttore_id" in self.model_fields_set:
            _dict['produttoreId'] = None

        # set to None if reparto_id (nullable) is None
        # and model_fields_set contains the field
        if self.reparto_id is None and "reparto_id" in self.model_fields_set:
            _dict['repartoId'] = None

        # set to None if nome_breve (nullable) is None
        # and model_fields_set contains the field
        if self.nome_breve is None and "nome_breve" in self.model_fields_set:
            _dict['nomeBreve'] = None

        # set to None if codice_fornitore (nullable) is None
        # and model_fields_set contains the field
        if self.codice_fornitore is None and "codice_fornitore" in self.model_fields_set:
            _dict['codiceFornitore'] = None

        # set to None if codice_produttore (nullable) is None
        # and model_fields_set contains the field
        if self.codice_produttore is None and "codice_produttore" in self.model_fields_set:
            _dict['codiceProduttore'] = None

        # set to None if bar_code (nullable) is None
        # and model_fields_set contains the field
        if self.bar_code is None and "bar_code" in self.model_fields_set:
            _dict['barCode'] = None

        # set to None if data_inserimento (nullable) is None
        # and model_fields_set contains the field
        if self.data_inserimento is None and "data_inserimento" in self.model_fields_set:
            _dict['dataInserimento'] = None

        # set to None if unit_misura_movimenti (nullable) is None
        # and model_fields_set contains the field
        if self.unit_misura_movimenti is None and "unit_misura_movimenti" in self.model_fields_set:
            _dict['unitàMisuraMovimenti'] = None

        # set to None if unit_misura_inventario (nullable) is None
        # and model_fields_set contains the field
        if self.unit_misura_inventario is None and "unit_misura_inventario" in self.model_fields_set:
            _dict['unitàMisuraInventario'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if conto_raw_vendita (nullable) is None
        # and model_fields_set contains the field
        if self.conto_raw_vendita is None and "conto_raw_vendita" in self.model_fields_set:
            _dict['contoRawVendita'] = None

        # set to None if conto_raw_acquisto (nullable) is None
        # and model_fields_set contains the field
        if self.conto_raw_acquisto is None and "conto_raw_acquisto" in self.model_fields_set:
            _dict['contoRawAcquisto'] = None

        # set to None if distinta_base (nullable) is None
        # and model_fields_set contains the field
        if self.distinta_base is None and "distinta_base" in self.model_fields_set:
            _dict['distintaBase'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Articolo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "categoriaMerceologicaId": obj.get("categoriaMerceologicaId"),
            "categoriaMerceologica": CategoriaMerceologica.from_dict(obj["categoriaMerceologica"]) if obj.get("categoriaMerceologica") is not None else None,
            "gruppoMerceologicoId": obj.get("gruppoMerceologicoId"),
            "gruppoMerceologico": GruppoMerceologico.from_dict(obj["gruppoMerceologico"]) if obj.get("gruppoMerceologico") is not None else None,
            "causaleIvaId": obj.get("causaleIvaId"),
            "causaleIva": CausaleIva.from_dict(obj["causaleIva"]) if obj.get("causaleIva") is not None else None,
            "tagliaId": obj.get("tagliaId"),
            "taglia": Taglia.from_dict(obj["taglia"]) if obj.get("taglia") is not None else None,
            "marcaId": obj.get("marcaId"),
            "marca": Marca.from_dict(obj["marca"]) if obj.get("marca") is not None else None,
            "produttoreId": obj.get("produttoreId"),
            "produttore": Produttore.from_dict(obj["produttore"]) if obj.get("produttore") is not None else None,
            "repartoId": obj.get("repartoId"),
            "reparto": Reparto.from_dict(obj["reparto"]) if obj.get("reparto") is not None else None,
            "nome": obj.get("nome"),
            "codice": obj.get("codice"),
            "nomeBreve": obj.get("nomeBreve"),
            "codiceFornitore": obj.get("codiceFornitore"),
            "codiceProduttore": obj.get("codiceProduttore"),
            "gestioneArticolo": obj.get("gestioneArticolo"),
            "contestoArticolo": obj.get("contestoArticolo"),
            "barCode": obj.get("barCode"),
            "costoUltimo": obj.get("costoUltimo"),
            "costoMedio": obj.get("costoMedio"),
            "unitàMisuraIntera": obj.get("unitàMisuraIntera"),
            "articoloComposto": obj.get("articoloComposto"),
            "stato": obj.get("stato"),
            "dataInserimento": obj.get("dataInserimento"),
            "unitàMisuraMovimenti": obj.get("unitàMisuraMovimenti"),
            "unitàMisuraInventario": obj.get("unitàMisuraInventario"),
            "fattoreConversioneUnitàMisura": obj.get("fattoreConversioneUnitàMisura"),
            "note": obj.get("note"),
            "mediaFile": ArticoloMediaFile.from_dict(obj["mediaFile"]) if obj.get("mediaFile") is not None else None,
            "contoRawVendita": obj.get("contoRawVendita"),
            "contoRawAcquisto": obj.get("contoRawAcquisto"),
            "distintaBase": [Componente.from_dict(_item) for _item in obj["distintaBase"]] if obj.get("distintaBase") is not None else None
        })
        return _obj

from amica_python_sdk.models.componente import Componente
# TODO: Rewrite to not use raise_errors
Articolo.model_rebuild(raise_errors=False)

