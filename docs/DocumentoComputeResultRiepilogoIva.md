# DocumentoComputeResultRiepilogoIva


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imponibile_lordo** | **float** |  | [optional] 
**imponibile** | **float** |  | [optional] 
**imposta** | **float** |  | [optional] 
**aliquota** | **float** |  | [optional] 
**causale_iva_id** | **int** |  | [optional] 
**causale_iva_codice** | **str** |  | [optional] 
**causale_iva_nome** | **str** |  | [optional] 

## Example

```python
from amica_python_sdk.models.documento_compute_result_riepilogo_iva import DocumentoComputeResultRiepilogoIva

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentoComputeResultRiepilogoIva from a JSON string
documento_compute_result_riepilogo_iva_instance = DocumentoComputeResultRiepilogoIva.from_json(json)
# print the JSON string representation of the object
print(DocumentoComputeResultRiepilogoIva.to_json())

# convert the object into a dict
documento_compute_result_riepilogo_iva_dict = documento_compute_result_riepilogo_iva_instance.to_dict()
# create an instance of DocumentoComputeResultRiepilogoIva from a dict
documento_compute_result_riepilogo_iva_from_dict = DocumentoComputeResultRiepilogoIva.from_dict(documento_compute_result_riepilogo_iva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


