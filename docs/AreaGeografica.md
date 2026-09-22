# AreaGeografica


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 

## Example

```python
from amica_python_sdk.models.area_geografica import AreaGeografica

# TODO update the JSON string below
json = "{}"
# create an instance of AreaGeografica from a JSON string
area_geografica_instance = AreaGeografica.from_json(json)
# print the JSON string representation of the object
print(AreaGeografica.to_json())

# convert the object into a dict
area_geografica_dict = area_geografica_instance.to_dict()
# create an instance of AreaGeografica from a dict
area_geografica_from_dict = AreaGeografica.from_dict(area_geografica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


