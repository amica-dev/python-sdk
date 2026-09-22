# SedeAltra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**indirizzo** | **str** |  | [optional] 
**localit** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**telefono1** | **str** |  | [optional] 
**telefono2** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.sede_altra import SedeAltra

# TODO update the JSON string below
json = "{}"
# create an instance of SedeAltra from a JSON string
sede_altra_instance = SedeAltra.from_json(json)
# print the JSON string representation of the object
print(SedeAltra.to_json())

# convert the object into a dict
sede_altra_dict = sede_altra_instance.to_dict()
# create an instance of SedeAltra from a dict
sede_altra_from_dict = SedeAltra.from_dict(sede_altra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


