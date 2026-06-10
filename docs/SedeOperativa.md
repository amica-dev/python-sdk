# SedeOperativa

Sede operativa.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**indirizzo** | **str** | Indirizzo. | [optional] 
**localit** | **str** | Città, comune o altro nome di località. | [optional] 
**cap** | **str** | CAP o codice di zona. | [optional] 
**provincia** | **str** | Provincia o nome dell&#39;area. | [optional] 
**telefono1** | **str** | Numero di telefono principale. | [optional] 
**telefono2** | **str** | Numero di telefono secondario. | [optional] 
**fax** | **str** | Numero di fax. | [optional] 

## Example

```python
from amica_sdk.models.sede_operativa import SedeOperativa

# TODO update the JSON string below
json = "{}"
# create an instance of SedeOperativa from a JSON string
sede_operativa_instance = SedeOperativa.from_json(json)
# print the JSON string representation of the object
print(SedeOperativa.to_json())

# convert the object into a dict
sede_operativa_dict = sede_operativa_instance.to_dict()
# create an instance of SedeOperativa from a dict
sede_operativa_from_dict = SedeOperativa.from_dict(sede_operativa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


