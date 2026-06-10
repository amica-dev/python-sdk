# DocumentoImportData

Dati di importazione del documento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **List[int]** | Identificativo del documento da importare. | [optional] 

## Example

```python
from amica_sdk.models.documento_import_data import DocumentoImportData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoImportData from a JSON string
documento_import_data_instance = DocumentoImportData.from_json(json)
# print the JSON string representation of the object
print(DocumentoImportData.to_json())

# convert the object into a dict
documento_import_data_dict = documento_import_data_instance.to_dict()
# create an instance of DocumentoImportData from a dict
documento_import_data_from_dict = DocumentoImportData.from_dict(documento_import_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


