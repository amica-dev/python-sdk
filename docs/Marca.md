# Marca

Marca.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome. | 

## Example

```python
from amica_python_sdk.models.marca import Marca

# TODO update the JSON string below
json = "{}"
# create an instance of Marca from a JSON string
marca_instance = Marca.from_json(json)
# print the JSON string representation of the object
print(Marca.to_json())

# convert the object into a dict
marca_dict = marca_instance.to_dict()
# create an instance of Marca from a dict
marca_from_dict = Marca.from_dict(marca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


