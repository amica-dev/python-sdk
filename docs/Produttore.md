# Produttore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 

## Example

```python
from amica_python_sdk.models.produttore import Produttore

# TODO update the JSON string below
json = "{}"
# create an instance of Produttore from a JSON string
produttore_instance = Produttore.from_json(json)
# print the JSON string representation of the object
print(Produttore.to_json())

# convert the object into a dict
produttore_dict = produttore_instance.to_dict()
# create an instance of Produttore from a dict
produttore_from_dict = Produttore.from_dict(produttore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


