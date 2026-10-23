# ListinoComputeModificaPrezzi

Parametri della procedura `ModificaPrezzi`. Va indicato uno solo fra `Percentuale` e `Importo`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operazione** | **str** | Se aumentare o diminuire i prezzi. | [optional] 
**percentuale** | **float** | Variazione percentuale di ogni prezzo, come frazione: &#x60;0.05&#x60; corrisponde al 5%. Il risultato è arrotondato ai decimali dei prezzi unitari delle preferenze. | [optional] 
**importo** | **float** | Importo fisso da aggiungere o togliere a ogni prezzo. Il risultato non è arrotondato. | [optional] 

## Example

```python
from amica_python_sdk.models.listino_compute_modifica_prezzi import ListinoComputeModificaPrezzi

# TODO update the JSON string below
json = "{}"
# create an instance of ListinoComputeModificaPrezzi from a JSON string
listino_compute_modifica_prezzi_instance = ListinoComputeModificaPrezzi.from_json(json)
# print the JSON string representation of the object
print(ListinoComputeModificaPrezzi.to_json())

# convert the object into a dict
listino_compute_modifica_prezzi_dict = listino_compute_modifica_prezzi_instance.to_dict()
# create an instance of ListinoComputeModificaPrezzi from a dict
listino_compute_modifica_prezzi_from_dict = ListinoComputeModificaPrezzi.from_dict(listino_compute_modifica_prezzi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


