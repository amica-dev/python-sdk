# amica-sdk
La Customers API fornisce accesso programmatico a tutti i dati aziendali gestiti da [Amica 20](https://gestionaleamica.com). Supporta il ciclo completo di documenti, fatture, magazzino, contabilità e anagrafiche. Per guide e documentazione completa, visitare [amica.dev](https://amica.dev/).

## Autenticazione

Tutte le richieste API richiedono un token OAuth 2.0 Bearer valido, da includere nell'header `Authorization`:

```
Authorization: Bearer <token>
```

### Registra la tua app

Per integrare la Customers API registra la tua applicazione sull'**App Store di Amica**. Al termine della registrazione ottieni una coppia di credenziali OAuth 2.0 — `client_id` e `client_secret` (il secret è mostrato **una sola volta**) — e scegli gli **scope** e il **flusso di autenticazione** desiderati.

### Scegli il flusso

- **Authorization Code con PKCE** (consigliato per app che operano per conto di un utente Amica): l'utente autorizza la tua app tramite la pagina di consenso dell'identity provider; la tua app riceve un `code` da scambiare con un access token.

  ```
  GET  {identity-provider}/connect/authorize?response_type=code&client_id=<client_id>&redirect_uri=<redirect_uri>&scope=openid%20read%20write%20documenti&code_challenge=<challenge>&code_challenge_method=S256
  POST {identity-provider}/connect/token
       grant_type=authorization_code&code=<code>&code_verifier=<verifier>&client_id=<client_id>&client_secret=<client_secret>&redirect_uri=<redirect_uri>
  ```

- **Client Credentials** (per integrazioni server-to-server, senza utente interattivo):

  ```
  POST {identity-provider}/connect/token
  Content-Type: application/x-www-form-urlencoded

  grant_type=client_credentials&client_id=<client_id>&client_secret=<client_secret>&scope=read write documenti contabilita
  ```

  > **Nota:** il flusso Client Credentials è disponibile solo per le **app private**, non per quelle pubblicate sul marketplace.

In entrambi i casi la risposta contiene l'`access_token` (JWT con `aud: amica-cloud`) da usare nelle chiamate successive finché non scade (`expires_in`), dopodiché va richiesto un nuovo token. Ogni token contiene uno o più **scope** che determinano le aree accessibili (vedi sotto). Dalla [API Reference](https://amica.dev) è possibile incollare un access token per provare gli endpoint direttamente dal browser.

## Scope di autorizzazione

L'accesso agli endpoint è governato dagli scope presenti nel token OAuth:

| Scope | Descrizione |
|-------|-------------|
| `comune` | Anagrafiche: contatti, indirizzi, nazioni, valute, modalità di pagamento, ecc. |
| `magazzino` | Magazzino: articoli, listini, movimenti di magazzino, giacenze, distinte base. |
| `contabilita` | Contabilità: registrazioni contabili, scadenze, castelletti IVA, fatture elettroniche XML. |
| `documenti` | Documenti: fatture, note di credito, DDT, ordini, preventivi, proforma ed emissione. |

Una richiesta verso un endpoint non coperto dallo scope del token riceverà una risposta `403 Forbidden`.

## Company ID

La maggior parte degli endpoint è relativa a una specifica azienda e segue il pattern:

```
/api/v3/{companyId}/risorsa
```

Il `companyId` è l'identificativo univoco di ciascun database aziendale. Usare l'endpoint `GET /api/v3/config/Azienda` per ottenere l'elenco delle aziende disponibili.

## Paginazione

Gli endpoint che restituiscono liste supportano la paginazione tramite query parameter:

| Parametro | Descrizione |
|-----------|-------------|
| `Skip` | Numero di elementi da saltare dall'inizio del set di risultati. |
| `Take` | Numero di elementi da includere nella risposta. |

La risposta include due header:

| Header | Descrizione |
|--------|-------------|
| `X-Read-TotalCount` | Numero totale di elementi che soddisfano il filtro corrente. |
| `X-Read-Count` | Numero di elementi effettivamente restituiti nel body della risposta. |

## Ordinamento e filtri

Gli endpoint lista accettano parametri aggiuntivi:

| Parametro | Descrizione |
|-----------|-------------|
| `Order` | Lista di proprietà per l'ordinamento, separate da virgola. Un segno meno (`-`) prima del nome indica ordine discendente. Es. `-RagioneSociale1,Citta`. |
| `Filter` | Condizioni di ricerca: lista di espressioni separate da virgola, ciascuna formata da nome campo, operatore, valore ed eventuale connettore logico. Operatori: `$eq`, `$ne`, `$gt`, `$lt`, `$lte`, `$gte`, `$ct` (contiene), `$nct`, `$sw` (inizia con), `$ew` (finisce con). Connettori: `$and` (default, omissibile) e `$or`; le sotto-query si racchiudono tra `[]`. Es. `RagioneSociale1 $ct acme $or, Fido $gt 1000`. |
| `SkipTotalCount` | Se `true`, l'header `X-Read-TotalCount` viene omesso dalla risposta: migliori prestazioni a scapito del conteggio totale. Default `false`. |

## Espansione oggetti correlati

Gli endpoint singoli e lista supportano il parametro `Expand`. Quando fornito, gli oggetti correlati vengono inclusi inline nella risposta anziché restituiti come riferimenti. È possibile specificare espansioni multiple separate da virgola.

## Gestione errori

L'API usa codici di stato HTTP standard e restituisce [RFC 7807](https://tools.ietf.org/html/rfc7807) Problem Details in caso di errore:

| Codice | Significato |
|--------|-------------|
| `400` | Bad Request — validazione fallita o parametro obbligatorio mancante. |
| `401` | Unauthorized — token mancante o scaduto. |
| `403` | Forbidden — il token non possiede lo scope richiesto. |
| `404` | Not Found — la risorsa richiesta non esiste. |
| `409` | Conflict — conflitto di concorrenza. |
| `422` | Unprocessable Entity — entità non processabile (es. token di concorrenza obsoleto). |

Alcune risposte `400` includono un campo `overridable` che indica se l'errore di validazione può essere ignorato impostando il parametro `validationOverride` a `true`.

## Controllo della concorrenza

Le entità contengono una proprietà `ConcurrencyToken`. Quando si aggiorna un'entità tramite `PUT`, il token nel body della richiesta viene confrontato con il valore memorizzato. Se differiscono, viene restituito un `422 Unprocessable Entity`. Usare sempre l'ultimo token ricevuto da una risposta `GET` o `POST`.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v3
- Package version: 1.0.0
- Generator version: 7.11.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://amica.dev](https://amica.dev)

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import amica_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import amica_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import amica_sdk
from amica_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with amica_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_sdk.AnagraficaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    selector = 'RagioneSociale1' # str | Il campo usato per distinguere gli elementi.
    skip = 100 # int | Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione. (optional)
    take = 25 # int | Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione. (optional)

    try:
        # Restituisce una lista di elementi distinti.
        api_response = api_instance.api_vversion_company_id_anagrafica_distinct_get(version, company_id, selector, skip=skip, take=take)
        print("The response of AnagraficaApi->api_vversion_company_id_anagrafica_distinct_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnagraficaApi->api_vversion_company_id_anagrafica_distinct_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnagraficaApi* | [**api_vversion_company_id_anagrafica_distinct_get**](docs/AnagraficaApi.md#api_vversion_company_id_anagrafica_distinct_get) | **GET** /api/v{version}/{companyId}/Anagrafica/distinct | Restituisce una lista di elementi distinti.
*AnagraficaApi* | [**api_vversion_company_id_anagrafica_get**](docs/AnagraficaApi.md#api_vversion_company_id_anagrafica_get) | **GET** /api/v{version}/{companyId}/Anagrafica | Restituisce una lista di elementi.
*AnagraficaApi* | [**api_vversion_company_id_anagrafica_id_delete**](docs/AnagraficaApi.md#api_vversion_company_id_anagrafica_id_delete) | **DELETE** /api/v{version}/{companyId}/Anagrafica/{id} | Elimina un elemento.
*AnagraficaApi* | [**api_vversion_company_id_anagrafica_id_get**](docs/AnagraficaApi.md#api_vversion_company_id_anagrafica_id_get) | **GET** /api/v{version}/{companyId}/Anagrafica/{id} | Restituisce un elemento.
*AnagraficaApi* | [**api_vversion_company_id_anagrafica_id_put**](docs/AnagraficaApi.md#api_vversion_company_id_anagrafica_id_put) | **PUT** /api/v{version}/{companyId}/Anagrafica/{id} | Aggiorna un elemento esistente.
*AnagraficaApi* | [**api_vversion_company_id_anagrafica_new_get**](docs/AnagraficaApi.md#api_vversion_company_id_anagrafica_new_get) | **GET** /api/v{version}/{companyId}/Anagrafica/new | Restituisce una nuova istanza di un contatto del tipo specificato.
*AnagraficaApi* | [**api_vversion_company_id_anagrafica_post**](docs/AnagraficaApi.md#api_vversion_company_id_anagrafica_post) | **POST** /api/v{version}/{companyId}/Anagrafica | Salva un nuovo elemento.
*AreaGeograficaApi* | [**api_vversion_company_id_area_geografica_distinct_get**](docs/AreaGeograficaApi.md#api_vversion_company_id_area_geografica_distinct_get) | **GET** /api/v{version}/{companyId}/AreaGeografica/distinct | Restituisce una lista di elementi distinti.
*AreaGeograficaApi* | [**api_vversion_company_id_area_geografica_get**](docs/AreaGeograficaApi.md#api_vversion_company_id_area_geografica_get) | **GET** /api/v{version}/{companyId}/AreaGeografica | Restituisce una lista di elementi.
*AreaGeograficaApi* | [**api_vversion_company_id_area_geografica_id_delete**](docs/AreaGeograficaApi.md#api_vversion_company_id_area_geografica_id_delete) | **DELETE** /api/v{version}/{companyId}/AreaGeografica/{id} | Elimina un elemento.
*AreaGeograficaApi* | [**api_vversion_company_id_area_geografica_id_get**](docs/AreaGeograficaApi.md#api_vversion_company_id_area_geografica_id_get) | **GET** /api/v{version}/{companyId}/AreaGeografica/{id} | Restituisce un elemento.
*AreaGeograficaApi* | [**api_vversion_company_id_area_geografica_id_put**](docs/AreaGeograficaApi.md#api_vversion_company_id_area_geografica_id_put) | **PUT** /api/v{version}/{companyId}/AreaGeografica/{id} | Aggiorna un elemento esistente.
*AreaGeograficaApi* | [**api_vversion_company_id_area_geografica_new_get**](docs/AreaGeograficaApi.md#api_vversion_company_id_area_geografica_new_get) | **GET** /api/v{version}/{companyId}/AreaGeografica/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*AreaGeograficaApi* | [**api_vversion_company_id_area_geografica_post**](docs/AreaGeograficaApi.md#api_vversion_company_id_area_geografica_post) | **POST** /api/v{version}/{companyId}/AreaGeografica | Salva un nuovo elemento.
*ArticoloApi* | [**api_vversion_company_id_articolo_get**](docs/ArticoloApi.md#api_vversion_company_id_articolo_get) | **GET** /api/v{version}/{companyId}/Articolo | Restituisce una lista di elementi.
*ArticoloApi* | [**api_vversion_company_id_articolo_id_delete**](docs/ArticoloApi.md#api_vversion_company_id_articolo_id_delete) | **DELETE** /api/v{version}/{companyId}/Articolo/{id} | Elimina un elemento.
*ArticoloApi* | [**api_vversion_company_id_articolo_id_get**](docs/ArticoloApi.md#api_vversion_company_id_articolo_id_get) | **GET** /api/v{version}/{companyId}/Articolo/{id} | Restituisce un elemento.
*ArticoloApi* | [**api_vversion_company_id_articolo_id_put**](docs/ArticoloApi.md#api_vversion_company_id_articolo_id_put) | **PUT** /api/v{version}/{companyId}/Articolo/{id} | Aggiorna un elemento esistente.
*ArticoloApi* | [**api_vversion_company_id_articolo_new_get**](docs/ArticoloApi.md#api_vversion_company_id_articolo_new_get) | **GET** /api/v{version}/{companyId}/Articolo/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ArticoloApi* | [**api_vversion_company_id_articolo_post**](docs/ArticoloApi.md#api_vversion_company_id_articolo_post) | **POST** /api/v{version}/{companyId}/Articolo | Salva un nuovo elemento.
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_bulk_delete**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_bulk_delete) | **DELETE** /api/v{version}/{companyId}/ArticoloMediaFile/bulk | Elimina in blocco tutti i file multimediali degli articoli.
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_bulk_get**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_bulk_get) | **GET** /api/v{version}/{companyId}/ArticoloMediaFile/bulk | Scarica tutti i file multimediali degli articoli come archivio ZIP.
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_get**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_get) | **GET** /api/v{version}/{companyId}/ArticoloMediaFile | Restituisce una lista di elementi.
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_id_delete**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_id_delete) | **DELETE** /api/v{version}/{companyId}/ArticoloMediaFile/{id} | Elimina un elemento.
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_id_get**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_id_get) | **GET** /api/v{version}/{companyId}/ArticoloMediaFile/{id} | Restituisce un elemento.
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_id_put**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_id_put) | **PUT** /api/v{version}/{companyId}/ArticoloMediaFile/{id} | Aggiorna un elemento esistente.
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_new_get**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_new_get) | **GET** /api/v{version}/{companyId}/ArticoloMediaFile/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ArticoloMediaFileApi* | [**api_vversion_company_id_articolo_media_file_post**](docs/ArticoloMediaFileApi.md#api_vversion_company_id_articolo_media_file_post) | **POST** /api/v{version}/{companyId}/ArticoloMediaFile | Salva un nuovo elemento.
*AziendaApi* | [**api_vversion_config_azienda_get**](docs/AziendaApi.md#api_vversion_config_azienda_get) | **GET** /api/v{version}/config/Azienda | Restituisce una lista di elementi.
*AziendaApi* | [**api_vversion_config_azienda_id_get**](docs/AziendaApi.md#api_vversion_config_azienda_id_get) | **GET** /api/v{version}/config/Azienda/{id} | Restituisce un elemento.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_collegadocumento_post**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_collegadocumento_post) | **POST** /api/v{version}/{companyId}/BeneServizio/collegadocumento | Collega un bene/servizio a un documento.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_compute_post**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_compute_post) | **POST** /api/v{version}/{companyId}/BeneServizio/compute | Calcola gli importi di un Amica.BeneServizio (vedi Amica.BeneServizioComputeResult), considerando parametri come quantità movimentata, IVA applicata, eventuali sconti.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_get**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_get) | **GET** /api/v{version}/{companyId}/BeneServizio | Restituisce una lista di elementi.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_id_delete**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_id_delete) | **DELETE** /api/v{version}/{companyId}/BeneServizio/{id} | Elimina un elemento.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_id_get**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_id_get) | **GET** /api/v{version}/{companyId}/BeneServizio/{id} | Restituisce un elemento.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_id_put**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_id_put) | **PUT** /api/v{version}/{companyId}/BeneServizio/{id} | Aggiorna un elemento esistente.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_new_get**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_new_get) | **GET** /api/v{version}/{companyId}/BeneServizio/new | Restituisce una nuova istanza di un bene/servizio.
*BeneServizioApi* | [**api_vversion_company_id_bene_servizio_post**](docs/BeneServizioApi.md#api_vversion_company_id_bene_servizio_post) | **POST** /api/v{version}/{companyId}/BeneServizio | Salva un nuovo elemento.
*CassaPrevidenzialeApi* | [**api_vversion_company_id_tabelle_cassa_previdenziale_get**](docs/CassaPrevidenzialeApi.md#api_vversion_company_id_tabelle_cassa_previdenziale_get) | **GET** /api/v{version}/{companyId}/tabelle/CassaPrevidenziale | Restituisce il contenuto della tabella come lista di elementi.
*CastellettoIvaApi* | [**api_vversion_company_id_castelletto_iva_get**](docs/CastellettoIvaApi.md#api_vversion_company_id_castelletto_iva_get) | **GET** /api/v{version}/{companyId}/CastellettoIva | Restituisce una lista di elementi.
*CastellettoIvaApi* | [**api_vversion_company_id_castelletto_iva_id_delete**](docs/CastellettoIvaApi.md#api_vversion_company_id_castelletto_iva_id_delete) | **DELETE** /api/v{version}/{companyId}/CastellettoIva/{id} | Elimina un elemento.
*CastellettoIvaApi* | [**api_vversion_company_id_castelletto_iva_id_get**](docs/CastellettoIvaApi.md#api_vversion_company_id_castelletto_iva_id_get) | **GET** /api/v{version}/{companyId}/CastellettoIva/{id} | Restituisce un elemento.
*CastellettoIvaApi* | [**api_vversion_company_id_castelletto_iva_id_put**](docs/CastellettoIvaApi.md#api_vversion_company_id_castelletto_iva_id_put) | **PUT** /api/v{version}/{companyId}/CastellettoIva/{id} | Aggiorna un elemento esistente.
*CastellettoIvaApi* | [**api_vversion_company_id_castelletto_iva_new_get**](docs/CastellettoIvaApi.md#api_vversion_company_id_castelletto_iva_new_get) | **GET** /api/v{version}/{companyId}/CastellettoIva/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*CastellettoIvaApi* | [**api_vversion_company_id_castelletto_iva_post**](docs/CastellettoIvaApi.md#api_vversion_company_id_castelletto_iva_post) | **POST** /api/v{version}/{companyId}/CastellettoIva | Salva un nuovo elemento.
*CategoriaAnagraficaApi* | [**api_vversion_company_id_categoria_anagrafica_distinct_get**](docs/CategoriaAnagraficaApi.md#api_vversion_company_id_categoria_anagrafica_distinct_get) | **GET** /api/v{version}/{companyId}/CategoriaAnagrafica/distinct | Restituisce una lista di elementi distinti.
*CategoriaAnagraficaApi* | [**api_vversion_company_id_categoria_anagrafica_get**](docs/CategoriaAnagraficaApi.md#api_vversion_company_id_categoria_anagrafica_get) | **GET** /api/v{version}/{companyId}/CategoriaAnagrafica | Restituisce una lista di elementi.
*CategoriaAnagraficaApi* | [**api_vversion_company_id_categoria_anagrafica_id_delete**](docs/CategoriaAnagraficaApi.md#api_vversion_company_id_categoria_anagrafica_id_delete) | **DELETE** /api/v{version}/{companyId}/CategoriaAnagrafica/{id} | Elimina un elemento.
*CategoriaAnagraficaApi* | [**api_vversion_company_id_categoria_anagrafica_id_get**](docs/CategoriaAnagraficaApi.md#api_vversion_company_id_categoria_anagrafica_id_get) | **GET** /api/v{version}/{companyId}/CategoriaAnagrafica/{id} | Restituisce un elemento.
*CategoriaAnagraficaApi* | [**api_vversion_company_id_categoria_anagrafica_id_put**](docs/CategoriaAnagraficaApi.md#api_vversion_company_id_categoria_anagrafica_id_put) | **PUT** /api/v{version}/{companyId}/CategoriaAnagrafica/{id} | Aggiorna un elemento esistente.
*CategoriaAnagraficaApi* | [**api_vversion_company_id_categoria_anagrafica_new_get**](docs/CategoriaAnagraficaApi.md#api_vversion_company_id_categoria_anagrafica_new_get) | **GET** /api/v{version}/{companyId}/CategoriaAnagrafica/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*CategoriaAnagraficaApi* | [**api_vversion_company_id_categoria_anagrafica_post**](docs/CategoriaAnagraficaApi.md#api_vversion_company_id_categoria_anagrafica_post) | **POST** /api/v{version}/{companyId}/CategoriaAnagrafica | Salva un nuovo elemento.
*CategoriaMerceologicaApi* | [**api_vversion_company_id_categoria_merceologica_get**](docs/CategoriaMerceologicaApi.md#api_vversion_company_id_categoria_merceologica_get) | **GET** /api/v{version}/{companyId}/CategoriaMerceologica | Restituisce una lista di elementi.
*CategoriaMerceologicaApi* | [**api_vversion_company_id_categoria_merceologica_id_delete**](docs/CategoriaMerceologicaApi.md#api_vversion_company_id_categoria_merceologica_id_delete) | **DELETE** /api/v{version}/{companyId}/CategoriaMerceologica/{id} | Elimina un elemento.
*CategoriaMerceologicaApi* | [**api_vversion_company_id_categoria_merceologica_id_get**](docs/CategoriaMerceologicaApi.md#api_vversion_company_id_categoria_merceologica_id_get) | **GET** /api/v{version}/{companyId}/CategoriaMerceologica/{id} | Restituisce un elemento.
*CategoriaMerceologicaApi* | [**api_vversion_company_id_categoria_merceologica_id_put**](docs/CategoriaMerceologicaApi.md#api_vversion_company_id_categoria_merceologica_id_put) | **PUT** /api/v{version}/{companyId}/CategoriaMerceologica/{id} | Aggiorna un elemento esistente.
*CategoriaMerceologicaApi* | [**api_vversion_company_id_categoria_merceologica_new_get**](docs/CategoriaMerceologicaApi.md#api_vversion_company_id_categoria_merceologica_new_get) | **GET** /api/v{version}/{companyId}/CategoriaMerceologica/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*CategoriaMerceologicaApi* | [**api_vversion_company_id_categoria_merceologica_post**](docs/CategoriaMerceologicaApi.md#api_vversion_company_id_categoria_merceologica_post) | **POST** /api/v{version}/{companyId}/CategoriaMerceologica | Salva un nuovo elemento.
*CausaleDocumentoApi* | [**api_vversion_company_id_causale_documento_get**](docs/CausaleDocumentoApi.md#api_vversion_company_id_causale_documento_get) | **GET** /api/v{version}/{companyId}/CausaleDocumento | Restituisce una lista di elementi.
*CausaleDocumentoApi* | [**api_vversion_company_id_causale_documento_id_delete**](docs/CausaleDocumentoApi.md#api_vversion_company_id_causale_documento_id_delete) | **DELETE** /api/v{version}/{companyId}/CausaleDocumento/{id} | Elimina un elemento.
*CausaleDocumentoApi* | [**api_vversion_company_id_causale_documento_id_get**](docs/CausaleDocumentoApi.md#api_vversion_company_id_causale_documento_id_get) | **GET** /api/v{version}/{companyId}/CausaleDocumento/{id} | Restituisce un elemento.
*CausaleDocumentoApi* | [**api_vversion_company_id_causale_documento_id_put**](docs/CausaleDocumentoApi.md#api_vversion_company_id_causale_documento_id_put) | **PUT** /api/v{version}/{companyId}/CausaleDocumento/{id} | Aggiorna un elemento esistente.
*CausaleDocumentoApi* | [**api_vversion_company_id_causale_documento_new_get**](docs/CausaleDocumentoApi.md#api_vversion_company_id_causale_documento_new_get) | **GET** /api/v{version}/{companyId}/CausaleDocumento/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*CausaleDocumentoApi* | [**api_vversion_company_id_causale_documento_post**](docs/CausaleDocumentoApi.md#api_vversion_company_id_causale_documento_post) | **POST** /api/v{version}/{companyId}/CausaleDocumento | Salva un nuovo elemento.
*CausaleIvaApi* | [**api_vversion_company_id_causale_iva_get**](docs/CausaleIvaApi.md#api_vversion_company_id_causale_iva_get) | **GET** /api/v{version}/{companyId}/CausaleIva | Restituisce una lista di elementi.
*CausaleIvaApi* | [**api_vversion_company_id_causale_iva_id_delete**](docs/CausaleIvaApi.md#api_vversion_company_id_causale_iva_id_delete) | **DELETE** /api/v{version}/{companyId}/CausaleIva/{id} | Elimina un elemento.
*CausaleIvaApi* | [**api_vversion_company_id_causale_iva_id_get**](docs/CausaleIvaApi.md#api_vversion_company_id_causale_iva_id_get) | **GET** /api/v{version}/{companyId}/CausaleIva/{id} | Restituisce un elemento.
*CausaleIvaApi* | [**api_vversion_company_id_causale_iva_id_put**](docs/CausaleIvaApi.md#api_vversion_company_id_causale_iva_id_put) | **PUT** /api/v{version}/{companyId}/CausaleIva/{id} | Aggiorna un elemento esistente.
*CausaleIvaApi* | [**api_vversion_company_id_causale_iva_new_get**](docs/CausaleIvaApi.md#api_vversion_company_id_causale_iva_new_get) | **GET** /api/v{version}/{companyId}/CausaleIva/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*CausaleIvaApi* | [**api_vversion_company_id_causale_iva_post**](docs/CausaleIvaApi.md#api_vversion_company_id_causale_iva_post) | **POST** /api/v{version}/{companyId}/CausaleIva | Salva un nuovo elemento.
*CausaleMagazzinoApi* | [**api_vversion_company_id_causale_magazzino_get**](docs/CausaleMagazzinoApi.md#api_vversion_company_id_causale_magazzino_get) | **GET** /api/v{version}/{companyId}/CausaleMagazzino | Restituisce una lista di elementi.
*CausaleMagazzinoApi* | [**api_vversion_company_id_causale_magazzino_id_delete**](docs/CausaleMagazzinoApi.md#api_vversion_company_id_causale_magazzino_id_delete) | **DELETE** /api/v{version}/{companyId}/CausaleMagazzino/{id} | Elimina un elemento.
*CausaleMagazzinoApi* | [**api_vversion_company_id_causale_magazzino_id_get**](docs/CausaleMagazzinoApi.md#api_vversion_company_id_causale_magazzino_id_get) | **GET** /api/v{version}/{companyId}/CausaleMagazzino/{id} | Restituisce un elemento.
*CausaleMagazzinoApi* | [**api_vversion_company_id_causale_magazzino_id_put**](docs/CausaleMagazzinoApi.md#api_vversion_company_id_causale_magazzino_id_put) | **PUT** /api/v{version}/{companyId}/CausaleMagazzino/{id} | Aggiorna un elemento esistente.
*CausaleMagazzinoApi* | [**api_vversion_company_id_causale_magazzino_new_get**](docs/CausaleMagazzinoApi.md#api_vversion_company_id_causale_magazzino_new_get) | **GET** /api/v{version}/{companyId}/CausaleMagazzino/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*CausaleMagazzinoApi* | [**api_vversion_company_id_causale_magazzino_post**](docs/CausaleMagazzinoApi.md#api_vversion_company_id_causale_magazzino_post) | **POST** /api/v{version}/{companyId}/CausaleMagazzino | Salva un nuovo elemento.
*CodicePagamentoApi* | [**api_vversion_company_id_tabelle_codice_pagamento_get**](docs/CodicePagamentoApi.md#api_vversion_company_id_tabelle_codice_pagamento_get) | **GET** /api/v{version}/{companyId}/tabelle/CodicePagamento | Restituisce il contenuto della tabella come lista di elementi.
*ContoContabileApi* | [**api_vversion_company_id_conto_contabile_get**](docs/ContoContabileApi.md#api_vversion_company_id_conto_contabile_get) | **GET** /api/v{version}/{companyId}/ContoContabile | Restituisce una lista di elementi.
*ContoContabileApi* | [**api_vversion_company_id_conto_contabile_id_delete**](docs/ContoContabileApi.md#api_vversion_company_id_conto_contabile_id_delete) | **DELETE** /api/v{version}/{companyId}/ContoContabile/{id} | Elimina un elemento.
*ContoContabileApi* | [**api_vversion_company_id_conto_contabile_id_get**](docs/ContoContabileApi.md#api_vversion_company_id_conto_contabile_id_get) | **GET** /api/v{version}/{companyId}/ContoContabile/{id} | Restituisce un elemento.
*ContoContabileApi* | [**api_vversion_company_id_conto_contabile_id_put**](docs/ContoContabileApi.md#api_vversion_company_id_conto_contabile_id_put) | **PUT** /api/v{version}/{companyId}/ContoContabile/{id} | Aggiorna un elemento esistente.
*ContoContabileApi* | [**api_vversion_company_id_conto_contabile_new_get**](docs/ContoContabileApi.md#api_vversion_company_id_conto_contabile_new_get) | **GET** /api/v{version}/{companyId}/ContoContabile/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ContoContabileApi* | [**api_vversion_company_id_conto_contabile_post**](docs/ContoContabileApi.md#api_vversion_company_id_conto_contabile_post) | **POST** /api/v{version}/{companyId}/ContoContabile | Salva un nuovo elemento.
*ContoContabileApi* | [**api_vversion_company_id_conto_contabile_repair_post**](docs/ContoContabileApi.md#api_vversion_company_id_conto_contabile_repair_post) | **POST** /api/v{version}/{companyId}/ContoContabile/repair | Valida le registrazioni contabili, cercando di correggere i problemi più comuni.
*DistintaBaseApi* | [**api_vversion_company_id_distinta_base_get**](docs/DistintaBaseApi.md#api_vversion_company_id_distinta_base_get) | **GET** /api/v{version}/{companyId}/DistintaBase | Restituisce una lista di elementi.
*DistintaBaseApi* | [**api_vversion_company_id_distinta_base_id_delete**](docs/DistintaBaseApi.md#api_vversion_company_id_distinta_base_id_delete) | **DELETE** /api/v{version}/{companyId}/DistintaBase/{id} | Elimina un elemento.
*DistintaBaseApi* | [**api_vversion_company_id_distinta_base_id_get**](docs/DistintaBaseApi.md#api_vversion_company_id_distinta_base_id_get) | **GET** /api/v{version}/{companyId}/DistintaBase/{id} | Restituisce un elemento.
*DistintaBaseApi* | [**api_vversion_company_id_distinta_base_id_put**](docs/DistintaBaseApi.md#api_vversion_company_id_distinta_base_id_put) | **PUT** /api/v{version}/{companyId}/DistintaBase/{id} | Aggiorna un elemento esistente.
*DistintaBaseApi* | [**api_vversion_company_id_distinta_base_new_get**](docs/DistintaBaseApi.md#api_vversion_company_id_distinta_base_new_get) | **GET** /api/v{version}/{companyId}/DistintaBase/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*DistintaBaseApi* | [**api_vversion_company_id_distinta_base_post**](docs/DistintaBaseApi.md#api_vversion_company_id_distinta_base_post) | **POST** /api/v{version}/{companyId}/DistintaBase | Salva un nuovo elemento.
*DocumentoApi* | [**api_vversion_company_id_documento_compute_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_compute_post) | **POST** /api/v{version}/{companyId}/Documento/compute | Calcola i totali di un documento.
*DocumentoApi* | [**api_vversion_company_id_documento_distinct_get**](docs/DocumentoApi.md#api_vversion_company_id_documento_distinct_get) | **GET** /api/v{version}/{companyId}/Documento/distinct | Restituisce una lista di elementi distinti.
*DocumentoApi* | [**api_vversion_company_id_documento_documento_id_emit_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_documento_id_emit_post) | **POST** /api/v{version}/{companyId}/Documento/{documentoId}/emit | Emette un documento.
*DocumentoApi* | [**api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post) | **POST** /api/v{version}/{companyId}/Documento/{documentoId}/newinstancefromtemplate | Replica un documento. Crea una copia con la data odierna e, se è un documento di vendita, un nuovo numero. Alcuni campi vengono reimpostati ai valori predefiniti (stato del documento, stato SDI, stato del pagamento, ecc.).
*DocumentoApi* | [**api_vversion_company_id_documento_get**](docs/DocumentoApi.md#api_vversion_company_id_documento_get) | **GET** /api/v{version}/{companyId}/Documento | Restituisce una lista di elementi.
*DocumentoApi* | [**api_vversion_company_id_documento_id_delete**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_delete) | **DELETE** /api/v{version}/{companyId}/Documento/{id} | Elimina un elemento.
*DocumentoApi* | [**api_vversion_company_id_documento_id_get**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_get) | **GET** /api/v{version}/{companyId}/Documento/{id} | Restituisce un elemento.
*DocumentoApi* | [**api_vversion_company_id_documento_id_import_acconto_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_import_acconto_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/acconto | Importa righe da uno o più acconti in un documento esistente.
*DocumentoApi* | [**api_vversion_company_id_documento_id_import_ddt_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_import_ddt_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/ddt | Importa righe da uno o più DDT in un documento esistente.
*DocumentoApi* | [**api_vversion_company_id_documento_id_import_ordine_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_import_ordine_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/ordine | Importa righe da uno o più ordini in un documento esistente.
*DocumentoApi* | [**api_vversion_company_id_documento_id_import_preventivo_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_import_preventivo_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/preventivo | Importa righe da uno o più preventivi in un documento esistente.
*DocumentoApi* | [**api_vversion_company_id_documento_id_import_proforma_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_import_proforma_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/proforma | Importa righe da una o più fatture proforma in un documento esistente.
*DocumentoApi* | [**api_vversion_company_id_documento_id_import_reso_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_import_reso_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/reso | Importa righe da uno o più resi in un documento esistente.
*DocumentoApi* | [**api_vversion_company_id_documento_id_put**](docs/DocumentoApi.md#api_vversion_company_id_documento_id_put) | **PUT** /api/v{version}/{companyId}/Documento/{id} | Aggiorna un elemento esistente.
*DocumentoApi* | [**api_vversion_company_id_documento_new_get**](docs/DocumentoApi.md#api_vversion_company_id_documento_new_get) | **GET** /api/v{version}/{companyId}/Documento/new | Restituisce una nuova istanza di un documento del tipo specificato.
*DocumentoApi* | [**api_vversion_company_id_documento_periodicinvoicing_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_periodicinvoicing_post) | **POST** /api/v{version}/{companyId}/Documento/periodicinvoicing | Genera fatture per tutti i contatti che corrispondono ai criteri di fatturazione periodica.
*DocumentoApi* | [**api_vversion_company_id_documento_post**](docs/DocumentoApi.md#api_vversion_company_id_documento_post) | **POST** /api/v{version}/{companyId}/Documento | Salva un nuovo elemento.
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_bulk_delete**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_bulk_delete) | **DELETE** /api/v{version}/{companyId}/DocumentoMediaFile/bulk | Elimina in blocco tutti i file multimediali dei documenti.
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_bulk_get**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_bulk_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile/bulk | Scarica tutti i file multimediali dei documenti come archivio ZIP.
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_get**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile | Restituisce una lista di elementi.
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_id_delete**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_id_delete) | **DELETE** /api/v{version}/{companyId}/DocumentoMediaFile/{id} | Elimina un elemento.
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_id_get**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_id_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile/{id} | Restituisce un elemento.
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_id_put**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_id_put) | **PUT** /api/v{version}/{companyId}/DocumentoMediaFile/{id} | Aggiorna un elemento esistente.
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_new_get**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_new_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*DocumentoMediaFileApi* | [**api_vversion_company_id_documento_media_file_post**](docs/DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_post) | **POST** /api/v{version}/{companyId}/DocumentoMediaFile | Salva un nuovo elemento.
*EventoApi* | [**api_vversion_evento_get**](docs/EventoApi.md#api_vversion_evento_get) | **GET** /api/v{version}/Evento | 
*EventoApi* | [**api_vversion_evento_id_delete**](docs/EventoApi.md#api_vversion_evento_id_delete) | **DELETE** /api/v{version}/Evento/{id} | Elimina un elemento.
*EventoApi* | [**api_vversion_evento_id_get**](docs/EventoApi.md#api_vversion_evento_id_get) | **GET** /api/v{version}/Evento/{id} | 
*EventoApi* | [**api_vversion_evento_id_put**](docs/EventoApi.md#api_vversion_evento_id_put) | **PUT** /api/v{version}/Evento/{id} | Aggiorna un elemento esistente.
*EventoApi* | [**api_vversion_evento_new_get**](docs/EventoApi.md#api_vversion_evento_new_get) | **GET** /api/v{version}/Evento/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*EventoApi* | [**api_vversion_evento_post**](docs/EventoApi.md#api_vversion_evento_post) | **POST** /api/v{version}/Evento | Salva un nuovo elemento.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/archivebydaterange | Scarica un archivio ZIP di fatture XML, filtrate per intervallo di date.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/archivebyfilename | Scarica un archivio ZIP di fatture XML, filtrate per nome file.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_bulk_delete**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_bulk_delete) | **DELETE** /api/v{version}/{companyId}/FatturaElettronicaXml/bulk | Elimina in blocco tutte le fatture XML dell&#39;azienda.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_bulk_get**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_bulk_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/bulk | Scarica tutte le fatture XML come archivio ZIP.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_bulk_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_bulk_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/bulk | Carica in blocco fatture XML da un archivio ZIP.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_export_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_export_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/export | Esporta uno o più documenti in una fattura XML.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/{fileName}/attachments | Scarica i file allegati di una fattura XML.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_file_name_get**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_file_name_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/{fileName} | Recupera una fattura XML per nome file.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_get**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml | Restituisce una lista di elementi.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_id_delete**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_id_delete) | **DELETE** /api/v{version}/{companyId}/FatturaElettronicaXml/{id} | Elimina un elemento.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_id_get**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_id_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/{id} | Restituisce un elemento.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_id_put**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_id_put) | **PUT** /api/v{version}/{companyId}/FatturaElettronicaXml/{id} | Aggiorna un elemento esistente.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_import_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_import_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/import | Importa una fattura XML.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_new_get**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_new_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_pair_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_pair_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/pair | Associa una fattura XML a un documento esistente.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml | Salva un nuovo elemento.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/sdi/download/esiti | Interroga il Sistema di Interscambio (SDI) e scarica gli esiti di invio delle fatture precedentemente caricate.
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/sdi/download/fatture | Scarica le nuove fatture dal Sistema di Interscambio (SDI).
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/sdi/upload | Invia una o più fatture al Sistema di Interscambio (SDI).
*FatturaElettronicaXmlApi* | [**api_vversion_company_id_fattura_elettronica_xml_stylesheet_post**](docs/FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_stylesheet_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/stylesheet | Applica un foglio di stile CSS a una fattura XML esistente e restituisce il risultato.
*FatturaElettronicaXmlTemplateApi* | [**api_vversion_company_id_fattura_elettronica_xml_template_get**](docs/FatturaElettronicaXmlTemplateApi.md#api_vversion_company_id_fattura_elettronica_xml_template_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXmlTemplate | Restituisce una lista di elementi.
*FatturaElettronicaXmlTemplateApi* | [**api_vversion_company_id_fattura_elettronica_xml_template_id_delete**](docs/FatturaElettronicaXmlTemplateApi.md#api_vversion_company_id_fattura_elettronica_xml_template_id_delete) | **DELETE** /api/v{version}/{companyId}/FatturaElettronicaXmlTemplate/{id} | Elimina un elemento.
*FatturaElettronicaXmlTemplateApi* | [**api_vversion_company_id_fattura_elettronica_xml_template_id_get**](docs/FatturaElettronicaXmlTemplateApi.md#api_vversion_company_id_fattura_elettronica_xml_template_id_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXmlTemplate/{id} | Restituisce un elemento.
*FatturaElettronicaXmlTemplateApi* | [**api_vversion_company_id_fattura_elettronica_xml_template_id_put**](docs/FatturaElettronicaXmlTemplateApi.md#api_vversion_company_id_fattura_elettronica_xml_template_id_put) | **PUT** /api/v{version}/{companyId}/FatturaElettronicaXmlTemplate/{id} | Aggiorna un elemento esistente.
*FatturaElettronicaXmlTemplateApi* | [**api_vversion_company_id_fattura_elettronica_xml_template_new_get**](docs/FatturaElettronicaXmlTemplateApi.md#api_vversion_company_id_fattura_elettronica_xml_template_new_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXmlTemplate/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*FatturaElettronicaXmlTemplateApi* | [**api_vversion_company_id_fattura_elettronica_xml_template_post**](docs/FatturaElettronicaXmlTemplateApi.md#api_vversion_company_id_fattura_elettronica_xml_template_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXmlTemplate | Salva un nuovo elemento.
*GiacenzaApi* | [**api_vversion_company_id_giacenza_distinct_get**](docs/GiacenzaApi.md#api_vversion_company_id_giacenza_distinct_get) | **GET** /api/v{version}/{companyId}/Giacenza/distinct | Restituisce una lista di elementi distinti.
*GiacenzaApi* | [**api_vversion_company_id_giacenza_get**](docs/GiacenzaApi.md#api_vversion_company_id_giacenza_get) | **GET** /api/v{version}/{companyId}/Giacenza | Restituisce una lista di elementi.
*GiacenzaApi* | [**api_vversion_company_id_giacenza_id_delete**](docs/GiacenzaApi.md#api_vversion_company_id_giacenza_id_delete) | **DELETE** /api/v{version}/{companyId}/Giacenza/{id} | Elimina un elemento.
*GiacenzaApi* | [**api_vversion_company_id_giacenza_id_get**](docs/GiacenzaApi.md#api_vversion_company_id_giacenza_id_get) | **GET** /api/v{version}/{companyId}/Giacenza/{id} | Restituisce un elemento.
*GiacenzaApi* | [**api_vversion_company_id_giacenza_id_put**](docs/GiacenzaApi.md#api_vversion_company_id_giacenza_id_put) | **PUT** /api/v{version}/{companyId}/Giacenza/{id} | Aggiorna un elemento esistente.
*GiacenzaApi* | [**api_vversion_company_id_giacenza_new_get**](docs/GiacenzaApi.md#api_vversion_company_id_giacenza_new_get) | **GET** /api/v{version}/{companyId}/Giacenza/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*GiacenzaApi* | [**api_vversion_company_id_giacenza_post**](docs/GiacenzaApi.md#api_vversion_company_id_giacenza_post) | **POST** /api/v{version}/{companyId}/Giacenza | Salva un nuovo elemento.
*GiornaleMagazzinoApi* | [**api_vversion_company_id_giornale_magazzino_get**](docs/GiornaleMagazzinoApi.md#api_vversion_company_id_giornale_magazzino_get) | **GET** /api/v{version}/{companyId}/GiornaleMagazzino | Restituisce una lista di elementi.
*GiornaleMagazzinoApi* | [**api_vversion_company_id_giornale_magazzino_id_delete**](docs/GiornaleMagazzinoApi.md#api_vversion_company_id_giornale_magazzino_id_delete) | **DELETE** /api/v{version}/{companyId}/GiornaleMagazzino/{id} | Elimina un elemento.
*GiornaleMagazzinoApi* | [**api_vversion_company_id_giornale_magazzino_id_get**](docs/GiornaleMagazzinoApi.md#api_vversion_company_id_giornale_magazzino_id_get) | **GET** /api/v{version}/{companyId}/GiornaleMagazzino/{id} | Restituisce un elemento.
*GiornaleMagazzinoApi* | [**api_vversion_company_id_giornale_magazzino_id_put**](docs/GiornaleMagazzinoApi.md#api_vversion_company_id_giornale_magazzino_id_put) | **PUT** /api/v{version}/{companyId}/GiornaleMagazzino/{id} | Aggiorna un elemento esistente.
*GiornaleMagazzinoApi* | [**api_vversion_company_id_giornale_magazzino_new_get**](docs/GiornaleMagazzinoApi.md#api_vversion_company_id_giornale_magazzino_new_get) | **GET** /api/v{version}/{companyId}/GiornaleMagazzino/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*GiornaleMagazzinoApi* | [**api_vversion_company_id_giornale_magazzino_post**](docs/GiornaleMagazzinoApi.md#api_vversion_company_id_giornale_magazzino_post) | **POST** /api/v{version}/{companyId}/GiornaleMagazzino | Salva un nuovo elemento.
*GruppoMerceologicoApi* | [**api_vversion_company_id_gruppo_merceologico_get**](docs/GruppoMerceologicoApi.md#api_vversion_company_id_gruppo_merceologico_get) | **GET** /api/v{version}/{companyId}/GruppoMerceologico | Restituisce una lista di elementi.
*GruppoMerceologicoApi* | [**api_vversion_company_id_gruppo_merceologico_id_delete**](docs/GruppoMerceologicoApi.md#api_vversion_company_id_gruppo_merceologico_id_delete) | **DELETE** /api/v{version}/{companyId}/GruppoMerceologico/{id} | Elimina un elemento.
*GruppoMerceologicoApi* | [**api_vversion_company_id_gruppo_merceologico_id_get**](docs/GruppoMerceologicoApi.md#api_vversion_company_id_gruppo_merceologico_id_get) | **GET** /api/v{version}/{companyId}/GruppoMerceologico/{id} | Restituisce un elemento.
*GruppoMerceologicoApi* | [**api_vversion_company_id_gruppo_merceologico_id_put**](docs/GruppoMerceologicoApi.md#api_vversion_company_id_gruppo_merceologico_id_put) | **PUT** /api/v{version}/{companyId}/GruppoMerceologico/{id} | Aggiorna un elemento esistente.
*GruppoMerceologicoApi* | [**api_vversion_company_id_gruppo_merceologico_new_get**](docs/GruppoMerceologicoApi.md#api_vversion_company_id_gruppo_merceologico_new_get) | **GET** /api/v{version}/{companyId}/GruppoMerceologico/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*GruppoMerceologicoApi* | [**api_vversion_company_id_gruppo_merceologico_post**](docs/GruppoMerceologicoApi.md#api_vversion_company_id_gruppo_merceologico_post) | **POST** /api/v{version}/{companyId}/GruppoMerceologico | Salva un nuovo elemento.
*IndirizzoApi* | [**api_vversion_company_id_indirizzo_get**](docs/IndirizzoApi.md#api_vversion_company_id_indirizzo_get) | **GET** /api/v{version}/{companyId}/Indirizzo | Restituisce una lista di elementi.
*IndirizzoApi* | [**api_vversion_company_id_indirizzo_id_delete**](docs/IndirizzoApi.md#api_vversion_company_id_indirizzo_id_delete) | **DELETE** /api/v{version}/{companyId}/Indirizzo/{id} | Elimina un elemento.
*IndirizzoApi* | [**api_vversion_company_id_indirizzo_id_get**](docs/IndirizzoApi.md#api_vversion_company_id_indirizzo_id_get) | **GET** /api/v{version}/{companyId}/Indirizzo/{id} | Restituisce un elemento.
*IndirizzoApi* | [**api_vversion_company_id_indirizzo_id_put**](docs/IndirizzoApi.md#api_vversion_company_id_indirizzo_id_put) | **PUT** /api/v{version}/{companyId}/Indirizzo/{id} | Aggiorna un elemento esistente.
*IndirizzoApi* | [**api_vversion_company_id_indirizzo_new_get**](docs/IndirizzoApi.md#api_vversion_company_id_indirizzo_new_get) | **GET** /api/v{version}/{companyId}/Indirizzo/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*IndirizzoApi* | [**api_vversion_company_id_indirizzo_post**](docs/IndirizzoApi.md#api_vversion_company_id_indirizzo_post) | **POST** /api/v{version}/{companyId}/Indirizzo | Salva un nuovo elemento.
*ListinoApi* | [**api_vversion_company_id_listino_get**](docs/ListinoApi.md#api_vversion_company_id_listino_get) | **GET** /api/v{version}/{companyId}/Listino | Restituisce una lista di elementi.
*ListinoApi* | [**api_vversion_company_id_listino_id_delete**](docs/ListinoApi.md#api_vversion_company_id_listino_id_delete) | **DELETE** /api/v{version}/{companyId}/Listino/{id} | Elimina un elemento.
*ListinoApi* | [**api_vversion_company_id_listino_id_get**](docs/ListinoApi.md#api_vversion_company_id_listino_id_get) | **GET** /api/v{version}/{companyId}/Listino/{id} | Restituisce un elemento.
*ListinoApi* | [**api_vversion_company_id_listino_id_put**](docs/ListinoApi.md#api_vversion_company_id_listino_id_put) | **PUT** /api/v{version}/{companyId}/Listino/{id} | Aggiorna un elemento esistente.
*ListinoApi* | [**api_vversion_company_id_listino_new_get**](docs/ListinoApi.md#api_vversion_company_id_listino_new_get) | **GET** /api/v{version}/{companyId}/Listino/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ListinoApi* | [**api_vversion_company_id_listino_post**](docs/ListinoApi.md#api_vversion_company_id_listino_post) | **POST** /api/v{version}/{companyId}/Listino | Salva un nuovo elemento.
*MagazzinoApi* | [**api_vversion_company_id_magazzino_get**](docs/MagazzinoApi.md#api_vversion_company_id_magazzino_get) | **GET** /api/v{version}/{companyId}/Magazzino | Restituisce una lista di elementi.
*MagazzinoApi* | [**api_vversion_company_id_magazzino_id_delete**](docs/MagazzinoApi.md#api_vversion_company_id_magazzino_id_delete) | **DELETE** /api/v{version}/{companyId}/Magazzino/{id} | Elimina un elemento.
*MagazzinoApi* | [**api_vversion_company_id_magazzino_id_get**](docs/MagazzinoApi.md#api_vversion_company_id_magazzino_id_get) | **GET** /api/v{version}/{companyId}/Magazzino/{id} | Restituisce un elemento.
*MagazzinoApi* | [**api_vversion_company_id_magazzino_id_put**](docs/MagazzinoApi.md#api_vversion_company_id_magazzino_id_put) | **PUT** /api/v{version}/{companyId}/Magazzino/{id} | Aggiorna un elemento esistente.
*MagazzinoApi* | [**api_vversion_company_id_magazzino_new_get**](docs/MagazzinoApi.md#api_vversion_company_id_magazzino_new_get) | **GET** /api/v{version}/{companyId}/Magazzino/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*MagazzinoApi* | [**api_vversion_company_id_magazzino_post**](docs/MagazzinoApi.md#api_vversion_company_id_magazzino_post) | **POST** /api/v{version}/{companyId}/Magazzino | Salva un nuovo elemento.
*MarcaApi* | [**api_vversion_company_id_marca_get**](docs/MarcaApi.md#api_vversion_company_id_marca_get) | **GET** /api/v{version}/{companyId}/Marca | Restituisce una lista di elementi.
*MarcaApi* | [**api_vversion_company_id_marca_id_delete**](docs/MarcaApi.md#api_vversion_company_id_marca_id_delete) | **DELETE** /api/v{version}/{companyId}/Marca/{id} | Elimina un elemento.
*MarcaApi* | [**api_vversion_company_id_marca_id_get**](docs/MarcaApi.md#api_vversion_company_id_marca_id_get) | **GET** /api/v{version}/{companyId}/Marca/{id} | Restituisce un elemento.
*MarcaApi* | [**api_vversion_company_id_marca_id_put**](docs/MarcaApi.md#api_vversion_company_id_marca_id_put) | **PUT** /api/v{version}/{companyId}/Marca/{id} | Aggiorna un elemento esistente.
*MarcaApi* | [**api_vversion_company_id_marca_new_get**](docs/MarcaApi.md#api_vversion_company_id_marca_new_get) | **GET** /api/v{version}/{companyId}/Marca/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*MarcaApi* | [**api_vversion_company_id_marca_post**](docs/MarcaApi.md#api_vversion_company_id_marca_post) | **POST** /api/v{version}/{companyId}/Marca | Salva un nuovo elemento.
*ModalitaPagamentoApi* | [**api_vversion_company_id_modalita_pagamento_distinct_get**](docs/ModalitaPagamentoApi.md#api_vversion_company_id_modalita_pagamento_distinct_get) | **GET** /api/v{version}/{companyId}/ModalitaPagamento/distinct | Restituisce una lista di elementi distinti.
*ModalitaPagamentoApi* | [**api_vversion_company_id_modalita_pagamento_get**](docs/ModalitaPagamentoApi.md#api_vversion_company_id_modalita_pagamento_get) | **GET** /api/v{version}/{companyId}/ModalitaPagamento | Restituisce una lista di elementi.
*ModalitaPagamentoApi* | [**api_vversion_company_id_modalita_pagamento_id_delete**](docs/ModalitaPagamentoApi.md#api_vversion_company_id_modalita_pagamento_id_delete) | **DELETE** /api/v{version}/{companyId}/ModalitaPagamento/{id} | Elimina un elemento.
*ModalitaPagamentoApi* | [**api_vversion_company_id_modalita_pagamento_id_get**](docs/ModalitaPagamentoApi.md#api_vversion_company_id_modalita_pagamento_id_get) | **GET** /api/v{version}/{companyId}/ModalitaPagamento/{id} | Restituisce un elemento.
*ModalitaPagamentoApi* | [**api_vversion_company_id_modalita_pagamento_id_put**](docs/ModalitaPagamentoApi.md#api_vversion_company_id_modalita_pagamento_id_put) | **PUT** /api/v{version}/{companyId}/ModalitaPagamento/{id} | Aggiorna un elemento esistente.
*ModalitaPagamentoApi* | [**api_vversion_company_id_modalita_pagamento_new_get**](docs/ModalitaPagamentoApi.md#api_vversion_company_id_modalita_pagamento_new_get) | **GET** /api/v{version}/{companyId}/ModalitaPagamento/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ModalitaPagamentoApi* | [**api_vversion_company_id_modalita_pagamento_post**](docs/ModalitaPagamentoApi.md#api_vversion_company_id_modalita_pagamento_post) | **POST** /api/v{version}/{companyId}/ModalitaPagamento | Salva un nuovo elemento.
*ModelloContabileApi* | [**api_vversion_company_id_modello_contabile_get**](docs/ModelloContabileApi.md#api_vversion_company_id_modello_contabile_get) | **GET** /api/v{version}/{companyId}/ModelloContabile | Restituisce una lista di elementi.
*ModelloContabileApi* | [**api_vversion_company_id_modello_contabile_id_delete**](docs/ModelloContabileApi.md#api_vversion_company_id_modello_contabile_id_delete) | **DELETE** /api/v{version}/{companyId}/ModelloContabile/{id} | Elimina un elemento.
*ModelloContabileApi* | [**api_vversion_company_id_modello_contabile_id_get**](docs/ModelloContabileApi.md#api_vversion_company_id_modello_contabile_id_get) | **GET** /api/v{version}/{companyId}/ModelloContabile/{id} | Restituisce un elemento.
*ModelloContabileApi* | [**api_vversion_company_id_modello_contabile_id_put**](docs/ModelloContabileApi.md#api_vversion_company_id_modello_contabile_id_put) | **PUT** /api/v{version}/{companyId}/ModelloContabile/{id} | Aggiorna un elemento esistente.
*ModelloContabileApi* | [**api_vversion_company_id_modello_contabile_new_get**](docs/ModelloContabileApi.md#api_vversion_company_id_modello_contabile_new_get) | **GET** /api/v{version}/{companyId}/ModelloContabile/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ModelloContabileApi* | [**api_vversion_company_id_modello_contabile_post**](docs/ModelloContabileApi.md#api_vversion_company_id_modello_contabile_post) | **POST** /api/v{version}/{companyId}/ModelloContabile | Salva un nuovo elemento.
*MovimentoMerceApi* | [**api_vversion_company_id_movimento_merce_get**](docs/MovimentoMerceApi.md#api_vversion_company_id_movimento_merce_get) | **GET** /api/v{version}/{companyId}/MovimentoMerce | Restituisce una lista di elementi.
*MovimentoMerceApi* | [**api_vversion_company_id_movimento_merce_id_delete**](docs/MovimentoMerceApi.md#api_vversion_company_id_movimento_merce_id_delete) | **DELETE** /api/v{version}/{companyId}/MovimentoMerce/{id} | Elimina un elemento.
*MovimentoMerceApi* | [**api_vversion_company_id_movimento_merce_id_get**](docs/MovimentoMerceApi.md#api_vversion_company_id_movimento_merce_id_get) | **GET** /api/v{version}/{companyId}/MovimentoMerce/{id} | Restituisce un elemento.
*MovimentoMerceApi* | [**api_vversion_company_id_movimento_merce_id_put**](docs/MovimentoMerceApi.md#api_vversion_company_id_movimento_merce_id_put) | **PUT** /api/v{version}/{companyId}/MovimentoMerce/{id} | Aggiorna un elemento esistente.
*MovimentoMerceApi* | [**api_vversion_company_id_movimento_merce_new_get**](docs/MovimentoMerceApi.md#api_vversion_company_id_movimento_merce_new_get) | **GET** /api/v{version}/{companyId}/MovimentoMerce/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*MovimentoMerceApi* | [**api_vversion_company_id_movimento_merce_post**](docs/MovimentoMerceApi.md#api_vversion_company_id_movimento_merce_post) | **POST** /api/v{version}/{companyId}/MovimentoMerce | Salva un nuovo elemento.
*NaturaIvaApi* | [**api_vversion_company_id_tabelle_natura_iva_get**](docs/NaturaIvaApi.md#api_vversion_company_id_tabelle_natura_iva_get) | **GET** /api/v{version}/{companyId}/tabelle/NaturaIva | Restituisce il contenuto della tabella come lista di elementi.
*NazioneApi* | [**api_vversion_company_id_nazione_distinct_get**](docs/NazioneApi.md#api_vversion_company_id_nazione_distinct_get) | **GET** /api/v{version}/{companyId}/Nazione/distinct | Restituisce una lista di elementi distinti.
*NazioneApi* | [**api_vversion_company_id_nazione_get**](docs/NazioneApi.md#api_vversion_company_id_nazione_get) | **GET** /api/v{version}/{companyId}/Nazione | Restituisce una lista di elementi.
*NazioneApi* | [**api_vversion_company_id_nazione_id_delete**](docs/NazioneApi.md#api_vversion_company_id_nazione_id_delete) | **DELETE** /api/v{version}/{companyId}/Nazione/{id} | Elimina un elemento.
*NazioneApi* | [**api_vversion_company_id_nazione_id_get**](docs/NazioneApi.md#api_vversion_company_id_nazione_id_get) | **GET** /api/v{version}/{companyId}/Nazione/{id} | Restituisce un elemento.
*NazioneApi* | [**api_vversion_company_id_nazione_id_put**](docs/NazioneApi.md#api_vversion_company_id_nazione_id_put) | **PUT** /api/v{version}/{companyId}/Nazione/{id} | Aggiorna un elemento esistente.
*NazioneApi* | [**api_vversion_company_id_nazione_new_get**](docs/NazioneApi.md#api_vversion_company_id_nazione_new_get) | **GET** /api/v{version}/{companyId}/Nazione/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*NazioneApi* | [**api_vversion_company_id_nazione_post**](docs/NazioneApi.md#api_vversion_company_id_nazione_post) | **POST** /api/v{version}/{companyId}/Nazione | Salva un nuovo elemento.
*PagamentoApi* | [**api_vversion_company_id_pagamento_distinct_get**](docs/PagamentoApi.md#api_vversion_company_id_pagamento_distinct_get) | **GET** /api/v{version}/{companyId}/Pagamento/distinct | Restituisce una lista di elementi distinti.
*PagamentoApi* | [**api_vversion_company_id_pagamento_get**](docs/PagamentoApi.md#api_vversion_company_id_pagamento_get) | **GET** /api/v{version}/{companyId}/Pagamento | Restituisce una lista di elementi.
*PagamentoApi* | [**api_vversion_company_id_pagamento_id_delete**](docs/PagamentoApi.md#api_vversion_company_id_pagamento_id_delete) | **DELETE** /api/v{version}/{companyId}/Pagamento/{id} | Elimina un elemento.
*PagamentoApi* | [**api_vversion_company_id_pagamento_id_get**](docs/PagamentoApi.md#api_vversion_company_id_pagamento_id_get) | **GET** /api/v{version}/{companyId}/Pagamento/{id} | Restituisce un elemento.
*PagamentoApi* | [**api_vversion_company_id_pagamento_id_put**](docs/PagamentoApi.md#api_vversion_company_id_pagamento_id_put) | **PUT** /api/v{version}/{companyId}/Pagamento/{id} | Aggiorna un elemento esistente.
*PagamentoApi* | [**api_vversion_company_id_pagamento_new_get**](docs/PagamentoApi.md#api_vversion_company_id_pagamento_new_get) | **GET** /api/v{version}/{companyId}/Pagamento/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*PagamentoApi* | [**api_vversion_company_id_pagamento_post**](docs/PagamentoApi.md#api_vversion_company_id_pagamento_post) | **POST** /api/v{version}/{companyId}/Pagamento | Salva un nuovo elemento.
*PreferenzeApi* | [**api_vversion_company_id_preferenze_get**](docs/PreferenzeApi.md#api_vversion_company_id_preferenze_get) | **GET** /api/v{version}/{companyId}/Preferenze | Restituisce una lista di elementi.
*PreferenzeApi* | [**api_vversion_company_id_preferenze_id_delete**](docs/PreferenzeApi.md#api_vversion_company_id_preferenze_id_delete) | **DELETE** /api/v{version}/{companyId}/Preferenze/{id} | Elimina un elemento.
*PreferenzeApi* | [**api_vversion_company_id_preferenze_id_get**](docs/PreferenzeApi.md#api_vversion_company_id_preferenze_id_get) | **GET** /api/v{version}/{companyId}/Preferenze/{id} | Restituisce un elemento.
*PreferenzeApi* | [**api_vversion_company_id_preferenze_id_put**](docs/PreferenzeApi.md#api_vversion_company_id_preferenze_id_put) | **PUT** /api/v{version}/{companyId}/Preferenze/{id} | Aggiorna un elemento esistente.
*PreferenzeApi* | [**api_vversion_company_id_preferenze_new_get**](docs/PreferenzeApi.md#api_vversion_company_id_preferenze_new_get) | **GET** /api/v{version}/{companyId}/Preferenze/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*PreferenzeApi* | [**api_vversion_company_id_preferenze_post**](docs/PreferenzeApi.md#api_vversion_company_id_preferenze_post) | **POST** /api/v{version}/{companyId}/Preferenze | Salva un nuovo elemento.
*PrestazioneApi* | [**api_vversion_company_id_prestazione_get**](docs/PrestazioneApi.md#api_vversion_company_id_prestazione_get) | **GET** /api/v{version}/{companyId}/Prestazione | Restituisce una lista di elementi.
*PrestazioneApi* | [**api_vversion_company_id_prestazione_id_delete**](docs/PrestazioneApi.md#api_vversion_company_id_prestazione_id_delete) | **DELETE** /api/v{version}/{companyId}/Prestazione/{id} | Elimina un elemento.
*PrestazioneApi* | [**api_vversion_company_id_prestazione_id_get**](docs/PrestazioneApi.md#api_vversion_company_id_prestazione_id_get) | **GET** /api/v{version}/{companyId}/Prestazione/{id} | Restituisce un elemento.
*PrestazioneApi* | [**api_vversion_company_id_prestazione_id_put**](docs/PrestazioneApi.md#api_vversion_company_id_prestazione_id_put) | **PUT** /api/v{version}/{companyId}/Prestazione/{id} | Aggiorna un elemento esistente.
*PrestazioneApi* | [**api_vversion_company_id_prestazione_new_get**](docs/PrestazioneApi.md#api_vversion_company_id_prestazione_new_get) | **GET** /api/v{version}/{companyId}/Prestazione/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*PrestazioneApi* | [**api_vversion_company_id_prestazione_post**](docs/PrestazioneApi.md#api_vversion_company_id_prestazione_post) | **POST** /api/v{version}/{companyId}/Prestazione | Salva un nuovo elemento.
*PrezzoApi* | [**api_vversion_company_id_prezzo_get**](docs/PrezzoApi.md#api_vversion_company_id_prezzo_get) | **GET** /api/v{version}/{companyId}/Prezzo | Restituisce una lista di elementi.
*PrezzoApi* | [**api_vversion_company_id_prezzo_id_delete**](docs/PrezzoApi.md#api_vversion_company_id_prezzo_id_delete) | **DELETE** /api/v{version}/{companyId}/Prezzo/{id} | Elimina un elemento.
*PrezzoApi* | [**api_vversion_company_id_prezzo_id_get**](docs/PrezzoApi.md#api_vversion_company_id_prezzo_id_get) | **GET** /api/v{version}/{companyId}/Prezzo/{id} | Restituisce un elemento.
*PrezzoApi* | [**api_vversion_company_id_prezzo_id_put**](docs/PrezzoApi.md#api_vversion_company_id_prezzo_id_put) | **PUT** /api/v{version}/{companyId}/Prezzo/{id} | Aggiorna un elemento esistente.
*PrezzoApi* | [**api_vversion_company_id_prezzo_new_get**](docs/PrezzoApi.md#api_vversion_company_id_prezzo_new_get) | **GET** /api/v{version}/{companyId}/Prezzo/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*PrezzoApi* | [**api_vversion_company_id_prezzo_post**](docs/PrezzoApi.md#api_vversion_company_id_prezzo_post) | **POST** /api/v{version}/{companyId}/Prezzo | Salva un nuovo elemento.
*ProduttoreApi* | [**api_vversion_company_id_produttore_get**](docs/ProduttoreApi.md#api_vversion_company_id_produttore_get) | **GET** /api/v{version}/{companyId}/Produttore | Restituisce una lista di elementi.
*ProduttoreApi* | [**api_vversion_company_id_produttore_id_delete**](docs/ProduttoreApi.md#api_vversion_company_id_produttore_id_delete) | **DELETE** /api/v{version}/{companyId}/Produttore/{id} | Elimina un elemento.
*ProduttoreApi* | [**api_vversion_company_id_produttore_id_get**](docs/ProduttoreApi.md#api_vversion_company_id_produttore_id_get) | **GET** /api/v{version}/{companyId}/Produttore/{id} | Restituisce un elemento.
*ProduttoreApi* | [**api_vversion_company_id_produttore_id_put**](docs/ProduttoreApi.md#api_vversion_company_id_produttore_id_put) | **PUT** /api/v{version}/{companyId}/Produttore/{id} | Aggiorna un elemento esistente.
*ProduttoreApi* | [**api_vversion_company_id_produttore_new_get**](docs/ProduttoreApi.md#api_vversion_company_id_produttore_new_get) | **GET** /api/v{version}/{companyId}/Produttore/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ProduttoreApi* | [**api_vversion_company_id_produttore_post**](docs/ProduttoreApi.md#api_vversion_company_id_produttore_post) | **POST** /api/v{version}/{companyId}/Produttore | Salva un nuovo elemento.
*ProgressivoInvioApi* | [**api_vversion_company_id_progressivo_invio_get**](docs/ProgressivoInvioApi.md#api_vversion_company_id_progressivo_invio_get) | **GET** /api/v{version}/{companyId}/ProgressivoInvio | Restituisce una lista di elementi.
*ProgressivoInvioApi* | [**api_vversion_company_id_progressivo_invio_id_delete**](docs/ProgressivoInvioApi.md#api_vversion_company_id_progressivo_invio_id_delete) | **DELETE** /api/v{version}/{companyId}/ProgressivoInvio/{id} | Elimina un elemento.
*ProgressivoInvioApi* | [**api_vversion_company_id_progressivo_invio_id_get**](docs/ProgressivoInvioApi.md#api_vversion_company_id_progressivo_invio_id_get) | **GET** /api/v{version}/{companyId}/ProgressivoInvio/{id} | Restituisce un elemento.
*ProgressivoInvioApi* | [**api_vversion_company_id_progressivo_invio_id_put**](docs/ProgressivoInvioApi.md#api_vversion_company_id_progressivo_invio_id_put) | **PUT** /api/v{version}/{companyId}/ProgressivoInvio/{id} | Aggiorna un elemento esistente.
*ProgressivoInvioApi* | [**api_vversion_company_id_progressivo_invio_new_get**](docs/ProgressivoInvioApi.md#api_vversion_company_id_progressivo_invio_new_get) | **GET** /api/v{version}/{companyId}/ProgressivoInvio/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ProgressivoInvioApi* | [**api_vversion_company_id_progressivo_invio_post**](docs/ProgressivoInvioApi.md#api_vversion_company_id_progressivo_invio_post) | **POST** /api/v{version}/{companyId}/ProgressivoInvio | Salva un nuovo elemento.
*RegistrazioneContabileApi* | [**api_vversion_company_id_registrazione_contabile_get**](docs/RegistrazioneContabileApi.md#api_vversion_company_id_registrazione_contabile_get) | **GET** /api/v{version}/{companyId}/RegistrazioneContabile | Restituisce una lista di elementi.
*RegistrazioneContabileApi* | [**api_vversion_company_id_registrazione_contabile_id_delete**](docs/RegistrazioneContabileApi.md#api_vversion_company_id_registrazione_contabile_id_delete) | **DELETE** /api/v{version}/{companyId}/RegistrazioneContabile/{id} | Elimina un elemento.
*RegistrazioneContabileApi* | [**api_vversion_company_id_registrazione_contabile_id_get**](docs/RegistrazioneContabileApi.md#api_vversion_company_id_registrazione_contabile_id_get) | **GET** /api/v{version}/{companyId}/RegistrazioneContabile/{id} | Restituisce un elemento.
*RegistrazioneContabileApi* | [**api_vversion_company_id_registrazione_contabile_id_put**](docs/RegistrazioneContabileApi.md#api_vversion_company_id_registrazione_contabile_id_put) | **PUT** /api/v{version}/{companyId}/RegistrazioneContabile/{id} | Aggiorna un elemento esistente.
*RegistrazioneContabileApi* | [**api_vversion_company_id_registrazione_contabile_new_get**](docs/RegistrazioneContabileApi.md#api_vversion_company_id_registrazione_contabile_new_get) | **GET** /api/v{version}/{companyId}/RegistrazioneContabile/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*RegistrazioneContabileApi* | [**api_vversion_company_id_registrazione_contabile_post**](docs/RegistrazioneContabileApi.md#api_vversion_company_id_registrazione_contabile_post) | **POST** /api/v{version}/{companyId}/RegistrazioneContabile | Salva un nuovo elemento.
*RegistrazioneContabileApi* | [**api_vversion_company_id_registrazione_contabile_validate_post**](docs/RegistrazioneContabileApi.md#api_vversion_company_id_registrazione_contabile_validate_post) | **POST** /api/v{version}/{companyId}/RegistrazioneContabile/validate | Valida le registrazioni contabili di un anno, cercando principalmente squilibri contabili.
*RepartoApi* | [**api_vversion_company_id_reparto_get**](docs/RepartoApi.md#api_vversion_company_id_reparto_get) | **GET** /api/v{version}/{companyId}/Reparto | Restituisce una lista di elementi.
*RepartoApi* | [**api_vversion_company_id_reparto_id_delete**](docs/RepartoApi.md#api_vversion_company_id_reparto_id_delete) | **DELETE** /api/v{version}/{companyId}/Reparto/{id} | Elimina un elemento.
*RepartoApi* | [**api_vversion_company_id_reparto_id_get**](docs/RepartoApi.md#api_vversion_company_id_reparto_id_get) | **GET** /api/v{version}/{companyId}/Reparto/{id} | Restituisce un elemento.
*RepartoApi* | [**api_vversion_company_id_reparto_id_put**](docs/RepartoApi.md#api_vversion_company_id_reparto_id_put) | **PUT** /api/v{version}/{companyId}/Reparto/{id} | Aggiorna un elemento esistente.
*RepartoApi* | [**api_vversion_company_id_reparto_new_get**](docs/RepartoApi.md#api_vversion_company_id_reparto_new_get) | **GET** /api/v{version}/{companyId}/Reparto/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*RepartoApi* | [**api_vversion_company_id_reparto_post**](docs/RepartoApi.md#api_vversion_company_id_reparto_post) | **POST** /api/v{version}/{companyId}/Reparto | Salva un nuovo elemento.
*RisorsaFinanziariaApi* | [**api_vversion_company_id_risorsa_finanziaria_get**](docs/RisorsaFinanziariaApi.md#api_vversion_company_id_risorsa_finanziaria_get) | **GET** /api/v{version}/{companyId}/RisorsaFinanziaria | Restituisce una lista di elementi.
*RisorsaFinanziariaApi* | [**api_vversion_company_id_risorsa_finanziaria_id_delete**](docs/RisorsaFinanziariaApi.md#api_vversion_company_id_risorsa_finanziaria_id_delete) | **DELETE** /api/v{version}/{companyId}/RisorsaFinanziaria/{id} | Elimina un elemento.
*RisorsaFinanziariaApi* | [**api_vversion_company_id_risorsa_finanziaria_id_get**](docs/RisorsaFinanziariaApi.md#api_vversion_company_id_risorsa_finanziaria_id_get) | **GET** /api/v{version}/{companyId}/RisorsaFinanziaria/{id} | Restituisce un elemento.
*RisorsaFinanziariaApi* | [**api_vversion_company_id_risorsa_finanziaria_id_put**](docs/RisorsaFinanziariaApi.md#api_vversion_company_id_risorsa_finanziaria_id_put) | **PUT** /api/v{version}/{companyId}/RisorsaFinanziaria/{id} | Aggiorna un elemento esistente.
*RisorsaFinanziariaApi* | [**api_vversion_company_id_risorsa_finanziaria_new_get**](docs/RisorsaFinanziariaApi.md#api_vversion_company_id_risorsa_finanziaria_new_get) | **GET** /api/v{version}/{companyId}/RisorsaFinanziaria/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*RisorsaFinanziariaApi* | [**api_vversion_company_id_risorsa_finanziaria_post**](docs/RisorsaFinanziariaApi.md#api_vversion_company_id_risorsa_finanziaria_post) | **POST** /api/v{version}/{companyId}/RisorsaFinanziaria | Salva un nuovo elemento.
*ScadenzaApi* | [**api_vversion_company_id_scadenza_distinct_get**](docs/ScadenzaApi.md#api_vversion_company_id_scadenza_distinct_get) | **GET** /api/v{version}/{companyId}/Scadenza/distinct | Restituisce una lista di elementi distinti.
*ScadenzaApi* | [**api_vversion_company_id_scadenza_get**](docs/ScadenzaApi.md#api_vversion_company_id_scadenza_get) | **GET** /api/v{version}/{companyId}/Scadenza | Restituisce una lista di elementi.
*ScadenzaApi* | [**api_vversion_company_id_scadenza_id_delete**](docs/ScadenzaApi.md#api_vversion_company_id_scadenza_id_delete) | **DELETE** /api/v{version}/{companyId}/Scadenza/{id} | Elimina un elemento.
*ScadenzaApi* | [**api_vversion_company_id_scadenza_id_get**](docs/ScadenzaApi.md#api_vversion_company_id_scadenza_id_get) | **GET** /api/v{version}/{companyId}/Scadenza/{id} | Restituisce un elemento.
*ScadenzaApi* | [**api_vversion_company_id_scadenza_id_put**](docs/ScadenzaApi.md#api_vversion_company_id_scadenza_id_put) | **PUT** /api/v{version}/{companyId}/Scadenza/{id} | Aggiorna un elemento esistente.
*ScadenzaApi* | [**api_vversion_company_id_scadenza_new_get**](docs/ScadenzaApi.md#api_vversion_company_id_scadenza_new_get) | **GET** /api/v{version}/{companyId}/Scadenza/new | Restituisce una nuova istanza di una scadenza del tipo specificato.
*ScadenzaApi* | [**api_vversion_company_id_scadenza_post**](docs/ScadenzaApi.md#api_vversion_company_id_scadenza_post) | **POST** /api/v{version}/{companyId}/Scadenza | Salva un nuovo elemento.
*SituazioneApi* | [**api_vversion_company_id_situazione_creditodebitomensile_get**](docs/SituazioneApi.md#api_vversion_company_id_situazione_creditodebitomensile_get) | **GET** /api/v{version}/{companyId}/Situazione/creditodebitomensile | Restituisce i saldi mensili di credito e debito dell&#39;azienda.
*SituazioneApi* | [**api_vversion_company_id_situazione_fatturatomensile_get**](docs/SituazioneApi.md#api_vversion_company_id_situazione_fatturatomensile_get) | **GET** /api/v{version}/{companyId}/Situazione/fatturatomensile | Restituisce il fatturato mensile dell&#39;azienda.
*SpesaApi* | [**api_vversion_company_id_spesa_distinct_get**](docs/SpesaApi.md#api_vversion_company_id_spesa_distinct_get) | **GET** /api/v{version}/{companyId}/Spesa/distinct | Restituisce una lista di elementi distinti.
*SpesaApi* | [**api_vversion_company_id_spesa_get**](docs/SpesaApi.md#api_vversion_company_id_spesa_get) | **GET** /api/v{version}/{companyId}/Spesa | Restituisce una lista di elementi.
*SpesaApi* | [**api_vversion_company_id_spesa_id_delete**](docs/SpesaApi.md#api_vversion_company_id_spesa_id_delete) | **DELETE** /api/v{version}/{companyId}/Spesa/{id} | Elimina un elemento.
*SpesaApi* | [**api_vversion_company_id_spesa_id_get**](docs/SpesaApi.md#api_vversion_company_id_spesa_id_get) | **GET** /api/v{version}/{companyId}/Spesa/{id} | Restituisce un elemento.
*SpesaApi* | [**api_vversion_company_id_spesa_id_put**](docs/SpesaApi.md#api_vversion_company_id_spesa_id_put) | **PUT** /api/v{version}/{companyId}/Spesa/{id} | Aggiorna un elemento esistente.
*SpesaApi* | [**api_vversion_company_id_spesa_new_get**](docs/SpesaApi.md#api_vversion_company_id_spesa_new_get) | **GET** /api/v{version}/{companyId}/Spesa/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*SpesaApi* | [**api_vversion_company_id_spesa_post**](docs/SpesaApi.md#api_vversion_company_id_spesa_post) | **POST** /api/v{version}/{companyId}/Spesa | Salva un nuovo elemento.
*SpesaDocumentoApi* | [**api_vversion_company_id_spesa_documento_get**](docs/SpesaDocumentoApi.md#api_vversion_company_id_spesa_documento_get) | **GET** /api/v{version}/{companyId}/SpesaDocumento | Restituisce una lista di elementi.
*SpesaDocumentoApi* | [**api_vversion_company_id_spesa_documento_id_delete**](docs/SpesaDocumentoApi.md#api_vversion_company_id_spesa_documento_id_delete) | **DELETE** /api/v{version}/{companyId}/SpesaDocumento/{id} | Elimina un elemento.
*SpesaDocumentoApi* | [**api_vversion_company_id_spesa_documento_id_get**](docs/SpesaDocumentoApi.md#api_vversion_company_id_spesa_documento_id_get) | **GET** /api/v{version}/{companyId}/SpesaDocumento/{id} | Restituisce un elemento.
*SpesaDocumentoApi* | [**api_vversion_company_id_spesa_documento_id_put**](docs/SpesaDocumentoApi.md#api_vversion_company_id_spesa_documento_id_put) | **PUT** /api/v{version}/{companyId}/SpesaDocumento/{id} | Aggiorna un elemento esistente.
*SpesaDocumentoApi* | [**api_vversion_company_id_spesa_documento_new_get**](docs/SpesaDocumentoApi.md#api_vversion_company_id_spesa_documento_new_get) | **GET** /api/v{version}/{companyId}/SpesaDocumento/new | Restituisce una nuova istanza di una spesa documento.
*SpesaDocumentoApi* | [**api_vversion_company_id_spesa_documento_post**](docs/SpesaDocumentoApi.md#api_vversion_company_id_spesa_documento_post) | **POST** /api/v{version}/{companyId}/SpesaDocumento | Salva un nuovo elemento.
*TagliaApi* | [**api_vversion_company_id_taglia_get**](docs/TagliaApi.md#api_vversion_company_id_taglia_get) | **GET** /api/v{version}/{companyId}/Taglia | Restituisce una lista di elementi.
*TagliaApi* | [**api_vversion_company_id_taglia_id_delete**](docs/TagliaApi.md#api_vversion_company_id_taglia_id_delete) | **DELETE** /api/v{version}/{companyId}/Taglia/{id} | Elimina un elemento.
*TagliaApi* | [**api_vversion_company_id_taglia_id_get**](docs/TagliaApi.md#api_vversion_company_id_taglia_id_get) | **GET** /api/v{version}/{companyId}/Taglia/{id} | Restituisce un elemento.
*TagliaApi* | [**api_vversion_company_id_taglia_id_put**](docs/TagliaApi.md#api_vversion_company_id_taglia_id_put) | **PUT** /api/v{version}/{companyId}/Taglia/{id} | Aggiorna un elemento esistente.
*TagliaApi* | [**api_vversion_company_id_taglia_new_get**](docs/TagliaApi.md#api_vversion_company_id_taglia_new_get) | **GET** /api/v{version}/{companyId}/Taglia/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*TagliaApi* | [**api_vversion_company_id_taglia_post**](docs/TagliaApi.md#api_vversion_company_id_taglia_post) | **POST** /api/v{version}/{companyId}/Taglia | Salva un nuovo elemento.
*ValutaApi* | [**api_vversion_company_id_valuta_get**](docs/ValutaApi.md#api_vversion_company_id_valuta_get) | **GET** /api/v{version}/{companyId}/Valuta | Restituisce una lista di elementi.
*ValutaApi* | [**api_vversion_company_id_valuta_id_delete**](docs/ValutaApi.md#api_vversion_company_id_valuta_id_delete) | **DELETE** /api/v{version}/{companyId}/Valuta/{id} | Elimina un elemento.
*ValutaApi* | [**api_vversion_company_id_valuta_id_get**](docs/ValutaApi.md#api_vversion_company_id_valuta_id_get) | **GET** /api/v{version}/{companyId}/Valuta/{id} | Restituisce un elemento.
*ValutaApi* | [**api_vversion_company_id_valuta_id_put**](docs/ValutaApi.md#api_vversion_company_id_valuta_id_put) | **PUT** /api/v{version}/{companyId}/Valuta/{id} | Aggiorna un elemento esistente.
*ValutaApi* | [**api_vversion_company_id_valuta_new_get**](docs/ValutaApi.md#api_vversion_company_id_valuta_new_get) | **GET** /api/v{version}/{companyId}/Valuta/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*ValutaApi* | [**api_vversion_company_id_valuta_post**](docs/ValutaApi.md#api_vversion_company_id_valuta_post) | **POST** /api/v{version}/{companyId}/Valuta | Salva un nuovo elemento.
*WebHookApi* | [**api_vversion_company_id_web_hook_get**](docs/WebHookApi.md#api_vversion_company_id_web_hook_get) | **GET** /api/v{version}/{companyId}/WebHook | Restituisce una lista di Amica.WebHook.
*WebHookApi* | [**api_vversion_company_id_web_hook_id_delete**](docs/WebHookApi.md#api_vversion_company_id_web_hook_id_delete) | **DELETE** /api/v{version}/{companyId}/WebHook/{id} | 
*WebHookApi* | [**api_vversion_company_id_web_hook_id_get**](docs/WebHookApi.md#api_vversion_company_id_web_hook_id_get) | **GET** /api/v{version}/{companyId}/WebHook/{id} | Restituisce un Amica.WebHook.
*WebHookApi* | [**api_vversion_company_id_web_hook_id_put**](docs/WebHookApi.md#api_vversion_company_id_web_hook_id_put) | **PUT** /api/v{version}/{companyId}/WebHook/{id} | Aggiorna un Amica.WebHook.
*WebHookApi* | [**api_vversion_company_id_web_hook_new_get**](docs/WebHookApi.md#api_vversion_company_id_web_hook_new_get) | **GET** /api/v{version}/{companyId}/WebHook/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
*WebHookApi* | [**api_vversion_company_id_web_hook_post**](docs/WebHookApi.md#api_vversion_company_id_web_hook_post) | **POST** /api/v{version}/{companyId}/WebHook | 


## Documentation For Models

 - [AllegatoDocumento](docs/AllegatoDocumento.md)
 - [Anagrafica](docs/Anagrafica.md)
 - [AnagraficaNominativo1](docs/AnagraficaNominativo1.md)
 - [AnagraficaNominativo2](docs/AnagraficaNominativo2.md)
 - [AnagraficaSedeLegale](docs/AnagraficaSedeLegale.md)
 - [AreaGeografica](docs/AreaGeografica.md)
 - [Articolo](docs/Articolo.md)
 - [ArticoloMediaFile](docs/ArticoloMediaFile.md)
 - [Azienda](docs/Azienda.md)
 - [Banca](docs/Banca.md)
 - [BancaDocumento](docs/BancaDocumento.md)
 - [BeneServizio](docs/BeneServizio.md)
 - [BeneServizioComputeData](docs/BeneServizioComputeData.md)
 - [BeneServizioComputeResult](docs/BeneServizioComputeResult.md)
 - [CassaPrevidenziale](docs/CassaPrevidenziale.md)
 - [CastellettoIva](docs/CastellettoIva.md)
 - [CategoriaAnagrafica](docs/CategoriaAnagrafica.md)
 - [CategoriaMerceologica](docs/CategoriaMerceologica.md)
 - [CausaleDocumento](docs/CausaleDocumento.md)
 - [CausaleIva](docs/CausaleIva.md)
 - [CausaleMagazzino](docs/CausaleMagazzino.md)
 - [CodicePagamento](docs/CodicePagamento.md)
 - [CollegaDocumentoData](docs/CollegaDocumentoData.md)
 - [Componente](docs/Componente.md)
 - [ContoContabile](docs/ContoContabile.md)
 - [ContoContabileValidationResult](docs/ContoContabileValidationResult.md)
 - [CreditoDebitoMensile](docs/CreditoDebitoMensile.md)
 - [DatiAggiuntivi](docs/DatiAggiuntivi.md)
 - [DatiPA](docs/DatiPA.md)
 - [DatiSdi](docs/DatiSdi.md)
 - [DatiTrasporto](docs/DatiTrasporto.md)
 - [DdtImportData](docs/DdtImportData.md)
 - [DistinctPropertyGroup](docs/DistinctPropertyGroup.md)
 - [Documento](docs/Documento.md)
 - [DocumentoCollegato](docs/DocumentoCollegato.md)
 - [DocumentoComputeData](docs/DocumentoComputeData.md)
 - [DocumentoComputeDataBeneServizio](docs/DocumentoComputeDataBeneServizio.md)
 - [DocumentoComputeDataSpesa](docs/DocumentoComputeDataSpesa.md)
 - [DocumentoComputeResult](docs/DocumentoComputeResult.md)
 - [DocumentoComputeResultRiepilogoIva](docs/DocumentoComputeResultRiepilogoIva.md)
 - [DocumentoImportData](docs/DocumentoImportData.md)
 - [DocumentoMediaFile](docs/DocumentoMediaFile.md)
 - [Evento](docs/Evento.md)
 - [FatturaElettronicaExportOptions](docs/FatturaElettronicaExportOptions.md)
 - [FatturaElettronicaExportResult](docs/FatturaElettronicaExportResult.md)
 - [FatturaElettronicaImportResult](docs/FatturaElettronicaImportResult.md)
 - [FatturaElettronicaUploadOptions](docs/FatturaElettronicaUploadOptions.md)
 - [FatturaElettronicaUploadResult](docs/FatturaElettronicaUploadResult.md)
 - [FatturaElettronicaXml](docs/FatturaElettronicaXml.md)
 - [FatturaElettronicaXmlGetArchiveByDateRangeOptions](docs/FatturaElettronicaXmlGetArchiveByDateRangeOptions.md)
 - [FatturaElettronicaXmlGetArchiveByFileNameOptions](docs/FatturaElettronicaXmlGetArchiveByFileNameOptions.md)
 - [FatturaElettronicaXmlStyleSheetData](docs/FatturaElettronicaXmlStyleSheetData.md)
 - [FatturaElettronicaXmlTemplate](docs/FatturaElettronicaXmlTemplate.md)
 - [FatturatoMensile](docs/FatturatoMensile.md)
 - [Giacenza](docs/Giacenza.md)
 - [GruppoMerceologico](docs/GruppoMerceologico.md)
 - [ImpostazioniSdi](docs/ImpostazioniSdi.md)
 - [Indirizzo](docs/Indirizzo.md)
 - [Listino](docs/Listino.md)
 - [Magazzino](docs/Magazzino.md)
 - [Marca](docs/Marca.md)
 - [ModalitaPagamento](docs/ModalitaPagamento.md)
 - [ModelloContabile](docs/ModelloContabile.md)
 - [ModelloContabileRiga](docs/ModelloContabileRiga.md)
 - [MovimentoMerce](docs/MovimentoMerce.md)
 - [MovimentoMerceRiga](docs/MovimentoMerceRiga.md)
 - [NaturaIva](docs/NaturaIva.md)
 - [Nazione](docs/Nazione.md)
 - [OrdiniImportData](docs/OrdiniImportData.md)
 - [Pagamento](docs/Pagamento.md)
 - [PeriodicInvoicingData](docs/PeriodicInvoicingData.md)
 - [Preferenze](docs/Preferenze.md)
 - [Prestazione](docs/Prestazione.md)
 - [Prezzo](docs/Prezzo.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [Produttore](docs/Produttore.md)
 - [ProgressivoInvio](docs/ProgressivoInvio.md)
 - [RegistrazioneContabile](docs/RegistrazioneContabile.md)
 - [RegistrazioneContabileRiga](docs/RegistrazioneContabileRiga.md)
 - [RegistrazioneContabileValidationResult](docs/RegistrazioneContabileValidationResult.md)
 - [Reparto](docs/Reparto.md)
 - [ResoImportData](docs/ResoImportData.md)
 - [RicercaArticolo](docs/RicercaArticolo.md)
 - [RisorsaFinanziaria](docs/RisorsaFinanziaria.md)
 - [Scadenza](docs/Scadenza.md)
 - [SchedaCliente](docs/SchedaCliente.md)
 - [SchedaFornitore](docs/SchedaFornitore.md)
 - [SedeAltra](docs/SedeAltra.md)
 - [SedeLegale](docs/SedeLegale.md)
 - [SedeOperativa](docs/SedeOperativa.md)
 - [Spesa](docs/Spesa.md)
 - [SpesaDocumento](docs/SpesaDocumento.md)
 - [Taglia](docs/Taglia.md)
 - [Valuta](docs/Valuta.md)
 - [WebHook](docs/WebHook.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="oauth2"></a>
### oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **read**: Accesso in lettura alle risorse
 - **write**: Accesso in scrittura alle risorse
 - **comune**: Anagrafiche e tabelle di base comuni
 - **magazzino**: Articoli, listini, giacenze e movimenti di magazzino
 - **documenti**: Documenti commerciali (ordini, DDT, preventivi, ...)
 - **contabilita**: Contabilità, fatture elettroniche, pagamenti e scadenze

<a id="oauth2"></a>
### oauth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://auth.amica20.it/connect/authorize
- **Scopes**: 
 - **read**: Accesso in lettura alle risorse
 - **write**: Accesso in scrittura alle risorse
 - **comune**: Anagrafiche e tabelle di base comuni
 - **magazzino**: Articoli, listini, giacenze e movimenti di magazzino
 - **documenti**: Documenti commerciali (ordini, DDT, preventivi, ...)
 - **contabilita**: Contabilità, fatture elettroniche, pagamenti e scadenze

<a id="bearer"></a>
### bearer

- **Type**: Bearer authentication (JWT)


## Author

assistenza@gestionaleamica.com


