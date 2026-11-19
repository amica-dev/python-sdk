# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — accesso negato (vedi sotto le possibili cause). | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Un `403` può avere tre cause; nelle ultime due il campo `code` della risposta indica quale:  - il token non possiede lo scope richiesto dall'endpoint; - `code: cloud_not_active` — l'account lavora con una connessione locale e la Cloud API non espone i suoi dati. Per attivare il servizio cloud contatta l'assistenza, poi richiedi un nuovo token: lo stato del servizio è letto al rilascio del token; - `code: company_license_not_active` — la licenza dell'azienda indicata nel percorso è scaduta o non è attiva. Le altre aziende con licenza attiva restano accessibili.  Il motivo dell'errore è sempre nel campo `detail`. Ogni risposta di errore riporta inoltre `overridable`: quando vale `true`, l'errore di validazione è *forzabile* e basta ripetere la stessa richiesta aggiungendo `validationOverride=true` alla query string perché il servizio la accetti. È il caso delle anomalie formali su dati reali — la partita IVA di un fornitore estero, per esempio — che il cliente ha comunque bisogno di registrare.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: 3.3.6
    Contact: assistenza@gestionaleamica.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from amica_python_sdk.models.articolo import Articolo
from amica_python_sdk.models.causale_iva import CausaleIva
from amica_python_sdk.models.dati_aggiuntivi import DatiAggiuntivi
from amica_python_sdk.models.listino import Listino
from amica_python_sdk.models.magazzino import Magazzino
from amica_python_sdk.models.prestazione import Prestazione
from amica_python_sdk.models.taglia import Taglia
from typing import Optional, Set
from typing_extensions import Self

