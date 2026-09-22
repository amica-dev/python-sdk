# amica_python_sdk.FatturaElettronicaXmlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/archivebydaterange | Scarica un archivio ZIP di fatture XML, filtrate per intervallo di date.
[**api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/archivebyfilename | Scarica un archivio ZIP di fatture XML, filtrate per nome file.
[**api_vversion_company_id_fattura_elettronica_xml_bulk_delete**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_bulk_delete) | **DELETE** /api/v{version}/{companyId}/FatturaElettronicaXml/bulk | Elimina in blocco tutte le fatture XML dell&#39;azienda.
[**api_vversion_company_id_fattura_elettronica_xml_bulk_get**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_bulk_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/bulk | Scarica tutte le fatture XML come archivio ZIP.
[**api_vversion_company_id_fattura_elettronica_xml_bulk_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_bulk_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/bulk | Carica in blocco fatture XML da un archivio ZIP.
[**api_vversion_company_id_fattura_elettronica_xml_export_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_export_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/export | Esporta uno o più documenti in una fattura XML.
[**api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/{fileName}/attachments | Scarica i file allegati di una fattura XML.
[**api_vversion_company_id_fattura_elettronica_xml_file_name_get**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_file_name_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/{fileName} | Recupera una fattura XML per nome file.
[**api_vversion_company_id_fattura_elettronica_xml_get**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml | Restituisce una lista di elementi.
[**api_vversion_company_id_fattura_elettronica_xml_id_delete**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_id_delete) | **DELETE** /api/v{version}/{companyId}/FatturaElettronicaXml/{id} | Elimina un elemento.
[**api_vversion_company_id_fattura_elettronica_xml_id_get**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_id_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/{id} | Restituisce un elemento.
[**api_vversion_company_id_fattura_elettronica_xml_id_put**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_id_put) | **PUT** /api/v{version}/{companyId}/FatturaElettronicaXml/{id} | Aggiorna un elemento esistente.
[**api_vversion_company_id_fattura_elettronica_xml_import_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_import_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/import | Importa una fattura XML.
[**api_vversion_company_id_fattura_elettronica_xml_new_get**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_new_get) | **GET** /api/v{version}/{companyId}/FatturaElettronicaXml/new | Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell&#39;applicazione (ad es., una nuova istanza di &#x60;Documento&#x60; avrà il &#x60;Numero&#x60; appropriato, basato sui documenti preesistenti di tipo compatibile).
[**api_vversion_company_id_fattura_elettronica_xml_pair_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_pair_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/pair | Associa una fattura XML a un documento esistente.
[**api_vversion_company_id_fattura_elettronica_xml_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml | Salva un nuovo elemento.
[**api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/sdi/download/esiti | Interroga il Sistema di Interscambio (SDI) e scarica gli esiti di invio delle fatture precedentemente caricate.
[**api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/sdi/download/fatture | Scarica le nuove fatture dal Sistema di Interscambio (SDI).
[**api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/sdi/upload | Invia una o più fatture al Sistema di Interscambio (SDI).
[**api_vversion_company_id_fattura_elettronica_xml_stylesheet_post**](FatturaElettronicaXmlApi.md#api_vversion_company_id_fattura_elettronica_xml_stylesheet_post) | **POST** /api/v{version}/{companyId}/FatturaElettronicaXml/stylesheet | Applica un foglio di stile CSS a una fattura XML esistente e restituisce il risultato.


# **api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post**
> api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_xml_get_archive_by_date_range_options=fattura_elettronica_xml_get_archive_by_date_range_options)

Scarica un archivio ZIP di fatture XML, filtrate per intervallo di date.

Non è possibile scaricare più di 350 file alla volta.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml_get_archive_by_date_range_options import FatturaElettronicaXmlGetArchiveByDateRangeOptions
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    fattura_elettronica_xml_get_archive_by_date_range_options = amica_python_sdk.FatturaElettronicaXmlGetArchiveByDateRangeOptions() # FatturaElettronicaXmlGetArchiveByDateRangeOptions | Opzioni di download. (optional)

    try:
        # Scarica un archivio ZIP di fatture XML, filtrate per intervallo di date.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_xml_get_archive_by_date_range_options=fattura_elettronica_xml_get_archive_by_date_range_options)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_archivebydaterange_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **fattura_elettronica_xml_get_archive_by_date_range_options** | [**FatturaElettronicaXmlGetArchiveByDateRangeOptions**](FatturaElettronicaXmlGetArchiveByDateRangeOptions.md)| Opzioni di download. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/zip, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**204** | No Content |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post**
> api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_xml_get_archive_by_file_name_options=fattura_elettronica_xml_get_archive_by_file_name_options)

Scarica un archivio ZIP di fatture XML, filtrate per nome file.

Non è possibile scaricare più di 350 file alla volta.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml_get_archive_by_file_name_options import FatturaElettronicaXmlGetArchiveByFileNameOptions
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    fattura_elettronica_xml_get_archive_by_file_name_options = amica_python_sdk.FatturaElettronicaXmlGetArchiveByFileNameOptions() # FatturaElettronicaXmlGetArchiveByFileNameOptions | Opzioni di download. (optional)

    try:
        # Scarica un archivio ZIP di fatture XML, filtrate per nome file.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_xml_get_archive_by_file_name_options=fattura_elettronica_xml_get_archive_by_file_name_options)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_archivebyfilename_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **fattura_elettronica_xml_get_archive_by_file_name_options** | [**FatturaElettronicaXmlGetArchiveByFileNameOptions**](FatturaElettronicaXmlGetArchiveByFileNameOptions.md)| Opzioni di download. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/zip, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**204** | No Content |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_bulk_delete**
> api_vversion_company_id_fattura_elettronica_xml_bulk_delete(company_id, version)

Elimina in blocco tutte le fatture XML dell'azienda.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    version = 'version_example' # str | 

    try:
        # Elimina in blocco tutte le fatture XML dell'azienda.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_bulk_delete(company_id, version)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_bulk_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successo. Tutte le fatture XML sono state eliminate. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_bulk_get**
> api_vversion_company_id_fattura_elettronica_xml_bulk_get(company_id, version)

Scarica tutte le fatture XML come archivio ZIP.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    version = 'version_example' # str | 

    try:
        # Scarica tutte le fatture XML come archivio ZIP.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_bulk_get(company_id, version)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_bulk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **version** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successo. Restituisce l&#39;archivio ZIP. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**404** | Non trovato. Nessun file disponibile. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_bulk_post**
> api_vversion_company_id_fattura_elettronica_xml_bulk_post(company_id, version, idempotency_key=idempotency_key, file=file)

Carica in blocco fatture XML da un archivio ZIP.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    version = 'version_example' # str | 
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    file = None # bytearray | Archivio ZIP contenente i file XML. (optional)

    try:
        # Carica in blocco fatture XML da un archivio ZIP.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_bulk_post(company_id, version, idempotency_key=idempotency_key, file=file)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **version** | **str**|  | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **file** | **bytearray**| Archivio ZIP contenente i file XML. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creato. I file sono stati caricati con successo. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request. Restituisce il motivo dell&#39;errore. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_export_post**
> FatturaElettronicaExportResult api_vversion_company_id_fattura_elettronica_xml_export_post(version, company_id, validation_override=validation_override, idempotency_key=idempotency_key, fattura_elettronica_export_options=fattura_elettronica_export_options)

Esporta uno o più documenti in una fattura XML.

Tutti i documenti devono riferirsi alla stessa <a href=\"#tag/Anagrafica\">Anagrafica</a>.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_export_options import FatturaElettronicaExportOptions
from amica_python_sdk.models.fattura_elettronica_export_result import FatturaElettronicaExportResult
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    fattura_elettronica_export_options = amica_python_sdk.FatturaElettronicaExportOptions() # FatturaElettronicaExportOptions | Opzioni di esportazione. (optional)

    try:
        # Esporta uno o più documenti in una fattura XML.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_export_post(version, company_id, validation_override=validation_override, idempotency_key=idempotency_key, fattura_elettronica_export_options=fattura_elettronica_export_options)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **fattura_elettronica_export_options** | [**FatturaElettronicaExportOptions**](FatturaElettronicaExportOptions.md)| Opzioni di esportazione. | [optional] 

### Return type

[**FatturaElettronicaExportResult**](FatturaElettronicaExportResult.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**404** | Not Found |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get**
> List[AllegatoDocumento] api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get(version, company_id, file_name)

Scarica i file allegati di una fattura XML.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.allegato_documento import AllegatoDocumento
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    file_name = 'file_name_example' # str | Nome del file.

    try:
        # Scarica i file allegati di una fattura XML.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get(version, company_id, file_name)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_file_name_attachments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **file_name** | **str**| Nome del file. | 

### Return type

[**List[AllegatoDocumento]**](AllegatoDocumento.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**404** | Not Found |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_file_name_get**
> api_vversion_company_id_fattura_elettronica_xml_file_name_get(version, company_id, file_name)

Recupera una fattura XML per nome file.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    file_name = 'file_name_example' # str | Nome del file.

    try:
        # Recupera una fattura XML per nome file.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_file_name_get(version, company_id, file_name)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_file_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **file_name** | **str**| Nome del file. | 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**404** | Not Found |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_get**
> List[FatturaElettronicaXml] api_vversion_company_id_fattura_elettronica_xml_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)

Restituisce una lista di elementi.

 La risposta include due header con informazioni sui risultati.  `X-Read-TotalCount` indica il numero di elementi che soddisfano il filtro impostato nella query;  `X-Read-Count` indica il numero di elementi effettivamente contenuti nella risposta.  I due header possono riportare valori diversi quando i parametri `Take` e `Skip` sono stati usati nelle opzioni di query.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
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
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_get(version, company_id, skip=skip, take=take, skip_total_count=skip_total_count, filter=filter, order=order, expand=expand)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_get: %s\n" % e)
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

[**List[FatturaElettronicaXml]**](FatturaElettronicaXml.md)

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

# **api_vversion_company_id_fattura_elettronica_xml_id_delete**
> FatturaElettronicaXml api_vversion_company_id_fattura_elettronica_xml_id_delete(version, company_id, id)

Elimina un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da eliminare.

    try:
        # Elimina un elemento.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_id_delete(version, company_id, id)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da eliminare. | 

### Return type

[**FatturaElettronicaXml**](FatturaElettronicaXml.md)

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

# **api_vversion_company_id_fattura_elettronica_xml_id_get**
> FatturaElettronicaXml api_vversion_company_id_fattura_elettronica_xml_id_get(version, company_id, id, expand=expand)

Restituisce un elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID dell'elemento da recuperare.
    expand = ['expand_example'] # List[str] |  (optional)

    try:
        # Restituisce un elemento.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_id_get(version, company_id, id, expand=expand)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID dell&#39;elemento da recuperare. | 
 **expand** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**FatturaElettronicaXml**](FatturaElettronicaXml.md)

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

# **api_vversion_company_id_fattura_elettronica_xml_id_put**
> FatturaElettronicaXml api_vversion_company_id_fattura_elettronica_xml_id_put(version, company_id, id, validation_override=validation_override, idempotency_key=idempotency_key, fattura_elettronica_xml=fattura_elettronica_xml)

Aggiorna un elemento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    id = 56 # int | ID univoco dell'elemento da aggiornare.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    fattura_elettronica_xml = amica_python_sdk.FatturaElettronicaXml() # FatturaElettronicaXml | Istanza dell'elemento da salvare. (optional)

    try:
        # Aggiorna un elemento esistente.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_id_put(version, company_id, id, validation_override=validation_override, idempotency_key=idempotency_key, fattura_elettronica_xml=fattura_elettronica_xml)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **id** | **int**| ID univoco dell&#39;elemento da aggiornare. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **fattura_elettronica_xml** | [**FatturaElettronicaXml**](FatturaElettronicaXml.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**FatturaElettronicaXml**](FatturaElettronicaXml.md)

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

# **api_vversion_company_id_fattura_elettronica_xml_import_post**
> List[FatturaElettronicaImportResult] api_vversion_company_id_fattura_elettronica_xml_import_post(version, company_id, idempotency_key=idempotency_key, data_consegna_sdi=data_consegna_sdi, identificativo_sdi=identificativo_sdi, file=file)

Importa una fattura XML.

Viene creato un nuovo <a href=\"#tag/Documento\">Documento</a> corrispondente al contenuto XML.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_import_result import FatturaElettronicaImportResult
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    data_consegna_sdi = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    identificativo_sdi = 'identificativo_sdi_example' # str |  (optional)
    file = None # bytearray | Contenuto del file. (optional)

    try:
        # Importa una fattura XML.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_import_post(version, company_id, idempotency_key=idempotency_key, data_consegna_sdi=data_consegna_sdi, identificativo_sdi=identificativo_sdi, file=file)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **data_consegna_sdi** | **datetime**|  | [optional] 
 **identificativo_sdi** | **str**|  | [optional] 
 **file** | **bytearray**| Contenuto del file. | [optional] 

### Return type

[**List[FatturaElettronicaImportResult]**](FatturaElettronicaImportResult.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_new_get**
> FatturaElettronicaXml api_vversion_company_id_fattura_elettronica_xml_new_get(version, company_id)

Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di `Documento` avrà il `Numero` appropriato, basato sui documenti preesistenti di tipo compatibile).

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.

    try:
        # Restituisce una nuova istanza di un oggetto. Dove necessario, i valori delle proprietà saranno coerenti con lo stato e la logica dell'applicazione (ad es., una nuova istanza di `Documento` avrà il `Numero` appropriato, basato sui documenti preesistenti di tipo compatibile).
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_new_get(version, company_id)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_new_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_new_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 

### Return type

[**FatturaElettronicaXml**](FatturaElettronicaXml.md)

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

# **api_vversion_company_id_fattura_elettronica_xml_pair_post**
> api_vversion_company_id_fattura_elettronica_xml_pair_post(version, company_id, idempotency_key=idempotency_key, file_name=file_name, progressivo=progressivo, documento_id=documento_id, file=file)

Associa una fattura XML a un documento esistente.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    file_name = 'file_name_example' # str |  (optional)
    progressivo = 'progressivo_example' # str |  (optional)
    documento_id = 56 # int |  (optional)
    file = None # bytearray | Contenuto del file. (optional)

    try:
        # Associa una fattura XML a un documento esistente.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_pair_post(version, company_id, idempotency_key=idempotency_key, file_name=file_name, progressivo=progressivo, documento_id=documento_id, file=file)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_pair_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **file_name** | **str**|  | [optional] 
 **progressivo** | **str**|  | [optional] 
 **documento_id** | **int**|  | [optional] 
 **file** | **bytearray**| Contenuto del file. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_post**
> FatturaElettronicaXml api_vversion_company_id_fattura_elettronica_xml_post(version, company_id, validation_override=validation_override, idempotency_key=idempotency_key, fattura_elettronica_xml=fattura_elettronica_xml)

Salva un nuovo elemento.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml import FatturaElettronicaXml
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    validation_override = True # bool | Se applicare eventualmente l'override della validazione. (optional)
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    fattura_elettronica_xml = amica_python_sdk.FatturaElettronicaXml() # FatturaElettronicaXml | Istanza dell'elemento da salvare. (optional)

    try:
        # Salva un nuovo elemento.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_post(version, company_id, validation_override=validation_override, idempotency_key=idempotency_key, fattura_elettronica_xml=fattura_elettronica_xml)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **validation_override** | **bool**| Se applicare eventualmente l&#39;override della validazione. | [optional] 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **fattura_elettronica_xml** | [**FatturaElettronicaXml**](FatturaElettronicaXml.md)| Istanza dell&#39;elemento da salvare. | [optional] 

### Return type

[**FatturaElettronicaXml**](FatturaElettronicaXml.md)

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

# **api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post**
> List[FatturaElettronicaImportResult] api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post(version, company_id, idempotency_key=idempotency_key)

Interroga il Sistema di Interscambio (SDI) e scarica gli esiti di invio delle fatture precedentemente caricate.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_import_result import FatturaElettronicaImportResult
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)

    try:
        # Interroga il Sistema di Interscambio (SDI) e scarica gli esiti di invio delle fatture precedentemente caricate.
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post(version, company_id, idempotency_key=idempotency_key)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_sdi_download_esiti_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 

### Return type

[**List[FatturaElettronicaImportResult]**](FatturaElettronicaImportResult.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post**
> List[FatturaElettronicaImportResult] api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post(version, company_id, idempotency_key=idempotency_key)

Scarica le nuove fatture dal Sistema di Interscambio (SDI).

Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in `SdiApiKey`.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_import_result import FatturaElettronicaImportResult
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)

    try:
        # Scarica le nuove fatture dal Sistema di Interscambio (SDI).
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post(version, company_id, idempotency_key=idempotency_key)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_sdi_download_fatture_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 

### Return type

[**List[FatturaElettronicaImportResult]**](FatturaElettronicaImportResult.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post**
> FatturaElettronicaUploadResult api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_upload_options=fattura_elettronica_upload_options)

Invia una o più fatture al Sistema di Interscambio (SDI).

Il <a href=\"https://gestionaleamica.com/Software/ServizioInterscambioFatture\">Servizio di Interscambio Documenti</a> deve essere attivo per l'azienda e la relativa chiave di attivazione deve essere presente in `SdiApiKey`.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_upload_options import FatturaElettronicaUploadOptions
from amica_python_sdk.models.fattura_elettronica_upload_result import FatturaElettronicaUploadResult
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    fattura_elettronica_upload_options = amica_python_sdk.FatturaElettronicaUploadOptions() # FatturaElettronicaUploadOptions | Opzioni di invio. (optional)

    try:
        # Invia una o più fatture al Sistema di Interscambio (SDI).
        api_response = api_instance.api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_upload_options=fattura_elettronica_upload_options)
        print("The response of FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_sdi_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **fattura_elettronica_upload_options** | [**FatturaElettronicaUploadOptions**](FatturaElettronicaUploadOptions.md)| Opzioni di invio. | [optional] 

### Return type

[**FatturaElettronicaUploadResult**](FatturaElettronicaUploadResult.md)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**404** | Not Found |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_vversion_company_id_fattura_elettronica_xml_stylesheet_post**
> api_vversion_company_id_fattura_elettronica_xml_stylesheet_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_xml_style_sheet_data=fattura_elettronica_xml_style_sheet_data)

Applica un foglio di stile CSS a una fattura XML esistente e restituisce il risultato.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2ClientCredentials):
* OAuth Authentication (oauth2):

```python
import amica_python_sdk
from amica_python_sdk.models.fattura_elettronica_xml_style_sheet_data import FatturaElettronicaXmlStyleSheetData
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
    api_instance = amica_python_sdk.FatturaElettronicaXmlApi(api_client)
    version = 'version_example' # str | Versione API.
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    idempotency_key = 'idempotency_key_example' # str | Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l'operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l'header `Idempotent-Replayed: true`. (optional)
    fattura_elettronica_xml_style_sheet_data = amica_python_sdk.FatturaElettronicaXmlStyleSheetData() # FatturaElettronicaXmlStyleSheetData | Opzioni di corrispondenza e stile. (optional)

    try:
        # Applica un foglio di stile CSS a una fattura XML esistente e restituisce il risultato.
        api_instance.api_vversion_company_id_fattura_elettronica_xml_stylesheet_post(version, company_id, idempotency_key=idempotency_key, fattura_elettronica_xml_style_sheet_data=fattura_elettronica_xml_style_sheet_data)
    except Exception as e:
        print("Exception when calling FatturaElettronicaXmlApi->api_vversion_company_id_fattura_elettronica_xml_stylesheet_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| Versione API. | 
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **idempotency_key** | **str**| Chiave di idempotenza (opzionale). Inviando la stessa chiave su un retry si riottiene la risposta della prima richiesta senza rieseguire l&#39;operazione: rende sicuri i retry automatici. Usa un valore univoco per operazione logica (es. un UUID). La risposta replicata riporta l&#39;header &#x60;Idempotent-Replayed: true&#x60;. | [optional] 
 **fattura_elettronica_xml_style_sheet_data** | [**FatturaElettronicaXmlStyleSheetData**](FatturaElettronicaXmlStyleSheetData.md)| Opzioni di corrispondenza e stile. | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer), [oauth2ClientCredentials](../README.md#oauth2ClientCredentials), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/xml, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**400** | Bad Request |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**404** | Not Found |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**429** | Troppe richieste: superato il limite di rate per il client. |  * RateLimit-Limit - Numero massimo di richieste consentite al client nella finestra corrente. <br>  * RateLimit-Remaining - Richieste ancora disponibili per il client nella finestra corrente. <br>  * RateLimit-Reset - Secondi al rinnovo dei permessi del client. <br>  * RateLimit-Policy - Policy di rate limiting applicata, nel formato &#x60;&lt;limite&gt;;w&#x3D;&lt;finestra in secondi&gt;&#x60;. <br>  * Retry-After - Secondi da attendere prima di inviare una nuova richiesta. <br>  * Idempotent-Replayed - Presente e pari a &#x60;true&#x60; quando la risposta è la replica di una richiesta precedente con la stessa Idempotency-Key. <br>  |
**409** | Conflitto: una richiesta con la stessa Idempotency-Key è ancora in elaborazione. |  -  |
**422** | La stessa Idempotency-Key è già stata usata per una richiesta con metodo, URL o corpo diversi. |  -  |
**401** | Non autenticato: access token mancante, non valido o scaduto. Ottieni un nuovo access token e ripeti la richiesta. La risposta non ha corpo. |  * WWW-Authenticate - Schema di autenticazione richiesto (&#x60;Bearer&#x60;) ed eventuale motivo del rifiuto del token. <br>  |
**403** | Accesso negato. Le cause possibili:  - il token non possiede lo scope richiesto dall&#39;operazione (risposta senza corpo); - &#x60;code: cloud_not_active&#x60;: l&#39;account lavora con una connessione locale e la Cloud API non espone i suoi dati; - &#x60;code: company_license_not_active&#x60;: la licenza dell&#39;azienda indicata nel percorso è scaduta o non è attiva; le altre aziende con licenza attiva restano accessibili. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

