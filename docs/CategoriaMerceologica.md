# CategoriaMerceologica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 

## Example

```python
from amica_python_sdk.models.categoria_merceologica import CategoriaMerceologica

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriaMerceologica from a JSON string
categoria_merceologica_instance = CategoriaMerceologica.from_json(json)
# print the JSON string representation of the object
print(CategoriaMerceologica.to_json())

# convert the object into a dict
categoria_merceologica_dict = categoria_merceologica_instance.to_dict()
# create an instance of CategoriaMerceologica from a dict
categoria_merceologica_from_dict = CategoriaMerceologica.from_dict(categoria_merceologica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


