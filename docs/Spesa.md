# Spesa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**nome** | **str** |  | 
**importo** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.spesa import Spesa

# TODO update the JSON string below
json = "{}"
# create an instance of Spesa from a JSON string
spesa_instance = Spesa.from_json(json)
# print the JSON string representation of the object
print(Spesa.to_json())

# convert the object into a dict
spesa_dict = spesa_instance.to_dict()
# create an instance of Spesa from a dict
spesa_from_dict = Spesa.from_dict(spesa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


