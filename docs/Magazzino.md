# Magazzino


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 
**indirizzo** | **str** |  | [optional] 
**localit** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.magazzino import Magazzino

# TODO update the JSON string below
json = "{}"
# create an instance of Magazzino from a JSON string
magazzino_instance = Magazzino.from_json(json)
# print the JSON string representation of the object
print(Magazzino.to_json())

# convert the object into a dict
magazzino_dict = magazzino_instance.to_dict()
# create an instance of Magazzino from a dict
magazzino_from_dict = Magazzino.from_dict(magazzino_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


