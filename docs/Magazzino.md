# Magazzino

Magazzino.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome. | 
**indirizzo** | **str** | Indirizzo. | [optional] 
**localit** | **str** | Località. | [optional] 
**cap** | **str** | CAP o codice di zona. | [optional] 
**provincia** | **str** | Provincia o nome dell&#39;area. | [optional] 
**note** | **str** | Note. | [optional] 

## Example

```python
from amica_python_sdk.models.magazzino import Magazzino

# TODO update the JSON string below
json = "{}"
# create an instance of Magazzino from a JSON string
magazzino_instance = Magazzino.from_json(json)
# print the JSON string representation of the object
print(Magazzino.to_json())

# convert the object into a dict
magazzino_dict = magazzino_instance.to_dict()
# create an instance of Magazzino from a dict
magazzino_from_dict = Magazzino.from_dict(magazzino_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


