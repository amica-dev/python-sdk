# Inventario


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**magazzino_id** | **int** |  | 
**magazzino** | [**Magazzino**](Magazzino.md) |  | [optional] 
**data** | **datetime** |  | 
**nome** | **str** |  | [optional] 
**fiscale** | **bool** |  | [optional] 
**valorizzazione** | **str** |  | 
**escludi_articoli_inattivi** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**righe** | [**List[InventarioRiga]**](InventarioRiga.md) |  | [optional] 

## Example

```python
from amica_python_sdk.models.inventario import Inventario

# TODO update the JSON string below
json = "{}"
# create an instance of Inventario from a JSON string
inventario_instance = Inventario.from_json(json)
# print the JSON string representation of the object
print(Inventario.to_json())

# convert the object into a dict
inventario_dict = inventario_instance.to_dict()
# create an instance of Inventario from a dict
inventario_from_dict = Inventario.from_dict(inventario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


