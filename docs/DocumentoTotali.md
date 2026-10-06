# DocumentoTotali


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**periodo** | **datetime** |  | [optional] 
**anagrafica_id** | **int** |  | [optional] 
**ragione_sociale** | **str** |  | [optional] 
**documenti** | **int** |  | [optional] 
**totale_imponibile** | **float** |  | [optional] 
**totale_esente** | **float** |  | [optional] 
**totale_imposta** | **float** |  | [optional] 
**totale_documento** | **float** |  | [optional] 

## Example

```python
from amica_python_sdk.models.documento_totali import DocumentoTotali

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoTotali from a JSON string
documento_totali_instance = DocumentoTotali.from_json(json)
# print the JSON string representation of the object
print(DocumentoTotali.to_json())

# convert the object into a dict
documento_totali_dict = documento_totali_instance.to_dict()
# create an instance of DocumentoTotali from a dict
documento_totali_from_dict = DocumentoTotali.from_dict(documento_totali_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


