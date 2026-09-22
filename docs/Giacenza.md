# Giacenza


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**magazzino_id** | **int** |  | [optional] 
**magazzino** | [**Magazzino**](Magazzino.md) |  | [optional] 
**articolo_id** | **int** |  | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**quantit_in_giacenza** | **float** |  | [optional] 
**quantit_impegnata** | **float** |  | [optional] 
**quantit_ordinata** | **float** |  | [optional] 
**scorta_minima** | **float** |  | [optional] 
**gestione_sottoscorta** | **bool** |  | [optional] 
**data_ultimo_carico** | **datetime** |  | [optional] 
**data_ultimo_scarico** | **datetime** |  | [optional] 
**carico_quantit** | **float** |  | [optional] 
**carico_valore** | **float** |  | [optional] 
**scarico_quantit** | **float** |  | [optional] 
**scarico_valore** | **float** |  | [optional] 
**identificativo** | **str** |  | [optional] 
**identificativo_esteso** | **str** |  | [optional] 
**data** | **datetime** |  | [optional] 
**colore** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.giacenza import Giacenza

# TODO update the JSON string below
json = "{}"
# create an instance of Giacenza from a JSON string
giacenza_instance = Giacenza.from_json(json)
# print the JSON string representation of the object
print(Giacenza.to_json())

# convert the object into a dict
giacenza_dict = giacenza_instance.to_dict()
# create an instance of Giacenza from a dict
giacenza_from_dict = Giacenza.from_dict(giacenza_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


