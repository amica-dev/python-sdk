# Spesa

Spesa.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di &#x60;CausaleIva&#x60;. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**nome** | **str** | Nome. | 
**importo** | **float** | Importo. | [optional] 

## Example

```python
from amica_python_sdk.models.spesa import Spesa

# TODO update the JSON string below
json = "{}"
# create an instance of Spesa from a JSON string
spesa_instance = Spesa.from_json(json)
# print the JSON string representation of the object
print(Spesa.to_json())

# convert the object into a dict
spesa_dict = spesa_instance.to_dict()
# create an instance of Spesa from a dict
spesa_from_dict = Spesa.from_dict(spesa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


