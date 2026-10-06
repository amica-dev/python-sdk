# Valuta

Valuta.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome. | 
**sigla** | **str** | Sigla (es. \&quot;EUR\&quot;). | 
**cambio** | **float** | Tasso di cambio rispetto all&#39;Euro. | [optional] 
**predefinita** | **bool** | Indica se questa è la valuta predefinita o meno. | [optional] 

## Example

```python
from amica_python_sdk.models.valuta import Valuta

# TODO update the JSON string below
json = "{}"
# create an instance of Valuta from a JSON string
valuta_instance = Valuta.from_json(json)
# print the JSON string representation of the object
print(Valuta.to_json())

# convert the object into a dict
valuta_dict = valuta_instance.to_dict()
# create an instance of Valuta from a dict
valuta_from_dict = Valuta.from_dict(valuta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


