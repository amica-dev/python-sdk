# amica_sdk.WebHookApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_vversion_company_id_web_hook_get**](WebHookApi.md#api_vversion_company_id_web_hook_get) | **GET** /api/v{version}/{companyId}/WebHook | Restituisce una lista di Amica.WebHook.
[**api_vversion_company_id_web_hook_id_delete**](WebHookApi.md#api_vversion_company_id_web_hook_id_delete) | **DELETE** /api/v{version}/{companyId}/WebHook/{id} | 
[**api_vversion_company_id_web_hook_id_get**](WebHookApi.md#api_vversion_company_id_web_hook_id_get) | **GET** /api/v{version}/{companyId}/WebHook/{id} | Restituisce un Amica.WebHook.
[**api_vversion_company_id_web_hook_id_put**](WebHookApi.md#api_vversion_company_id_web_hook_id_put) | **PUT** /api/v{version}/{companyId}/WebHook/{id} | Aggiorna un Amica.WebHook.
[**api_vversion_company_id_web_hook_new_get**](WebHookApi.md#api_vversion_company_id_web_hook_new_get) | **GET** /api/v{version}/{companyId}/WebHook/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
[**api_vversion_company_id_web_hook_post**](WebHookApi.md#api_vversion_company_id_web_hook_post) | **POST** /api/v{version}/{companyId}/WebHook | 


# **api_vversion_company_id_web_hook_get**
> List[WebHook] api_vversion_company_id_web_hook_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)

Restituisce una lista di Amica.WebHook.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.web_hook import WebHook
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
    api_instance = amica_sdk.WebHookApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    skip = 100 # int | Numero di elementi da escludere dall'inizio del risultato. Combinato con `Take`, è utile per la paginazione. (optional)
    take = 25 # int | Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione. (optional)
    skip_total_count = True # bool | Indica se l'header `X-Read-TotalCount` debba essere escluso dalla risposta. Impostare a `true` per prestazioni migliori a scapito dell'accuratezza. Il valore predefinito è `false`. (optional)
    filter = 'field1 $eq hello $or, field2 $gt 10' # str | Condizioni di ricerca. Elenco di espressioni separate da virgola. Ogni espressione è composta da nome del campo, operatore di confronto, valore ed eventualmente un connettore logico. Operatori validi: `$eq` (uguale), `$ne` (diverso), `$gt` (maggiore di), `$lt` (minore di), `$lte` (minore o uguale), `$gte` (maggiore o uguale), `$ct` (contiene), `$nct` (non contiene), `$sw` (inizia con), `$ew` (finisce con). Più espressioni possono essere concatenate con un connettore logico `$and` o `$or` (`$and` può essere omesso). Le query annidate si esprimono racchiudendo le sotto-query tra parentesi quadre (`[]`). Nell'esempio vengono inclusi tutti gli elementi con `field1=\"hello\"` oppure `field2>10`. (optional)
    order = '-field1,field2' # str | Opzioni di ordinamento. Un segno meno (trattino) prima del nome indica ordinamento discendente. Nell'esempio i risultati sono ordinati prima per `field1` (discendente), poi per `field2`. (optional)
    expand = ['Rows'] # List[str] | Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata. (optional)

    try:
        # Restituisce una lista di Amica.WebHook.
        api_response = api_instance.api_vversion_company_id_web_hook_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)
        print("The response of WebHookApi->api_vversion_company_id_web_hook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHookApi->api_vversion_company_id_web_hook_get: %s\n" % e)
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

[**List[WebHook]**](WebHook.md)

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

# **api_vversion_company_id_web_hook_id_delete**
> WebHook api_vversion_company_id_web_hook_id_delete(version, company_id, id)



### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.web_hook import WebHook
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
    api_instance = amica_sdk.WebHookApi(api_client)
    version = 'version_example' # str | 
    company_id = 'company_id_example' # str | 
    id = 56 # int | 

    try:
        api_response = api_instance.api_vversion_company_id_web_hook_id_delete(version, company_id, id)
        print("The response of WebHookApi->api_vversion_company_id_web_hook_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHookApi->api_vversion_company_id_web_hook_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **company_id** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_web_hook_id_get**
> WebHook api_vversion_company_id_web_hook_id_get(version, company_id, id, expand=expand)

Restituisce un Amica.WebHook.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.web_hook import WebHook
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
    api_instance = amica_sdk.WebHookApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del WebHook.
    expand = ['Rows'] # List[str] | Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un'unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge `expand=Rows` alla chiamata. (optional)

    try:
        # Restituisce un Amica.WebHook.
        api_response = api_instance.api_vversion_company_id_web_hook_id_get(version, company_id, id, expand=expand)
        print("The response of WebHookApi->api_vversion_company_id_web_hook_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHookApi->api_vversion_company_id_web_hook_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del WebHook. | 
 **expand** | [**List[str]**](str.md)| Elenco separato da virgole di oggetti da espandere. Permette di recuperare gli oggetti correlati in un&#39;unica chiamata. Ad esempio, per includere i beni e servizi associati a ciascun documento si aggiunge &#x60;expand&#x3D;Rows&#x60; alla chiamata. | [optional] 

### Return type

[**WebHook**](WebHook.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_web_hook_id_put**
> WebHook api_vversion_company_id_web_hook_id_put(version, company_id, id, validation_override=validation_override, web_hook=web_hook)

Aggiorna un Amica.WebHook.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.web_hook import WebHook
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
    api_instance = amica_sdk.WebHookApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID del WebHook.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    web_hook = amica_sdk.WebHook() # WebHook | Istanza con i valori aggiornati. (optional)

    try:
        # Aggiorna un Amica.WebHook.
        api_response = api_instance.api_vversion_company_id_web_hook_id_put(version, company_id, id, validation_override=validation_override, web_hook=web_hook)
        print("The response of WebHookApi->api_vversion_company_id_web_hook_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHookApi->api_vversion_company_id_web_hook_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID del WebHook. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **web_hook** | [**WebHook**](WebHook.md)| Istanza con i valori aggiornati. | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Content |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_web_hook_new_get**
> WebHook api_vversion_company_id_web_hook_new_get(version, company_id)

Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.web_hook import WebHook
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
    api_instance = amica_sdk.WebHookApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.

    try:
        # Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di Amica.Documento avrà il Amica.Documento.Numero appropriato, basato sui documenti preesistenti di tipo compatibile).
        api_response = api_instance.api_vversion_company_id_web_hook_new_get(version, company_id)
        print("The response of WebHookApi->api_vversion_company_id_web_hook_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHookApi->api_vversion_company_id_web_hook_new_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 

### Return type

[**WebHook**](WebHook.md)

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

# **api_vversion_company_id_web_hook_post**
> WebHook api_vversion_company_id_web_hook_post(version, company_id, validation_override=validation_override, web_hook=web_hook)



### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.web_hook import WebHook
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
    api_instance = amica_sdk.WebHookApi(api_client)
    version = 'version_example' # str | 
    company_id = 'company_id_example' # str | 
    validation_override = True # bool |  (optional)
    web_hook = amica_sdk.WebHook() # WebHook |  (optional)

    try:
        api_response = api_instance.api_vversion_company_id_web_hook_post(version, company_id, validation_override=validation_override, web_hook=web_hook)
        print("The response of WebHookApi->api_vversion_company_id_web_hook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebHookApi->api_vversion_company_id_web_hook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **company_id** | **str**|  | 
 **validation_override** | **bool**|  | [optional] 
 **web_hook** | [**WebHook**](WebHook.md)|  | [optional] 

### Return type

[**WebHook**](WebHook.md)

### Authorization

[bearer](../README.md#bearer), [oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**409** | Conflict |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

