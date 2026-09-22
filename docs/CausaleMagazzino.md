# CausaleMagazzino


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | 
**codice** | **str** |  | 
**movimento_di_carico** | **bool** |  | [optional] 
**tipo_causale_magazzino** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.causale_magazzino import CausaleMagazzino

# TODO update the JSON string below
json = "{}"
# create an instance of CausaleMagazzino from a JSON string
causale_magazzino_instance = CausaleMagazzino.from_json(json)
# print the JSON string representation of the object
print(CausaleMagazzino.to_json())

# convert the object into a dict
causale_magazzino_dict = causale_magazzino_instance.to_dict()
# create an instance of CausaleMagazzino from a dict
causale_magazzino_from_dict = CausaleMagazzino.from_dict(causale_magazzino_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


