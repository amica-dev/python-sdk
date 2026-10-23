# ListinoComputeAggiungi

Parametri della procedura `Aggiungi`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filtro** | **str** | Quali articoli aggiungere. | [optional] 
**id** | **int** | Identificativo univoco del produttore, della marca, della categoria o del gruppo merceologico, secondo &#x60;Filtro&#x60;. | [optional] 
**dal** | **datetime** | Con &#x60;DataInserimento&#x60;, si aggiungono gli articoli inseriti in questa data o dopo. | [optional] 

## Example

```python
from amica_python_sdk.models.listino_compute_aggiungi import ListinoComputeAggiungi

# TODO update the JSON string below
json = "{}"
# create an instance of ListinoComputeAggiungi from a JSON string
listino_compute_aggiungi_instance = ListinoComputeAggiungi.from_json(json)
# print the JSON string representation of the object
print(ListinoComputeAggiungi.to_json())

# convert the object into a dict
listino_compute_aggiungi_dict = listino_compute_aggiungi_instance.to_dict()
# create an instance of ListinoComputeAggiungi from a dict
listino_compute_aggiungi_from_dict = ListinoComputeAggiungi.from_dict(listino_compute_aggiungi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


