# Nazione

Nazione.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome. | 
**codice** | **str** | Un codice nazione ISO 3166-1 Alpha 2 valido. | 

## Example

```python
from amica_python_sdk.models.nazione import Nazione

# TODO update the JSON string below
json = "{}"
# create an instance of Nazione from a JSON string
nazione_instance = Nazione.from_json(json)
# print the JSON string representation of the object
print(Nazione.to_json())

# convert the object into a dict
nazione_dict = nazione_instance.to_dict()
# create an instance of Nazione from a dict
nazione_from_dict = Nazione.from_dict(nazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


