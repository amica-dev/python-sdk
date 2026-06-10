# amica_sdk.DocumentoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_vversion_company_id_documento_compute_post**](DocumentoApi.md#api_vversion_company_id_documento_compute_post) | **POST** /api/v{version}/{companyId}/Documento/compute | Calcola i totali di un documento.
[**api_vversion_company_id_documento_distinct_get**](DocumentoApi.md#api_vversion_company_id_documento_distinct_get) | **GET** /api/v{version}/{companyId}/Documento/distinct | Restituisce una lista di elementi distinti.
[**api_vversion_company_id_documento_documento_id_emit_post**](DocumentoApi.md#api_vversion_company_id_documento_documento_id_emit_post) | **POST** /api/v{version}/{companyId}/Documento/{documentoId}/emit | Emette un documento.
[**api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post**](DocumentoApi.md#api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post) | **POST** /api/v{version}/{companyId}/Documento/{documentoId}/newinstancefromtemplate | Replica un documento. Crea una copia con la data odierna e, se è un documento di vendita, un nuovo numero. Alcuni campi vengono reimpostati ai valori predefiniti (stato del documento, stato SDI, stato del pagamento, ecc.).
[**api_vversion_company_id_documento_get**](DocumentoApi.md#api_vversion_company_id_documento_get) | **GET** /api/v{version}/{companyId}/Documento | Restituisce una lista di elementi.
[**api_vversion_company_id_documento_id_delete**](DocumentoApi.md#api_vversion_company_id_documento_id_delete) | **DELETE** /api/v{version}/{companyId}/Documento/{id} | Elimina un elemento.
[**api_vversion_company_id_documento_id_get**](DocumentoApi.md#api_vversion_company_id_documento_id_get) | **GET** /api/v{version}/{companyId}/Documento/{id} | Restituisce un elemento.
[**api_vversion_company_id_documento_id_import_acconto_post**](DocumentoApi.md#api_vversion_company_id_documento_id_import_acconto_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/acconto | Importa righe da uno o più acconti in un documento esistente.
[**api_vversion_company_id_documento_id_import_ddt_post**](DocumentoApi.md#api_vversion_company_id_documento_id_import_ddt_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/ddt | Importa righe da uno o più DDT in un documento esistente.
[**api_vversion_company_id_documento_id_import_ordine_post**](DocumentoApi.md#api_vversion_company_id_documento_id_import_ordine_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/ordine | Importa righe da uno o più ordini in un documento esistente.
[**api_vversion_company_id_documento_id_import_preventivo_post**](DocumentoApi.md#api_vversion_company_id_documento_id_import_preventivo_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/preventivo | Importa righe da uno o più preventivi in un documento esistente.
[**api_vversion_company_id_documento_id_import_proforma_post**](DocumentoApi.md#api_vversion_company_id_documento_id_import_proforma_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/proforma | Importa righe da una o più fatture proforma in un documento esistente.
[**api_vversion_company_id_documento_id_import_reso_post**](DocumentoApi.md#api_vversion_company_id_documento_id_import_reso_post) | **POST** /api/v{version}/{companyId}/Documento/{id}/import/reso | Importa righe da uno o più resi in un documento esistente.
[**api_vversion_company_id_documento_id_put**](DocumentoApi.md#api_vversion_company_id_documento_id_put) | **PUT** /api/v{version}/{companyId}/Documento/{id} | Aggiorna un elemento esistente.
[**api_vversion_company_id_documento_new_get**](DocumentoApi.md#api_vversion_company_id_documento_new_get) | **GET** /api/v{version}/{companyId}/Documento/new | Restituisce una nuova istanza di un documento del tipo specificato.
[**api_vversion_company_id_documento_periodicinvoicing_post**](DocumentoApi.md#api_vversion_company_id_documento_periodicinvoicing_post) | **POST** /api/v{version}/{companyId}/Documento/periodicinvoicing | Genera fatture per tutti i contatti che corrispondono ai criteri di fatturazione periodica.
[**api_vversion_company_id_documento_post**](DocumentoApi.md#api_vversion_company_id_documento_post) | **POST** /api/v{version}/{companyId}/Documento | Salva un nuovo elemento.


# **api_vversion_company_id_documento_compute_post**
> DocumentoComputeResult api_vversion_company_id_documento_compute_post(version, company_id, documento_compute_data=documento_compute_data)

Calcola i totali di un documento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento_compute_data import DocumentoComputeData
from amica_sdk.models.documento_compute_result import DocumentoComputeResult
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    documento_compute_data = amica_sdk.DocumentoComputeData() # DocumentoComputeData | Dati di input per l'operazione di calcolo. (optional)

    try:
        # Calcola i totali di un documento.
        api_response = api_instance.api_vversion_company_id_documento_compute_post(version, company_id, documento_compute_data=documento_compute_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_compute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_compute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **documento_compute_data** | [**DocumentoComputeData**](DocumentoComputeData.md)| Dati di input per l&#39;operazione di calcolo. | [optional] 

### Return type

[**DocumentoComputeResult**](DocumentoComputeResult.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il risultato del calcolo. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore (di solito un problema di validazione). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_distinct_get**
> List[DistinctPropertyGroup] api_vversion_company_id_documento_distinct_get(version, company_id, selector, skip=skip, take=take)

Restituisce una lista di elementi distinti.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.distinct_property_group import DistinctPropertyGroup
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    selector = 'RagioneSociale1' # str | Il campo usato per distinguere gli elementi.
    skip = 100 # int | Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione. (optional)
    take = 25 # int | Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione. (optional)

    try:
        # Restituisce una lista di elementi distinti.
        api_response = api_instance.api_vversion_company_id_documento_distinct_get(version, company_id, selector, skip=skip, take=take)
        print("The response of DocumentoApi->api_vversion_company_id_documento_distinct_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_distinct_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **selector** | **str**| Il campo usato per distinguere gli elementi. | 
 **skip** | **int**| Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con &#x60;Take&#x60;, è utile per la paginazione. | [optional] 
 **take** | **int**| Numero di elementi da includere nel risultato. Combinato con &#x60;Skip&#x60;, è utile per la paginazione. | [optional] 

### Return type

[**List[DistinctPropertyGroup]**](DistinctPropertyGroup.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce la lista degli elementi distinti. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_documento_id_emit_post**
> Documento api_vversion_company_id_documento_documento_id_emit_post(version, company_id, documento_id)

Emette un documento.

A seconda del tipo di documento, l'emissione comporta una serie di operazioni amministrative e contabili:               1) Aggiornamento dell'Amica.Anagrafica coinvolta (fatturato, numero fatture, ecc.);              2) Creazione della registrazione contabile di emissione;              3) Creazione delle scadenze attive o passive, in base al tipo di pagamento;              4) Eventuale autoproduzione dei beni fatturati tramite distinta base, se l'opzione è attiva;              5) Creazione del movimento di magazzino;              6) Aggiornamento delle giacenze dei beni coinvolti, nei rispettivi magazzini;              7) Aggiornamento di eventuali ordini collegati.               Un documento già emesso non può essere riemesso. Alcuni tipi di documento non supportano l'emissione (ordini e preventivi, ad esempio).

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    documento_id = 56 # int | ID univoco del documento da emettere.

    try:
        # Emette un documento.
        api_response = api_instance.api_vversion_company_id_documento_documento_id_emit_post(version, company_id, documento_id)
        print("The response of DocumentoApi->api_vversion_company_id_documento_documento_id_emit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_documento_id_emit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **documento_id** | **int**| ID univoco del documento da emettere. | 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il documento aggiornato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore (di solito un problema di validazione). |  -  |
**404** | Non trovato. L&#39;elemento non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post**
> Documento api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post(version, documento_id, company_id)

Replica un documento. Crea una copia con la data odierna e, se è un documento di vendita, un nuovo numero. Alcuni campi vengono reimpostati ai valori predefiniti (stato del documento, stato SDI, stato del pagamento, ecc.).

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    documento_id = 56 # int | ID univoco del documento.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.

    try:
        # Replica un documento. Crea una copia con la data odierna e, se è un documento di vendita, un nuovo numero. Alcuni campi vengono reimpostati ai valori predefiniti (stato del documento, stato SDI, stato del pagamento, ecc.).
        api_response = api_instance.api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post(version, documento_id, company_id)
        print("The response of DocumentoApi->api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_documento_id_newinstancefromtemplate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **documento_id** | **int**| ID univoco del documento. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_get**
> List[Documento] api_vversion_company_id_documento_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)

Restituisce una lista di elementi.

 La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    skip = 100 # int | Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione. (optional)
    take = 25 # int | Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione. (optional)
    skip_total_count = True # bool | Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`. (optional)
    filter = 'field1 $eq hello $or, field2 $gt 10' # str | Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`. (optional)
    order = '-field1,field2' # str | Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`. (optional)
    expand = ['Rows'] # List[str] | Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata. (optional)

    try:
        # Restituisce una lista di elementi.
        api_response = api_instance.api_vversion_company_id_documento_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)
        print("The response of DocumentoApi->api_vversion_company_id_documento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **skip** | **int**| Numero di elementi da escludere dall&#39;inizio del risultato. Combinato con &#x60;Take&#x60;, è utile per la paginazione. | [optional] 
 **take** | **int**| Numero di elementi da includere nel risultato. Combinato con &#x60;Skip&#x60;, è utile per la paginazione. | [optional] 
 **skip_total_count** | **bool**| Indica se l&#39;header &#x60;X-Read-TotalCount&#x60; debba essere escluso dalla risposta. Impostare a &#x60;true&#x60; per prestazioni migliori a scapito dell&#39;accuratezza. Il valore predefinito è &#x60;false&#x60;. | [optional] 
 **filter** | **str**| Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: &#x60;$eq&#x60; (uguale), &#x60;$ne&#x60; (diverso), &#x60;$gt&#x60; (maggiore di), &#x60;$lt&#x60; (minore di), &#x60;$lte&#x60; (minore o uguale), &#x60;$gte&#x60; (maggiore o uguale), &#x60;$ct&#x60; (contiene), &#x60;$nct&#x60; (non contiene), &#x60;$sw&#x60; (inizia con), &#x60;$ew&#x60; (finisce con). Più espressioni possono essere concatenate con un connettore logico &#x60;$and&#x60; o &#x60;$or&#x60; (&#x60;$and&#x60; può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (&#x60;[]&#x60;). Nell&#39;esempio vengono inclusi tutti gli elementi con &#x60;field1&#x3D;\&quot;hello\&quot;&#x60; oppure &#x60;field2&gt;10&#x60;. | [optional] 
 **order** | **str**| Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell&#39;esempio i risultati sono ordinati prima per &#x60;field1&#x60; (discendente), poi per &#x60;field2&#x60;. | [optional] 
 **expand** | [**List[str]**](str.md)| Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un&#39;unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge &#x60;expand&#x3D;Rows&#x60; alla chiamata. | [optional] 

### Return type

[**List[Documento]**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce la lista degli elementi corrispondenti ai criteri di ricerca. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_delete**
> Documento api_vversion_company_id_documento_id_delete(version, company_id, id)

Elimina un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da eliminare.

    try:
        # Elimina un elemento.
        api_response = api_instance.api_vversion_company_id_documento_id_delete(version, company_id, id)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da eliminare. | 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;elemento eliminato. |  -  |
**404** | Non trovato. L&#39;elemento non è stato trovato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_get**
> Documento api_vversion_company_id_documento_id_get(version, company_id, id, expand=expand)

Restituisce un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da recuperare.
    expand = ['Rows'] # List[str] | Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata. (optional)

    try:
        # Restituisce un elemento.
        api_response = api_instance.api_vversion_company_id_documento_id_get(version, company_id, id, expand=expand)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da recuperare. | 
 **expand** | [**List[str]**](str.md)| Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un&#39;unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge &#x60;expand&#x3D;Rows&#x60; alla chiamata. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;elemento richiesto. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. L&#39;elemento non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_import_acconto_post**
> Documento api_vversion_company_id_documento_id_import_acconto_post(version, company_id, id, validation_override=validation_override, documento_import_data=documento_import_data)

Importa righe da uno o più acconti in un documento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
from amica_sdk.models.documento_import_data import DocumentoImportData
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del documento di destinazione.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    documento_import_data = amica_sdk.DocumentoImportData() # DocumentoImportData | Opzioni di importazione, inclusi gli ID degli acconti da importare. (optional)

    try:
        # Importa righe da uno o più acconti in un documento esistente.
        api_response = api_instance.api_vversion_company_id_documento_id_import_acconto_post(version, company_id, id, validation_override=validation_override, documento_import_data=documento_import_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_import_acconto_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_import_acconto_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del documento di destinazione. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **documento_import_data** | [**DocumentoImportData**](DocumentoImportData.md)| Opzioni di importazione, inclusi gli ID degli acconti da importare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il documento aggiornato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. Il documento di destinazione non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_import_ddt_post**
> Documento api_vversion_company_id_documento_id_import_ddt_post(version, company_id, id, validation_override=validation_override, ddt_import_data=ddt_import_data)

Importa righe da uno o più DDT in un documento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.ddt_import_data import DdtImportData
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del documento di destinazione.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    ddt_import_data = amica_sdk.DdtImportData() # DdtImportData | Opzioni di importazione, inclusi gli ID dei DDT da importare. (optional)

    try:
        # Importa righe da uno o più DDT in un documento esistente.
        api_response = api_instance.api_vversion_company_id_documento_id_import_ddt_post(version, company_id, id, validation_override=validation_override, ddt_import_data=ddt_import_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_import_ddt_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_import_ddt_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del documento di destinazione. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **ddt_import_data** | [**DdtImportData**](DdtImportData.md)| Opzioni di importazione, inclusi gli ID dei DDT da importare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il documento aggiornato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. Il documento di destinazione non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_import_ordine_post**
> Documento api_vversion_company_id_documento_id_import_ordine_post(version, company_id, id, validation_override=validation_override, ordini_import_data=ordini_import_data)

Importa righe da uno o più ordini in un documento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
from amica_sdk.models.ordini_import_data import OrdiniImportData
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del documento di destinazione.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    ordini_import_data = amica_sdk.OrdiniImportData() # OrdiniImportData | Opzioni di importazione, inclusi gli ID degli ordini da importare. (optional)

    try:
        # Importa righe da uno o più ordini in un documento esistente.
        api_response = api_instance.api_vversion_company_id_documento_id_import_ordine_post(version, company_id, id, validation_override=validation_override, ordini_import_data=ordini_import_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_import_ordine_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_import_ordine_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del documento di destinazione. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **ordini_import_data** | [**OrdiniImportData**](OrdiniImportData.md)| Opzioni di importazione, inclusi gli ID degli ordini da importare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il documento aggiornato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. Il documento di destinazione non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_import_preventivo_post**
> Documento api_vversion_company_id_documento_id_import_preventivo_post(version, company_id, id, validation_override=validation_override, documento_import_data=documento_import_data)

Importa righe da uno o più preventivi in un documento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
from amica_sdk.models.documento_import_data import DocumentoImportData
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del documento di destinazione.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    documento_import_data = amica_sdk.DocumentoImportData() # DocumentoImportData | Opzioni di importazione, inclusi gli ID dei preventivi da importare. (optional)

    try:
        # Importa righe da uno o più preventivi in un documento esistente.
        api_response = api_instance.api_vversion_company_id_documento_id_import_preventivo_post(version, company_id, id, validation_override=validation_override, documento_import_data=documento_import_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_import_preventivo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_import_preventivo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del documento di destinazione. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **documento_import_data** | [**DocumentoImportData**](DocumentoImportData.md)| Opzioni di importazione, inclusi gli ID dei preventivi da importare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il documento aggiornato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. Il documento di destinazione non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_import_proforma_post**
> Documento api_vversion_company_id_documento_id_import_proforma_post(version, company_id, id, validation_override=validation_override, documento_import_data=documento_import_data)

Importa righe da una o più fatture proforma in un documento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
from amica_sdk.models.documento_import_data import DocumentoImportData
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del documento di destinazione.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    documento_import_data = amica_sdk.DocumentoImportData() # DocumentoImportData | Opzioni di importazione, inclusi gli ID delle proforma da importare. (optional)

    try:
        # Importa righe da una o più fatture proforma in un documento esistente.
        api_response = api_instance.api_vversion_company_id_documento_id_import_proforma_post(version, company_id, id, validation_override=validation_override, documento_import_data=documento_import_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_import_proforma_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_import_proforma_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del documento di destinazione. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **documento_import_data** | [**DocumentoImportData**](DocumentoImportData.md)| Opzioni di importazione, inclusi gli ID delle proforma da importare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il documento aggiornato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. Il documento di destinazione non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_import_reso_post**
> Documento api_vversion_company_id_documento_id_import_reso_post(version, company_id, id, validation_override=validation_override, reso_import_data=reso_import_data)

Importa righe da uno o più resi in un documento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
from amica_sdk.models.reso_import_data import ResoImportData
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del documento di destinazione.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    reso_import_data = amica_sdk.ResoImportData() # ResoImportData | Opzioni di importazione, inclusi gli ID dei resi da importare. (optional)

    try:
        # Importa righe da uno o più resi in un documento esistente.
        api_response = api_instance.api_vversion_company_id_documento_id_import_reso_post(version, company_id, id, validation_override=validation_override, reso_import_data=reso_import_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_import_reso_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_import_reso_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del documento di destinazione. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **reso_import_data** | [**ResoImportData**](ResoImportData.md)| Opzioni di importazione, inclusi gli ID dei resi da importare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce il documento aggiornato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. Il documento di destinazione non è stato trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_id_put**
> Documento api_vversion_company_id_documento_id_put(version, company_id, id, validation_override=validation_override, documento=documento)

Aggiorna un elemento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID univoco dell'elemento da aggiornare.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    documento = amica_sdk.Documento() # Documento | Istanza dell'elemento da salvare. (optional)

    try:
        # Aggiorna un elemento esistente.
        api_response = api_instance.api_vversion_company_id_documento_id_put(version, company_id, id, validation_override=validation_override, documento=documento)
        print("The response of DocumentoApi->api_vversion_company_id_documento_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID univoco dell&#39;elemento da aggiornare. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **documento** | [**Documento**](Documento.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;elemento aggiornato con un nuovo valore di Amica.BaseEntity.ConcurrencyToken. |  -  |
**422** | Conflitto. Restituisce il motivo del conflitto. |  -  |
**404** | Non trovato. L&#39;elemento non è stato trovato. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore (di solito un problema di validazione). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_new_get**
> Documento api_vversion_company_id_documento_new_get(version, company_id)

Restituisce una nuova istanza di un documento del tipo specificato.

Richiede il parametro query `TipoDocumento` (int) che indica il tipo di documento da creare.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.

    try:
        # Restituisce una nuova istanza di un documento del tipo specificato.
        api_response = api_instance.api_vversion_company_id_documento_new_get(version, company_id)
        print("The response of DocumentoApi->api_vversion_company_id_documento_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_new_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_periodicinvoicing_post**
> List[Documento] api_vversion_company_id_documento_periodicinvoicing_post(version, company_id, id=id, validation_override=validation_override, periodic_invoicing_data=periodic_invoicing_data)

Genera fatture per tutti i contatti che corrispondono ai criteri di fatturazione periodica.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
from amica_sdk.models.periodic_invoicing_data import PeriodicInvoicingData
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | Non utilizzato. (optional)
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    periodic_invoicing_data = amica_sdk.PeriodicInvoicingData() # PeriodicInvoicingData | Criteri e opzioni di fatturazione periodica. (optional)

    try:
        # Genera fatture per tutti i contatti che corrispondono ai criteri di fatturazione periodica.
        api_response = api_instance.api_vversion_company_id_documento_periodicinvoicing_post(version, company_id, id=id, validation_override=validation_override, periodic_invoicing_data=periodic_invoicing_data)
        print("The response of DocumentoApi->api_vversion_company_id_documento_periodicinvoicing_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_periodicinvoicing_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| Non utilizzato. | [optional] 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **periodic_invoicing_data** | [**PeriodicInvoicingData**](PeriodicInvoicingData.md)| Criteri e opzioni di fatturazione periodica. | [optional] 

### Return type

[**List[Documento]**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce la lista dei documenti generati. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  -  |
**404** | Non trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_post**
> Documento api_vversion_company_id_documento_post(version, company_id, validation_override=validation_override, documento=documento)

Salva un nuovo elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento import Documento
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
    api_instance = amica_sdk.DocumentoApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    documento = amica_sdk.Documento() # Documento | Istanza dell'elemento da salvare. (optional)

    try:
        # Salva un nuovo elemento.
        api_response = api_instance.api_vversion_company_id_documento_post(version, company_id, validation_override=validation_override, documento=documento)
        print("The response of DocumentoApi->api_vversion_company_id_documento_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoApi->api_vversion_company_id_documento_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **documento** | [**Documento**](Documento.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**Documento**](Documento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creato. Restituisce l&#39;elemento salvato con il Amica.BaseEntity.ConcurrencyToken aggiornato. |  -  |
**409** | Conflitto. Restituisce il motivo del conflitto. |  -  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore (di solito un problema di validazione). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

