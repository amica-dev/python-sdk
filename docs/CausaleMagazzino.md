# CausaleMagazzino

Causale di un movimento di magazzino.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome o descrizione. | 
**codice** | **str** | Codice o identificativo univoco. | 
**movimento_di_carico** | **bool** | Indica se l&#39;utilizzo causa la creazione di un movimento di carico. | [optional] 
**tipo_causale_magazzino** | **str** | Tipologia del movimento di magazzino. | [optional] 

## Example

```python
from amica_python_sdk.models.causale_magazzino import CausaleMagazzino

# TODO update the JSON string below
json = "{}"
# create an instance of CausaleMagazzino from a JSON string
causale_magazzino_instance = CausaleMagazzino.from_json(json)
# print the JSON string representation of the object
print(CausaleMagazzino.to_json())

# convert the object into a dict
causale_magazzino_dict = causale_magazzino_instance.to_dict()
# create an instance of CausaleMagazzino from a dict
causale_magazzino_from_dict = CausaleMagazzino.from_dict(causale_magazzino_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


