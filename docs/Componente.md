# Componente


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**articolo_id** | **int** |  | [optional] 
**articolo** | [**Articolo**](Articolo.md) |  | [optional] 
**articolo_componente_id** | **int** |  | [optional] 
**articolo_componente** | [**Articolo**](Articolo.md) |  | [optional] 
**quantita_necessaria** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.componente import Componente

# TODO update the JSON string below
json = "{}"
# create an instance of Componente from a JSON string
componente_instance = Componente.from_json(json)
# print the JSON string representation of the object
print(Componente.to_json())

# convert the object into a dict
componente_dict = componente_instance.to_dict()
# create an instance of Componente from a dict
componente_from_dict = Componente.from_dict(componente_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


