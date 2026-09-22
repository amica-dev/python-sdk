# AnagraficaNominativo2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome** | **str** |  | [optional] 
**incarico** | **str** |  | [optional] 
**telefono1** | **str** |  | [optional] 
**telefono2** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**e_mail** | **str** |  | [optional] 
**note** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.anagrafica_nominativo2 import AnagraficaNominativo2

# TODO update the JSON string below
json = "{}"
# create an instance of AnagraficaNominativo2 from a JSON string
anagrafica_nominativo2_instance = AnagraficaNominativo2.from_json(json)
# print the JSON string representation of the object
print(AnagraficaNominativo2.to_json())

# convert the object into a dict
anagrafica_nominativo2_dict = anagrafica_nominativo2_instance.to_dict()
# create an instance of AnagraficaNominativo2 from a dict
anagrafica_nominativo2_from_dict = AnagraficaNominativo2.from_dict(anagrafica_nominativo2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


