# Nazione


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 
**codice** | **str** |  | 

## Example

```python
from amica_python_sdk.models.nazione import Nazione

# TODO update the JSON string below
json = "{}"
# create an instance of Nazione from a JSON string
nazione_instance = Nazione.from_json(json)
# print the JSON string representation of the object
print(Nazione.to_json())

# convert the object into a dict
nazione_dict = nazione_instance.to_dict()
# create an instance of Nazione from a dict
nazione_from_dict = Nazione.from_dict(nazione_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


