# Azienda

Dati dell'intestatario della licenza Amica.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Ragione sociale, così come registrata all&#39;attivazione della licenza Amica. | 
**license_key** | **str** | Chiave di licenza Amica. | [optional] 

## Example

```python
from amica_sdk.models.azienda import Azienda

# TODO update the JSON string below
json = "{}"
# create an instance of Azienda from a JSON string
azienda_instance = Azienda.from_json(json)
# print the JSON string representation of the object
print(Azienda.to_json())

# convert the object into a dict
azienda_dict = azienda_instance.to_dict()
# create an instance of Azienda from a dict
azienda_from_dict = Azienda.from_dict(azienda_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


