# ArticoloColore

Colore disponibile per un articolo gestito a taglie e colori. Alimenta la scelta del colore nelle righe di documenti e movimenti merce, dove il colore resta comunque testo libero.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identificativo univoco. | [optional] 
**concurrency_token** | **int** | Il token di concorrenza implementa il controllo di concorrenza ottimistica: a ogni operazione di aggiornamento o cancellazione il valore del token sul database viene confrontato con quello sull&#39;entità. Se i valori coincidono, l&#39;operazione viene eseguita; se differiscono, si assume che un altro utente abbia effettuato una scrittura nel frattempo e l&#39;aggiornamento viene rifiutato. | [optional] 
**articolo_id** | **int** | Identificativo univoco di &#x60;Articolo&#x60;. | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**colore** | **str** | Nome del colore. Il confronto ignora maiuscole e minuscole: &#x60;Rosso&#x60; e &#x60;rosso&#x60; sono lo stesso colore. | 

## Example

```python
from amica_python_sdk.models.articolo_colore import ArticoloColore

# TODO update the JSON string below
json = "{}"
# create an instance of ArticoloColore from a JSON string
articolo_colore_instance = ArticoloColore.from_json(json)
# print the JSON string representation of the object
print(ArticoloColore.to_json())

# convert the object into a dict
articolo_colore_dict = articolo_colore_instance.to_dict()
# create an instance of ArticoloColore from a dict
articolo_colore_from_dict = ArticoloColore.from_dict(articolo_colore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


