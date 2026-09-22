# GruppoMerceologico


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 

## Example

```python
from amica_python_sdk.models.gruppo_merceologico import GruppoMerceologico

# TODO update the JSON string below
json = "{}"
# create an instance of GruppoMerceologico from a JSON string
gruppo_merceologico_instance = GruppoMerceologico.from_json(json)
# print the JSON string representation of the object
print(GruppoMerceologico.to_json())

# convert the object into a dict
gruppo_merceologico_dict = gruppo_merceologico_instance.to_dict()
# create an instance of GruppoMerceologico from a dict
gruppo_merceologico_from_dict = GruppoMerceologico.from_dict(gruppo_merceologico_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


