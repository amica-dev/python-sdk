# amica_sdk.DocumentoMediaFileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_vversion_company_id_documento_media_file_bulk_delete**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_bulk_delete) | **DELETE** /api/v{version}/{companyId}/DocumentoMediaFile/bulk | Elimina in blocco tutti i file multimediali dei documenti.
[**api_vversion_company_id_documento_media_file_bulk_get**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_bulk_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile/bulk | Scarica tutti i file multimediali dei documenti come archivio ZIP.
[**api_vversion_company_id_documento_media_file_get**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile | Restituisce una lista di elementi.
[**api_vversion_company_id_documento_media_file_id_delete**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_id_delete) | **DELETE** /api/v{version}/{companyId}/DocumentoMediaFile/{id} | Elimina un elemento.
[**api_vversion_company_id_documento_media_file_id_get**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_id_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile/{id} | Restituisce un elemento.
[**api_vversion_company_id_documento_media_file_id_put**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_id_put) | **PUT** /api/v{version}/{companyId}/DocumentoMediaFile/{id} | Aggiorna un elemento esistente.
[**api_vversion_company_id_documento_media_file_new_get**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_new_get) | **GET** /api/v{version}/{companyId}/DocumentoMediaFile/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
[**api_vversion_company_id_documento_media_file_post**](DocumentoMediaFileApi.md#api_vversion_company_id_documento_media_file_post) | **POST** /api/v{version}/{companyId}/DocumentoMediaFile | Salva un nuovo elemento.


# **api_vversion_company_id_documento_media_file_bulk_delete**
> api_vversion_company_id_documento_media_file_bulk_delete(company_id, version)

Elimina in blocco tutti i file multimediali dei documenti.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    version = 'version_example' # str | 

    try:
        # Elimina in blocco tutti i file multimediali dei documenti.
        api_instance.api_vversion_company_id_documento_media_file_bulk_delete(company_id, version)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_bulk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successo. Tutti i file sono stati eliminati. |  -  |
**404** | Non trovato. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_media_file_bulk_get**
> api_vversion_company_id_documento_media_file_bulk_get(company_id, version)

Scarica tutti i file multimediali dei documenti come archivio ZIP.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    version = 'version_example' # str | 

    try:
        # Scarica tutti i file multimediali dei documenti come archivio ZIP.
        api_instance.api_vversion_company_id_documento_media_file_bulk_get(company_id, version)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_bulk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;archivio ZIP. |  -  |
**404** | Non trovato. Nessun file disponibile. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_documento_media_file_get**
> List[DocumentoMediaFile] api_vversion_company_id_documento_media_file_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)

Restituisce una lista di elementi.

 La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento_media_file import DocumentoMediaFile
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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
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
        api_response = api_instance.api_vversion_company_id_documento_media_file_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)
        print("The response of DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_get: %s\n" % e)
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

[**List[DocumentoMediaFile]**](DocumentoMediaFile.md)

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

# **api_vversion_company_id_documento_media_file_id_delete**
> DocumentoMediaFile api_vversion_company_id_documento_media_file_id_delete(version, company_id, id)

Elimina un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento_media_file import DocumentoMediaFile
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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da eliminare.

    try:
        # Elimina un elemento.
        api_response = api_instance.api_vversion_company_id_documento_media_file_id_delete(version, company_id, id)
        print("The response of DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da eliminare. | 

### Return type

[**DocumentoMediaFile**](DocumentoMediaFile.md)

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

# **api_vversion_company_id_documento_media_file_id_get**
> DocumentoMediaFile api_vversion_company_id_documento_media_file_id_get(version, company_id, id, expand=expand)

Restituisce un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento_media_file import DocumentoMediaFile
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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da recuperare.
    expand = ['Rows'] # List[str] | Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata. (optional)

    try:
        # Restituisce un elemento.
        api_response = api_instance.api_vversion_company_id_documento_media_file_id_get(version, company_id, id, expand=expand)
        print("The response of DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da recuperare. | 
 **expand** | [**List[str]**](str.md)| Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un&#39;unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge &#x60;expand&#x3D;Rows&#x60; alla chiamata. | [optional] 

### Return type

[**DocumentoMediaFile**](DocumentoMediaFile.md)

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

# **api_vversion_company_id_documento_media_file_id_put**
> DocumentoMediaFile api_vversion_company_id_documento_media_file_id_put(version, company_id, id, validation_override=validation_override, documento_media_file=documento_media_file)

Aggiorna un elemento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento_media_file import DocumentoMediaFile
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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID univoco dell'elemento da aggiornare.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    documento_media_file = amica_sdk.DocumentoMediaFile() # DocumentoMediaFile | Istanza dell'elemento da salvare. (optional)

    try:
        # Aggiorna un elemento esistente.
        api_response = api_instance.api_vversion_company_id_documento_media_file_id_put(version, company_id, id, validation_override=validation_override, documento_media_file=documento_media_file)
        print("The response of DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID univoco dell&#39;elemento da aggiornare. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **documento_media_file** | [**DocumentoMediaFile**](DocumentoMediaFile.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**DocumentoMediaFile**](DocumentoMediaFile.md)

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

# **api_vversion_company_id_documento_media_file_new_get**
> DocumentoMediaFile api_vversion_company_id_documento_media_file_new_get(version, company_id)

Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento_media_file import DocumentoMediaFile
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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.

    try:
        # Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
        api_response = api_instance.api_vversion_company_id_documento_media_file_new_get(version, company_id)
        print("The response of DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_new_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 

### Return type

[**DocumentoMediaFile**](DocumentoMediaFile.md)

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

# **api_vversion_company_id_documento_media_file_post**
> DocumentoMediaFile api_vversion_company_id_documento_media_file_post(version, company_id, validation_override=validation_override, documento_media_file=documento_media_file)

Salva un nuovo elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.documento_media_file import DocumentoMediaFile
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
    api_instance = amica_sdk.DocumentoMediaFileApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    documento_media_file = amica_sdk.DocumentoMediaFile() # DocumentoMediaFile | Istanza dell'elemento da salvare. (optional)

    try:
        # Salva un nuovo elemento.
        api_response = api_instance.api_vversion_company_id_documento_media_file_post(version, company_id, validation_override=validation_override, documento_media_file=documento_media_file)
        print("The response of DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentoMediaFileApi->api_vversion_company_id_documento_media_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **documento_media_file** | [**DocumentoMediaFile**](DocumentoMediaFile.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**DocumentoMediaFile**](DocumentoMediaFile.md)

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

