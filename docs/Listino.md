# Listino


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**fornitore_id** | **int** |  | [optional] 
**fornitore** | [**Anagrafica**](Anagrafica.md) |  | [optional] 
**valuta_id** | **int** |  | [optional] 
**valuta** | [**Valuta**](Valuta.md) |  | [optional] 
**nome** | **str** |  | 
**iva_inclusa** | **bool** |  | [optional] 
**ricarico** | **float** |  | [optional] 
**data_creazione** | **datetime** |  | [optional] 
**valido_dal** | **datetime** |  | [optional] 
**valido_al** | **datetime** |  | [optional] 
**tipo_listino** | **str** |  | [optional] 
**calcolo_prezzi** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**righe** | [**List[Prezzo]**](Prezzo.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.listino import Listino

# TODO update the JSON string below
json = "{}"
# create an instance of Listino from a JSON string
listino_instance = Listino.from_json(json)
# print the JSON string representation of the object
print(Listino.to_json())

# convert the object into a dict
listino_dict = listino_instance.to_dict()
# create an instance of Listino from a dict
listino_from_dict = Listino.from_dict(listino_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


