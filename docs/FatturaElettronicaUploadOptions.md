# FatturaElettronicaUploadOptions

Opzioni di caricamento della fattura elettronica.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Nome del file XML da caricare. | [optional] 

## Example

```python
from amica_python_sdk.models.fattura_elettronica_upload_options import FatturaElettronicaUploadOptions

# TODO update the JSON string below
json = "{}"
# create an instance of FatturaElettronicaUploadOptions from a JSON string
fattura_elettronica_upload_options_instance = FatturaElettronicaUploadOptions.from_json(json)
# print the JSON string representation of the object
print(FatturaElettronicaUploadOptions.to_json())

# convert the object into a dict
fattura_elettronica_upload_options_dict = fattura_elettronica_upload_options_instance.to_dict()
# create an instance of FatturaElettronicaUploadOptions from a dict
fattura_elettronica_upload_options_from_dict = FatturaElettronicaUploadOptions.from_dict(fattura_elettronica_upload_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


