# Valuta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 
**sigla** | **str** |  | 
**cambio** | **float** |  | [optional] 
**predefinita** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.valuta import Valuta

# TODO update the JSON string below
json = "{}"
# create an instance of Valuta from a JSON string
valuta_instance = Valuta.from_json(json)
# print the JSON string representation of the object
print(Valuta.to_json())

# convert the object into a dict
valuta_dict = valuta_instance.to_dict()
# create an instance of Valuta from a dict
valuta_from_dict = Valuta.from_dict(valuta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


