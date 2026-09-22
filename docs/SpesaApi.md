# amica_python_sdk.SpesaApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_vversion_company_id_spesa_distinct_get**](SpesaApi.md#api_vversion_company_id_spesa_distinct_get) | **GET** /api/v{version}/{companyId}/Spesa/distinct | Restituisce una lista di elementi distinti.
[**api_vversion_company_id_spesa_get**](SpesaApi.md#api_vversion_company_id_spesa_get) | **GET** /api/v{version}/{companyId}/Spesa | Restituisce una lista di elementi.
[**api_vversion_company_id_spesa_id_delete**](SpesaApi.md#api_vversion_company_id_spesa_id_delete) | **DELETE** /api/v{version}/{companyId}/Spesa/{id} | Elimina un elemento.
[**api_vversion_company_id_spesa_id_get**](SpesaApi.md#api_vversion_company_id_spesa_id_get) | **GET** /api/v{version}/{companyId}/Spesa/{id} | Restituisce un elemento.
[**api_vversion_company_id_spesa_id_put**](SpesaApi.md#api_vversion_company_id_spesa_id_put) | **PUT** /api/v{version}/{companyId}/Spesa/{id} | Aggiorna un elemento esistente.
[**api_vversion_company_id_spesa_new_get**](SpesaApi.md#api_vversion_company_id_spesa_new_get) | **GET** /api/v{version}/{companyId}/Spesa/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di &#x60;Documento&#x60; avrà il &#x60;Numero&#x60; appropriato, basato sui documenti preesistenti di tipo compatibile).
[**api_vversion_company_id_spesa_post**](SpesaApi.md#api_vversion_company_id_spesa_post) | **POST** /api/v{version}/{companyId}/Spesa | Salva un nuovo elemento.


# **api_vversion_company_id_spesa_distinct_get**
> List[DistinctPropertyGroup] api_vversion_company_id_spesa_distinct_get(version, company_id, selector, skip=skip, take=take)

Restituisce una lista di elementi distinti.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.distinct_property_group import DistinctPropertyGroup
from amica_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with amica_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_python_sdk.SpesaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    selector = 'RagioneSociale1' # str | Il campo usato per distinguere gli elementi.
    skip = 100 # int | Numero di elementi, a partire dal primo, da escludere dal risultato. Combinato con `Take`, è utile per la paginazione. (optional)
    take = 25 # int | Numero di elementi da includere nel risultato. Combinato con `Skip`, è utile per la paginazione. (optional)

    try:
        # Restituisce una lista di elementi distinti.
        api_response = api_instance.api_vversion_company_id_spesa_distinct_get(version, company_id, selector, skip=skip, take=take)
        print("The response of SpesaApi->api_vversion_company_id_spesa_distinct_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpesaApi->api_vversion_company_id_spesa_distinct_get: %s\n" % e)
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

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce la lista degli elementi distinti. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_spesa_get**
> List[Spesa] api_vversion_company_id_spesa_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)

Restituisce una lista di elementi.

 La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.spesa import Spesa
from amica_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with amica_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_python_sdk.SpesaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    skip = 56 # int |  (optional)
    take = 56 # int |  (optional)
    skip_total_count = True # bool |  (optional)
    filter = 'filter_example' # str |  (optional)
    order = 'order_example' # str |  (optional)
    expand = ['expand_example'] # List[str] |  (optional)

    try:
        # Restituisce una lista di elementi.
        api_response = api_instance.api_vversion_company_id_spesa_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)
        print("The response of SpesaApi->api_vversion_company_id_spesa_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpesaApi->api_vversion_company_id_spesa_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **skip** | **int**|  | [optional] 
 **take** | **int**|  | [optional] 
 **skip_total_count** | **bool**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 
 **expand** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[Spesa]**](Spesa.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce la lista degli elementi corrispondenti ai criteri di ricerca. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_spesa_id_delete**
> Spesa api_vversion_company_id_spesa_id_delete(version, company_id, id)

Elimina un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.spesa import Spesa
from amica_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with amica_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_python_sdk.SpesaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da eliminare.

    try:
        # Elimina un elemento.
        api_response = api_instance.api_vversion_company_id_spesa_id_delete(version, company_id, id)
        print("The response of SpesaApi->api_vversion_company_id_spesa_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpesaApi->api_vversion_company_id_spesa_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da eliminare. | 

### Return type

[**Spesa**](Spesa.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;elemento eliminato. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**404** | Non trovato. L&#39;elemento non è stato trovato. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_spesa_id_get**
> Spesa api_vversion_company_id_spesa_id_get(version, company_id, id, expand=expand)

Restituisce un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.spesa import Spesa
from amica_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with amica_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_python_sdk.SpesaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da recuperare.
    expand = ['expand_example'] # List[str] |  (optional)

    try:
        # Restituisce un elemento.
        api_response = api_instance.api_vversion_company_id_spesa_id_get(version, company_id, id, expand=expand)
        print("The response of SpesaApi->api_vversion_company_id_spesa_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpesaApi->api_vversion_company_id_spesa_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da recuperare. | 
 **expand** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Spesa**](Spesa.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;elemento richiesto. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**404** | Non trovato. L&#39;elemento non è stato trovato. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_spesa_id_put**
> Spesa api_vversion_company_id_spesa_id_put(version, company_id, id, validation_override=validation_override, idempotency_key=idempotency_key, spesa=spesa)

Aggiorna un elemento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.spesa import Spesa
from amica_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with amica_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_python_sdk.SpesaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID univoco dell'elemento da aggiornare.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    spesa = amica_python_sdk.Spesa() # Spesa | Istanza dell'elemento da salvare. (optional)

    try:
        # Aggiorna un elemento esistente.
        api_response = api_instance.api_vversion_company_id_spesa_id_put(version, company_id, id, validation_override=validation_override, idempotency_key=idempotency_key, spesa=spesa)
        print("The response of SpesaApi->api_vversion_company_id_spesa_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpesaApi->api_vversion_company_id_spesa_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID univoco dell&#39;elemento da aggiornare. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **spesa** | [**Spesa**](Spesa.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**Spesa**](Spesa.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;elemento aggiornato con un nuovo valore di &#x60;ConcurrencyToken&#x60;. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**422** | Conflitto. Restituisce il motivo del conflitto. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**404** | Non trovato. L&#39;elemento non è stato trovato. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore (di solito un problema di validazione). |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_spesa_new_get**
> Spesa api_vversion_company_id_spesa_new_get(version, company_id)

Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di `Documento` avrà il `Numero` appropriato, basato sui documenti preesistenti di tipo compatibile).

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.spesa import Spesa
from amica_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with amica_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_python_sdk.SpesaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.

    try:
        # Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di `Documento` avrà il `Numero` appropriato, basato sui documenti preesistenti di tipo compatibile).
        api_response = api_instance.api_vversion_company_id_spesa_new_get(version, company_id)
        print("The response of SpesaApi->api_vversion_company_id_spesa_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpesaApi->api_vversion_company_id_spesa_new_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 

### Return type

[**Spesa**](Spesa.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_spesa_post**
> Spesa api_vversion_company_id_spesa_post(version, company_id, validation_override=validation_override, idempotency_key=idempotency_key, spesa=spesa)

Salva un nuovo elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.spesa import Spesa
from amica_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = amica_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer
configuration = amica_python_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with amica_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = amica_python_sdk.SpesaApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    spesa = amica_python_sdk.Spesa() # Spesa | Istanza dell'elemento da salvare. (optional)

    try:
        # Salva un nuovo elemento.
        api_response = api_instance.api_vversion_company_id_spesa_post(version, company_id, validation_override=validation_override, idempotency_key=idempotency_key, spesa=spesa)
        print("The response of SpesaApi->api_vversion_company_id_spesa_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpesaApi->api_vversion_company_id_spesa_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **spesa** | [**Spesa**](Spesa.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**Spesa**](Spesa.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creato. Restituisce l&#39;elemento salvato con il &#x60;ConcurrencyToken&#x60; aggiornato. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto. Restituisce il motivo del conflitto. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore (di solito un problema di validazione). |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

