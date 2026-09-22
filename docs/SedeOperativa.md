# SedeOperativa


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
from amica_python_sdk.models.sede_operativa import SedeOperativa

# TODO update the JSON string below
json = "{}"
# create an instance of SedeOperativa from a JSON string
sede_operativa_instance = SedeOperativa.from_json(json)
# print the JSON string representation of the object
print(SedeOperativa.to_json())

# convert the object into a dict
sede_operativa_dict = sede_operativa_instance.to_dict()
# create an instance of SedeOperativa from a dict
sede_operativa_from_dict = SedeOperativa.from_dict(sede_operativa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


