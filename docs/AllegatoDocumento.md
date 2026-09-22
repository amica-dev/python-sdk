# AllegatoDocumento


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome** | **str** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**formato** | **str** |  | [optional] 
**data_documento** | **datetime** |  | [optional] 
**numero_documento** | **str** |  | [optional] 
**allegato** | **bytearray** |  | [optional] 

## Example

```python
from amica_python_sdk.models.allegato_documento import AllegatoDocumento

# TODO update the JSON string below
json = "{}"
# create an instance of AllegatoDocumento from a JSON string
allegato_documento_instance = AllegatoDocumento.from_json(json)
# print the JSON string representation of the object
print(AllegatoDocumento.to_json())

# convert the object into a dict
allegato_documento_dict = allegato_documento_instance.to_dict()
# create an instance of AllegatoDocumento from a dict
allegato_documento_from_dict = AllegatoDocumento.from_dict(allegato_documento_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


