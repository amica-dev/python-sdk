# DocumentoComputeDataSpesa

Metadati della spesa di documento.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**causale_iva_id** | **int** | Identificativo univoco del codice IVA. | [optional] 
**importo** | **float** | Importo. | [optional] 

## Example

```python
from amica_python_sdk.models.documento_compute_data_spesa import DocumentoComputeDataSpesa

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoComputeDataSpesa from a JSON string
documento_compute_data_spesa_instance = DocumentoComputeDataSpesa.from_json(json)
# print the JSON string representation of the object
print(DocumentoComputeDataSpesa.to_json())

# convert the object into a dict
documento_compute_data_spesa_dict = documento_compute_data_spesa_instance.to_dict()
# create an instance of DocumentoComputeDataSpesa from a dict
documento_compute_data_spesa_from_dict = DocumentoComputeDataSpesa.from_dict(documento_compute_data_spesa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


