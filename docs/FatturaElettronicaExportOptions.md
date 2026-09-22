# FatturaElettronicaExportOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documento_id** | **List[int]** |  | [optional] 

## Example

```python
from amica_python_sdk.models.fattura_elettronica_export_options import FatturaElettronicaExportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaExportOptions from a JSON string
fattura_elettronica_export_options_instance = FatturaElettronicaExportOptions.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaExportOptions.to_json())

# convert the object into a dict
fattura_elettronica_export_options_dict = fattura_elettronica_export_options_instance.to_dict()
# create an instance of FatturaElettronicaExportOptions from a dict
fattura_elettronica_export_options_from_dict = FatturaElettronicaExportOptions.from_dict(fattura_elettronica_export_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