class BeneServizio(BaseModel):
    """
    Bene o servizio fatturato.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    documento_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del `Documento` (documento).", alias="documentoId")
    documento: Optional[Documento] = None
    articolo_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco dell'`Articolo` (articolo o prodotto).", alias="articoloId")
    articolo: Optional[Articolo] = None
    prestazione_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della `Prestazione` (prestazione).", alias="prestazioneId")
    prestazione: Optional[Prestazione] = None
    magazzino_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del `Magazzino` (magazzino). Obbligatorio quando viene usato `Codice`.", alias="magazzinoId")
    magazzino: Optional[Magazzino] = None
    causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della `CausaleIva`.", alias="causaleIvaId")
    causale_iva: Optional[CausaleIva] = Field(default=None, alias="causaleIva")
    listino_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del `Listino` (listino).", alias="listinoId")
    listino: Optional[Listino] = None
    ordine_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del `Documento` (ordine).", alias="ordineId")
    bene_servizio_ordine_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del `BeneServizio` (bene o servizio) all'interno dell'ordine referenziato da `OrdineId`.", alias="beneServizioOrdineId")
    taglia_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della `Taglia` (taglia).", alias="tagliaId")
    taglia: Optional[Taglia] = None
    ritenuta_fiscale: Optional[StrictBool] = Field(default=None, description="Indica se al bene o servizio deve essere applicata una ritenuta fiscale. `true` se deve essere applicata, `false` altrimenti.", alias="ritenutaFiscale")
    posizione: Optional[StrictInt] = Field(default=None, description="Indice di riga all'interno del documento. Questa proprietà è utilizzata solo dal client desktop Amica 20 per Windows e deve essere considerata obsoleta.")
    codice: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=30)]] = Field(default=None, description="Codice del bene o servizio.")
    descrizione: Optional[StrictStr] = Field(default=None, description="Descrizione. Obbligatoria, tranne che sulle righe di totale per aliquota create dall'importazione dei DDT con `Totali`: hanno `CausaleIvaId` e `Importo` ma niente `ArticoloId` né descrizione, e la fattura elettronica usa come loro descrizione il riferimento al DDT che le precede.")
    unit_misura: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=15)]] = Field(default=None, description="Unità di misura.", alias="unitàMisura")
    quantit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità movimentata.", alias="quantità")
    quantit_evasa: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità dell'ordine evasa. Questo valore viene aggiornato automaticamente quando viene emessa una fattura o un DDT che contiene un riferimento a un ordine ed è attivo <a href=\"https://gestionaleamica.com/Software/GestioneOrdiniPreventivi\">Ordini e Preventivi</a>.", alias="quantitàEvasa")
    quantit_da_evadere: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quantità che resta da evadere.", alias="quantitàDaEvadere")
    sconto1: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Primo sconto percentuale, applicato al prezzo del bene o servizio. Il valore è una frazione: `0.05` corrisponde al 5%.")
    sconto2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Secondo sconto percentuale, applicato dopo l'applicazione di `Sconto1` Il valore è una frazione: `0.03` corrisponde al 3%.")
    sconto3: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Terzo sconto percentuale, applicato dopo l'applicazione di `Sconto2` Il valore è una frazione: `0.02` corrisponde al 2%.")
    sconto4: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quarto sconto percentuale, applicato dopo l'applicazione di `Sconto3` Il valore è una frazione: `0.01` corrisponde all'1%.")
    sconto_incondizionato: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sconto incondizionato, in valuta, applicato al prezzo del bene o servizio.", alias="scontoIncondizionato")
    provvigione_agente: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Provvigione corrisposta all'agente, in percentuale.", alias="provvigioneAgente")
    provvigione_capo_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Provvigione corrisposta al capo area, in percentuale.", alias="provvigioneCapoArea")
    prezzo_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco del `Prezzo` (prezzo).", alias="prezzoId")
    prezzo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Prezzo.")
    prezzo_scontato: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Prezzo scontato, cioè al netto degli sconti percentuali indicati e dello sconto incondizionato.", alias="prezzoScontato")
    prezzo_ivato: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Prezzo comprensivo di IVA.", alias="prezzoIvato")
    importo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo, determinato come prodotto di `Quantità` e `PrezzoScontato`.")
    importo_ivato: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo IVA inclusa, calcolato dalla API in lettura come `beneservizio/compute` a partire dai prezzi salvati e dal flag `IvaEsclusa` del documento. Non viene memorizzato: in `POST` e `PUT` è ignorato. Con IVA inclusa è la base dell'imposta del riepilogo, da passare nella riga di `documento/compute` (`ImportoIvato`). Assente sulle righe senza prezzo.", alias="importoIvato")
    dati_aggiuntivi: Optional[DatiAggiuntivi] = Field(default=None, alias="datiAggiuntivi")
    sconto: Optional[StrictStr] = Field(default=None, description="Descrizione di tutti gli sconti combinati (es: \"10,5%+5€\").")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "documentoId", "documento", "articoloId", "articolo", "prestazioneId", "prestazione", "magazzinoId", "magazzino", "causaleIvaId", "causaleIva", "listinoId", "listino", "ordineId", "beneServizioOrdineId", "tagliaId", "taglia", "ritenutaFiscale", "posizione", "codice", "descrizione", "unitàMisura", "quantità", "quantitàEvasa", "quantitàDaEvadere", "sconto1", "sconto2", "sconto3", "sconto4", "scontoIncondizionato", "provvigioneAgente", "provvigioneCapoArea", "prezzoId", "prezzo", "prezzoScontato", "prezzoIvato", "importo", "importoIvato", "datiAggiuntivi", "sconto"]

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
        """Create an instance of BeneServizio from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "quantit_da_evadere",
            "sconto",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of documento
        if self.documento:
            _dict['documento'] = self.documento.to_dict()
        # override the default output from pydantic by calling `to_dict()` of articolo
        if self.articolo:
            _dict['articolo'] = self.articolo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prestazione
        if self.prestazione:
            _dict['prestazione'] = self.prestazione.to_dict()
        # override the default output from pydantic by calling `to_dict()` of magazzino
        if self.magazzino:
            _dict['magazzino'] = self.magazzino.to_dict()
        # override the default output from pydantic by calling `to_dict()` of causale_iva
        if self.causale_iva:
            _dict['causaleIva'] = self.causale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of listino
        if self.listino:
            _dict['listino'] = self.listino.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taglia
        if self.taglia:
            _dict['taglia'] = self.taglia.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dati_aggiuntivi
        if self.dati_aggiuntivi:
            _dict['datiAggiuntivi'] = self.dati_aggiuntivi.to_dict()
        # set to None if articolo_id (nullable) is None
        # and model_fields_set contains the field
        if self.articolo_id is None and "articolo_id" in self.model_fields_set:
            _dict['articoloId'] = None

        # set to None if prestazione_id (nullable) is None
        # and model_fields_set contains the field
        if self.prestazione_id is None and "prestazione_id" in self.model_fields_set:
            _dict['prestazioneId'] = None

        # set to None if magazzino_id (nullable) is None
        # and model_fields_set contains the field
        if self.magazzino_id is None and "magazzino_id" in self.model_fields_set:
            _dict['magazzinoId'] = None

        # set to None if causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_iva_id is None and "causale_iva_id" in self.model_fields_set:
            _dict['causaleIvaId'] = None

        # set to None if listino_id (nullable) is None
        # and model_fields_set contains the field
        if self.listino_id is None and "listino_id" in self.model_fields_set:
            _dict['listinoId'] = None

        # set to None if ordine_id (nullable) is None
        # and model_fields_set contains the field
        if self.ordine_id is None and "ordine_id" in self.model_fields_set:
            _dict['ordineId'] = None

        # set to None if bene_servizio_ordine_id (nullable) is None
        # and model_fields_set contains the field
        if self.bene_servizio_ordine_id is None and "bene_servizio_ordine_id" in self.model_fields_set:
            _dict['beneServizioOrdineId'] = None

        # set to None if taglia_id (nullable) is None
        # and model_fields_set contains the field
        if self.taglia_id is None and "taglia_id" in self.model_fields_set:
            _dict['tagliaId'] = None

        # set to None if codice (nullable) is None
        # and model_fields_set contains the field
        if self.codice is None and "codice" in self.model_fields_set:
            _dict['codice'] = None

        # set to None if descrizione (nullable) is None
        # and model_fields_set contains the field
        if self.descrizione is None and "descrizione" in self.model_fields_set:
            _dict['descrizione'] = None

        # set to None if unit_misura (nullable) is None
        # and model_fields_set contains the field
        if self.unit_misura is None and "unit_misura" in self.model_fields_set:
            _dict['unitàMisura'] = None

        # set to None if quantit (nullable) is None
        # and model_fields_set contains the field
        if self.quantit is None and "quantit" in self.model_fields_set:
            _dict['quantità'] = None

        # set to None if sconto1 (nullable) is None
        # and model_fields_set contains the field
        if self.sconto1 is None and "sconto1" in self.model_fields_set:
            _dict['sconto1'] = None

        # set to None if sconto2 (nullable) is None
        # and model_fields_set contains the field
        if self.sconto2 is None and "sconto2" in self.model_fields_set:
            _dict['sconto2'] = None

        # set to None if sconto3 (nullable) is None
        # and model_fields_set contains the field
        if self.sconto3 is None and "sconto3" in self.model_fields_set:
            _dict['sconto3'] = None

        # set to None if sconto4 (nullable) is None
        # and model_fields_set contains the field
        if self.sconto4 is None and "sconto4" in self.model_fields_set:
            _dict['sconto4'] = None

        # set to None if sconto_incondizionato (nullable) is None
        # and model_fields_set contains the field
        if self.sconto_incondizionato is None and "sconto_incondizionato" in self.model_fields_set:
            _dict['scontoIncondizionato'] = None

        # set to None if provvigione_agente (nullable) is None
        # and model_fields_set contains the field
        if self.provvigione_agente is None and "provvigione_agente" in self.model_fields_set:
            _dict['provvigioneAgente'] = None

        # set to None if provvigione_capo_area (nullable) is None
        # and model_fields_set contains the field
        if self.provvigione_capo_area is None and "provvigione_capo_area" in self.model_fields_set:
            _dict['provvigioneCapoArea'] = None

        # set to None if prezzo_id (nullable) is None
        # and model_fields_set contains the field
        if self.prezzo_id is None and "prezzo_id" in self.model_fields_set:
            _dict['prezzoId'] = None

        # set to None if prezzo (nullable) is None
        # and model_fields_set contains the field
        if self.prezzo is None and "prezzo" in self.model_fields_set:
            _dict['prezzo'] = None

        # set to None if prezzo_scontato (nullable) is None
        # and model_fields_set contains the field
        if self.prezzo_scontato is None and "prezzo_scontato" in self.model_fields_set:
            _dict['prezzoScontato'] = None

        # set to None if prezzo_ivato (nullable) is None
        # and model_fields_set contains the field
        if self.prezzo_ivato is None and "prezzo_ivato" in self.model_fields_set:
            _dict['prezzoIvato'] = None

        # set to None if importo (nullable) is None
        # and model_fields_set contains the field
        if self.importo is None and "importo" in self.model_fields_set:
            _dict['importo'] = None

        # set to None if importo_ivato (nullable) is None
        # and model_fields_set contains the field
        if self.importo_ivato is None and "importo_ivato" in self.model_fields_set:
            _dict['importoIvato'] = None

        # set to None if sconto (nullable) is None
        # and model_fields_set contains the field
        if self.sconto is None and "sconto" in self.model_fields_set:
            _dict['sconto'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BeneServizio from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "documentoId": obj.get("documentoId"),
            "documento": Documento.from_dict(obj["documento"]) if obj.get("documento") is not None else None,
            "articoloId": obj.get("articoloId"),
            "articolo": Articolo.from_dict(obj["articolo"]) if obj.get("articolo") is not None else None,
            "prestazioneId": obj.get("prestazioneId"),
            "prestazione": Prestazione.from_dict(obj["prestazione"]) if obj.get("prestazione") is not None else None,
            "magazzinoId": obj.get("magazzinoId"),
            "magazzino": Magazzino.from_dict(obj["magazzino"]) if obj.get("magazzino") is not None else None,
            "causaleIvaId": obj.get("causaleIvaId"),
            "causaleIva": CausaleIva.from_dict(obj["causaleIva"]) if obj.get("causaleIva") is not None else None,
            "listinoId": obj.get("listinoId"),
            "listino": Listino.from_dict(obj["listino"]) if obj.get("listino") is not None else None,
            "ordineId": obj.get("ordineId"),
            "beneServizioOrdineId": obj.get("beneServizioOrdineId"),
            "tagliaId": obj.get("tagliaId"),
            "taglia": Taglia.from_dict(obj["taglia"]) if obj.get("taglia") is not None else None,
            "ritenutaFiscale": obj.get("ritenutaFiscale"),
            "posizione": obj.get("posizione"),
            "codice": obj.get("codice"),
            "descrizione": obj.get("descrizione"),
            "unitàMisura": obj.get("unitàMisura"),
            "quantità": obj.get("quantità"),
            "quantitàEvasa": obj.get("quantitàEvasa"),
            "quantitàDaEvadere": obj.get("quantitàDaEvadere"),
            "sconto1": obj.get("sconto1"),
            "sconto2": obj.get("sconto2"),
            "sconto3": obj.get("sconto3"),
            "sconto4": obj.get("sconto4"),
            "scontoIncondizionato": obj.get("scontoIncondizionato"),
            "provvigioneAgente": obj.get("provvigioneAgente"),
            "provvigioneCapoArea": obj.get("provvigioneCapoArea"),
            "prezzoId": obj.get("prezzoId"),
            "prezzo": obj.get("prezzo"),
            "prezzoScontato": obj.get("prezzoScontato"),
            "prezzoIvato": obj.get("prezzoIvato"),
            "importo": obj.get("importo"),
            "importoIvato": obj.get("importoIvato"),
            "datiAggiuntivi": DatiAggiuntivi.from_dict(obj["datiAggiuntivi"]) if obj.get("datiAggiuntivi") is not None else None,
            "sconto": obj.get("sconto")
        })
        return _obj

from amica_python_sdk.models.documento import Documento
# TODO: Rewrite to not use raise_errors
BeneServizio.model_rebuild(raise_errors=False)

