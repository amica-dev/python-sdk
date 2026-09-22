# RegistrazioneContabileValidationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registrazione_id** | **int** |  | [optional] 
**data** | **datetime** |  | [optional] 
**numero** | **int** |  | [optional] 
**errori** | **List[str]** |  | [optional] 

## Example

```python
from amica_python_sdk.models.registrazione_contabile_validation_result import RegistrazioneContabileValidationResult

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrazioneContabileValidationResult from a JSON string
registrazione_contabile_validation_result_instance = RegistrazioneContabileValidationResult.from_json(json)
# print the JSON string representation of the object
print(RegistrazioneContabileValidationResult.to_json())

# convert the object into a dict
registrazione_contabile_validation_result_dict = registrazione_contabile_validation_result_instance.to_dict()
# create an instance of RegistrazioneContabileValidationResult from a dict
registrazione_contabile_validation_result_from_dict = RegistrazioneContabileValidationResult.from_dict(registrazione_contabile_validation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


