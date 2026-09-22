# FatturaElettronicaExportResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | [optional] 
**valido** | **bool** |  | [optional] [readonly] 
**errori** | **List[str]** |  | [optional] 
**xml** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.fattura_elettronica_export_result import FatturaElettronicaExportResult

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaExportResult from a JSON string
fattura_elettronica_export_result_instance = FatturaElettronicaExportResult.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaExportResult.to_json())

# convert the object into a dict
fattura_elettronica_export_result_dict = fattura_elettronica_export_result_instance.to_dict()
# create an instance of FatturaElettronicaExportResult from a dict
fattura_elettronica_export_result_from_dict = FatturaElettronicaExportResult.from_dict(fattura_elettronica_export_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


