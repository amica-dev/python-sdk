# amica_sdk.CodicePagamentoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_vversion_company_id_tabelle_codice_pagamento_get**](CodicePagamentoApi.md#api_vversion_company_id_tabelle_codice_pagamento_get) | **GET** /api/v{version}/{companyId}/tabelle/CodicePagamento | Restituisce il contenuto della tabella come lista di elementi.


# **api_vversion_company_id_tabelle_codice_pagamento_get**
> List[CodicePagamento] api_vversion_company_id_tabelle_codice_pagamento_get(company_id, version)

Restituisce il contenuto della tabella come lista di elementi.

### Example

* Bearer (JWT) Authentication (bearer):
* OAuth Authentication (oauth2):
* OAuth Authentication (oauth2):

```python
import amica_sdk
from amica_sdk.models.codice_pagamento import CodicePagamento
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
    api_instance = amica_sdk.CodicePagamentoApi(api_client)
    company_id = 'company_id_example' # str | ID univoco dell'azienda.
    version = 'version_example' # str | 

    try:
        # Restituisce il contenuto della tabella come lista di elementi.
        api_response = api_instance.api_vversion_company_id_tabelle_codice_pagamento_get(company_id, version)
        print("The response of CodicePagamentoApi->api_vversion_company_id_tabelle_codice_pagamento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodicePagamentoApi->api_vversion_company_id_tabelle_codice_pagamento_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| ID univoco dell&#39;azienda. | 
 **version** | **str**|  | 

### Return type

[**List[CodicePagamento]**](CodicePagamento.md)

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

