# CategoriaAnagrafica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 

## Example

```python
from amica_python_sdk.models.categoria_anagrafica import CategoriaAnagrafica

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriaAnagrafica from a JSON string
categoria_anagrafica_instance = CategoriaAnagrafica.from_json(json)
# print the JSON string representation of the object
print(CategoriaAnagrafica.to_json())

# convert the object into a dict
categoria_anagrafica_dict = categoria_anagrafica_instance.to_dict()
# create an instance of CategoriaAnagrafica from a dict
categoria_anagrafica_from_dict = CategoriaAnagrafica.from_dict(categoria_anagrafica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


