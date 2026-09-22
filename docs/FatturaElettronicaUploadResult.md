# FatturaElettronicaUploadResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messaggi** | **List[str]** |  | [optional] 
**esito** | **str** |  | [optional] 
**is_success** | **bool** |  | [optional] [readonly] 

## Example

```python
from amica_python_sdk.models.fattura_elettronica_upload_result import FatturaElettronicaUploadResult

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaUploadResult from a JSON string
fattura_elettronica_upload_result_instance = FatturaElettronicaUploadResult.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaUploadResult.to_json())

# convert the object into a dict
fattura_elettronica_upload_result_dict = fattura_elettronica_upload_result_instance.to_dict()
# create an instance of FatturaElettronicaUploadResult from a dict
fattura_elettronica_upload_result_from_dict = FatturaElettronicaUploadResult.from_dict(fattura_elettronica_upload_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


