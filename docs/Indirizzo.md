# Indirizzo

Indirizzo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**anagrafica_id** | **int** | Identificativo univoco di Amica.Anagrafica. | [optional] 
**ragione_sociale1** | **str** | Ragione sociale, oppure nome e cognome della persona fisica. | [optional] 
**ragione_sociale2** | **str** | Eventuale seconda riga della ragione sociale. | [optional] 
**via** | **str** | Indirizzo (via). | [optional] 
**localit** | **str** | Località. | [optional] 
**cap** | **str** | CAP o codice di avviamento postale. | [optional] 
**provincia** | **str** | Provincia, contea o nome dell&#39;area. | [optional] 
**telefono1** | **str** | Numero di telefono principale. | [optional] 
**telefono2** | **str** | Numero di telefono secondario. | [optional] 
**fax** | **str** | Numero di fax. | [optional] 
**email** | **str** | Indirizzo email. | [optional] 
**stato** | **bool** | Indica se l&#39;indirizzo è attivo oppure no. | [optional] 

## Example

```python
from amica_python_sdk.models.indirizzo import Indirizzo

# TODO update the JSON string below
json = "{}"
# create an instance of Indirizzo from a JSON string
indirizzo_instance = Indirizzo.from_json(json)
# print the JSON string representation of the object
print(Indirizzo.to_json())

# convert the object into a dict
indirizzo_dict = indirizzo_instance.to_dict()
# create an instance of Indirizzo from a dict
indirizzo_from_dict = Indirizzo.from_dict(indirizzo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


