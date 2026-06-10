# RicercaArticolo

Opzioni di ricerca degli articoli.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**vendite_campo1** | **str** | Campo di ricerca preferito per gli articoli in vendita. | [optional] 
**vendite_campo2** | **str** | Secondo campo di ricerca per gli articoli in vendita. | [optional] 
**vendite_campo3** | **str** | Terzo campo di ricerca per gli articoli in vendita. | [optional] 
**vendite_campo4** | **str** | Quarto campo di ricerca per gli articoli in vendita. | [optional] 
**acquisti_campo1** | **str** | Campo di ricerca preferito per gli articoli in acquisto. | [optional] 
**acquisti_campo2** | **str** | Secondo campo di ricerca per gli articoli in acquisto. | [optional] 
**acquisti_campo3** | **str** | Terzo campo di ricerca per gli articoli in acquisto. | [optional] 
**acquisti_campo4** | **str** | Quarto campo di ricerca per gli articoli in acquisto. | [optional] 

## Example

```python
from amica_sdk.models.ricerca_articolo import RicercaArticolo

# TODO update the JSON string below
json = "{}"
# create an instance of RicercaArticolo from a JSON string
ricerca_articolo_instance = RicercaArticolo.from_json(json)
# print the JSON string representation of the object
print(RicercaArticolo.to_json())

# convert the object into a dict
ricerca_articolo_dict = ricerca_articolo_instance.to_dict()
# create an instance of RicercaArticolo from a dict
ricerca_articolo_from_dict = RicercaArticolo.from_dict(ricerca_articolo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


