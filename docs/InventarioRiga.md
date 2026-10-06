# InventarioRiga


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**inventario_id** | **int** |  | [optional] 
**articolo_id** | **int** |  | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**quantit** | **float** |  | [optional] 
**valore** | **float** |  | [optional] 
**identificativo** | **str** |  | [optional] 
**identificativo_esteso** | **str** |  | [optional] 
**data** | **datetime** |  | [optional] 
**colore** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.inventario_riga import InventarioRiga

# TODO update the JSON string below
json = "{}"
# create an instance of InventarioRiga from a JSON string
inventario_riga_instance = InventarioRiga.from_json(json)
# print the JSON string representation of the object
print(InventarioRiga.to_json())

# convert the object into a dict
inventario_riga_dict = inventario_riga_instance.to_dict()
# create an instance of InventarioRiga from a dict
inventario_riga_from_dict = InventarioRiga.from_dict(inventario_riga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


