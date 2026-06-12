# Reparto

Reparto.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**causale_iva_id** | **int** | Identificativo univoco di Amica.Reparto.CausaleIva. | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**numero** | **int** | Numero del reparto. | [optional] 
**prezzo** | **float** | Prezzo associato al reparto. | [optional] 
**sconto** | **float** | Sconto riconosciuto all&#39;utilizzo del reparto (percentuale). | [optional] 

## Example

```python
from amica_python_sdk.models.reparto import Reparto

# TODO update the JSON string below
json = "{}"
# create an instance of Reparto from a JSON string
reparto_instance = Reparto.from_json(json)
# print the JSON string representation of the object
print(Reparto.to_json())

# convert the object into a dict
reparto_dict = reparto_instance.to_dict()
# create an instance of Reparto from a dict
reparto_from_dict = Reparto.from_dict(reparto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


