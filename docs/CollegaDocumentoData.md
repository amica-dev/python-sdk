# CollegaDocumentoData

Documenti da referenziare nel documento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documento** | [**DocumentoCollegato**](DocumentoCollegato.md) |  | [optional] 

## Example

```python
from amica_sdk.models.collega_documento_data import CollegaDocumentoData

# TODO update the JSON string below
json = "{}"
# create an instance of CollegaDocumentoData from a JSON string
collega_documento_data_instance = CollegaDocumentoData.from_json(json)
# print the JSON string representation of the object
print(CollegaDocumentoData.to_json())

# convert the object into a dict
collega_documento_data_dict = collega_documento_data_instance.to_dict()
# create an instance of CollegaDocumentoData from a dict
collega_documento_data_from_dict = CollegaDocumentoData.from_dict(collega_documento_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


