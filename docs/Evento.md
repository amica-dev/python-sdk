# Evento

Un evento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**event_guid** | **str** | GUID dell&#39;evento. | [optional] 
**type** | **str** | Tipo di evento. | [optional] 
**company_id** | **str** | Identificativo dell&#39;azienda per cui l&#39;evento è stato scatenato. | [optional] 
**date_time** | **datetime** | Data e ora in cui l&#39;evento si è verificato. | [optional] 
**api_version** | **str** | Versione dell&#39;API. | [optional] 
**application_id** | **str** | Application ID del client. Vedi &lt;a href&#x3D;\&quot;https://amica.dev/api/required-headers/\&quot;&gt;required headers&lt;/a&gt; per maggiori informazioni. | [optional] 
**object** | **object** | Payload. | [optional] 

## Example

```python
from amica_sdk.models.evento import Evento

# TODO update the JSON string below
json = "{}"
# create an instance of Evento from a JSON string
evento_instance = Evento.from_json(json)
# print the JSON string representation of the object
print(Evento.to_json())

# convert the object into a dict
evento_dict = evento_instance.to_dict()
# create an instance of Evento from a dict
evento_from_dict = Evento.from_dict(evento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


