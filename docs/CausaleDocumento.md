# CausaleDocumento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 

## Example

```python
from amica_python_sdk.models.causale_documento import CausaleDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of CausaleDocumento from a JSON string
causale_documento_instance = CausaleDocumento.from_json(json)
# print the JSON string representation of the object
print(CausaleDocumento.to_json())

# convert the object into a dict
causale_documento_dict = causale_documento_instance.to_dict()
# create an instance of CausaleDocumento from a dict
causale_documento_from_dict = CausaleDocumento.from_dict(causale_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


