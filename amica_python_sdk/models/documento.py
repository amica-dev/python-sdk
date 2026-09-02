# coding: utf-8

"""
    Amica Cloud API

    L'Amica Cloud API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).  ## Autenticazione  Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:  ``` Authorization: Bearer <token> ```  ### Registra la tua app  Per integrare l'Amica Cloud API registra la tua applicazione sull'[**App Store di Amica**](https://apps.amica20.it). Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.  ### Scegli il flusso  La scelta dipende da **come** la tua applicazione si autentica:  - C'è un **utente** che può accedere via browser (web app, SPA, app mobile)? → **Authorization Code con PKCE**. - È un **servizio headless** (backend, batch, integrazione server-to-server) di una **singola azienda**, senza un utente che effettua il login? → **Client Credentials**.  #### Authorization Code con PKCE  Consigliato per le app che operano per conto di un utente Amica ed è l'**unico flusso disponibile per le app pubblicate sul marketplace**. Una sola registrazione serve un numero qualsiasi di aziende: ogni utente autorizza la tua app per la propria azienda tramite la pagina di consenso dell'identity provider, e il token riceve automaticamente il contesto di quell'azienda. La tua app riceve un `code` da scambiare con un access token.  ``` GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256 POST {identity-provider}/connect/token      grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri> ```  #### Client Credentials  Per integrazioni **server-to-server** senza utente interattivo. Disponibile solo per le **app private**, non per quelle pubblicate sul marketplace. Un'app Client Credentials è **legata a una singola azienda** — quella dell'utente che la registra — e il token ne riceve automaticamente il contesto. Per servire un'azienda diversa serve una registrazione separata; se devi distribuire la stessa app a più aziende usa invece **Authorization Code**.  ``` POST {identity-provider}/connect/token Content-Type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=comune read write documenti ```  > **Importante:** non includere lo scope `openid` (né `profile`/`email`) in questo flusso. `openid` attiva OpenID Connect — richiede un utente che effettua il login e l'emissione di un ID token — cosa che un flusso server-to-server non prevede: la richiesta viene rifiutata con l'errore `Client cannot request OpenID scopes in client credentials flow`. Indica solo gli scope di risorsa (`comune`, `magazzino`, `documenti`, `contabilita`, ed eventualmente `read`/`write`).  In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.  ## Scope di autorizzazione  L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:  | Scope | Descrizione | |-|-| | `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. | | `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. | | `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. | | `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |  Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.  ## Company ID  La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:  ``` /api/v3/{companyId}/risorsa ```  Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.  ## Paginazione  Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:  | Parametro | Descrizione | |-|-| | `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. | | `Take` | Numero di elementi da includere nella risposta. |  La risposta include due header:  | Header | Descrizione | |-|-| | `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. | | `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |  ## Ordinamento e filtri  Gli endpoint lista accettano parametri aggiuntivi:  | Parametro | Descrizione | |-|-| | `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. | | `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. | | `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |  ## Espansione oggetti correlati  Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.  ## Gestione errori  L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:  | Codice | Significato | |-|-| | `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. | | `401` | Unauthorized — token mancante o scaduto. | | `403` | Forbidden — il token non possiede lo scope richiesto. | | `404` | Not Found — la risorsa richiesta non esiste. | | `409` | Conflict — conflitto di concorrenza. | | `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |  Il motivo dell'errore è sempre nel campo `detail`. Ogni risposta di errore riporta inoltre `overridable`: quando vale `true`, l'errore di validazione è *forzabile* e basta ripetere la stessa richiesta aggiungendo `validationOverride=true` alla query string perché il servizio la accetti. È il caso delle anomalie formali su dati reali — la partita IVA di un fornitore estero, per esempio — che il cliente ha comunque bisogno di registrare.  ## Controllo della concorrenza  Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`. 

    The version of the OpenAPI document: 3.0.1
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
from amica_python_sdk.models.anagrafica import Anagrafica
from amica_python_sdk.models.banca_documento import BancaDocumento
from amica_python_sdk.models.causale_documento import CausaleDocumento
from amica_python_sdk.models.causale_iva import CausaleIva
from amica_python_sdk.models.causale_magazzino import CausaleMagazzino
from amica_python_sdk.models.dati_pa import DatiPA
from amica_python_sdk.models.dati_sdi import DatiSdi
from amica_python_sdk.models.dati_trasporto import DatiTrasporto
from amica_python_sdk.models.documento_media_file import DocumentoMediaFile
from amica_python_sdk.models.indirizzo import Indirizzo
from amica_python_sdk.models.pagamento import Pagamento
from amica_python_sdk.models.progressivo_invio import ProgressivoInvio
from amica_python_sdk.models.spesa_documento import SpesaDocumento
from amica_python_sdk.models.valuta import Valuta
from typing import Optional, Set
from typing_extensions import Self

class Documento(BaseModel):
    """
    Un documento (fattura, documento di trasporto, ecc.)
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco.")
    concurrency_token: Optional[StrictInt] = Field(default=None, description="Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull'entità. Se i valori coincidono, l'operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l'aggiornamento viene rifiutato.", alias="concurrencyToken")
    anagrafica_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Anagrafica`.", alias="anagraficaId")
    anagrafica: Optional[Anagrafica] = None
    causale_documento_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `CausaleDocumento`.", alias="causaleDocumentoId")
    causale_documento: Optional[CausaleDocumento] = Field(default=None, alias="causaleDocumento")
    agente_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Anagrafica` dell'agente.", alias="agenteId")
    agente: Optional[Anagrafica] = None
    pagamento_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Pagamento`.", alias="pagamentoId")
    pagamento: Optional[Pagamento] = None
    vettore_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Anagrafica` del vettore.", alias="vettoreId")
    vettore: Optional[Anagrafica] = None
    cassa_previdenziale_causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della causale IVA della cassa previdenziale.", alias="cassaPrevidenzialeCausaleIvaId")
    modello_id: Optional[StrictInt] = Field(default=None, description="Obsoleto. Non utilizzare.", alias="modelloId")
    cassa_previdenziale_causale_iva: Optional[CausaleIva] = Field(default=None, alias="cassaPrevidenzialeCausaleIva")
    destinazione_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Indirizzo` di destinazione.", alias="destinazioneId")
    destinazione: Optional[Indirizzo] = None
    valuta_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `Valuta`.", alias="valutaId")
    valuta: Optional[Valuta] = None
    causale_magazzino_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco di `CausaleMagazzino`.", alias="causaleMagazzinoId")
    causale_magazzino: Optional[CausaleMagazzino] = Field(default=None, alias="causaleMagazzino")
    iva1_causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della prima causale IVA.", alias="iva1CausaleIvaId")
    iva1_causale_iva: Optional[CausaleIva] = Field(default=None, alias="iva1CausaleIva")
    iva2_causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della seconda causale IVA.", alias="iva2CausaleIvaId")
    iva2_causale_iva: Optional[CausaleIva] = Field(default=None, alias="iva2CausaleIva")
    iva3_causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della terza causale IVA.", alias="iva3CausaleIvaId")
    iva3_causale_iva: Optional[CausaleIva] = Field(default=None, alias="iva3CausaleIva")
    iva4_causale_iva_id: Optional[StrictInt] = Field(default=None, description="Identificativo univoco della quarta causale IVA.", alias="iva4CausaleIvaId")
    iva4_causale_iva: Optional[CausaleIva] = Field(default=None, alias="iva4CausaleIva")
    tipo_documento: Optional[StrictStr] = Field(default=None, description="Tipologia del documento.", alias="tipoDocumento")
    documento_fiscale: Optional[StrictStr] = Field(default=None, description="Tipo di documento fiscale.", alias="documentoFiscale")
    destinazione_diversa: Optional[StrictBool] = Field(default=None, description="Indica se la destinazione della merce è diversa dall'indirizzo principale.", alias="destinazioneDiversa")
    iva_esclusa: Optional[StrictBool] = Field(default=None, description="Indica se i prezzi inseriti sono da considerarsi al netto dell'IVA. Se `false`, l'IVA verrà scorporata in fase di elaborazione (app ufficiali).", alias="ivaEsclusa")
    ritenuta_include_cassa_previdenziale: Optional[StrictBool] = Field(default=None, description="Indica se la ritenuta deve essere applicata anche all'importo della cassa previdenziale riportato nel documento.", alias="ritenutaIncludeCassaPrevidenziale")
    classe_documento: Optional[StrictStr] = Field(default=None, description="Classe del documento.", alias="classeDocumento")
    contatto: Optional[StrictInt] = Field(default=None, description="Persona di contatto preferita, `AnagraficaNominativo1` oppure `AnagraficaNominativo2`.")
    numero_parte_testo: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=40)]] = Field(default=None, description="La parte alfanumerica del numero del documento, se presente. Ad esempio, \"bis\" per il documento num. 99/bis.", alias="numeroParteTesto")
    numero_parte_numerica: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(default=None, description="Il numero del documento, nella sua parte numerica. Ad esempio, 99 per il num. 99/bis.", alias="numeroParteNumerica")
    data: Optional[datetime] = Field(default=None, description="Data del documento.")
    stato: Optional[StrictStr] = Field(default=None, description="Lo stato corrente del documento. Ad esempio: Bozza, oppure Emesso.")
    data_scadenza_preventivo: Optional[datetime] = Field(default=None, description="La data di scadenza, nel caso in cui il documento sia un preventivo.", alias="dataScadenzaPreventivo")
    data_inizio_scadenze: Optional[datetime] = Field(default=None, description="Data della prima scadenza di pagamento.", alias="dataInizioScadenze")
    sconto_percentuale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sconto, in percentuale, da calcolare sull'intero importo del documento.", alias="scontoPercentuale")
    sconto_incondizionato_importo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sconto, in valuta, da applicare all'intero importo del documento.", alias="scontoIncondizionatoImporto")
    abbuono_importo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo dell'abbuono.", alias="abbuonoImporto")
    ritenuta_percentuale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quota della ritenuta da applicare al documento.", alias="ritenutaPercentuale")
    enasarco_percentuale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Contributo Enasarco da applicare al documento.", alias="enasarcoPercentuale")
    enasarco_importo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo Enasarco.", alias="enasarcoImporto")
    quota_ritenuta_su_imponibile: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Quota dell'imponibile su cui applicare la ritenuta.", alias="quotaRitenutaSuImponibile")
    cambio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Tasso di cambio rispetto all'Euro, nel caso in cui la `Valuta` del documento non sia l'Euro.")
    cassa_previdenziale_nome: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=50)]] = Field(default=None, description="Nome della cassa previdenziale applicata al documento.", alias="cassaPrevidenzialeNome")
    cassa_previdenziale_percentuale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Aliquota (percentuale) della cassa previdenziale da applicare al documento.", alias="cassaPrevidenzialePercentuale")
    note: Optional[StrictStr] = Field(default=None, description="Note.")
    sconto_pagamento_percentuale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sconto riconosciuto in base alla modalità di pagamento utilizzata (es: +5% in caso di rimessa diretta).", alias="scontoPagamentoPercentuale")
    iva1_imponibile: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva1CausaleIva`", alias="iva1Imponibile")
    iva2_imponibile: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva2CausaleIva`", alias="iva2Imponibile")
    iva3_imponibile: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva3CausaleIva`", alias="iva3Imponibile")
    iva4_imponibile: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva4CausaleIva`", alias="iva4Imponibile")
    iva1_imponibile_lordo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva1CausaleIva` al lordo di eventuali sconti di fattura.", alias="iva1ImponibileLordo")
    iva2_imponibile_lordo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva2CausaleIva` al lordo di eventuali sconti di fattura.", alias="iva2ImponibileLordo")
    iva3_imponibile_lordo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva3CausaleIva` al lordo di eventuali sconti di fattura.", alias="iva3ImponibileLordo")
    iva4_imponibile_lordo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile attribuibile a `Iva4CausaleIva` al lordo di eventuali sconti di fattura.", alias="iva4ImponibileLordo")
    iva1_imposta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imposta per `Iva1CausaleIva`", alias="iva1Imposta")
    iva2_imposta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imposta per `Iva2CausaleIva`", alias="iva2Imposta")
    iva3_imposta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imposta per `Iva3CausaleIva`", alias="iva3Imposta")
    iva4_imposta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imposta per `Iva4CausaleIva`", alias="iva4Imposta")
    totale_ritenuta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo della ritenuta.", alias="totaleRitenuta")
    totale_cassa_previdenziale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo della cassa previdenziale.", alias="totaleCassaPrevidenziale")
    totale_spese: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale delle spese esenti e non esenti.", alias="totaleSpese")
    totale_spese_esenti: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale delle spese esenti da IVA.", alias="totaleSpeseEsenti")
    totale_spese_non_esenti: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale delle spese non esenti da IVA.", alias="totaleSpeseNonEsenti")
    totale_merce: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo della merce.", alias="totaleMerce")
    totale_merce_scontata: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo della merce scontata.", alias="totaleMerceScontata")
    totale_imponibile: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Totale imponibile, considerando tutte le causali IVA coinvolte.", alias="totaleImponibile")
    totale_imposta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Imposta IVA.", alias="totaleImposta")
    totale_esente: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importi esenti da IVA.", alias="totaleEsente")
    totale_documento: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo totale del documento.", alias="totaleDocumento")
    netto_a_pagare: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Netto a pagare.", alias="nettoAPagare")
    totale_split_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo dello split payment.", alias="totaleSplitPayment")
    bollo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo del bollo.")
    xml_file_name: Optional[StrictStr] = Field(default=None, description="Nome del file XML.", alias="xmlFileName")
    riferimento_amministrazione: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, description="Numero di riferimento dell'amministrazione.", alias="riferimentoAmministrazione")
    banca: Optional[BancaDocumento] = None
    dati_trasporto: Optional[DatiTrasporto] = Field(default=None, alias="datiTrasporto")
    dati_sdi: Optional[DatiSdi] = Field(default=None, alias="datiSdi")
    dati_pa: Optional[DatiPA] = Field(default=None, alias="datiPA")
    righe: Optional[List[BeneServizio]] = Field(default=None, description="Righe del documento.")
    spese_documento: Optional[List[SpesaDocumento]] = Field(default=None, description="Elenco delle spese.", alias="speseDocumento")
    scadenze: Optional[List[Scadenza]] = Field(default=None, description="Elenco delle scadenze.")
    numero: Optional[StrictStr] = Field(default=None, description="Numero completo del documento. Ad esempio, `99/bis`. Generato a partire da `NumeroParteNumerica` e `NumeroParteTesto`. Nota bene: proprietà valorizzata solo nel caso di un'istanza salvata sul backend.")
    media_file: Optional[DocumentoMediaFile] = Field(default=None, alias="mediaFile")
    allegato: Optional[StrictStr] = Field(default=None, description="Obsoleto. Non utilizzare.")
    bonus_fiscale_causale: Optional[StrictStr] = Field(default=None, description="Causale del bonus fiscale.", alias="bonusFiscaleCausale")
    bonus_fiscale_importo: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Importo del bonus fiscale.", alias="bonusFiscaleImporto")
    bonus_fiscale_percentuale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Percentuale del bonus fiscale.", alias="bonusFiscalePercentuale")
    progressivo_invio: Optional[List[ProgressivoInvio]] = Field(default=None, description="Numeri di invio (progressivi), così come restituiti dallo Sdi.", alias="progressivoInvio")
    __properties: ClassVar[List[str]] = ["id", "concurrencyToken", "anagraficaId", "anagrafica", "causaleDocumentoId", "causaleDocumento", "agenteId", "agente", "pagamentoId", "pagamento", "vettoreId", "vettore", "cassaPrevidenzialeCausaleIvaId", "modelloId", "cassaPrevidenzialeCausaleIva", "destinazioneId", "destinazione", "valutaId", "valuta", "causaleMagazzinoId", "causaleMagazzino", "iva1CausaleIvaId", "iva1CausaleIva", "iva2CausaleIvaId", "iva2CausaleIva", "iva3CausaleIvaId", "iva3CausaleIva", "iva4CausaleIvaId", "iva4CausaleIva", "tipoDocumento", "documentoFiscale", "destinazioneDiversa", "ivaEsclusa", "ritenutaIncludeCassaPrevidenziale", "classeDocumento", "contatto", "numeroParteTesto", "numeroParteNumerica", "data", "stato", "dataScadenzaPreventivo", "dataInizioScadenze", "scontoPercentuale", "scontoIncondizionatoImporto", "abbuonoImporto", "ritenutaPercentuale", "enasarcoPercentuale", "enasarcoImporto", "quotaRitenutaSuImponibile", "cambio", "cassaPrevidenzialeNome", "cassaPrevidenzialePercentuale", "note", "scontoPagamentoPercentuale", "iva1Imponibile", "iva2Imponibile", "iva3Imponibile", "iva4Imponibile", "iva1ImponibileLordo", "iva2ImponibileLordo", "iva3ImponibileLordo", "iva4ImponibileLordo", "iva1Imposta", "iva2Imposta", "iva3Imposta", "iva4Imposta", "totaleRitenuta", "totaleCassaPrevidenziale", "totaleSpese", "totaleSpeseEsenti", "totaleSpeseNonEsenti", "totaleMerce", "totaleMerceScontata", "totaleImponibile", "totaleImposta", "totaleEsente", "totaleDocumento", "nettoAPagare", "totaleSplitPayment", "bollo", "xmlFileName", "riferimentoAmministrazione", "banca", "datiTrasporto", "datiSdi", "datiPA", "righe", "speseDocumento", "scadenze", "numero", "mediaFile", "allegato", "bonusFiscaleCausale", "bonusFiscaleImporto", "bonusFiscalePercentuale", "progressivoInvio"]

    @field_validator('tipo_documento')
    def tipo_documento_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Ddt', 'FatturaAccompagnatoria', 'FatturaAcconto', 'FatturaDifferita', 'FatturaProfessionista', 'RicevutaFiscale', 'NotaCredito', 'NotaDebito', 'Scontrino', 'OrdineCliente', 'Preventivo', 'DdtFornitore', 'FatturaAccompagnatoriaFornitore', 'FatturaDifferitaFornitore', 'FatturaProfessionistaFornitore', 'NotaCreditoFornitore', 'NotaDebitoFornitore', 'PreventivoFornitore', 'OrdineFornitore', 'ResoCliente', 'FatturaAccontoFornitore', 'FatturaProForma', 'IntegrazioneFatturaReverseChargeInterno', 'IntegrazioneAcquistoServiziEstero', 'IntegrazioneAcquistoBeniIntracomunitari', 'IntegrazioneAcquistoBeniArt17', 'AutofatturaRegolarizzazioneFatture', 'AutofatturaSplafonamento', 'EstrazioneBeniDepositoIva', 'EstrazioneBeniDepositoIvaConVersamentoIva', 'FatturaDifferitaArt21Comma4LetteraA', 'FatturaDifferitaArt21Comma4LetteraB', 'CessioniBeniAmmortizzabiliEPassaggiInterni', 'FatturaAutoconsumoOCessioniGratuite', 'IntegrazioneFatturaReverseChargeInternoFornitore', 'IntegrazioneAcquistoServiziEsteroFornitore', 'IntegrazioneAcquistoBeniIntracomunitariFornitore', 'IntegrazioneAcquistoBeniArt17Fornitore', 'AutofatturaRegolarizzazioneFattureFornitore', 'AutofatturaSplafonamentoFornitore', 'EstrazioneBeniDepositoIvaFornitore', 'EstrazioneBeniDepositoIvaConVersamentoIvaFornitore', 'FatturaDifferitaArt21Comma4LetteraAFornitore', 'FatturaDifferitaArt21Comma4LetteraBFornitore', 'CessioniBeniAmmortizzabiliEPassaggiInterniFornitore', 'FatturaAutoconsumoOCessioniGratuiteFornitore', 'AcquistoSanMarinoConIva', 'ComunicazioneOmessaOIrregolareFatturazione', 'ComunicazioneOmessaOIrregolareFatturazioneFornitore']):
            raise ValueError("must be one of enum values ('Ddt', 'FatturaAccompagnatoria', 'FatturaAcconto', 'FatturaDifferita', 'FatturaProfessionista', 'RicevutaFiscale', 'NotaCredito', 'NotaDebito', 'Scontrino', 'OrdineCliente', 'Preventivo', 'DdtFornitore', 'FatturaAccompagnatoriaFornitore', 'FatturaDifferitaFornitore', 'FatturaProfessionistaFornitore', 'NotaCreditoFornitore', 'NotaDebitoFornitore', 'PreventivoFornitore', 'OrdineFornitore', 'ResoCliente', 'FatturaAccontoFornitore', 'FatturaProForma', 'IntegrazioneFatturaReverseChargeInterno', 'IntegrazioneAcquistoServiziEstero', 'IntegrazioneAcquistoBeniIntracomunitari', 'IntegrazioneAcquistoBeniArt17', 'AutofatturaRegolarizzazioneFatture', 'AutofatturaSplafonamento', 'EstrazioneBeniDepositoIva', 'EstrazioneBeniDepositoIvaConVersamentoIva', 'FatturaDifferitaArt21Comma4LetteraA', 'FatturaDifferitaArt21Comma4LetteraB', 'CessioniBeniAmmortizzabiliEPassaggiInterni', 'FatturaAutoconsumoOCessioniGratuite', 'IntegrazioneFatturaReverseChargeInternoFornitore', 'IntegrazioneAcquistoServiziEsteroFornitore', 'IntegrazioneAcquistoBeniIntracomunitariFornitore', 'IntegrazioneAcquistoBeniArt17Fornitore', 'AutofatturaRegolarizzazioneFattureFornitore', 'AutofatturaSplafonamentoFornitore', 'EstrazioneBeniDepositoIvaFornitore', 'EstrazioneBeniDepositoIvaConVersamentoIvaFornitore', 'FatturaDifferitaArt21Comma4LetteraAFornitore', 'FatturaDifferitaArt21Comma4LetteraBFornitore', 'CessioniBeniAmmortizzabiliEPassaggiInterniFornitore', 'FatturaAutoconsumoOCessioniGratuiteFornitore', 'AcquistoSanMarinoConIva', 'ComunicazioneOmessaOIrregolareFatturazione', 'ComunicazioneOmessaOIrregolareFatturazioneFornitore')")
        return value

    @field_validator('documento_fiscale')
    def documento_fiscale_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Vendita', 'Acquisto', 'NonFiscale']):
            raise ValueError("must be one of enum values ('Vendita', 'Acquisto', 'NonFiscale')")
        return value

    @field_validator('classe_documento')
    def classe_documento_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Vendita', 'Acquisto']):
            raise ValueError("must be one of enum values ('Vendita', 'Acquisto')")
        return value

    @field_validator('stato')
    def stato_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Bozza', 'Fatturato', 'Emesso', 'FatturaAccontoScontataInFattura', 'PreventivoChiuso', 'OrdineEvaso', 'OrdineParzialmenteEvaso', 'OrdineAnnullato', 'ResoAccreditato', 'DdtNonFatturare']):
            raise ValueError("must be one of enum values ('Bozza', 'Fatturato', 'Emesso', 'FatturaAccontoScontataInFattura', 'PreventivoChiuso', 'OrdineEvaso', 'OrdineParzialmenteEvaso', 'OrdineAnnullato', 'ResoAccreditato', 'DdtNonFatturare')")
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
        """Create an instance of Documento from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of anagrafica
        if self.anagrafica:
            _dict['anagrafica'] = self.anagrafica.to_dict()
        # override the default output from pydantic by calling `to_dict()` of causale_documento
        if self.causale_documento:
            _dict['causaleDocumento'] = self.causale_documento.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agente
        if self.agente:
            _dict['agente'] = self.agente.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pagamento
        if self.pagamento:
            _dict['pagamento'] = self.pagamento.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vettore
        if self.vettore:
            _dict['vettore'] = self.vettore.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cassa_previdenziale_causale_iva
        if self.cassa_previdenziale_causale_iva:
            _dict['cassaPrevidenzialeCausaleIva'] = self.cassa_previdenziale_causale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destinazione
        if self.destinazione:
            _dict['destinazione'] = self.destinazione.to_dict()
        # override the default output from pydantic by calling `to_dict()` of valuta
        if self.valuta:
            _dict['valuta'] = self.valuta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of causale_magazzino
        if self.causale_magazzino:
            _dict['causaleMagazzino'] = self.causale_magazzino.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iva1_causale_iva
        if self.iva1_causale_iva:
            _dict['iva1CausaleIva'] = self.iva1_causale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iva2_causale_iva
        if self.iva2_causale_iva:
            _dict['iva2CausaleIva'] = self.iva2_causale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iva3_causale_iva
        if self.iva3_causale_iva:
            _dict['iva3CausaleIva'] = self.iva3_causale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of iva4_causale_iva
        if self.iva4_causale_iva:
            _dict['iva4CausaleIva'] = self.iva4_causale_iva.to_dict()
        # override the default output from pydantic by calling `to_dict()` of banca
        if self.banca:
            _dict['banca'] = self.banca.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dati_trasporto
        if self.dati_trasporto:
            _dict['datiTrasporto'] = self.dati_trasporto.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dati_sdi
        if self.dati_sdi:
            _dict['datiSdi'] = self.dati_sdi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dati_pa
        if self.dati_pa:
            _dict['datiPA'] = self.dati_pa.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in righe (list)
        _items = []
        if self.righe:
            for _item_righe in self.righe:
                if _item_righe:
                    _items.append(_item_righe.to_dict())
            _dict['righe'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in spese_documento (list)
        _items = []
        if self.spese_documento:
            for _item_spese_documento in self.spese_documento:
                if _item_spese_documento:
                    _items.append(_item_spese_documento.to_dict())
            _dict['speseDocumento'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in scadenze (list)
        _items = []
        if self.scadenze:
            for _item_scadenze in self.scadenze:
                if _item_scadenze:
                    _items.append(_item_scadenze.to_dict())
            _dict['scadenze'] = _items
        # override the default output from pydantic by calling `to_dict()` of media_file
        if self.media_file:
            _dict['mediaFile'] = self.media_file.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in progressivo_invio (list)
        _items = []
        if self.progressivo_invio:
            for _item_progressivo_invio in self.progressivo_invio:
                if _item_progressivo_invio:
                    _items.append(_item_progressivo_invio.to_dict())
            _dict['progressivoInvio'] = _items
        # set to None if causale_documento_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_documento_id is None and "causale_documento_id" in self.model_fields_set:
            _dict['causaleDocumentoId'] = None

        # set to None if agente_id (nullable) is None
        # and model_fields_set contains the field
        if self.agente_id is None and "agente_id" in self.model_fields_set:
            _dict['agenteId'] = None

        # set to None if pagamento_id (nullable) is None
        # and model_fields_set contains the field
        if self.pagamento_id is None and "pagamento_id" in self.model_fields_set:
            _dict['pagamentoId'] = None

        # set to None if vettore_id (nullable) is None
        # and model_fields_set contains the field
        if self.vettore_id is None and "vettore_id" in self.model_fields_set:
            _dict['vettoreId'] = None

        # set to None if cassa_previdenziale_causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.cassa_previdenziale_causale_iva_id is None and "cassa_previdenziale_causale_iva_id" in self.model_fields_set:
            _dict['cassaPrevidenzialeCausaleIvaId'] = None

        # set to None if modello_id (nullable) is None
        # and model_fields_set contains the field
        if self.modello_id is None and "modello_id" in self.model_fields_set:
            _dict['modelloId'] = None

        # set to None if destinazione_id (nullable) is None
        # and model_fields_set contains the field
        if self.destinazione_id is None and "destinazione_id" in self.model_fields_set:
            _dict['destinazioneId'] = None

        # set to None if valuta_id (nullable) is None
        # and model_fields_set contains the field
        if self.valuta_id is None and "valuta_id" in self.model_fields_set:
            _dict['valutaId'] = None

        # set to None if causale_magazzino_id (nullable) is None
        # and model_fields_set contains the field
        if self.causale_magazzino_id is None and "causale_magazzino_id" in self.model_fields_set:
            _dict['causaleMagazzinoId'] = None

        # set to None if iva1_causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.iva1_causale_iva_id is None and "iva1_causale_iva_id" in self.model_fields_set:
            _dict['iva1CausaleIvaId'] = None

        # set to None if iva2_causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.iva2_causale_iva_id is None and "iva2_causale_iva_id" in self.model_fields_set:
            _dict['iva2CausaleIvaId'] = None

        # set to None if iva3_causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.iva3_causale_iva_id is None and "iva3_causale_iva_id" in self.model_fields_set:
            _dict['iva3CausaleIvaId'] = None

        # set to None if iva4_causale_iva_id (nullable) is None
        # and model_fields_set contains the field
        if self.iva4_causale_iva_id is None and "iva4_causale_iva_id" in self.model_fields_set:
            _dict['iva4CausaleIvaId'] = None

        # set to None if contatto (nullable) is None
        # and model_fields_set contains the field
        if self.contatto is None and "contatto" in self.model_fields_set:
            _dict['contatto'] = None

        # set to None if numero_parte_testo (nullable) is None
        # and model_fields_set contains the field
        if self.numero_parte_testo is None and "numero_parte_testo" in self.model_fields_set:
            _dict['numeroParteTesto'] = None

        # set to None if data_scadenza_preventivo (nullable) is None
        # and model_fields_set contains the field
        if self.data_scadenza_preventivo is None and "data_scadenza_preventivo" in self.model_fields_set:
            _dict['dataScadenzaPreventivo'] = None

        # set to None if data_inizio_scadenze (nullable) is None
        # and model_fields_set contains the field
        if self.data_inizio_scadenze is None and "data_inizio_scadenze" in self.model_fields_set:
            _dict['dataInizioScadenze'] = None

        # set to None if cassa_previdenziale_nome (nullable) is None
        # and model_fields_set contains the field
        if self.cassa_previdenziale_nome is None and "cassa_previdenziale_nome" in self.model_fields_set:
            _dict['cassaPrevidenzialeNome'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        # set to None if xml_file_name (nullable) is None
        # and model_fields_set contains the field
        if self.xml_file_name is None and "xml_file_name" in self.model_fields_set:
            _dict['xmlFileName'] = None

        # set to None if riferimento_amministrazione (nullable) is None
        # and model_fields_set contains the field
        if self.riferimento_amministrazione is None and "riferimento_amministrazione" in self.model_fields_set:
            _dict['riferimentoAmministrazione'] = None

        # set to None if righe (nullable) is None
        # and model_fields_set contains the field
        if self.righe is None and "righe" in self.model_fields_set:
            _dict['righe'] = None

        # set to None if spese_documento (nullable) is None
        # and model_fields_set contains the field
        if self.spese_documento is None and "spese_documento" in self.model_fields_set:
            _dict['speseDocumento'] = None

        # set to None if scadenze (nullable) is None
        # and model_fields_set contains the field
        if self.scadenze is None and "scadenze" in self.model_fields_set:
            _dict['scadenze'] = None

        # set to None if numero (nullable) is None
        # and model_fields_set contains the field
        if self.numero is None and "numero" in self.model_fields_set:
            _dict['numero'] = None

        # set to None if allegato (nullable) is None
        # and model_fields_set contains the field
        if self.allegato is None and "allegato" in self.model_fields_set:
            _dict['allegato'] = None

        # set to None if bonus_fiscale_causale (nullable) is None
        # and model_fields_set contains the field
        if self.bonus_fiscale_causale is None and "bonus_fiscale_causale" in self.model_fields_set:
            _dict['bonusFiscaleCausale'] = None

        # set to None if progressivo_invio (nullable) is None
        # and model_fields_set contains the field
        if self.progressivo_invio is None and "progressivo_invio" in self.model_fields_set:
            _dict['progressivoInvio'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Documento from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "concurrencyToken": obj.get("concurrencyToken"),
            "anagraficaId": obj.get("anagraficaId"),
            "anagrafica": Anagrafica.from_dict(obj["anagrafica"]) if obj.get("anagrafica") is not None else None,
            "causaleDocumentoId": obj.get("causaleDocumentoId"),
            "causaleDocumento": CausaleDocumento.from_dict(obj["causaleDocumento"]) if obj.get("causaleDocumento") is not None else None,
            "agenteId": obj.get("agenteId"),
            "agente": Anagrafica.from_dict(obj["agente"]) if obj.get("agente") is not None else None,
            "pagamentoId": obj.get("pagamentoId"),
            "pagamento": Pagamento.from_dict(obj["pagamento"]) if obj.get("pagamento") is not None else None,
            "vettoreId": obj.get("vettoreId"),
            "vettore": Anagrafica.from_dict(obj["vettore"]) if obj.get("vettore") is not None else None,
            "cassaPrevidenzialeCausaleIvaId": obj.get("cassaPrevidenzialeCausaleIvaId"),
            "modelloId": obj.get("modelloId"),
            "cassaPrevidenzialeCausaleIva": CausaleIva.from_dict(obj["cassaPrevidenzialeCausaleIva"]) if obj.get("cassaPrevidenzialeCausaleIva") is not None else None,
            "destinazioneId": obj.get("destinazioneId"),
            "destinazione": Indirizzo.from_dict(obj["destinazione"]) if obj.get("destinazione") is not None else None,
            "valutaId": obj.get("valutaId"),
            "valuta": Valuta.from_dict(obj["valuta"]) if obj.get("valuta") is not None else None,
            "causaleMagazzinoId": obj.get("causaleMagazzinoId"),
            "causaleMagazzino": CausaleMagazzino.from_dict(obj["causaleMagazzino"]) if obj.get("causaleMagazzino") is not None else None,
            "iva1CausaleIvaId": obj.get("iva1CausaleIvaId"),
            "iva1CausaleIva": CausaleIva.from_dict(obj["iva1CausaleIva"]) if obj.get("iva1CausaleIva") is not None else None,
            "iva2CausaleIvaId": obj.get("iva2CausaleIvaId"),
            "iva2CausaleIva": CausaleIva.from_dict(obj["iva2CausaleIva"]) if obj.get("iva2CausaleIva") is not None else None,
            "iva3CausaleIvaId": obj.get("iva3CausaleIvaId"),
            "iva3CausaleIva": CausaleIva.from_dict(obj["iva3CausaleIva"]) if obj.get("iva3CausaleIva") is not None else None,
            "iva4CausaleIvaId": obj.get("iva4CausaleIvaId"),
            "iva4CausaleIva": CausaleIva.from_dict(obj["iva4CausaleIva"]) if obj.get("iva4CausaleIva") is not None else None,
            "tipoDocumento": obj.get("tipoDocumento"),
            "documentoFiscale": obj.get("documentoFiscale"),
            "destinazioneDiversa": obj.get("destinazioneDiversa"),
            "ivaEsclusa": obj.get("ivaEsclusa"),
            "ritenutaIncludeCassaPrevidenziale": obj.get("ritenutaIncludeCassaPrevidenziale"),
            "classeDocumento": obj.get("classeDocumento"),
            "contatto": obj.get("contatto"),
            "numeroParteTesto": obj.get("numeroParteTesto"),
            "numeroParteNumerica": obj.get("numeroParteNumerica"),
            "data": obj.get("data"),
            "stato": obj.get("stato"),
            "dataScadenzaPreventivo": obj.get("dataScadenzaPreventivo"),
            "dataInizioScadenze": obj.get("dataInizioScadenze"),
            "scontoPercentuale": obj.get("scontoPercentuale"),
            "scontoIncondizionatoImporto": obj.get("scontoIncondizionatoImporto"),
            "abbuonoImporto": obj.get("abbuonoImporto"),
            "ritenutaPercentuale": obj.get("ritenutaPercentuale"),
            "enasarcoPercentuale": obj.get("enasarcoPercentuale"),
            "enasarcoImporto": obj.get("enasarcoImporto"),
            "quotaRitenutaSuImponibile": obj.get("quotaRitenutaSuImponibile"),
            "cambio": obj.get("cambio"),
            "cassaPrevidenzialeNome": obj.get("cassaPrevidenzialeNome"),
            "cassaPrevidenzialePercentuale": obj.get("cassaPrevidenzialePercentuale"),
            "note": obj.get("note"),
            "scontoPagamentoPercentuale": obj.get("scontoPagamentoPercentuale"),
            "iva1Imponibile": obj.get("iva1Imponibile"),
            "iva2Imponibile": obj.get("iva2Imponibile"),
            "iva3Imponibile": obj.get("iva3Imponibile"),
            "iva4Imponibile": obj.get("iva4Imponibile"),
            "iva1ImponibileLordo": obj.get("iva1ImponibileLordo"),
            "iva2ImponibileLordo": obj.get("iva2ImponibileLordo"),
            "iva3ImponibileLordo": obj.get("iva3ImponibileLordo"),
            "iva4ImponibileLordo": obj.get("iva4ImponibileLordo"),
            "iva1Imposta": obj.get("iva1Imposta"),
            "iva2Imposta": obj.get("iva2Imposta"),
            "iva3Imposta": obj.get("iva3Imposta"),
            "iva4Imposta": obj.get("iva4Imposta"),
            "totaleRitenuta": obj.get("totaleRitenuta"),
            "totaleCassaPrevidenziale": obj.get("totaleCassaPrevidenziale"),
            "totaleSpese": obj.get("totaleSpese"),
            "totaleSpeseEsenti": obj.get("totaleSpeseEsenti"),
            "totaleSpeseNonEsenti": obj.get("totaleSpeseNonEsenti"),
            "totaleMerce": obj.get("totaleMerce"),
            "totaleMerceScontata": obj.get("totaleMerceScontata"),
            "totaleImponibile": obj.get("totaleImponibile"),
            "totaleImposta": obj.get("totaleImposta"),
            "totaleEsente": obj.get("totaleEsente"),
            "totaleDocumento": obj.get("totaleDocumento"),
            "nettoAPagare": obj.get("nettoAPagare"),
            "totaleSplitPayment": obj.get("totaleSplitPayment"),
            "bollo": obj.get("bollo"),
            "xmlFileName": obj.get("xmlFileName"),
            "riferimentoAmministrazione": obj.get("riferimentoAmministrazione"),
            "banca": BancaDocumento.from_dict(obj["banca"]) if obj.get("banca") is not None else None,
            "datiTrasporto": DatiTrasporto.from_dict(obj["datiTrasporto"]) if obj.get("datiTrasporto") is not None else None,
            "datiSdi": DatiSdi.from_dict(obj["datiSdi"]) if obj.get("datiSdi") is not None else None,
            "datiPA": DatiPA.from_dict(obj["datiPA"]) if obj.get("datiPA") is not None else None,
            "righe": [BeneServizio.from_dict(_item) for _item in obj["righe"]] if obj.get("righe") is not None else None,
            "speseDocumento": [SpesaDocumento.from_dict(_item) for _item in obj["speseDocumento"]] if obj.get("speseDocumento") is not None else None,
            "scadenze": [Scadenza.from_dict(_item) for _item in obj["scadenze"]] if obj.get("scadenze") is not None else None,
            "numero": obj.get("numero"),
            "mediaFile": DocumentoMediaFile.from_dict(obj["mediaFile"]) if obj.get("mediaFile") is not None else None,
            "allegato": obj.get("allegato"),
            "bonusFiscaleCausale": obj.get("bonusFiscaleCausale"),
            "bonusFiscaleImporto": obj.get("bonusFiscaleImporto"),
            "bonusFiscalePercentuale": obj.get("bonusFiscalePercentuale"),
            "progressivoInvio": [ProgressivoInvio.from_dict(_item) for _item in obj["progressivoInvio"]] if obj.get("progressivoInvio") is not None else None
        })
        return _obj

from amica_python_sdk.models.bene_servizio import BeneServizio
from amica_python_sdk.models.scadenza import Scadenza
# TODO: Rewrite to not use raise_errors
Documento.model_rebuild(raise_errors=False)

