# ContoContabile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**banca_id** | **int** |  | [optional] 
**sezione** | **str** |  | [optional] 
**tipo** | **str** |  | [optional] 
**raw** | **str** |  | [optional] 
**sottoconto** | **str** |  | [optional] 
**descrizione** | **str** |  | [optional] 
**conto** | **str** |  | [optional] [readonly] 

## Example

```python
from amica_python_sdk.models.conto_contabile import ContoContabile

# TODO update the JSON string below
json = "{}"
# create an instance of ContoContabile from a JSON string
conto_contabile_instance = ContoContabile.from_json(json)
# print the JSON string representation of the object
print(ContoContabile.to_json())

# convert the object into a dict
conto_contabile_dict = conto_contabile_instance.to_dict()
# create an instance of ContoContabile from a dict
conto_contabile_from_dict = ContoContabile.from_dict(conto_contabile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


