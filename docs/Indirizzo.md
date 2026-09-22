# Indirizzo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**anagrafica_id** | **int** |  | [optional] 
**ragione_sociale1** | **str** |  | [optional] 
**ragione_sociale2** | **str** |  | [optional] 
**via** | **str** |  | [optional] 
**localit** | **str** |  | [optional] 
**cap** | **str** |  | [optional] 
**provincia** | **str** |  | [optional] 
**telefono1** | **str** |  | [optional] 
**telefono2** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**stato** | **bool** |  | [optional] 

## Example

```python
from amica_python_sdk.models.indirizzo import Indirizzo

# TODO update the JSON string below
json = "{}"
# create an instance of Indirizzo from a JSON string
indirizzo_instance = Indirizzo.from_json(json)
# print the JSON string representation of the object
print(Indirizzo.to_json())

# convert the object into a dict
indirizzo_dict = indirizzo_instance.to_dict()
# create an instance of Indirizzo from a dict
indirizzo_from_dict = Indirizzo.from_dict(indirizzo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


