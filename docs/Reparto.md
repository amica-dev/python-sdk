# Reparto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva** | [**CausaleIva**](CausaleIva.md) |  | [optional] 
**numero** | **int** |  | [optional] 
**prezzo** | **float** |  | [optional] 
**sconto** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.reparto import Reparto

# TODO update the JSON string below
json = "{}"
# create an instance of Reparto from a JSON string
reparto_instance = Reparto.from_json(json)
# print the JSON string representation of the object
print(Reparto.to_json())

# convert the object into a dict
reparto_dict = reparto_instance.to_dict()
# create an instance of Reparto from a dict
reparto_from_dict = Reparto.from_dict(reparto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


