# ContoContabileValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conto_id** | **int** |  | [optional] 
**conto** | **str** |  | [optional] 
**sezione** | **str** |  | [optional] 
**errori** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.conto_contabile_validation_result import ContoContabileValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ContoContabileValidationResult from a JSON string
conto_contabile_validation_result_instance = ContoContabileValidationResult.from_json(json)
# print the JSON string representation of the object
print(ContoContabileValidationResult.to_json())

# convert the object into a dict
conto_contabile_validation_result_dict = conto_contabile_validation_result_instance.to_dict()
# create an instance of ContoContabileValidationResult from a dict
conto_contabile_validation_result_from_dict = ContoContabileValidationResult.from_dict(conto_contabile_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


