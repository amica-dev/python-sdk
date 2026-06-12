# Banca

Banca.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**nome** | **str** | Nome. | [optional] 
**iban** | **str** | Codice IBAN. | [optional] 
**abi** | **str** | Codice ABI. | [optional] 
**cab** | **str** | Codice CAB. | [optional] 
**conto_corrente** | **str** | Numero di conto corrente. | [optional] 
**bic** | **str** | Codice BIC. | [optional] 

## Example

```python
from amica_python_sdk.models.banca import Banca

# TODO update the JSON string below
json = "{}"
# create an instance of Banca from a JSON string
banca_instance = Banca.from_json(json)
# print the JSON string representation of the object
print(Banca.to_json())

# convert the object into a dict
banca_dict = banca_instance.to_dict()
# create an instance of Banca from a dict
banca_from_dict = Banca.from_dict(banca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


