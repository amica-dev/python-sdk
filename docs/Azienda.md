# Azienda


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 
**license_key** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.azienda import Azienda

# TODO update the JSON string below
json = "{}"
# create an instance of Azienda from a JSON string
azienda_instance = Azienda.from_json(json)
# print the JSON string representation of the object
print(Azienda.to_json())

# convert the object into a dict
azienda_dict = azienda_instance.to_dict()
# create an instance of Azienda from a dict
azienda_from_dict = Azienda.from_dict(azienda_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


