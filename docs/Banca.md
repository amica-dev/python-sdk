# Banca


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**concurrency_token** | **int** |  | [optional] 
**nome** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**abi** | **str** |  | [optional] 
**cab** | **str** |  | [optional] 
**conto_corrente** | **str** |  | [optional] 
**bic** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.banca import Banca

# TODO update the JSON string below
json = "{}"
# create an instance of Banca from a JSON string
banca_instance = Banca.from_json(json)
# print the JSON string representation of the object
print(Banca.to_json())

# convert the object into a dict
banca_dict = banca_instance.to_dict()
# create an instance of Banca from a dict
banca_from_dict = Banca.from_dict(banca_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


